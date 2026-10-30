---
layout: research-note
status: research
title: "Beyond LLMs: World Models, Abstraction, and the Next Architecture of AI"
date: 2026-10-30
author: Jason Kronemeyer
categories:
  - Artificial Intelligence
  - Research Notes
tags:
  - AI
  - world models
  - JEPA
  - physical AI
  - abstraction
  - hierarchical planning
  - knowledge infrastructure
  - First Five
description: "A research note examining Yann LeCun's argument that the next major advance in AI may depend on world models, predictive abstraction, and hierarchical planning rather than larger language models alone."
---

## Executive Summary

Yann LeCun argues that the next major advance in artificial intelligence is unlikely to come simply from making large language models larger. LLMs are extraordinarily capable at manipulating language and other discrete symbolic representations, but intelligence in the physical world requires something different: the ability to construct useful representations of reality, predict how actions will change that reality, and plan toward desired outcomes.

His proposed direction centers on **world models** and **Joint Embedding Predictive Architectures (JEPA)**. Rather than attempting to generate every detail of a future state, these systems would learn abstract representations that preserve what is useful and predictable while ignoring irrelevant or inherently unpredictable detail. Intelligence therefore becomes partly a problem of **abstraction**: representing the world at the right level for the task at hand.

A particularly important aspect of LeCun's argument is **hierarchical planning**. Complex goals can be decomposed into increasingly concrete subgoals, allowing a system to reason differently about long-term objectives and immediate actions. This suggests an architecture of intelligence that can be summarized as:

> **Observe → Represent → Abstract → Predict → Plan → Act → Observe**

For my work on knowledge and intelligent infrastructure, the significance extends beyond robotics. Ontologies, knowledge graphs, semantic models, provenance systems, and world models all confront a related challenge: **reality contains far more information than a useful model can or should represent**. The central question is therefore not simply how much data an intelligent system possesses, but how effectively it can organize that information into representations that support prediction, reasoning, and action.

This also provides a useful point of comparison with my **First Five Things to Teach a Computer** framework. The two should not be conflated. The First Five concerns how a domain is structured and represented for computation; LeCun's world-model approach concerns how an intelligent system learns representations that allow it to anticipate changes and select actions. Together, however, they point toward a broader proposition: **intelligence depends as much on representation and abstraction as it does on computation.**

## Central Argument

LeCun challenges the assumption that performance on intellectually difficult tasks demonstrates general or human-like intelligence. Computers have long exceeded humans at particular tasks such as calculation and games, yet machines remain much less capable at understanding and acting within the messy physical world.

The distinction, in his account, comes partly from the nature of the information involved. Language, programming code, and mathematics can be represented largely as sequences of discrete symbols. The physical world is continuous, high-dimensional, noisy, uncertain, and only partially predictable.

A genuinely intelligent agent operating in such an environment therefore cannot simply predict every detail. It needs to determine **which features matter, represent them at an appropriate level of abstraction, predict the consequences of possible actions, and use those predictions to plan**.

## From Generative Models to World Models

LeCun describes a **world model** as an internal model capable of predicting how the state of the world will change when an action occurs.

Given a representation of the world at time *t* and a contemplated action, the world model predicts a resulting state at *t + 1*. This makes planning possible:

> **Current State + Possible Action → Predicted Future State**

An intelligent agent could evaluate possible futures and select actions that move the world closer to a desired state.

This is particularly important for robotics and what LeCun describes as **physical AI**. A child can frequently encounter a new physical task and construct a workable sequence of actions without seeing thousands of training demonstrations. For LeCun, achieving something resembling this ability would be a more meaningful demonstration of machine intelligence than surpassing another bounded benchmark.

## Hierarchical Intelligence

One of the strongest concepts in the talk is that useful world models need to operate **hierarchically**.

LeCun illustrates this with traveling from New York to Paris. A person does not plan every muscular movement involved in the journey. Instead, the goal can be decomposed across levels of abstraction:

> **Be in Paris**  
> ↓  
> **Take a flight**  
> ↓  
> **Get to the airport**  
> ↓  
> **Get to the street**  
> ↓  
> **Leave the building**  
> ↓  
> **Stand up**

Long-range planning operates through relatively abstract representations. As an agent approaches an immediate action, progressively greater detail becomes relevant.

Intelligence, from this perspective, is not simply possessing a model of the world. It also requires an ability to **move between levels of abstraction appropriate to different spatial, temporal, and functional scales**.

## JEPA and Predictive Abstraction

LeCun connects this approach to **JEPA**, or **Joint Embedding Predictive Architecture**.

Instead of requiring an AI system to reconstruct every detail of an observation, JEPA seeks to learn abstract representations and make predictions within that representation space.

This addresses an important problem: much of reality simply cannot be predicted. A useful model therefore needs to distinguish among information that matters, information that can be predicted, information that is inherently uncertain, and detail that can safely be ignored.

Scientific models already operate this way. An engineer does not need to calculate the trajectory of every individual molecule of air to reason about airflow around an aircraft. An appropriate abstraction preserves the information needed for the problem while discarding vast quantities of unnecessary detail.

