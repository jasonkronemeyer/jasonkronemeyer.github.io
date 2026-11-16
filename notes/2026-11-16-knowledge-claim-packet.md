---
layout: research-note
title: "Knowledge Claim Packets: A Governance and Verification Architecture for Portable, Provenance-Aware Knowledge"
subtitle: "Toward verifiable, contextual, and community-governed knowledge infrastructure"
author: Jason Kronemeyer
date: 2026-11-16
categories:
  - research
  - knowledge-infrastructure
  - artificial-intelligence
  - semantic-web
  - provenance
tags:
  - Knowledge Claim Packet
  - KCP
  - provenance
  - knowledge graphs
  - Semantic Web
  - trustworthy AI
  - knowledge commons
  - digital signatures
  - transparency logs
  - governance
  - DOIN
  - Common Cartridge
  - interoperability
description: "A research paper introducing the Knowledge Claim Packet as a portable, provenance-aware unit of knowledge and examining its verification, governance, interoperability, and potential originality."
keywords:
  - Knowledge Claim Packet
  - provenance
  - knowledge governance
  - semantic authority
  - knowledge graphs
  - trustworthy AI
  - federated knowledge commons
  - digital signatures
  - transparency logs
  - nanopublications
  - SCITT
  - W3C PROV
  - DOIN
status: brainstorming
version: 0.1
license: CC BY 4.0
---

# Knowledge Claim Packets: A Governance and Verification Architecture for Portable, Provenance-Aware Knowledge

## Abstract

Contemporary knowledge infrastructures increasingly require more than the exchange of information or machine-readable semantics. Artificial intelligence, knowledge graphs, research-data systems, and federated knowledge environments must also account for the provenance, context, authority, evidentiary basis, and revision history of the claims they process. Existing standards and technologies address portions of this requirement through persistent identifiers, semantic representations, provenance models, digital signatures, verifiable credentials, content-authenticity mechanisms, and transparency systems. These capabilities, however, are commonly implemented as separate layers and do not necessarily provide a general-purpose unit for exchanging an assertion together with the information required to evaluate its origin, applicability, governance, and evolution.

This paper introduces the **Knowledge Claim Packet (KCP)** as a proposed portable, provenance-aware representation of a knowledge claim. The proposed model binds a machine-readable assertion to a persistent identifier and provides mechanisms for associating that assertion with supporting evidence, source attribution, temporal and geographic context, methodology, confidence, permissions, licensing, semantic mappings, governance authority, validation status, related or competing claims, and version relationships. A central design principle is the explicit separation of **verification from epistemic validity**. Cryptographic mechanisms may establish the integrity, authorship, sequence, and provenance of a claim record, but they cannot establish the truth of the underlying assertion. Credibility, applicability, and acceptance remain subject to evidence, context, governance, and domain-specific judgment.

The study is organized around four research questions: **RQ1:** What information must accompany a machine-readable claim for its provenance, context, authority, applicability, and revision history to remain interpretable across systems and organizational boundaries? **RQ2:** To what extent can existing Web, Semantic Web, provenance, credentialing, transparency, and cryptographic standards be composed to support such portable claims, and where do interoperability gaps remain? **RQ3:** Can a claim-centered verification architecture establish integrity, authorship, sequence, and governance history without centralizing the underlying knowledge or conflating verification with truth? **RQ4:** How can such a model support federated knowledge commons and AI-mediated retrieval while preserving local or community authority over evidence, definitions, permissions, and contextual interpretation?

The paper develops KCP as an interoperability architecture rather than a replacement for existing standards. Its verification model combines deterministic representation, cryptographic fingerprints, digital signatures, version and governance events, append-oriented histories, Merkle aggregation, and optional external transparency anchoring. Sensitive evidence, personal information, community-controlled data, and mutable knowledge remain within appropriate repositories and governance boundaries. Comparison with nanopublications, W3C PROV, SEPIO, Research Objects, FAIR Digital Objects, Verifiable Credentials, C2PA, SCITT, in-toto, SLSA, and related systems suggests that most individual KCP mechanisms have substantial prior art. The potentially distinctive contribution lies instead in their composition around an authority-scoped, governable, plural knowledge claim.

Educational interoperability is considered as a motivating application through a proposed KCP verification sidecar for standards-conformant Common Cartridge artifacts. More broadly, the paper advances a proposition for investigation: **provenance, context, authority, and governance should travel with knowledge**. KCP is therefore presented not as a universal mechanism for determining truth, but as a possible connective layer among Semantic Web technologies, knowledge graphs, reproducible digital artifacts, trustworthy AI, and community-governed knowledge infrastructures.

---

## 1. Introduction

The history of networked information systems can be understood partly as a history of increasingly sophisticated forms of portability.

The World Wide Web made documents and information resources globally addressable. The Semantic Web extended that architecture toward machine-readable meaning through persistent identifiers, structured assertions, shared vocabularies, ontologies, graph representations, and query languages. Contemporary artificial intelligence introduces another requirement. Systems increasingly retrieve, combine, summarize, transform, and act upon information originating from many independent sources. In such environments, machine-readable meaning alone is insufficient.

A system may need to determine not merely what a statement says, but also who asserted it, what evidence supports it, when and where it applies, what methodology produced it, who has authority over its interpretation, whether it has been challenged, and whether a newer claim has superseded it.

Consider a conventional knowledge-graph assertion:

```text
Community A
    ↓
hasBroadbandCondition
    ↓
ReliabilityConcern
```

The relationship is machine-readable, but it leaves important questions unanswered:

- Who made the assertion?
- What evidence supports it?
- When was the observation made?
- Where does the assertion apply?
- What method produced it?
- Who has authority to interpret or approve it?
- Has it been reviewed?
- Is it contested?
- Has it been superseded?
- Has the record changed since publication?

These questions become particularly consequential when knowledge is consumed by artificial-intelligence systems capable of synthesizing recommendations, generating explanations, or initiating actions.

The Knowledge Claim Packet begins from a simple proposition:

> **Provenance, context, authority, and governance should travel with knowledge.**

The proposal is not that every statement should become immutable, cryptographically signed, or publicly recorded. Nor is KCP intended to create a technological mechanism for determining truth. Instead, KCP asks whether a portable knowledge claim can carry enough information about its evidence, context, provenance, authority, and history to remain interpretable and independently verifiable as it crosses technical and organizational boundaries.

---

## 2. Research Questions

The proposed research is organized around four primary questions.

### RQ1 — Portable Knowledge Context

**What information must accompany a machine-readable claim for its provenance, context, authority, applicability, and revision history to remain interpretable across systems and organizational boundaries?**

This question concerns the minimum viable information necessary to make a claim meaningfully portable without creating an excessively complex representation.

### RQ2 — Standards Composition and Interoperability

**To what extent can existing Web, Semantic Web, provenance, credentialing, transparency, and cryptographic standards be composed to support portable knowledge claims, and where do interoperability gaps remain?**

The objective is explicitly not to replace existing standards where they already provide appropriate capabilities.

### RQ3 — Independent Verification

**Can a claim-centered verification architecture establish integrity, authorship, sequence, and governance history without centralizing the underlying knowledge or conflating verification with truth?**

