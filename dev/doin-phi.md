---
layout: post
title: "Phi-4 in DOIN: Technical Architecture for Open-Source Reasoning at the Edge"
date: 2026-06-09
author: Jason Kronemeyer
categories: [infrastructure, ai, doin, compass]
tags: [phi-4, doin, graphrag, bayesian-networks, edge-compute, open-source, multimodal, digital-equity]
status: draft
series: compass
description: >
  A technical architecture document mapping Microsoft's Phi-4 small language model family
  into the Digital Opportunities Intelligence Network (DOIN), covering GraphRAG reasoning,
  multi-agent orchestration, edge deployment, multimodal accessibility, and education.
---

## Introduction

The Digital Opportunities Intelligence Network (DOIN) is a next-generation decision support system designed to transform how we understand and solve the digital divide. It moves beyond static maps and spreadsheets to create a dynamic, predictive intelligence engine for digital opportunity, grounded in the six-dimension Digital Opportunities Compass framework developed by Dagg, Rhinesmith, Bauer, Byrum, and Schill (2023).

DOIN's intelligence layer requires a language model capable of evidence-grounded reasoning, causal inference, and natural language synthesis — one that can operate across a distributed infrastructure spanning community edge devices, regional campuses, and cloud batch processing. Microsoft's Phi-4 family of small language models meets these requirements with open weights, MIT licensing, and a deployment profile engineered for the full latency-versus-accuracy spectrum.

This document specifies where Phi-4 sits within the DOIN architecture, how each variant maps to a deployment tier, and what capabilities each integration enables for policymakers, Digital Navigators, educators, and community members across the Eastern Upper Peninsula and beyond.

## 1. DOIN Architecture Overview

DOIN operates as a three-layer system, each layer building on the one beneath it.

### 1.1 Layer 1 — The Compass (The Map)