The deeper proposition is therefore:

> **Abstraction is not merely a convenience for intelligence. It may be one of its essential mechanisms.**

## Connection to Knowledge Infrastructure

This argument becomes especially interesting when moved beyond robotics.

Knowledge systems face a similar representational problem. Data alone does not constitute intelligence. A useful knowledge system must identify meaningful entities and relationships, preserve context and provenance, select appropriate abstractions, and transform information into representations that support reasoning and action.

That suggests an expanded architecture:

> **Reality → Observation → Representation → Abstraction → Prediction → Planning → Action → New Observation**

Knowledge graphs, ontologies, semantic models, provenance systems, and learned world models occupy different places within this architecture, but they address a common challenge: **How do we construct actionable representations of a world that is vastly more complicated than any model of it can ever be?**

For intelligent infrastructure, this is a particularly useful distinction. Sensors and operational systems can produce enormous quantities of observations. Data platforms can collect those observations. Knowledge models can establish entities, relationships, context, and provenance. Predictive systems can then begin asking a different question: *Given what we know about the present state of this system, what is likely to happen if something changes or if we take a particular action?*

The progression is therefore not simply from more data to more intelligence. It is from **observation to increasingly useful representations of the world**.

## Connection to the First Five

This creates an intriguing connection with my **First Five Things to Teach a Computer** framework.

The frameworks address different parts of the problem:

### First Five

> *What does a computer need to know about this domain for computation to become meaningful?*

### World Models

> *Given a representation of that domain, how might a machine predict what happens next and determine what actions to take?*

The First Five therefore concerns **domain representation and structure**, while a world model concerns **state, dynamics, prediction, and action**.

This connection is my interpretation, not a claim made by LeCun. The distinction is important. The **First Five Things to Teach a Computer is my original framework**, while JEPA and the world-model architecture discussed here derive from LeCun's research.

Placed alongside one another, however, they suggest a larger architecture for intelligent systems in which structured knowledge and learned predictive representations may ultimately complement each other:

> **Know what exists → Understand relationships → Represent the current state → Predict change → Plan → Act → Learn**

That progression may be especially important as we move from today's generative AI toward intelligent systems embedded in organizations, communities, buildings, infrastructure, transportation, energy systems, and other physical environments.

## Implications for Intelligent Infrastructure

The important horizon may therefore lie beyond the current framing of generative AI.

The objective becomes systems capable of:

> **Representing → Abstracting → Predicting → Planning → Acting → Learning**

For intelligent infrastructure, that is a consequential distinction. The long-term goal would not merely be infrastructure that can answer questions about itself. It would be infrastructure that can **understand its present state, recognize relationships, anticipate plausible future states, evaluate possible actions, and help people make better decisions**.

Consider a school campus, community broadband network, energy system, water system, transportation network, or smart building. A generative interface might allow someone to ask questions about that infrastructure. A more sophisticated intelligent system could potentially reason over its condition, dependencies, operating environment, historical behavior, and possible future states.

The difference is subtle but profound. One system **talks about the world**. The other begins constructing and using a **model of the world**.

That is a considerably broader conception of intelligence than generating the next token.

## Research Questions

LeCun's argument raises several questions that deserve further investigation:

1. How might ontologies and knowledge graphs complement learned world models?
2. What role should provenance play when a predictive system constructs increasingly abstract representations?
3. How can world models distinguish between uncertainty, missing information, and genuinely unpredictable phenomena?
4. Can hierarchical world models provide a useful architecture for intelligent buildings, energy systems, broadband networks, and other cyber-physical infrastructure?
5. Where does explicit domain knowledge end and learned representation begin?
6. Could the First Five provide a structured domain layer upon which predictive world models operate?
7. What governance mechanisms become necessary when systems move from providing information to recommending or taking actions?

These questions connect the emerging research around world models to a larger challenge I am interested in: **how we build infrastructure that does not merely collect data, but becomes progressively more capable of supporting human learning, reasoning, and decision-making.**

## Primary Source

LeCun, Yann. Interview on world models, JEPA, physical AI, hierarchical planning, and the future of artificial intelligence. *YouTube*. [Original video](https://youtu.be/DK0jypclGSk?si=-oVuBj7YoXQ0mLyP). Accessed 30 Oct. 2026.

> **Citation note:** The source citation above is intentionally conservative. The supplied video establishes Yann LeCun as the speaker and provides the content used for this research note, but I have not independently established the video's formal title, publisher or channel, event name, or publication date. Those fields should be added to the citation only after they are verified.

## Provenance Note

The descriptions of **JEPA, world models, hierarchical planning, physical AI, and predictive abstraction** in this research note are derived from the supplied transcript of Yann LeCun's talk.

The connections to **knowledge graphs, ontologies, semantic models, provenance, knowledge infrastructure, and intelligent infrastructure** are my synthesis and interpretation.

The **First Five Things to Teach a Computer** is my original framework. The comparison between the First Five and world models is also my interpretation and should not be attributed to LeCun.

The broader proposed progression:

> **Know → Represent → Predict → Plan → Act → Learn**

is presented here as a synthesis for further research rather than as LeCun's framework.