This question encompasses canonicalization, cryptographic fingerprints, digital signatures, version chains, governance events, Merkle structures, transparency mechanisms, and optional external anchoring.

### RQ4 — Federated Knowledge Governance

**How can portable knowledge claims support federated knowledge commons and AI-mediated retrieval while preserving local or community authority over evidence, definitions, permissions, and contextual interpretation?**

This question extends interoperability beyond technical data exchange to the governance of meaning itself.

---

## 3. Proposed Contributions

The paper proposes four principal research contributions.

### 3.1 A Claim-Centered Knowledge Model

KCP treats the **claim**, rather than the document, dataset, graph, database record, or embedding, as a potentially useful unit of knowledge exchange.

The contribution is not simply the representation of an assertion. Nanopublications and other semantic models already provide strong precedents for atomic assertions with provenance.[^nanopub2010] The research question is whether evidence, applicability, authority, governance, and verification can be composed around the claim in a sufficiently general and interoperable manner.

### 3.2 A Governance Architecture

KCP proposes a distinction among:

- issuer;
- evidence provider;
- reviewer;
- governing authority;
- semantic or community authority;
- relying party; and
- verifier.

It further proposes first-class lifecycle events such as:

```text
REGISTER
REVIEW
APPROVE
CHALLENGE
SUPERSEDE
RETRACT
MAP
DEPRECATE
```

The potentially distinctive element is not any individual event, but their treatment as portable, attributable, potentially signed governance objects that preserve rather than overwrite knowledge history.

### 3.3 A Verification Architecture

KCP proposes a verification pipeline based on established cryptographic mechanisms:

```text
Knowledge Claim Packet
        ↓
Canonicalization
        ↓
Cryptographic Fingerprint
        ↓
Digital Signature
        ↓
Verification Record
        ↓
Append-Oriented History
        ↓
Merkle Batch
        ↓
External Transparency Anchor
```

The contribution is therefore architectural composition rather than a new cryptographic primitive.

### 3.4 An Interoperability Model

KCP is intended to compose with existing standards rather than replace them. Candidate interoperability targets include RDF, JSON-LD, W3C PROV, RDF Dataset Canonicalization, persistent identifiers, Verifiable Credentials, Research Objects, FAIR Digital Objects, C2PA, SCITT, and domain-specific standards.

---

## 4. The Knowledge Claim Packet

A concise definition is:

> **A Knowledge Claim Packet is a portable, machine-readable representation that binds a knowledge assertion to sufficient provenance, evidence, context, authority, governance, and version information to support its interpretation, exchange, and independent verification across systems.**

A conceptual packet may contain:

```text
Knowledge Claim Packet
│
├── Persistent identifier
├── Assertion
│   ├── Subject
│   ├── Relationship
│   └── Object
│
├── Evidence references
├── Source attribution
├── Issuer
├── Authority
├── Temporal context
├── Geographic context
├── Applicability
├── Method
├── Confidence
├── Permissions
├── License
├── Semantic mappings
├── Validation status
├── Supporting claims
├── Competing claims
├── Governance status
├── Version relationships
└── Verification information
```

Not every packet would necessarily contain every field. A core specification could define a minimal interoperable representation while domain profiles add requirements appropriate to science, education, public policy, community knowledge, or other environments.

---

## 5. Claims Rather Than Facts

A foundational design decision is that KCP represents **claims**, not unquestionable facts.

A packet might state:

```text
Claim:
Community A has a broadband reliability concern.

Observed:
March 2027

Evidence:
Community survey and network measurements

Method:
Defined measurement protocol

Issuer:
Organization X

Authority:
Community A

Confidence:
Moderate

Geographic scope:
Community A service area

Status:
Community reviewed

Version:
2.0

Supersedes:
Claim version 1.0
```

The architecture preserves the distinction between:

> “This assertion was made.”

and:

> “This assertion is true.”

That distinction is consistent with adjacent provenance and authenticity systems. SCITT explicitly recognizes that a signed statement may be false and that transparency registration establishes provenance rather than factual accuracy.[^scitt] C2PA similarly addresses content provenance and authenticity rather than determining whether the represented content is true.[^c2pa]

---

## 6. Verification Is Not Truth

KCP separates several questions that are frequently collapsed into a single concept of “trust.”

| Question | Architectural concern |
|---|---|
| Is this the same packet? | Integrity |
| Who issued it? | Authenticity |
| Where did it come from? | Provenance |
| Who has standing to govern it? | Authority |
| Has it changed? | Version history |
| Can its history be independently inspected? | Transparency |
| What supports or contradicts it? | Evidence |
| Where and when does it apply? | Applicability |
| How strongly is it supported? | Confidence |
| Should a relying party depend on it? | Trust |
| Is it sufficiently justified? | Epistemic validity |
| Is the assertion actually correct? | Truth |

Cryptographic verification can address only a subset of these questions.

A valid signature can establish that a particular key signed a particular representation. A cryptographic fingerprint can establish whether the representation changed. A transparency log can provide evidence that a record existed in a particular history.

None of these mechanisms establishes the truth of the underlying assertion.

This distinction is not itself novel. It is well established in authenticity, provenance, credentialing, and transparency systems.[^scitt] [^c2pa] The KCP contribution is to make the distinction an explicit architectural invariant of a portable knowledge-claim system.

---

## 7. Provenance and Evidence

W3C PROV provides a mature general model for provenance through entities, activities, agents, attribution, association, delegation, derivation, revision, invalidation, time, location, and provenance bundles.[^prov]

KCP should therefore not invent a parallel provenance vocabulary where PROV or compatible models are sufficient.

Similarly, SEPIO provides an important precedent for representing scientific assertions, evidence lines, supporting information, methods, agents, confidence, and evaluation provenance.[^sepio]

KCP's research opportunity lies in defining a portable profile that connects these capabilities to:

- claim identity;
- applicability;
- authority;
- governance events;
- competing claims;
- semantic mappings;
- cryptographic verification; and
- federated exchange.

Evidence itself need not be embedded in the packet. A KCP may instead reference evidence through persistent identifiers and cryptographic fingerprints.

This permits:

```text
Knowledge Claim Packet
        │
        ├── Evidence reference A
        ├── Evidence reference B
        └── Evidence reference C
```

while the evidence remains in appropriate repositories.

---

## 8. Issuer and Authority

One of the more important KCP distinctions is between **issuer** and **authority**.

The issuer answers:

> Who technically created or published this packet?

Authority answers:

> Who has standing to approve, govern, interpret, or define this knowledge within the relevant scope?

These roles may be identical, but they need not be.

For example:

```text
Issuer:
Regional research organization

Authority:
Local community

Evidence custodian:
University repository

Reviewer:
Independent technical panel
```

Existing systems already distinguish related roles. PROV supports agents, roles, and delegation.[^prov] PAV distinguishes authors, contributors, curators, creators, sources, and versions.[^pav] Verifiable Credentials distinguish issuers, holders, credential subjects, and verifiers.[^vc] SCITT distinguishes statement issuers, transparency services, registration policies, and relying parties.[^scitt]

