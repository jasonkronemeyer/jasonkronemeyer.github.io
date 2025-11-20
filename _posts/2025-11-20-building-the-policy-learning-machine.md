---
title: "Building the Digital Opportunities Intelligence Newtork: A Blueprint for Project Compass"
date: 2025-11-20
layout: post
categories: [dev, research]
status: draft
---

This is not just a "database" or a "dashboard." It is a **Cyber-Physical System for Policy Intelligence**—a "Policy Learning Machine" that closes the loop between *intervention* (what we do) and *impact* (what actually happens).

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
*   **Hard Data:** FCC Maps, Census (ACS), Speed Tests.
*   **Soft Data:** Survey results (Hajek estimators), Navigator logs, Qualitative interviews.

### Layer 2: The Intelligence Engine (The "Reasoning")
**Bayesian Networks (Causal Inference):**
Unlike a standard AI that just predicts "next word," this component calculates *probability*.

*   **Input:** "We have high infrastructure but low aspiration."
*   **Calculation:**  
    $$ P(Equity \mid HighInfra, LowAsp) = 32\% $$
*   **Simulation:** "What if we add Navigators?"  
    $$ \rightarrow P(Equity) = 68\% $$

**GraphRAG (The Interface):**
Retrieval-Augmented Generation that "reads" the graph to answer natural language questions. It prevents hallucination by grounding answers in specific nodes (e.g., "Baraga County's Gini coefficient is 0.45").

### Layer 3: The Human Interface (The "Action")
**For Policymakers:** A "What-If" Simulator.
> "Show me the most cost-effective intervention for rural veterans in Michigan."

**For Navigators:** A "Next Best Action" Guide.
> "I'm working with a senior who has a device but is afraid to use it. What does the theory suggest?"
>
> **System Response:** "Apply Dweck's Growth Mindset interventions. Here is a script..."

## 3. The Prototype Specification

To build this prototype, we need to construct a "Vertical Slice"—a fully functional system for **one specific use case** (e.g., "K-12 Education in Rural Michigan").

### Phase 1: The Ontology (The Skeleton)
We need to expand the existing Digital Compass Ontology to include the theoretical dimensions.

*   **Current:** `Navigator -> serves -> Population`
*   **Required:** `Intervention -> targets -> (Capability | Aspiration | Mindset)`

### Phase 2: The Data Ingestion (The Flesh)
Ingest a small, clean dataset to populate the graph.

*   **Target:** 5 Counties (e.g., Chippewa, Mackinac, Luce, Van Buren, and Roscommon).
*   **Data:**
    *   Infrastructure scores (Connectivity).
    *   Demographic data (Context).
    *   *Synthetic* Survey Data (to represent Aspiration/Mindset scores for the prototype).

### Phase 3: The "Brain" (Bayesian + LLM)
*   **Step A:** Define a simple Causal Graph (DAG).
    *   `Infra -> Access`
    *   `Navigators -> Skills`
    *   `Access + Skills -> Equity`
*   **Step B:** Connect an LLM (like GPT-4 or a local Llama) to query this graph via Cypher.