The Digital Opportunities Compass provides the measurement framework organized across six domains: Contexts, Governance, Connectivity, Skills, Applications, and Outcomes. These dimensions map to the theoretical pipeline from Opportunity (Sen's capabilities) through Aspiration (Appadurai's navigation) to Growth Mindset (Dweck's learning) to Equity.

**Phi-4's role in this layer:** None directly. The Compass is a measurement and organizational framework. Phi-4 consumes Compass-structured data; it does not define it.

### 1.2 Layer 2 — The Network (The Structure)

The Knowledge Graph ingests and links census demographics, infrastructure maps, federal policy documents, stakeholder feedback, and research findings into a web of relationships using Neo4j, RDF/OWL, and SHACL schemas. The embedding layer (Harrier-oss-v1) converts unstructured text into vector representations stored in FAISS for semantic retrieval.

**Phi-4's role in this layer:** Phi-4-mini (3.8B) serves as a data integration assistant, parsing incoming documents, extracting entities, and suggesting Knowledge Graph node/edge mappings during the ontologist workflow. Its 128K context window accommodates full policy documents without chunking, and its function-calling capability enables direct interaction with Neo4j via MCP tool servers.

### 1.3 Layer 3 — The Intelligence (The Engine)

The Intelligence layer combines Bayesian Networks (causal prediction) with GraphRAG (evidence-grounded AI Q&A). It operationalizes the Policy Learning Approach using Gini coefficients to measure inequality gaps, Hajek estimators to correct for data biases, and Bayesian inference to model cause-and-effect. It allows policymakers to ask "What if?" questions with traceable, citation-backed reasoning.

**Phi-4's role in this layer:** Primary. Phi-4 is the reasoning and synthesis engine that completes the GraphRAG pipeline:

```

Question
↓
Harrier retrieves from Knowledge Graph (embedding layer)
↓
Bayesian Network provides predictions (causal layer)
↓
Phi-4 synthesizes evidence-grounded answer (reasoning layer)
↓
Citable, traceable, actionable response

```

## 2. Phi-4 Family Variant Mapping

The Phi-4 family includes three primary variants, each optimized for a different point on the latency-versus-accuracy spectrum. DOIN deploys all three.

### 2.1 Phi-4-mini (3.8B Parameters)

| Attribute | Specification |
|---|---|
| Parameters | 3.8 billion |
| Context Window | 128,000 tokens |
| VRAM Requirement | ~3 GB (quantized) |
| Key Strengths | Reasoning, function calling, long-context tasks |
| Deployment Target | Micro Edge AI Pods, community kiosks, school laptops |
| License | MIT |

**DOIN Functions:**
- DataAgent brain in the MultiAgentGraphRAG architecture
- Knowledge Graph data integration assistant (entity extraction, relationship suggestion)
- Community-facing Q&A at Digital Navigator kiosks and library access points
- Student-facing interactive AI for Tech Changemakers and AI Connect curriculum
- Function calling into Neo4j, FAISS, and external data APIs via MCP tool servers

**Why 128K context matters for DOIN:** A single Phi-4-mini instance can hold an entire county's Compass assessment, the full BEAD state plan excerpt, and the user's question in a single prompt — enabling coherent, cross-referential reasoning without retrieval fragmentation.

### 2.2 Phi-4 (14B Parameters)

| Attribute | Specification |
|---|---|
| Parameters | 14 billion |
| Context Window | 16,000 tokens |
| VRAM Requirement | ~10 GB (quantized) |
| Key Strengths | MMLU 84.8%, MATH 80.4%, HumanEval 82.6% |
| Deployment Target | Campus/regional edge servers, CTTC data center |
| License | MIT |

**DOIN Functions:**
- Primary GraphRAG synthesis engine for policy Q&A
- TheoryAgent, EvidenceAgent, and SynthesisAgent brain in MultiAgentGraphRAG
- Bayesian inference chain reasoning ("What if we invest $X in digital literacy here?")
- Report generation (Compass dimension analyses, intervention recommendations)
- Complex multi-step reasoning across Compass dimensions

**Why 14B at the campus edge matters for DOIN:** The 14B variant delivers reasoning quality competitive with models four to ten times its size on mathematical and logical tasks. DOIN's Bayesian reasoning layer requires a model that can handle Gini coefficients, Hajek estimators, and conditional probability chains without hallucinating the mathematics. Phi-4's training emphasis on synthetic textbook-style data and mathematical reasoning makes it uniquely suited to this requirement.

### 2.3 Phi-4-multimodal (5.6B Parameters)

| Attribute | Specification |
|---|---|
| Parameters | 5.6 billion |
| Modalities | Speech + Vision + Text (unified architecture) |
| Architecture | Mixture-of-LoRAs across modalities |
| Speech Languages | English, French, Spanish, Japanese |
| Deployment Target | Digital Navigator kiosks, smart building edge, field inspection |
| License | MIT |

**DOIN Functions:**
- Voice-first community interface for Digital Navigators and accessibility
- Speech-to-text transcription for EUPConnect Steering Committee meetings
- Vision-based document processing (policy PDFs, handwritten community feedback)
- Smart building visual analytics (occupancy detection, energy dashboard interpretation)
- Cross-border French-English speech input for Canadian partnerships
- Assistive technology for individuals with disabilities (28.7% of EUP population)

**Why multimodal matters for DOIN:** Digital equity is fundamentally about access. A text-only AI interface excludes residents with limited literacy, visual impairments, or discomfort with keyboards. Phi-4-multimodal enables a resident to walk up to a kiosk, speak a question about broadband programs, and receive a reasoned, evidence-grounded answer. This is the DOIN vision made tangible — intelligence that meets people where they are.

## 3. Multi-Agent GraphRAG Architecture

DOIN's advanced policy questions require coordinated reasoning across multiple knowledge domains. The MultiAgentGraphRAG architecture deploys specialized agents, each powered by a Phi-4 variant matched to its computational requirements.

### 3.1 Agent Topology

```

┌──────────────────────────────────────────────────────────┐
│                    SynthesisAgent                         │
│                    (Phi-4 14B)                            │
│         Combines all inputs into final answer             │
└────────────┬──────────┬──────────┬───────────────────────┘
│          │          │
┌────────▼──┐  ┌────▼─────┐  ┌▼───────────────┐
│TheoryAgent│  │Evidence  │  │PredictionAgent  │
│(Phi-4 14B)│  │Agent     │  │(Phi-4 14B)      │
│           │  │(Phi-4 14B│  │                 │
│Retrieves  │  │Retrieves │  │Runs Bayesian    │
│Sen,       │  │Hampton & │  │predictions      │
│Appadurai, │  │Bauer,    │  │                 │
│Dweck,     │  │research  │  │P(Equity |       │
│Toyama     │  │findings  │  │ Opportunity,    │
└───────────┘  └──────────┘  │ Aspiration,     │
│ Mindset)        │
┌────────┴────────┐
│   DataAgent     │
│  (Phi-4-mini    │
│   3.8B)         │
│                 │
│Retrieves county │
│data, runs       │
│lookups via MCP  │
│tools            │
└─────────────────┘

````

### 3.2 Agent Specifications

**TheoryAgent** — Retrieves and interprets relevant theoretical frameworks from the Knowledge Graph. When a policymaker asks about digital literacy investment, TheoryAgent identifies that Sen's capabilities approach (Opportunity), Appadurai's capacity to aspire (Aspiration), and Dweck's growth mindset (mechanism) all apply, and provides the theoretical grounding for the recommendation.

- Model: Phi-4 (14B)
- Retrieval source: Harrier-embedded theory corpus
- Output: Theoretical framework analysis with citations

**EvidenceAgent** — Retrieves empirical research findings, particularly the Hampton and Bauer (2020) Michigan data and the Dagg et al. (2023) Compass metrics. Provides the evidence base that validates or challenges theoretical predictions.

- Model: Phi-4 (14B)
- Retrieval source: Harrier-embedded research corpus
- Output: Evidence summary with DOIs and source attribution

**DataAgent** — Retrieves county-level and state-level data from the Knowledge Graph via function calls. Handles structured queries against Neo4j (SPARQL/Cypher), census APIs, and broadband availability databases.

- Model: Phi-4-mini (3.8B)
- Tools: Neo4j MCP server, Census API MCP server, FAISS vector store
- Output: Structured data tables, Compass dimension scores

**PredictionAgent** — Runs Bayesian inference chains using the causal model. Given observed Compass scores and a proposed intervention, predicts the probability distribution of outcomes.

- Model: Phi-4 (14B) or Phi-4-reasoning
- Tools: pgmpy/bnlearn Bayesian network via MCP server
- Output: Conditional probability estimates, confidence intervals

**SynthesisAgent** — Combines outputs from all four agents into a coherent, citable, actionable policy recommendation. Ensures every claim is traceable to a theory, evidence source, data point, or prediction.

- Model: Phi-4 (14B)
- Input: Concatenated agent outputs
- Output: Natural language recommendation with full citation chain

### 3.3 Example Query Flow

**User Question:** "Should we prioritize infrastructure or Digital Navigators in Mackinac County?"

1. **DataAgent** (Phi-4-mini) retrieves Mackinac County Compass scores: low Connectivity (infrastructure gap), moderate Skills, low Applications.
2. **TheoryAgent** (Phi-4) identifies Toyama's amplification principle: technology amplifies existing human intent and capacity. Without capacity (Skills), infrastructure alone underperforms.
3. **EvidenceAgent** (Phi-4) retrieves Hampton and Bauer (2020): infrastructure is necessary but not sufficient; digital navigation increases adoption among underserved populations.
4. **PredictionAgent** (Phi-4) runs Bayesian inference: P(Adoption | Infrastructure + Navigator) = 0.73 vs. P(Adoption | Infrastructure only) = 0.41.
5. **SynthesisAgent** (Phi-4) produces: "Infrastructure first to close the Connectivity gap (Opportunity stage), with concurrent Digital Navigator deployment to build Skills and Applications (Aspiration + Mindset stages). The Bayesian model predicts 73% adoption with both interventions vs. 41% with infrastructure alone. This aligns with Toyama's amplification principle and Hampton & Bauer's Michigan findings."

## 4. Edge Deployment Architecture

DOIN's distributed deployment maps directly to the NOVA multi-tier edge AI infrastructure, with Phi-4 variants matched to each tier alongside their Harrier embedding counterparts.

### 4.1 Deployment Tiers

| Tier | Infrastructure | Phi-4 Variant | Harrier Variant | Power | Use Case |
|---|---|---|---|---|---|
| **Micro Edge AI Pod** | Containerized compute at school IDFs, library kiosks, CTTC walk-in closets | Phi-4-mini (3.8B) | harrier-270M | 100–200 kW shared | Community Q&A, navigator tools, student AI |
| **Campus Edge** | Regional data center at CTTC, school campus MDF | Phi-4 (14B) + Phi-4-multimodal (5.6B) | harrier-0.6B | ~1 MW | GraphRAG policy Q&A, smart building analytics, meeting transcription |
| **Cloud/Batch** | Snowflake, Azure, or partner cloud | Phi-4-reasoning-plus (14B) | harrier-27B | Cloud-managed | Full corpus re-indexing, statewide policy analysis, deep Bayesian modeling |

### 4.2 Infrastructure Integration

DOIN's physical infrastructure leverages the Passive Optical LAN (POLAN) and Fault-Managed Power Systems (FMPS) architecture documented in the EUPConnect infrastructure planning. This architecture creates a centralized power node where all building systems draw power and data from a single distribution point — an ideal topology for edge AI deployment.

**POLAN + Phi-4 integration:**
- Fiber backbone provides the low-latency, high-bandwidth connectivity required for model serving
- Centralized power nodes concentrate GPU/compute at the MDF, reducing distributed power complexity
- Class 4 power systems (NEC Article 725, UL 62368-1) enable low-voltage DC distribution to edge inference devices without conduit requirements
- NOVA high-density fiber panels support the east-west DCI traffic patterns emerging from distributed AI inference

**Container runtime:**

```yaml
# docker-compose.yml — Campus Edge Deployment
version: '3.8'
services:
  phi4-inference:
    image: vllm/vllm-openai:latest
    command: >
      --model microsoft/phi-4
      --tensor-parallel-size 1
      --max-model-len 16384
      --gpu-memory-utilization 0.9
    ports:
      - "8000:8000"
    deploy:
      resources:
        reservations:
          devices:
            - capabilities: [gpu]

  phi4-mini-agents:
    image: vllm/vllm-openai:latest
    command: >
      --model microsoft/phi-4-mini
      --max-model-len 131072
      --gpu-memory-utilization 0.85
    ports:
      - "8001:8000"
    deploy:
      resources:
        reservations:
          devices:
            - capabilities: [gpu]

  phi4-multimodal:
    image: vllm/vllm-openai:latest
    command: >
      --model microsoft/phi-4-multimodal
      --trust-remote-code
    ports:
      - "8002:8000"
    deploy:
      resources:
        reservations:
          devices:
            - capabilities: [gpu]

  harrier-embeddings:
    image: sentence-transformers/serving:latest
    environment:
      - MODEL_NAME=microsoft/harrier-oss-v1-0.6b
    ports:
      - "8003:8080"

  neo4j:
    image: neo4j:5-community
    ports:
      - "7474:7474"
      - "7687:7687"
    volumes:
      - neo4j_data:/data

  faiss-server:
    image: faiss-server:latest
    volumes:
      - faiss_index:/index
    ports:
      - "8004:8080"

  mcp-gateway:
    image: docker/mcp-gateway:latest
    environment:
      - MCP_TOOLS=neo4j,faiss,census-api,bayesian
    ports:
      - "8005:8080"

volumes:
  neo4j_data:
  faiss_index:
````

### 4.3 MCP Tool Server Architecture

Model Context Protocol (MCP) provides the standardized interface between Phi-4 agents and external tools. Following Docker's secure-by-default recommendations, each MCP server runs in an isolated container with secret management restricting credential access to authorized containers only.

```
┌─────────────────────────────────────────────────────────┐
│                  Phi-4 Agent Layer                        │
│    TheoryAgent · EvidenceAgent · DataAgent                │
│    PredictionAgent · SynthesisAgent                       │
├────────────────────┬────────────────────────────────────┤
│                    │ MCP Gateway                         │
│                    │ (Authentication, Logging, Policy)    │
├────────┬───────────┼───────────┬────────────────────────┤
│ Neo4j  │ FAISS     │ Census    │ Bayesian               │
│ MCP    │ MCP       │ API MCP   │ MCP                    │
│ Server │ Server    │ Server    │ Server                 │
│        │           │           │ (pgmpy/bnlearn)        │
└────────┴───────────┴───────────┴────────────────────────┘
```

**Tool budget management:** Each Phi-4 agent is configured with a maximum of four to six MCP tools to avoid overloading the context window. The DataAgent, which requires the most tool diversity, uses Phi-4-mini's 128K context to accommodate tool descriptions alongside data retrieval results.

## 5. Multimodal Accessibility Layer

### 5.1 Digital Navigator Voice Interface

The EUPCC Digital Equity Hub deploys Digital Navigators across Chippewa, Luce, and Mackinac counties to help underserved populations — including elders and seniors (PP1), Native Americans (PP2), individuals with disabilities (PP3), and veterans (PP4) — navigate digital resources.

Phi-4-multimodal transforms this interaction from text-dependent to voice-first:

```
Resident speaks question (English or French)
  ↓
Phi-4-multimodal transcribes speech to text (on-device)
  ↓
Harrier-0.6B embeds question for Knowledge Graph retrieval
  ↓
Phi-4 (14B) synthesizes evidence-grounded answer
  ↓
Response displayed on screen + spoken via TTS
```

**Privacy architecture:** All speech processing occurs on-device or at the campus edge. No audio data leaves the local network. This is critical for Tribal data sovereignty and for building trust with populations historically excluded from digital systems.

### 5.2 Smart Building Integration

The POLAN + FMPS distributed edge architecture in DOIN-connected facilities (schools, CTTC, community centers) generates continuous sensor data. Phi-4-multimodal processes visual feeds for:

* **Occupancy analytics:** Camera-based occupancy detection for HVAC optimization, reducing energy costs at the centralized power node
* **Maintenance prediction:** Visual inspection of infrastructure components, with Phi-4-multimodal identifying wear patterns and suggesting maintenance schedules
* **Safety monitoring:** Integration with InformaCast and AtlasIED mass notification systems for automated visual threat assessment

## 6. Education and Workforce Development

### 6.1 AI Literacy Curriculum Integration

The "First Five Things to Teach a Computer" framework from AI Connect provides the pedagogical structure. Phi-4-mini serves as the student-facing AI that makes each lesson tangible:

| Lesson                    | Phi-4-mini Application                                                                                   |
| ------------------------- | -------------------------------------------------------------------------------------------------------- |
| Teach it to communicate   | Students prompt Phi-4-mini with natural language, observe how instruction clarity affects output quality |
| Teach it to play music    | Students use function calling to connect Phi-4-mini to audio generation tools                            |
| Teach it to draw pictures | Students instruct Phi-4-mini to generate image prompts, exploring how language shapes visual output      |
| Teach it to do math       | Students test Phi-4-mini's mathematical reasoning (MATH 80.4%), comparing AI and human problem-solving   |
| Teach it to play games    | Students build simple game agents, learning about decision trees and reward functions                    |

**Deployment for education:** Phi-4-mini runs on school laptops via Foundry Local (CPU-only mode, \~3 GB RAM). No cloud dependency, no per-student API costs, no student data leaving the building. Open weights enable students to inspect the model architecture — aligned with the "learning in public" philosophy.

### 6.2 BICSI and CTE Workforce Training

The Cloverland Technology and Training Center (CTTC) workforce pipeline trains technicians in fiber construction, network operations, and converged IT/OT systems. Phi-4 enhances this training through:

* **Interactive technical Q\&A:** Trainees query Phi-4 about NEC Article 725, UL 62368-1, POLAN design principles, and FMP specifications — receiving technically accurate, contextually grounded answers from the DOIN Knowledge Graph
* **Scenario-based learning:** Phi-4's reasoning capability generates "What if?" scenarios for network design decisions, helping trainees understand the cascading effects of architectural choices
* **Code generation:** Phi-4's HumanEval 82.6% performance supports trainees learning Python for network automation, configuration scripting, and data analysis

## 7. Policy Learning Machine Integration

DOIN's Policy Learning Machine operates in continuous cycles: Observe, Interpret, Model, Recommend, Measure, Update. Phi-4 powers each stage with a different reasoning mode:

| Cycle Stage   | Phi-4 Function                                                                 | Variant           |
| ------------- | ------------------------------------------------------------------------------ | ----------------- |
| **Observe**   | Parse incoming data signals, extract entities, flag anomalies                  | Phi-4-mini (3.8B) |
| **Interpret** | Classify observations by Compass dimension, identify theoretical relevance     | Phi-4 (14B)       |
| **Model**     | Generate Bayesian network structure hypotheses, validate causal assumptions    | Phi-4 (14B)       |
| **Recommend** | Synthesize multi-agent analysis into actionable policy recommendations         | Phi-4 (14B)       |
| **Measure**   | Compare predicted outcomes to observed outcomes, quantify model accuracy       | Phi-4-mini (3.8B) |
| **Update**    | Generate model revision proposals, explain reasoning for parameter adjustments | Phi-4 (14B)       |

This cycle transforms DOIN from a static analytical tool into a continuously learning system — one that improves its predictions as new data flows in from Digital Navigator interactions, census updates, infrastructure deployment reports, and community feedback.

## 8. Licensing and Consortium Deployment

All Phi-4 variants are released under the MIT license, enabling unrestricted use across the EUPConnect consortium:

* **Five Nations Advisors** — Commercial advisory use without licensing restrictions
* **Bay Mills Community College** — Educational deployment with student access to open weights
* **Lake Superior State University (CFRE)** — Research applications with full model inspection
* **Sault Area Public Schools** — Student-facing AI on school devices without per-seat costs
* **Cloverland Electric / CTTC** — Workforce training with technical Q\&A capabilities
* **Tribal partners** — On-premises deployment ensuring data sovereignty with no cloud dependencies

## 9. Technology Stack Summary

| Layer               | Component                     | Technology                                   |
| ------------------- | ----------------------------- | -------------------------------------------- |
| **Reasoning**       | Phi-4 (14B)                   | PyTorch, Transformers, Flash Attention, vLLM |
| **Edge Reasoning**  | Phi-4-mini (3.8B)             | Foundry Local, vLLM, ONNX Runtime            |
| **Multimodal**      | Phi-4-multimodal (5.6B)       | PyTorch, Mixture-of-LoRAs, vLLM              |
| **Embeddings**      | Harrier-oss-v1 (0.6B default) | Sentence Transformers, PyTorch               |
| **Vector Store**    | FAISS                         | faiss-gpu / faiss-cpu                        |
| **Knowledge Graph** | Neo4j Community Edition       | Cypher, RDF/OWL, SHACL                       |
| **Agent Protocol**  | Model Context Protocol (MCP)  | Docker MCP Gateway                           |
| **Containers**      | Docker Compose                | Docker Engine, GPU passthrough               |
| **Causal Model**    | Bayesian Networks             | pgmpy, bnlearn                               |
| **Network**         | POLAN + FMPS                  | Tellabs, Cisco Meraki, Clearfield NOVA       |

## 10. Conclusion

Phi-4 completes the DOIN intelligence stack. Where Harrier-oss-v1 provides the semantic retrieval layer — finding the right evidence across 94 languages and three deployment scales — Phi-4 provides the reasoning layer that transforms retrieved evidence into actionable intelligence.

The Phi-4 family's three-variant architecture mirrors DOIN's distributed deployment model: Phi-4-mini at the community edge for real-time interaction, Phi-4 at the campus for deep policy reasoning, and Phi-4-multimodal bridging the accessibility gap for populations that text-only interfaces cannot serve. All variants share MIT licensing, PyTorch compatibility, and the mathematical reasoning strength that DOIN's Bayesian inference chains demand.

Together, Harrier and Phi-4 represent a complete open-source AI stack for evidence-based policymaking — one that can be deployed, inspected, and governed by the communities it serves. This is not AI as a service. This is AI as infrastructure.

***

*Part of: Project Compass (Merit Network) — Digital Opportunities Intelligence Network (DOIN)*

*Working draft 🔬 Learning in Public — This site is my digital laboratory — a space for curiosity, experimentation, and evolving ideas.*

*© 2026 Jason Kronemeyer. All rights reserved.*



---

### Sources Referenced

This document draws from your existing DOIN framework documentation including [TrainingCompassOverview.html](https://jasonkronemeyercom-my.sharepoint.com/personal/jason_jasonkronemeyer_com/Documents/CODE/jasonkronemeyer.github.io/_site/dev/TrainingCompassOverview.html?web=1&EntityRepresentationId=056b7b0e-afc7-4791-a700-aa43c0824c56) , [TrainingCompassGraphRAG.html](https://jasonkronemeyercom-my.sharepoint.com/personal/jason_jasonkronemeyer_com/Documents/CODE/jasonkronemeyer.github.io/_site/dev/TrainingCompassGraphRAG.html?web=1&EntityRepresentationId=49ec62ff-e735-4f8c-b27a-29d44d7b761e), the [PL.html](https://jasonkronemeyercom-my.sharepoint.com/personal/jason_jasonkronemeyer_com/Documents/CODE/jasonkronemeyer.github.io/_site/dev/PL.html?web=1&EntityRepresentationId=47136b82-2e89-4632-9961-3ac008434286) Compass framework connection , your [training-the-compass-digital-opportunities-intelligence-framework.html](https://jasonkronemeyercom-my.sharepoint.com/personal/jason_jasonkronemeyer_com/Documents/CODE/jasonkronemeyer.github.io/_site/2025/11/07/training-the-compass-digital-opportunities-intelligence-framework.html?web=1&EntityRepresentationId=9c31259f-4f13-463e-b0eb-afad6fe03d48) , the [MCP Servers_Docker_and_AI Agent Integration.docx](https://jasonkronemeyercom-my.sharepoint.com/personal/jason_jasonkronemeyer_com/_layouts/15/Doc.aspx?sourcedoc=%7BC22E9CAC-60BC-4B3B-BE5C-1F599BC34C30%7D&file=MCP%20Servers_Docker_and_AI%20Agent%20Integration.docx&action=default&mobileredirect=true&DefaultItemOpen=1&EntityRepresentationId=8784babe-18a8-4daf-addf-db62e1f1c16a) technical report, [Docker-State-of-Agentic-AI-white-paper.pdf](https://jasonkronemeyercom-my.sharepoint.com/personal/jason_jasonkronemeyer_com/Documents/Docker-State-of-Agentic-AI-white-paper.pdf?web=1&EntityRepresentationId=8104918f-37b3-4ce0-bcb2-586a502cdb4d) , the [daf62f4a-7f5d-45b1-bcf9-e12e632cc881.pdf](https://jasonkronemeyercom-my.sharepoint.com/personal/jason_jasonkronemeyer_com/Documents/daf62f4a-7f5d-45b1-bcf9-e12e632cc881.pdf?web=1&EntityRepresentationId=9e93f1b0-5d03-478c-bca2-2f4a5598fcb8) NOVA edge AI infrastructure presentation, the [EUP MITTEN Narrative v3.docx](https://jasonkronemeyercom.sharepoint.com/sites/eupconnect/_layouts/15/Doc.aspx?sourcedoc=%7BD0A60320-C215-4DE2-9585-E7180E3D3758%7D&file=EUP%20MITTEN%20Narrative%20v3.docx&action=default&mobileredirect=true&DefaultItemOpen=1&EntityRepresentationId=9a8b7965-608c-4cb2-8297-50db9d22dfec) program narrative, your [ai-connect-curiosity.html](https://jasonkronemeyercom-my.sharepoint.com/personal/jason_jasonkronemeyer_com/Documents/CODE/jasonkronemeyer.github.io/_site/2026/03/23/ai-connect-curiosity.html?web=1&EntityRepresentationId=fac370bd-a1c5-4c7b-8277-f7af53e09bf2) education framework, and the [finding_digital_divide.html](https://jasonkronemeyercom-my.sharepoint.com/personal/jason_jasonkronemeyer_com/Documents/CODE/jasonkronemeyer.github.io/_site/notes/finding_digital_divide.html?web=1&EntityRepresentationId=76ca75ec-9701-4e77-9d02-148856fdac36) Bayesian Networks article.