KCP's potentially distinctive contribution is therefore narrower: **semantic or community authority as a first-class, scoped property of a portable knowledge claim and its governance history**.

Authority could be scoped by:

- domain;
- geography;
- jurisdiction;
- community;
- vocabulary;
- time;
- purpose; or
- governance policy.

Multiple authorities could legitimately reach different conclusions without requiring the infrastructure to collapse them into one canonical answer.

---

## 9. Governance Events

Knowledge changes through more than content editing. It is reviewed, challenged, approved, mapped, superseded, deprecated, and sometimes withdrawn.

KCP therefore proposes governance events as first-class objects.

### REGISTER

Introduces a claim or version into a governed verification environment.

### REVIEW

Records formal examination of a claim, evidence set, mapping, or other knowledge object.

### APPROVE

Records acceptance by a defined authority for a specified scope or purpose.

### CHALLENGE

Records a formal dispute, objection, or competing interpretation without deleting the original claim.

### SUPERSEDE

Indicates that a newer claim or version replaces an earlier one for a defined purpose while preserving the earlier record.

### RETRACT

Withdraws a claim from active reliance without erasing its historical existence.

### MAP

Records a governed semantic relationship between independently defined concepts or claims.

### DEPRECATE

Indicates that an object should no longer be preferred for future use while retaining it for historical interpretation.

These concepts individually have substantial precedent. PROV represents revision and invalidation.[^prov] Nanopublications support supersession and retraction.[^nanopub] Semantic-reviewing research has represented submissions, reviews, responses, and decisions as nanopublications.[^semanticreview] SCITT supports registration, amended statements, conflicting statements, and supersession.[^scitt]

The research contribution would therefore need to arise from the **uniform lifecycle model**, authority semantics, signed event representation, and preservation of plural governance histories.

---

## 10. Competing Claims

Many knowledge systems implicitly seek a single canonical representation.

KCP instead assumes that disagreement is a normal property of knowledge.

A knowledge environment might contain:

```text
Claim A
   │
   ├── supportedBy → Evidence 1
   └── authority → Community A

Claim B
   │
   ├── supportedBy → Evidence 2
   └── authority → Agency B

Claim C
   │
   ├── contradicts → Claim A
   └── authority → Research Group C
```

The infrastructure need not decide which claim is universally correct.

Instead, it can preserve:

- who asserted each claim;
- what evidence supports it;
- where it applies;
- who recognizes it;
- what contradicts it;
- how it has changed; and
- which relying parties choose to accept it.

SEPIO and evidence-graph systems already provide mechanisms for support and contradiction.[^sepio] SCITT permits conflicting signed statements from multiple issuers.[^scitt]

KCP extends this pattern by coupling disagreement with authority, applicability, semantic mappings, and governance history.

---

## 11. Semantic Interoperability Without Semantic Homogenization

Traditional interoperability efforts can create pressure toward a single canonical vocabulary.

Federated knowledge environments may instead require preservation of legitimate semantic differences.

Consider:

```text
Concept: Digital Access

Federal definition
        ↕
State definition
        ↕
Research definition
        ↕
Tribal definition
        ↕
Local community definition
```

These definitions may overlap without being identical.

A KCP-compatible mapping system could express relationships such as:

```text
broaderThan
narrowerThan
approximatelyEquivalent
usedBy
validWithin
contestedBy
supersedes
```

The `MAP` event would record not merely that a mapping exists, but:

- who asserted the mapping;
- under what authority;
- when it was created;
- what evidence or rationale supports it;
- whether it has been challenged; and
- whether it remains current.

This leads to a broader principle:

> **Semantic interoperability need not require semantic homogenization.**

The related concept of **semantic sovereignty** describes the ability of a community or institution to retain authority over its own definitions and contextual interpretations while participating in interoperable knowledge systems.

---

## 12. Verification Architecture

The proposed verification architecture is intentionally conservative.

### 12.1 Canonicalization

A packet must first be transformed into a deterministic representation.

RDF Dataset Canonicalization 1.0 provides an important standards precedent for deterministic RDF normalization suitable for comparison, hashing, and digital signatures.[^rdfc]

### 12.2 Fingerprinting

The canonical representation can be processed through a cryptographic hash function such as SHA-256.

```text
KCP
 ↓
Canonical representation
 ↓
SHA-256
 ↓
Fingerprint
```

Trusty URIs provide an important precedent for content-addressed semantic objects and nanopublications.[^trusty]

### 12.3 Digital Signatures

The verification record can then be digitally signed.

```text
Verification Record
        +
Issuer Private Key
        ↓
Digital Signature
```

Digital signatures over semantic assertions and structured claims have substantial prior art and should not be presented as a KCP invention.[^semantic-signatures]

### 12.4 Append-Oriented History

Verification and governance events can be recorded in an append-oriented history.

Earlier records remain inspectable even when a claim is superseded or retracted.

### 12.5 Merkle Aggregation

Multiple verification records can be combined through a Merkle tree:

```text
        ROOT
       /    \
     AB      CD
    / \      / \
   A   B    C   D
```

Only the root needs to be externally anchored.

### 12.6 External Transparency

The root or equivalent verification record can be anchored through:

- a transparency service;
- trusted timestamping;
- an institutional log;
- a consortium ledger;
- multiple independent services; or
- optionally, a public blockchain.

SCITT and Certificate Transparency provide strong precedents for append-only, independently auditable transparency structures.[^scitt] [^ct]

---

## 13. Blockchain as an Optional Adapter

Blockchain should not be the center of the KCP architecture.

The stronger principle is:

> **Blockchain may notarize knowledge history; it should not contain the knowledge itself.**

The architecture therefore separates:

```text
OFF-CHAIN / GOVERNED

Knowledge
Evidence
Documents
Community information
Personal information
Learner records

        │
        │ identifiers / fingerprints
        ▼

VERIFICATION LAYER

Claim identifier
Fingerprint
Issuer
Authority
Version
Governance event
Timestamp
Signature
```

This separation is important because immutable infrastructure can conflict with:

- correction;
- withdrawal;
- privacy;
- consent;
- community governance;
- legal deletion requirements; and
- changing access conditions.

SCITT already supports detached or hashed payloads, including cases involving large or sensitive content.[^scitt] KCP therefore does not claim novelty for off-chain storage itself.

Its research contribution would concern the governance rules determining **what must be public, what may remain private, and how a verifier distinguishes unavailable evidence from nonexistent evidence**.

---

## 14. Closest Precedents

### 14.1 Nanopublications

Nanopublications are the closest established precedent to the claim-centered portion of KCP.

The nanopublication model was introduced to make scientific assertions identifiable, attributable, connectable, and assessable in context.[^nanopub2010] Contemporary nanopublication infrastructure supports small RDF knowledge graphs, provenance, publication metadata, Trusty URI content addressing, signatures, immutable publication, supersession, retraction, licensing, and decentralized replication.[^nanopub]

KCP therefore should not claim to invent:

- atomic knowledge claims;
- claim-level provenance;
- immutable semantic publication;
- content-addressed semantic objects;
- signed semantic claims;
- supersession; or
- retraction.

### 14.2 W3C PROV

PROV provides a mature provenance framework based on entities, activities, and agents.[^prov]

