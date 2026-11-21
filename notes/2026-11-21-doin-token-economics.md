---
layout: research-note
title: "DOIN Token Economics: Quantifying Transaction-Cost Savings"
date: 2026-11-21
author: "Jason Kronemeyer"
categories:
  - research
  - doin
  - knowledge-infrastructure
tags:
  - token-economics
  - transaction-costs
  - DGML
  - NVNM
  - RAG
  - knowledge-objects
summary: "An illustrative model of how DOIN can reduce token consumption by replacing repeated document-centric retrieval with reusable knowledge objects, selective provenance, and delta processing."
description: "A research note estimating first-transaction and lifecycle token savings from the DOIN knowledge-development architecture."
status: draft
published: false
permalink: /research/doin-token-economics/
---

# DOIN Token Economics: Quantifying Transaction-Cost Savings

## Executive summary

DOIN could plausibly reduce large-language-model token consumption by **60–90% per transaction**, depending on corpus size, query volume, change rate, and how effectively reusable knowledge objects replace repeated document retrieval.

The central economic shift is:

> **Traditional RAG repeatedly tokenizes evidence. DOIN tokenizes evidence once, develops reusable knowledge, and subsequently processes mostly changes and targeted provenance.**

Under the illustrative model in this note, DOIN reduces:

- first-transaction consumption by approximately **64%**;
- subsequent-transaction consumption by approximately **89%**; and
- five-transaction lifecycle consumption by approximately **84%**.

These figures are hypotheses for pilot testing, not production forecasts.

## Illustrative transaction model

Consider a data-center financing or asset-diligence process with:

- **3,000 pages** of contracts, studies, financials, appraisals, and operating data;
- **450 words per page**;
- approximately **1.33 tokens per word**;
- **250 analytical questions**;
- **32,000 retrieved tokens** per traditional RAG question;
- **4,000 tokens** per DOIN knowledge query; and
- **5% of source knowledge changing** between transactions.

The resulting source corpus is approximately **1.80 million tokens**.

## First-transaction comparison

| Activity | Traditional document/RAG model | DOIN model |
|---|---:|---:|
| Initial source processing | 1.80M | 2.51M |
| 250 analytical queries | 8.00M | 1.00M |
| **First-transaction total** | **9.80M** | **3.51M** |
| **Reduction** |  | **6.28M, or 64%** |

The DOIN initial-processing estimate is intentionally higher than the raw corpus. It applies a **1.4× factor** for knowledge extraction, structured output, lineage creation, and validation.

Even with that upfront cost, DOIN wins in this example because subsequent questions query compact, reusable knowledge objects instead of repeatedly retrieving large passages from the source documents.

## Subsequent transaction: delta diligence

For a refinancing, sale, securitization, or second underwriting, assume only **5%** of the underlying knowledge state changes.

| Activity | Traditional re-diligence | DOIN delta diligence |
|---|---:|---:|
| Evidence processing | 1.80M | 0.13M |
| 250 analytical queries | 8.00M | 1.00M |
| **Total** | **9.80M** | **1.13M** |
| **Reduction** |  | **8.67M, or 89%** |

The diligence model changes from **re-establish everything** to **validate what changed and recompute what depends on it**.

## Five-transaction lifecycle

Using the same assumptions across one initial transaction and four subsequent transactions:

| Model | Five-transaction tokens |
|---|---:|
| Repeated document/RAG diligence | **48.98M** |
| DOIN knowledge development | **8.02M** |
| **Tokens avoided** | **40.96M** |
| **Lifecycle reduction** | **84%** |

In this illustration, DOIN consumes approximately **one-sixth as many tokens** over five related transactions.

## Model equations

Traditional document-centric processing can be represented as:

```text
T_traditional = T_corpus + Q × T_RAG-context
```

A subsequent DOIN transaction can be represented as:

```text
T_DOIN = T_corpus × delta × V + Q × T_knowledge-context
```

Where:

- `Q` is the number of analytical questions;
- `delta` is the proportion of knowledge that changed;
- `V` is extraction and validation overhead; and
- `T_knowledge-context` is the compact knowledge, rights, and provenance context supplied per query.

## Expected savings range

| DOIN maturity | Potential token reduction | Operating condition |
|---|---:|---|
| Basic structured retrieval | **30–50%** | Documents are still retrieved frequently |
| Mature knowledge-object retrieval | **60–75%** | Common facts and calculations are reusable |
| Delta diligence | **80–90%** | Only changed objects and dependencies are reprocessed |
| Repetitive portfolio workflows | **90%+ may be possible** | Standardized assets, high query reuse, and low change rates |

