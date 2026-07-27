---
title: "Organize Before You Encode: Jessica Talisman's Ontology Pipeline as a Blueprint for Knowledge Infrastructure"
subtitle: "A Compass Series Working Paper"
author: "Jason Kronemeyer"
affiliation: "EUPConnect Collaborative | Quello Center, Michigan State University | Bay Mills Community College"
series: "Compass Series"
document_type: "Working Paper"
date: 2026-07-26
location: "Eastern Upper Peninsula, Michigan"
license: "CC BY 4.0"
keywords:
  - ontology pipeline
  - knowledge infrastructure
  - procedural knowledge ontology
  - controlled vocabulary
  - knowledge graph
  - digital opportunity
  - provenance
status: "Working draft for discussion — not for citation without permission"
---

# Organize Before You Encode

## A Compass Series Working Paper on Jessica Talisman's Ontology Pipeline

---

### Abstract

Organizations racing to deploy AI agents keep discovering the same hard truth: buying a
platform is not the same as building an understanding. Jessica Talisman's **Ontology
Pipeline™** offers a disciplined alternative — a staged, iterative method for turning
scattered, tacit process knowledge into a queryable, machine-reasonable knowledge graph.
This working paper summarizes the pipeline, situates it within the library and
information-science and Semantic Web traditions it draws from, connects it to the
Procedural Knowledge Ontology (PKO) as a real-world proof point, and translates its
"order of operations" argument into four organizational commitments. The intent is
practical: to give community and public-sector teams — the audience of the Compass series —
a defensible sequence for building knowledge infrastructure that AI can actually use.

---

### 1. The problem this paper addresses

The current wave of enterprise AI investment tends to begin at the wrong end of the
pipeline. Organizations purchase the *implementation tier* — graph databases, catalogs,
retrieval-augmented-generation vendors — and expect meaning to rise out of sheer data
volume. When it does not, the failure gets blamed on the language models rather than on
the missing organizing principles beneath them.

Talisman's counter-argument is an argument about **order of operations**. A resource must
be *identifiable*, then *describable*, then *classifiable*, then *relatable* before a
knowledge graph can express it — and the tacit knowledge behind all of it must be captured
before any of that can begin. Skip a layer and every layer above it inherits the ambiguity
you failed to resolve.

---

### 2. What the Ontology Pipeline is

The **Ontology Pipeline™** is a repeatable, staged framework for building semantic
knowledge infrastructure, from controlled vocabularies through fully realized knowledge
graphs. Talisman codified it after a 2025 Data Day Texas talk and has implemented versions
of it across roughly six institutions over a decade of practice. It is not an invention
from scratch; it is an adaptation of the well-established **Semantic Spectrum** and the
knowledge-organization traditions of library and information science.

Two design principles govern the whole method:

- **Every stage is a usable product.** Each layer produces a standalone, valuable data
  product *and* prepares the foundation for the next. You cannot build a sound layer on top
  of an undefined one below it.
- **The work is iterative, not linear.** Because knowledge is dynamic, the pipeline is a
  cycle of continuous refinement rather than a one-time build.

---

### 3. The six stages

| # | Stage | Purpose | Typical standard |
|---|-------|---------|------------------|
| 1 | **Controlled Vocabulary** | Reconcile duplicates, resolve synonyms, and give every term one clear meaning and a stable identifier. | ANSI/NISO Z39.19 |
| 2 | **Metadata Standards / Schema** | Establish structural, descriptive, and administrative control; prepare integration patterns. | Dublin Core, DCAT |
| 3 | **Taxonomy** | Structure the vocabulary into parent–child hierarchies. | SKOS |
| 4 | **Thesaurus** | Add associative and equivalence relations (broader/narrower/related, synonyms); enable entity resolution. | SKOS-XL |
| 5 | **Ontology** | Introduce formal logic — classes, properties, rules — so machines can reason over the domain. | OWL / RDFS |
| 6 | **Knowledge Graph** | Assemble all prior layers into a cohesive, queryable, visual representation of the domain. | RDF / property graph |

Talisman's own metaphor for skipping ahead is blunt: jumping straight to ontologies "is
like being thrown into the deep end of the pool without knowing how to swim." A thesaurus,
in her framing, is simply "a taxonomy that has grown up."

---

### 4. Why it matters: ontologies as symbolic ballast for AI

The pipeline's payoff is epistemic reliability. Ontologies are a form of **symbolic AI** —
a context-rich, logically explicit counterbalance to the probabilistic "fog" of generative
models. They supply the disambiguation and descriptive precision that separate dependable
machine reasoning from hallucination. In other words, the pipeline is not an academic
exercise in tidiness; it is the infrastructure that lets an AI agent trace *why* it reached
a decision, grounded in defined entities, roles, conditions, and policies.