It already supports:

- attribution;
- association;
- delegation;
- derivation;
- revision;
- invalidation;
- primary sources;
- quotation;
- time;
- location; and
- provenance bundles.

KCP should reuse or map to PROV rather than create a competing provenance ontology.

### 14.3 SEPIO

SEPIO is particularly relevant to KCP's epistemic layer because it models scientific assertions, evidence, methods, agents, confidence, and evaluation provenance.[^sepio]

Its profile-oriented approach also demonstrates that a shared semantic core can coexist with domain-specific extensions.

### 14.4 Research Objects and RO-Crate

Research Objects and RO-Crate package research artifacts with structured metadata, contributors, licensing, actions, and provenance.[^rocrate]

Their primary unit, however, is an aggregate research object rather than an independently governed atomic claim.

### 14.5 FAIR Digital Objects

FAIR Digital Objects combine persistent identifiers, metadata, typing, predictable resolution, and machine-actionable operations.[^fdo]

KCP can be understood as exploring whether a **knowledge claim** can behave as a specialized digital object with additional epistemic and governance semantics.

### 14.6 Verifiable Credentials

The W3C Verifiable Credentials model provides cryptographically verifiable claims and distinguishes issuer, holder, credential subject, and verifier roles.[^vc]

KCP differs primarily in purpose. A KCP is not necessarily a credential about a subject. It is intended as a general knowledge-governance object.

### 14.7 C2PA

C2PA provides provenance and authenticity mechanisms for digital media.[^c2pa]

Its importance to KCP is conceptual: provenance and authenticity can be verified without claiming that the represented content is factually true.

### 14.8 SCITT

SCITT is the closest precedent to the proposed KCP transparency layer.

It provides:

- signed statements;
- issuer identities;
- transparency services;
- registration policies;
- append-only verifiable histories;
- receipts;
- independent auditing;
- conflicting statements;
- supersession;
- detached sensitive payloads; and
- relying-party trust decisions.[^scitt]

SCITT substantially anticipates the KCP verification substrate.

The principal distinction is that SCITT intentionally treats statement content as domain-specific, whereas KCP proposes a normative model for knowledge claims, evidence, applicability, semantic authority, competing claims, and governance events.

### 14.9 in-toto and SLSA

in-toto and SLSA provide important precedents for software supply-chain provenance and artifact attestations.[^intoto] [^slsa]

KCP applies a related question to knowledge:

> Can a relying party determine where a knowledge artifact came from, what transformations occurred, who authorized them, and whether the artifact has changed?

---

## 15. Novelty Assessment

The strongest conclusion from the current prior-art review is that **KCP's individual mechanisms are largely established**.

### Established mechanisms

Strong prior art exists for:

- machine-readable claims;
- persistent identifiers;
- provenance;
- evidence graphs;
- statement metadata;
- canonicalization;
- cryptographic hashing;
- digital signatures;
- content addressing;
- version chains;
- supersession;
- retraction;
- append-only logs;
- Merkle trees;
- transparency services;
- blockchain anchoring;
- detached sensitive payloads; and
- authenticity-versus-truth distinctions.

### Potentially distinctive integration

The more defensible originality lies in the combination of:

```text
Portable claim
      +
Evidence
      +
Applicability
      +
Provenance
      +
Issuer
      +
Semantic/community authority
      +
Competing claims
      +
Signed governance events
      +
Version history
      +
Transparency verification
      +
Federated custody
```

No single reviewed architecture clearly combines this complete set as one general-purpose knowledge-governance protocol.

That conclusion should remain cautious. It is an academic prior-art assessment, not a legal patentability determination.

---

## 16. Narrowest Defensible Originality Claim

The narrowest defensible formulation is:

> **KCP proposes a federated, authority-scoped lifecycle for portable knowledge claims in which signed governance events preserve approval, challenge, semantic mapping, supersession, retraction, and deprecation without erasing competing claims or conflating cryptographic verification with epistemic validity.**

A broader but still defensible academic formulation is:

> **KCP integrates established provenance, semantic-web, cryptographic, and transparency mechanisms around a portable knowledge claim whose evidence, contextual applicability, authority, competing interpretations, and governance history remain independently represented and auditable.**

Claims that should be avoided include assertions that KCP is:

- the first portable signed knowledge claim;
- the first claim-plus-provenance representation;
- the first immutable semantic assertion;
- the first signed review system;
- the first system supporting supersession or retraction;
- the first use of Merkle trees for provenance;
- the first blockchain knowledge-provenance architecture;
- the first system preserving conflicting signed statements; or
- the first architecture distinguishing authenticity from truth.

---

## 17. Federated Knowledge Commons

KCP is particularly relevant to a federated knowledge commons.

Consider:

```text
Community A
      │
Community B
      │
Library
      │
University
      │
Government agency
      │
Research organization
```

Each participant may maintain its own:

- repositories;
- vocabularies;
- evidence;
- permissions;
- governance;
- interpretations; and
- technical infrastructure.

KCP asks whether these participants can exchange claims without requiring a single centralized knowledge authority.

The resulting architecture is not a universal database of truth.

It is closer to:

> **a verifiable record of what was asserted, by whom, based on what evidence, under what conditions, with what authority, and how understanding changed over time.**

This distinction is especially important for community-governed knowledge.

The CARE Principles for Indigenous Data Governance emphasize Collective Benefit, Authority to Control, Responsibility, and Ethics, providing an important governance counterweight to purely technical notions of openness and interoperability.[^care]

KCP should not presume that cryptographic verifiability creates a right to access, publish, or reuse knowledge.

---

## 18. Provenance-Aware AI Retrieval

Conventional retrieval-augmented generation commonly follows:

```text
Question
   ↓
Retrieve documents or chunks
   ↓
Rank by relevance
   ↓
Generative model
   ↓
Answer
```

A KCP-aware architecture could instead support:

```text
Question
   ↓
Entity resolution
   ↓
Context resolution
   ↓
Candidate claims
   ↓
Applicability filtering
   ↓
Authority evaluation
   ↓
Provenance evaluation
   ↓
Evidence retrieval
   ↓
Competing-claim retrieval
   ↓
Revision-history check
   ↓
Generative synthesis
   ↓
Answer + evidence trail
```

This idea also has emerging precedents. Provenance-aware retrieval systems and evidence graphs increasingly preserve source relationships, supporting and contradicting evidence, and source-tracing metadata.

KCP's research question is therefore not whether provenance-aware retrieval is entirely new.

It is whether retrieval over the complete:

```text
claim
+
evidence
+
authority
+
applicability
+
competition
+
revision
+
governance
```

bundle produces measurable improvements in:

- source attribution;
- contradiction handling;
- temporal applicability;
- geographic applicability;
- abstention;
- superseded-claim detection;
- auditability; and
- explanation.

---

## 19. Educational Interoperability as a Testbed

Educational interoperability provides a bounded environment in which KCP can be tested against mature standards.

The proposed architecture is:

```text
Source Course Graph
        │
        ▼
Reproducible Build
        │
        ├── CASE competencies
        ├── QTI assessments
        ├── LTI integrations
        └── learning resources
        │
        ▼
Common Cartridge
        +
KCP Release Sidecar
        │
        ▼
Validation
        │
        ▼
LMS Import
```