The estimates are most sensitive to:

1. the amount of evidence that changes between transactions; and
2. whether agents query compact knowledge objects or continue retrieving large source passages.

## Sources of token savings

### Extract once, query many times

A covenant, lease term, power commitment, or property attribute should not be rediscovered from its source document every time an agent receives a related question. DOIN extracts it into an attributed knowledge object and reuses it.

### Retrieve facts before passages

A traditional system may retrieve many pages to answer a narrow question such as the current debt-yield threshold. DOIN can initially provide the threshold, effective date, knowledge type, source pointer, rights status, and verification status. The source clause is retrieved only when inspection or challenge requires it.

### Reuse deterministic calculations

Debt yield, leverage, lease exposure, power utilization, covenant headroom, and model features should be calculated once per relevant state change rather than regenerated conversationally for every query.

### Traverse provenance selectively

DOIN does not need to insert the full evidentiary history into every prompt. It can initially return:

```text
claim + type + current value + source ID + verification status
```

The complete DGML and NVNM provenance chain is loaded only when policy, audit, or user need requires it.

### Process the delta

When 5% of an asset's knowledge changes, DOIN should:

1. identify the changed evidence;
2. update the affected knowledge objects;
3. traverse dependent calculations and conclusions;
4. invalidate or recompute those dependencies; and
5. leave the unaffected knowledge state intact.

This is the primary source of lifecycle savings.

## Converting tokens to dollars

Token reduction is not equivalent to total transaction-cost reduction. Gross model-cost savings can be expressed as:

```text
Model savings =
  (input tokens avoided / 1,000,000 × input price)
+ (output tokens avoided / 1,000,000 × output price)
- incremental DOIN infrastructure cost
```

For the five-transaction illustration, gross consumption falls by approximately **40.96 million tokens**.

The financial result will depend on:

- model and inference provider;
- input/output token mix;
- prompt caching;
- embedding and reranking costs;
- MongoDB, PostgreSQL, or graph infrastructure;
- DGML extraction costs;
- NVNM attestation costs; and
- human validation and exception handling.

The larger economic benefit may come from analyst and diligence time rather than inference fees. Token savings are best treated as an observable proxy for repetitive evidence-processing work that the architecture has eliminated.

## Proposed operating metrics

A DOIN pilot should instrument:

1. source tokens ingested per asset;
2. knowledge objects created per million source tokens;
3. tokens per answered diligence question;
4. percentage of answers resolved without source-document retrieval;
5. average provenance tokens added per answer;
6. percentage of the corpus reprocessed after an update;
7. tokens per initial transaction;
8. tokens per subsequent transaction; and
9. token reuse ratio.

Define token reuse ratio as:

```text
Token reuse ratio =
  estimated document tokens avoided / DOIN tokens consumed
```

For the illustrative five-transaction lifecycle:

```text
(48.98M - 8.02M) / 8.02M ≈ 5.1
```

Each token consumed by the DOIN approach therefore avoids approximately **5.1 additional tokens** of repeated document-centric processing in this model.

## Risks and limitations

- The model assumes knowledge objects remain materially smaller than retrieved document context.
- Weak entity resolution or lineage quality could force repeated source retrieval and reduce savings.
- Rights restrictions may require controlled source access or prohibit persistent derived representations for some content.
- Verification, exception handling, and human review may offset part of the model-cost reduction.
- Token savings do not prove improved accuracy, legal sufficiency, or underwriting quality.
- Cryptographic provenance can prove integrity and lineage, but it cannot prove that the original evidence or analytical conclusion was correct.

## Research hypothesis and pilot design

A defensible initial hypothesis is:

> **DOIN can reduce first-transaction token consumption by approximately 50–70% and subsequent-transaction consumption by 80–90%, producing an estimated 75–85% lifecycle reduction across five related transactions.**

Test that hypothesis on one representative asset using the same corpus and diligence questions across three configurations:

1. standard document RAG;
2. DGML-enhanced RAG; and
3. full DOIN knowledge-object retrieval with selective provenance.

Measure token volume, answer accuracy, source-grounding rate, latency, human-review time, and rights-policy compliance. The result should establish an empirical **tokens-per-transaction baseline** and isolate savings attributable to structured knowledge, delta processing, caching, and targeted provenance retrieval.

## Conclusion

DOIN's transaction-cost advantage is not simply cheaper inference. It is the conversion of repeatedly processed evidence into persistent, rights-aware, and verifiable knowledge.

The target operating model is:

> **Develop knowledge once, reuse it across questions and transactions, and spend new tokens primarily on changes, exceptions, and judgment.**