This is where provenance — a recurring concern in the Compass and DOIN work — becomes
structural rather than aspirational. When each term carries a stable identifier and each
relationship is formally expressed, the lineage of a conclusion is inspectable by design.

---

### 5. A proof point: the Procedural Knowledge Ontology (PKO)

Talisman points to the **Procedural Knowledge Ontology (PKO)** as evidence of a
fully-realized ontology stage in the wild. PKO models procedures as first-class objects —
`Procedure`, `Step`, `SetOfSteps`, `StepVerification`, `Action`, `Tool`, `Function`,
`ExpertiseLevel`, `Agent` (`Person` / `Role` / `Organisation` / `Software`), and
`Resource` (`Document` / `Media` / `Page`), together with status transitions such as
Create, Modify, Approve, Validate, and Archive.

**Provenance of PKO itself:**

- **Authors:** Valentina Anita Carriero, Mario Scrocca, Ilaria Baroni, Antonia Azzini, and
  Irene Celino.
- **Institution:** Cefriel – Politecnico di Milano (Milan, Italy); released under CC BY 4.0
  and hosted at `w3id.org/pko`.
- **Method:** Built with the Linked Open Terms methodology from ~54 competency questions
  and 60+ fact patterns across three industrial use cases (plant safety, CNC machine
  commissioning, and human–machine electrical-grid operations).
- **Lineage:** Reuses and extends PROV-O, P-Plan, DCAT, OWL-Time, ADMS, Metadata4Ing, and
  PRO — so PKO's own roots trace back to established W3C-era standards.
- **Publication:** "Procedural Knowledge Ontology (PKO)," arXiv:2503.20634 (March 2025),
  presented at the 22nd European Semantic Web Conference (ESWC 2025); developed under the
  EU-funded PERKS project.

PKO demonstrates the pipeline's endpoint: process knowledge, elicited and organized, then
encoded into logic a machine can act on.

---

### 6. From principle to practice: four commitments for organizations

Talisman distills the operational implications into four commitments. Read alongside the
pipeline, they are simply the pipeline's demands expressed as management decisions.

1. **Acknowledge the knowledge-management problem.** Hire knowledge engineers,
   ontologists, and information architects — not only orchestration engineers. The bottleneck
   is meaning, not plumbing.
2. **Invest in elicitation infrastructure.** Decision traces are mostly tacit today. Capture
   them deliberately through critical-incident interviews, ethnographic observation, and
   structured workshops. *You cannot skip elicitation.*
3. **Build the knowledge model before the persistence layer.** Define what a "decision"
   means in your domain; model entities, roles, conditions, and policies. That model *is*
   your ontology — and it must precede the database.
4. **Design for knowledge capture as a primary objective.** Build prompt libraries, central
   registries, and formal representations. Make the entire AI proposition about process,
   procedure, and knowledge — not about the tool.

---

### 7. Why this belongs in the Compass conversation

For the Eastern Upper Peninsula — and for rural and public-sector institutions generally —
the temptation is to treat AI as something you *purchase*. The Ontology Pipeline reframes it
as something you *cultivate*, starting from the knowledge your people already hold. That
reframing is capacity-building in the truest sense: elicitation before encoding honors local
expertise as the raw material, and provenance-aware ontologies keep community intelligence
transparent and inspectable rather than locked inside a vendor's black box.

The order of operations is the whole argument. Organize before you encode.

---

### Sources and provenance

- Talisman, Jessica. *Ontology Pipeline: A Framework for Knowledge Engineering.* Technics
  Publications (forthcoming, 2026); chapters serialized via the *Intentional Arrangement*
  newsletter.
- Talisman, Jessica. Presentations: "What Knowledge Infrastructure Looks Like" and "Context
  Graph: Decision Tracing for AI Agents" (2026).
- Carriero, V. A., Scrocca, M., Baroni, I., Azzini, A., & Celino, I. "Procedural Knowledge
  Ontology (PKO)." arXiv:2503.20634; ESWC 2025; Cefriel – Politecnico di Milano; `w3id.org/pko`.
- Framework lineage: the Semantic Spectrum; Gail Hodge's knowledge-organization stack;
  Robert J. Glushko, *The Discipline of Organizing*; Elaine Svenonius, *The Intellectual
  Foundation of Information Organization*; ANSI/NISO Z39.19; W3C SKOS / SKOS-XL / OWL / PROV-O.

---

*Compass Series working paper. Prepared for discussion within the EUPConnect Collaborative
and partners. Drafted July 26, 2026.*