Common Cartridge remains the standards-conformant portability boundary.[^cc]

KCP does not replace:

- Common Cartridge;
- CASE;
- QTI;
- LTI;
- Open Badges; or
- Comprehensive Learner Records.

Instead, a KCP sidecar could state:

> This cartridge was generated from this source repository and revision, using these competency mappings and assessment versions, under these licenses, through this build process, passed these validation tests, was issued by this organization, has this cryptographic fingerprint, and supersedes this earlier release.

This creates an educational analogue to software supply-chain provenance.

---

## 20. DOIN and the Course Interchange

Within the developing **Digital Opportunities Intelligence Network (DOIN)**, KCP could become the portable claim and verification layer beneath a broader knowledge commons.

A future DOIN Course Interchange could treat Common Cartridge as one serialization or export profile of a richer source graph.

```text
Source Course Graph
        │
        ├── Resources
        ├── Competencies
        ├── Assessments
        ├── Tools
        ├── Adaptations
        ├── Provenance
        └── Governance
        │
        ▼
KCP / Provenance Layer
        │
        ├── Common Cartridge
        ├── QTI
        ├── CASE
        ├── LTI
        └── Other profiles
```

The important architectural principle is that DOIN should not create a proprietary island.

Established standards should remain responsible for the domains they already serve.

KCP should fill only the provenance and governance gaps that remain.

---

## 21. Research Methodology

The proposed research can be pursued through a design-science methodology combining conceptual modeling, standards analysis, prototype development, interoperability testing, and comparative evaluation.

### Phase 1 — Conceptual Model

Define:

- minimal KCP core;
- optional profiles;
- authority model;
- applicability model;
- evidence relationships;
- governance-event vocabulary; and
- version semantics.

### Phase 2 — Minimal Verification

Implement:

```text
KCP
 ↓
canonicalization
 ↓
fingerprint
 ↓
verification record
 ↓
append-oriented history
```

### Phase 3 — Digital Signatures

Add:

```text
Issuer
  ↓
Key
  ↓
Signature
  ↓
Verification
```

The implementation should remain algorithm-agile.

### Phase 4 — Merkle Batching

Aggregate verification records:

```text
Verification records
        ↓
Merkle tree
        ↓
Merkle root
```

### Phase 5 — External Transparency

Anchor the Merkle root through an independent transparency or timestamping mechanism.

Only after this architecture works end-to-end should a blockchain adapter be evaluated.

### Phase 6 — Educational Interoperability

Test KCP against a reproducible Common Cartridge workflow.

### Phase 7 — Provenance-Aware Retrieval

Compare KCP-aware retrieval with document-, vector-, and graph-centered retrieval.

### Phase 8 — Federated Knowledge Exchange

Test exchange among independently governed repositories and authorities.

---

## 22. Evaluation

KCP should be evaluated across four dimensions.

### Technical

- deterministic verification;
- tamper detection;
- signature verification;
- version-chain integrity;
- Merkle-proof verification;
- transparency verification; and
- independent implementation compatibility.

### Semantic

- preservation of claim identity;
- provenance;
- applicability;
- authority;
- semantic mappings;
- evidence relationships; and
- competing claims.

### Governance

- authority separation;
- review;
- challenge;
- supersession;
- retraction;
- mapping;
- deprecation; and
- preservation of historical states.

### AI Retrieval

- citation accuracy;
- source traceability;
- contradiction detection;
- temporal applicability;
- geographic applicability;
- superseded-claim detection;
- abstention; and
- reconstruction of the evidentiary basis of an answer.

---

## 23. Risks and Limitations

### Excessive complexity

A packet containing every possible provenance and governance field could become impractical.

**Mitigation:** define a minimal core and optional profiles.

### Duplication of standards

KCP could inadvertently recreate capabilities already provided by PROV, Verifiable Credentials, SCITT, nanopublications, or domain standards.

**Mitigation:** require explicit reuse-or-gap analysis before introducing new constructs.

### False assurance

Users may interpret a valid signature as evidence that a claim is true.

**Mitigation:** make verification-versus-validity separation normative in the specification and APIs.

### Privacy leakage

Hashes, identifiers, timestamps, and relationship metadata can themselves reveal sensitive information.

**Mitigation:** apply minimum-disclosure principles and threat modeling to verification metadata.

### Semantic centralization

Interoperability mechanisms can unintentionally privilege one vocabulary or authority.

**Mitigation:** preserve scoped authority and explicit mappings rather than silently collapsing meanings.

### Governance capture

A technically decentralized system can still become institutionally centralized.

**Mitigation:** make authority, policy, and governance events inspectable and permit multiple independent authorities.

---

## 24. Discussion

The strongest interpretation of KCP is not as a new cryptographic technology.

Hashing, signatures, canonicalization, Merkle trees, transparency logs, provenance ontologies, persistent identifiers, and signed statements are established technologies.

Nor is the strongest interpretation that KCP invents atomic semantic claims. Nanopublications provide substantial prior art.

The more interesting research question is architectural:

> **What happens when the portable unit is not merely a signed assertion, but a governable knowledge claim whose evidence, applicability, authority, competing interpretations, semantic mappings, and lifecycle remain independently inspectable?**

This shifts the problem from:

> Can we prove who signed this statement?

toward:

> Can we preserve enough of the social, semantic, evidentiary, and governance context of a claim for another system to interpret it responsibly?

That is a substantially different objective.

It also suggests that trustworthy knowledge infrastructure cannot be reduced to cryptography.

Trust emerges from the interaction of:

```text
Identity
+
Integrity
+
Evidence
+
Context
+
Authority
+
Governance
+
Transparency
+
Judgment
```

KCP attempts to make those relationships explicit without pretending that any technical mechanism can eliminate uncertainty or disagreement.

---

## 25. Conclusion

The Web made information addressable.

The Semantic Web made relationships and meaning increasingly machine-readable.

Artificial intelligence and federated knowledge systems now expose another requirement: knowledge must remain connected to the evidence, context, authority, and history necessary to interpret it responsibly.

The Knowledge Claim Packet is proposed as one possible response.

Its central proposition is straightforward:

> **Provenance, context, authority, and governance should travel with knowledge.**

The current prior-art assessment suggests that KCP's originality should not be framed around individual technical mechanisms. Nanopublications, W3C PROV, SEPIO, Research Objects, FAIR Digital Objects, Verifiable Credentials, C2PA, SCITT, transparency logs, in-toto, SLSA, and related systems already occupy substantial portions of the design space.

The potentially distinctive contribution lies instead in their disciplined composition around a **portable, authority-scoped, governable, plural knowledge claim**.

Such a claim can be signed without being declared true.

It can be challenged without being erased.

It can be superseded without losing its history.

It can be mapped to another community's terminology without surrendering its original meaning.

It can carry evidence without requiring that evidence to become public.

It can participate in a shared knowledge commons without requiring a single centralized authority.

The long-term objective is therefore not a universal database of truth.

It is something more modest and potentially more useful:

