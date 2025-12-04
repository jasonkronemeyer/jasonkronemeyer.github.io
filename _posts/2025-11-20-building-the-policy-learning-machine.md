---
title: "Building the Digital Opportunities Intelligence Network: A Blueprint for Project Compass"
date: 2025-11-20
layout: post
categories: [dev, research]
status: draft
---

# Introduction to Project Compass

Project Compass is a practical, place‑centered decision engine — a "Digital Opportunities Intelligence Network" that blends on‑the‑ground practitioner insight with rigorous statistical learning. It’s both a map and a laboratory: the Compass surfaces local strengths, capacity, and lived realities (not just infrastructure metrics), while the Policy Learning Machine uses causal reasoning, knowledge graphs, and comparative evidence to continuously evaluate which interventions actually move the needle toward digital equity. The result will be a tool designed for local planners, navigators, and policymakers to craft context‑aware strategies, measure impact, and iterate toward durable, equitable outcomes.

The Digital Opportunities Intelligence Network is not just a "database" or a "dashboard." It is a **Cyber-Physical System for Policy Intelligence**—a "Policy Learning Machine" that closes the loop between *intervention* (what we do) and *impact* (what actually happens).

This prototype builds on and was inspired by prior work that argues for an integrated monitoring, evaluation, and policy‑learning approach. See: "A Comprehensive Framework to Monitor, Evaluate, and Guide Broadband and Digital Equity Policy" (Bauer, Dagg, Rhinesmith, Byrum, Schill — SSRN, Aug 31, 2023) — https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4557340

> "a dynamic broadband policy learning system can be developed." — Bauer et al. (2023), SSRN

We are building the Policy Learning Machine as a practical instantiation of this idea: a system that continuously uses data and causal reasoning to learn which local interventions shift outcomes, and to help planners prioritize investments in context.

> "Local context, including infrastructure, socioeconomic factors, and community assets, significantly affects policy and program development." — Dagg et al. (2024), TPRC / SSRN

That insight informs the Machine's data model: we explicitly encode local assets, capacity, and socio-economic context so recommendations are tailored to place rather than being one‑size‑fits‑all.

Here is the architectural blueprint for the prototype we are building.

## 1. The Core Concept: The "Policy Learning Machine"

The prototype is a decision-support engine that answers the question: *"If we do X in this specific community, what is the probability of achieving Digital Equity?"*

It replaces "guesswork" with **Probabilistic Causal Reasoning**.

## 2. System Architecture (The 3-Layer Stack)

### Layer 1: The Knowledge Graph (The "Memory")
**Role:** The structured brain of the system. It stores not just data, but *relationships* and *theory*.

**Ontology (The Schema):**
*   **Entities:** `County`, `SchoolDistrict`, `Household`, `Navigator`, `Policy`, `Theory`.
*   **Theoretical Nodes:** `Capability` (Sen), `Aspiration` (Appadurai), `Mindset` (Dweck).
*   **Relationships:**
    *   `(Infrastructure)-[:ENABLES]->(Capability)`
    *   `(Navigator)-[:THICKENS]->(Aspiration)`
    *   `(Aspiration)-[:DRIVES]->(Adoption)`

**Data Sources:**
*   **Hard Data:** FCC Maps, Census (ACS), Speed Tests, Socio-Economic...
*   **Soft Data:** Survey results (Gini Coefficients, Hajek estimators...), Navigator logs, Qualitative interviews...

### Layer 2: The Intelligence Engine (The "Reasoning")
**Bayesian Networks (Causal Inference):**
Unlike a standard AI that just predicts "next word," this component calculates *probability*.

*   **Input:** "We have high infrastructure but low aspiration."
*   **Calculation:**  
    $$ P(Equity \mid HighInfra, LowAsp) = 32\% $$
*   **Simulation:** "What if we add Navigators?"  
    $$ \rightarrow P(Equity) = 68\% $$

**GraphRAG (The Interface):**
Retrieval-Augmented Generation that "reads" the graph to answer natural language questions. It prevents hallucination by grounding answers in specific nodes (e.g., "Mackinac County's Gini coefficient is 0.45").

### Layer 3: The Human Interface (The "Action")
**For Policymakers:** A "What-If" Simulator.
> "Show me the most cost-effective intervention for rural veterans in Michigan."

**For Navigators:** A "Next Best Action" Guide.
> "I'm working with a senior who has a device but is afraid to use it. What does the theory suggest?"
>
> **System Response:** "Apply Dweck's Growth Mindset interventions. Here is a script..."

## 3. The Prototype Specification

To build this prototype, we need to construct a "Vertical Slice"—a fully functional system for cross-domain use that spans multiple sectors (e.g., Rural Michigan across K‑12, workforce, healthcare, and public libraries). This slice should demonstrate end‑to‑end capability: ingesting heterogeneous data, encoding theory‑informed relationships, running causal inference, and delivering role‑specific actions.

Scope:
- Populations: students, job seekers, seniors, veterans, small businesses
- Settings: schools, workforce centers, clinics, libraries, community orgs
- Interventions: devices, connectivity, skills training, navigator support, mindset/aspiration programs

Outcomes:
- Cross‑sector equity metrics (access, adoption, skills, utilization)
- Place‑aware recommendations for different actors (policymakers, navigators, practitioners)
- What‑if simulations that compare interventions across domains and audiences
- Graph‑grounded answers that integrate infrastructure, context, and human factors
- Demonstrated learning loop: intervention → measurement → updated causal beliefs → improved guidance

### Phase 1: The Ontology (The Map Legend)
We need to expand the existing Digital Compass Ontology to include the theoretical dimensions. Just as a map legend defines the symbols for roads and rivers, our ontology defines the structural relationships of our policy landscape.

*   **Current:** `Navigator -> serves -> Population`
*   **Required:** `Intervention -> targets -> (Capability | Aspiration | Mindset)`

### Phase 2: The Data Ingestion (The Terrain)
Ingest a small, clean dataset to populate the graph. This represents the actual terrain we are navigating—the ground truth of our communities.

*   **Target:** 5 Counties and the Townships / Cities Contained within them (e.g., Chippewa, Mackinac, Luce, Van Buren, and Roscommon).
*   **Data:**
    *   Infrastructure scores (Connectivity).
    *   Demographic data (Context).
    *   *Synthetic* Survey Data (to represent Aspiration/Mindset scores for the prototype).

### Phase 3: The Intelligence (The Pathfinder)
This is the reasoning engine that helps us navigate from where we are to where we want to be.

*   **Step A:** Define a simple Causal Graph (DAG).
    *   `Infra -> Access`
    *   `Navigators -> Skills`
    *   `Access + Skills -> Equity`
*   **Step B:** Connect AI agents to query this graph.

## Further reading / references

- Bauer, J. M., Dagg, P. R., Rhinesmith, C., Byrum, G., & Schill, A. (2023). "A Comprehensive Framework to Monitor, Evaluate, and Guide Broadband and Digital Equity Policy." SSRN. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4557340

- Dagg, P., Knittel, M., Rhinesmith, C., Joon Oh, & others (2024). "Beyond Access and Infrastructure: Evaluating the Impact of Local Contexts on Digital Equity Strategies through the Lens of the Digital Opportunities Compass." Proceedings of TPRC 2024. SSRN. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4911656