> **a verifiable record of what was asserted, by whom, based on what evidence, under what conditions, with what authority, and how understanding changed over time.**

That is the research opportunity represented by the Knowledge Claim Packet.

---

# Glossary

## A

### AI — Artificial Intelligence

Computer systems designed to perform tasks associated with human intelligence, including reasoning, language processing, retrieval, classification, and generation. In the KCP architecture, AI is primarily considered as a consumer of provenance-aware knowledge claims.

### Append-Only Log

A record structure in which new entries may be added but existing entries are not silently modified or removed. Append-only logs support auditability and tamper detection in the KCP verification layer.

### Applicability

The conditions under which a knowledge claim is relevant or appropriately interpreted, including time, geography, jurisdiction, population, methodology, or other contextual boundaries.

### Assertion

A machine-readable statement expressing a proposition about an entity, relationship, event, observation, or condition. An assertion is the semantic core of a Knowledge Claim Packet.

### Attestation

A signed statement asserting something about an artifact, process, identity, or event. Software supply-chain systems such as in-toto and SLSA use attestations to describe how artifacts were produced.

### Authority

An individual, community, institution, or other entity recognized as having responsibility for approving, governing, interpreting, or defining a claim within a particular scope. KCP distinguishes authority from the technical issuer of a claim.

---

## B

### Blockchain

A distributed ledger in which records are cryptographically linked and replicated among participants. In KCP, blockchain is considered an optional external anchoring mechanism rather than the repository for knowledge or evidence.

---

## C

### C2PA — Coalition for Content Provenance and Authenticity

An industry standards organization developing technical specifications for recording the provenance and editing history of digital media. C2PA is an important precedent for distinguishing content provenance and authenticity from truth.

### Canonicalization

The process of converting a digital representation into a deterministic form so that equivalent representations produce the same cryptographic fingerprint. Canonicalization is necessary for reliable hashing and digital signatures.

### CARE Principles

Principles for Indigenous Data Governance organized around **Collective Benefit, Authority to Control, Responsibility, and Ethics**. They emphasize governance and community authority over data and knowledge rather than unrestricted openness.

### Challenge

A governance event indicating that an existing claim, interpretation, mapping, or evidentiary basis has been formally questioned. In KCP, a challenge does not automatically erase or invalidate the challenged claim.

### Claim

A proposition asserted about an entity, relationship, observation, event, or condition. KCP treats claims as attributable, contextual, revisable assertions rather than unquestioned facts.

### Common Cartridge

A 1EdTech interoperability standard for packaging and exchanging digital learning materials among learning-management systems and other educational platforms.

### Community Authority

Authority held by a community to define, interpret, approve, restrict, challenge, or govern knowledge concerning its own context, terminology, experience, or interests.

### Competing Claims

Two or more claims that provide different, incompatible, or contradictory assertions about the same or related subjects. KCP is designed to preserve competing claims rather than requiring the infrastructure to force consensus.

### Confidence

An assessment of the strength, reliability, or certainty associated with a claim. Confidence is an epistemic property and should not be confused with cryptographic verification.

### Content Addressing

Identifying a digital object using a cryptographic digest derived from its contents rather than solely through a location-based identifier.

### Cryptographic Anchor

A cryptographically verifiable reference placed in an independent system to demonstrate that a particular record or collection of records existed in a particular state.

### Cryptographic Fingerprint

A fixed-length digest generated from digital content using a cryptographic hash function. A fingerprint can reveal whether the content has changed.

---

## D

### Decentralized Knowledge Graph

A knowledge graph whose information, governance, or storage is distributed among multiple independently operated systems rather than controlled by a single central repository.

### Deprecation

A governance action indicating that a claim, vocabulary term, mapping, specification, or other object should no longer be preferred for future use while preserving its historical existence.

### DID — Decentralized Identifier

A type of persistent identifier designed to support decentralized identity systems without requiring a single centralized identity provider.

### Digital Signature

A cryptographic mechanism allowing a verifier to determine whether digital content was signed using a particular cryptographic key and whether the signed content has subsequently changed.

### Distributed Ledger

A replicated record system maintained across multiple participants or nodes. Blockchain is one form of distributed ledger.

### DOI — Digital Object Identifier

A persistent identifier commonly used for scholarly publications, datasets, and other research objects.

### DOIN — Digital Opportunities Intelligence Network

A developing knowledge-infrastructure framework used as a motivating environment for KCP research. DOIN treats knowledge graphs, provenance, governance, and continuous learning as components of a broader knowledge commons.

### DOIN Course Interchange

A proposed architecture in which course content, competencies, assessments, tools, provenance, and adaptations are represented in a richer source model while established standards such as Common Cartridge remain interoperability and export boundaries.

---

## E

### Epistemic Assessment

Evaluation of whether a claim is credible, justified, applicable, or sufficiently supported by evidence.

### Epistemic Validity

The degree to which a claim is justified or credible based on evidence, methodology, context, reasoning, and relevant standards of judgment. Cryptographic verification does not establish epistemic validity.

### Evidence

Information offered in support of or opposition to a claim, including observations, measurements, datasets, documents, testimony, analyses, or other claims.

### Evidence Graph

A graph representation connecting claims to supporting or contradicting evidence, sources, methods, contributors, and related claims.

---

## F

### FAIR — Findable, Accessible, Interoperable, and Reusable

Principles for improving the management and reuse of digital research objects and data.

### FAIR Digital Object — FDO

A machine-actionable digital object associated with a persistent identifier, metadata, type information, and defined operations intended to support FAIR digital infrastructure.

### Federated Knowledge Commons

A knowledge environment in which independently governed communities, institutions, or systems exchange and relate knowledge while retaining control over their own evidence, definitions, permissions, and governance.

### Fingerprint

See **Cryptographic Fingerprint**.

---

## G

### Governance

The policies, roles, authorities, and processes through which claims and related knowledge objects are registered, reviewed, approved, challenged, mapped, superseded, retracted, or deprecated.

### Governance Event

A recorded action affecting the status, interpretation, or lifecycle of a claim. Proposed KCP events include `REGISTER`, `REVIEW`, `APPROVE`, `CHALLENGE`, `SUPERSEDE`, `RETRACT`, `MAP`, and `DEPRECATE`.

### Governance History

The ordered record of governance events associated with a claim or knowledge object.

---

## H

### Hash

The output of a mathematical function that converts digital content into a fixed-length value. Cryptographic hashes are designed so that even small changes to the input produce substantially different outputs.

---

## I

### in-toto

A software supply-chain security framework for recording and verifying the steps through which software artifacts are produced. It is an important precedent for KCP's proposed knowledge-artifact supply-chain model.

### Integrity

The property that a digital object remains unchanged relative to a previously established representation.

### Interoperability

The ability of independently developed systems to exchange, interpret, and use information while preserving an acceptable degree of meaning and function.

### Issuer

The person, organization, system, or agent that creates or publishes a claim, credential, attestation, or verification record. In KCP, the issuer is explicitly distinguishable from the authority governing the claim.

---

## K

### KCP — Knowledge Claim Packet

A proposed portable, machine-readable representation that binds a knowledge assertion to provenance, evidence, context, authority, governance, applicability, version history, and verification information.

### Knowledge Commons

A shared environment in which knowledge resources are contributed, governed, maintained, and reused collectively under defined institutional or community arrangements.

### Knowledge Graph

A structured representation of entities, concepts, and relationships, typically expressed as nodes and edges with machine-readable semantics.

### Knowledge Provenance

The documented origin and history of a knowledge claim, including its sources, evidence, contributors, methods, transformations, derivations, revisions, and governance events.

---

## L

### Lifecycle Event

An event representing a change in the status or governance of a claim, such as registration, review, approval, challenge, supersession, retraction, mapping, or deprecation.

---

## M

### MAP

A proposed KCP governance event recording a semantic relationship between independently defined concepts, claims, vocabularies, or identifiers.

### Merkle Batch

A collection of verification records whose hashes are combined through a Merkle tree so that the entire collection can be represented by a single root hash.

### Merkle Root

The top-level cryptographic hash produced by a Merkle tree. Anchoring the root can provide evidence about the integrity of all records included in the tree.

### Merkle Tree

A hierarchical cryptographic structure in which hashes of individual records are recursively combined into a single root hash. Merkle trees support efficient integrity and inclusion proofs.

### Minimum Disclosure

An architectural principle under which only the information necessary for a particular verification or governance purpose is disclosed, while sensitive evidence or knowledge remains protected.

---

## N

### Nanopublication

A small, machine-readable scholarly publication centered on an atomic assertion and accompanied by provenance and publication information. Nanopublications are one of the closest established precedents to the claim-centered portion of KCP.

---

## O

### Off-Chain

Information stored outside a blockchain or immutable ledger. KCP proposes keeping substantive knowledge, evidence, personal information, and sensitive community data off-chain while optionally anchoring minimal cryptographic verification information.

---

## P

### PAV — Provenance, Authoring and Versioning

A lightweight provenance vocabulary that distinguishes roles such as author, contributor, curator, creator, source, and version relationships.

### Persistent Identifier — PID

A durable identifier intended to continue identifying an entity or object even if its storage location or implementation changes.

### Prior Art

Publicly available knowledge, publications, patents, systems, standards, or disclosures that predate a proposed invention and may be relevant when assessing originality or patent novelty.

### PROV / PROV-O — W3C Provenance / Provenance Ontology

A W3C family of standards for representing provenance through entities, activities, agents, derivations, attribution, delegation, revision, and related relationships.

### Provenance

Information describing the origin, custody, derivation, transformation, attribution, and history of a digital object or knowledge claim.

### Provenance-Aware Retrieval

A retrieval approach that considers not only semantic relevance but also source, evidence, authority, time, geography, confidence, applicability, and revision history.

---

## Q

### QTI — Question and Test Interoperability

A 1EdTech standard for exchanging digital assessment items, tests, response processing, and related assessment information.

---

## R

### RAG — Retrieval-Augmented Generation

An AI architecture in which external information is retrieved and supplied to a generative model as context for producing an answer.

### RDF — Resource Description Framework

A W3C data model for representing machine-readable statements as relationships among identified resources.

### RDF 1.2

A newer generation of RDF specifications that, among other capabilities, supports richer mechanisms for making statements about individual RDF statements.

### RDFC-1.0 — RDF Dataset Canonicalization 1.0

A W3C specification defining deterministic canonicalization of RDF datasets so that equivalent datasets can be consistently compared, hashed, or digitally signed.

### Research Object

A structured aggregation of research materials such as data, software, workflows, documentation, and provenance.

### RETRACT

A proposed KCP governance event indicating that an authority or issuer has withdrawn a claim from active reliance while preserving its historical record.

### REVIEW

A proposed KCP governance event recording formal examination of a claim, evidence set, mapping, or other knowledge object.

### RO-Crate — Research Object Crate

A structured packaging approach based on JSON-LD for describing research objects, their constituent resources, contributors, licensing, and provenance.

---

## S

### SCITT — Supply Chain Integrity, Transparency, and Trust

An IETF architecture for signed statements, transparency services, registration policies, receipts, and independently verifiable histories. SCITT is one of the closest precedents to KCP's proposed verification and transparency layer.

### Semantic Authority

Authority to define, interpret, approve, or govern the meaning of a concept or relationship within a particular community, institution, domain, or context.

### Semantic Digital Signature

A digital-signature approach applied to semantic assertions or structured knowledge rather than merely to an opaque file.

### Semantic Homogenization

The process of forcing independently defined concepts or vocabularies into a single supposedly universal meaning.

### Semantic Interoperability

The ability of systems to exchange information while preserving or appropriately mapping its meaning.

### Semantic Mapping

An explicit relationship between concepts, identifiers, vocabularies, or ontologies indicating equivalence, approximation, hierarchy, replacement, or another semantic relationship.

### Semantic Sovereignty

A proposed principle under which a community or institution retains authority over its own definitions, classifications, and contextual interpretations while participating in interoperable knowledge systems.

### Semantic Web

Web standards and practices intended to make data and relationships machine-readable through globally identifiable resources, structured representations, shared vocabularies, and formal semantics.

### SEPIO — Scientific Evidence and Provenance Information Ontology

An ontology for representing scientific assertions, evidence, provenance, confidence, methods, and related epistemic information.

### SHA-256 — Secure Hash Algorithm 256-bit

A widely used cryptographic hash function producing a 256-bit digest.

### Sidecar

A separate but associated file or object that adds information to a primary artifact without changing the primary artifact's format. A KCP could, for example, accompany a Common Cartridge as a provenance and verification sidecar.

### Signed Governance Event

A governance event whose contents and responsible actor are cryptographically signed, allowing its integrity and authorship to be independently checked.

### Signed Statement

A machine-readable assertion accompanied by a digital signature establishing its cryptographic origin and integrity.

### SLSA — Supply-chain Levels for Software Artifacts

A framework for improving software supply-chain integrity through provenance, build controls, and artifact attestations. KCP draws an analogy between software supply-chain provenance and knowledge-artifact provenance.

### Solid

A set of decentralized Web technologies associated with user-controlled data storage and interoperable applications. Solid is relevant to KCP's federated and locally governed knowledge model.

### SUPERSEDE

A proposed KCP governance event indicating that a newer claim or version replaces an earlier one for a defined purpose while preserving the earlier record.

### Supersession

The relationship between an earlier claim or version and a newer claim intended to replace it.

---

## T

### Transparency Anchor

An independently verifiable record demonstrating that a particular verification record or Merkle root existed at a particular point or sequence in history.

### Transparency Log

An append-oriented, independently auditable record system used to make signed statements or verification events inspectable and tamper-evident.

### Trust

A contextual judgment about whether an actor, source, process, claim, or system should be relied upon for a particular purpose. Trust is distinct from cryptographic verification.

### Trusty URI

A content-addressed URI mechanism developed in connection with nanopublications that incorporates a cryptographic hash into an identifier, allowing the referenced content to be independently verified.

---

## V

### Validation

Evaluation of an object against structural, semantic, procedural, or domain-specific requirements. Passing validation does not necessarily establish that a claim is true.

### VC — Verifiable Credential

A cryptographically verifiable digital credential conforming to the W3C Verifiable Credentials model. VCs distinguish roles such as issuer, holder, credential subject, and verifier.

### Verification

The process of determining whether specified properties—such as integrity, signature validity, authorship, sequence, or anchoring—can be independently confirmed.

### Verification Record

A minimal record associated with a KCP that may contain its identifier, version, fingerprint, issuer, authority, timestamp, predecessor relationship, governance event, and digital signature.

### Version Chain

An ordered relationship among successive versions of a claim or packet in which each version can reference its predecessor.

---

## W

### W3C — World Wide Web Consortium

An international standards organization responsible for Web standards relevant to KCP, including RDF, PROV, Verifiable Credentials, and RDF Dataset Canonicalization.

---

# KCP Governance Event Vocabulary

| Event | Meaning |
|---|---|
| `REGISTER` | Introduces a claim or version into a governed verification environment. |
| `REVIEW` | Records formal examination of a claim, evidence set, or mapping. |
| `APPROVE` | Records acceptance by a defined authority for a specified scope or purpose. |
| `CHALLENGE` | Records a formal dispute, objection, or competing interpretation without deleting the original claim. |
| `SUPERSEDE` | Indicates that a newer claim or version replaces an earlier one while preserving history. |
| `RETRACT` | Withdraws a claim from active reliance without erasing its historical existence. |
| `MAP` | Records a governed semantic relationship between independently defined concepts or claims. |
| `DEPRECATE` | Indicates that an object should no longer be preferred for future use while retaining it for historical interpretation. |

---

# Core KCP Distinctions

| Term | Question |
|---|---|
| **Integrity** | Is this the same digital object that was originally registered? |
| **Authenticity** | Did the identified issuer sign this object? |
| **Provenance** | Where did this knowledge come from and how did it develop? |
| **Authority** | Who has standing to govern or interpret it in this context? |
| **Transparency** | Can its recorded history be independently inspected? |
| **Evidence** | What supports or contradicts the assertion? |
| **Applicability** | Where, when, and under what conditions does the claim apply? |
| **Confidence** | How strongly is the claim supported or assessed? |
| **Trust** | Should a particular relying party depend on it for this purpose? |
| **Epistemic validity** | Is the claim sufficiently justified by evidence and reasoning? |
| **Truth** | Is the underlying assertion actually correct? |

> **Cryptographic verification can establish identity, integrity, authorship, and history; it cannot establish the truth of a knowledge claim.**

---

# References

[^nanopub2010]: Groth, P., Gibson, A., & Velterop, J. (2010). *The anatomy of a nanopublication*. Information Services & Use, 30(1–2), 51–56. This work introduced the nanopublication model as a mechanism for publishing small scientific assertions together with provenance and publication information.

[^nanopub]: Nanopublications. *Nanopublication Guidelines and Technical Documentation*. Nanopublication infrastructure provides assertion, provenance, publication-information, Trusty URI, signing, versioning, supersession, retraction, and decentralized-publication mechanisms. See the Nanopublications project and associated technical specifications.

[^trusty]: Kuhn, T., & Dumontier, M. (2015). *Trusty URIs: Verifiable, immutable, and permanent digital artifacts for linked data*. Trusty URIs provide content-addressed identifiers for RDF and nanopublication artifacts.

[^prov]: World Wide Web Consortium. (2013). *PROV-O: The PROV Ontology*. W3C Recommendation. https://www.w3.org/TR/prov-o/

[^pav]: Ciccarese, P., Soiland-Reyes, S., Belhajjame, K., Gray, A. J. G., Goble, C., & Clark, T. *PAV ontology: Provenance, Authoring and Versioning*. PAV distinguishes authorship, contribution, curation, creation, source, and version relationships.

[^sepio]: Scientific Evidence and Provenance Information Ontology project. *SEPIO: Scientific Evidence and Provenance Information Ontology*. SEPIO provides models for scientific assertions, evidence, methods, confidence, and provenance.

[^rocrate]: RO-Crate Research Data Packaging. *RO-Crate Specification*. https://www.researchobject.org/ro-crate/ . RO-Crate uses JSON-LD to describe research objects, constituent resources, contributors, licensing, actions, and provenance.

[^fdo]: FAIR Digital Objects Forum. *FAIR Digital Object Framework*. FAIR Digital Objects combine persistent identifiers, metadata, typing, predictable resolution, and machine-actionable operations.

[^vc]: World Wide Web Consortium. *Verifiable Credentials Data Model*. https://www.w3.org/TR/vc-data-model/ . The model distinguishes credential issuers, holders, subjects, and verifiers and provides mechanisms for cryptographically verifiable claims.

[^c2pa]: Coalition for Content Provenance and Authenticity. *C2PA Technical Specification*. https://c2pa.org/specifications/ . C2PA provides mechanisms for recording and verifying digital-content provenance and editing history while distinguishing provenance from factual truth.

[^scitt]: Internet Engineering Task Force. (2026). *RFC 9943: An Architecture for Trustworthy and Transparent Digital Supply Chains / Supply Chain Integrity, Transparency, and Trust (SCITT)*. SCITT defines signed statements, transparency services, registration policies, receipts, append-only verifiable histories, conflicting statements, supersession, and detached payload patterns.

[^rdfc]: World Wide Web Consortium. (2024). *RDF Dataset Canonicalization 1.0*. W3C Recommendation. https://www.w3.org/TR/rdf-canon/ . RDFC-1.0 defines deterministic canonicalization of RDF datasets for comparison, hashing, and digital signatures.

[^semanticreview]: Research on nanopublication-based semantic reviewing has demonstrated machine-readable representations of scholarly submissions, reviews, responses, decisions, and publication processes, providing prior art for governance events around semantic claims.

[^semantic-signatures]: Prior work and patent literature on semantic digital signatures predates KCP, including systems for digitally signing semantic assertions and structured knowledge representations. The KCP proposal therefore treats digital signatures as an established mechanism rather than a novel cryptographic contribution.

[^ct]: Laurie, B., Langley, A., & Kasper, E. (2013). *RFC 6962: Certificate Transparency*. Internet Engineering Task Force. Certificate Transparency established widely used patterns for append-only Merkle-tree transparency logs and independent auditing.

[^intoto]: Torres-Arias, S., Afzali, H., Kuppusamy, T. K., Curtmola, R., & Cappos, J. *in-toto: Providing farm-to-table guarantees for bits and bytes*. The in-toto framework records and verifies software supply-chain steps and provides an important precedent for artifact provenance.

[^slsa]: Open Source Security Foundation. *Supply-chain Levels for Software Artifacts (SLSA)*. https://slsa.dev/ . SLSA defines provenance and integrity practices for software artifacts and build systems.

[^care]: Global Indigenous Data Alliance. *CARE Principles for Indigenous Data Governance*. https://www.gida-global.org/care . CARE defines Collective Benefit, Authority to Control, Responsibility, and Ethics as principles for Indigenous data governance.

[^cc]: 1EdTech Consortium. *Common Cartridge Specification*. https://www.1edtech.org/standards/common-cartridge . Common Cartridge defines interoperable packaging and exchange of digital learning resources among educational platforms.
