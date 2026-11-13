---
layout: post
title: "We Have Traveled a Long Way"
subtitle: "Learning Notes on the Digital Navigator Ontology, Project Compass, and DOIN"
date: 2026-11-13
author: Jason Kronemeyer
categories:
  - learning-notes
  - digital-opportunity
tags:
  - DOIN
  - Project Compass
  - Digital Opportunities Compass
  - ontology
  - knowledge graphs
  - digital navigation
  - provenance
  - network science
  - community intelligence
  - policy learning
description: "A reflective learning note tracing the evolution from an early Digital Navigator ontology toward Project Compass and the Digital Opportunities Intelligence Network as a provenance-aware, community-centered learning system."
excerpt: "We began by asking what a Digital Navigator needs to know. Eighteen months later, the larger question is how communities can continuously construct, validate, connect, learn from, and act on knowledge about digital opportunity."
---

# We Have Traveled a Long Way

## Executive Summary

Over roughly the last 18 months, our work has moved from designing an ontology around the knowledge needs of a Digital Navigator toward a much larger question: **How can a community continuously construct, connect, validate, learn from, and act upon knowledge about its own digital opportunities?** The early ontology organized concepts such as people, devices, connectivity, resources, and skills. That work remains valuable, but it now looks less like the whole system and more like a Digital Navigation domain ontology within a larger knowledge architecture.

The **Digital Opportunities Compass** provides the conceptual framework for understanding digital opportunity across Contexts, Governance, Connectivity, Skills, Applications, and Outcomes. **Project Compass** moves that framework into participatory community practice, where local people and institutions contribute situated knowledge about needs, assets, relationships, aspirations, and conditions. **DOIN, the Digital Opportunities Intelligence Network**, increasingly represents the intelligence and learning infrastructure that can connect those observations over time.

This progression also changes how we understand the knowledge graph. The graph is not DOIN itself. It is better understood as the **governed semantic memory of DOIN**: a place where entities, relationships, evidence, claims, provenance, observations, interventions, and outcomes can remain connected and revisable. Ontology gives that memory structure; provenance tells us how we know; network science helps reveal relationships; analysis tests hypotheses; and Project Compass provides a recurring community learning process.

The emerging cycle is therefore larger than data collection: **Question → Evidence → Claim → Knowledge → Decision → Intervention → Outcome → Learning → New Question.** The Compass helps organize what we ask and observe. Project Compass grounds that work in communities. The graph remembers. The network reveals. DOIN learns.

Looking back, the ontology was never really the destination. It became part of the infrastructure for a community-centered learning system. That also reveals a deeper connection to my **First Five Things to Teach a Computer** framework: when we teach a computer what our community means, the discipline of formalizing that knowledge exposes our own assumptions, disagreements, missing evidence, and unanswered questions. We teach the system, and the process teaches us.

## Reflection

We have traveled a long way.

Looking back at the ontology work from early 2025, I can see many of the concepts that eventually became important to the Digital Opportunities Intelligence Network, but I do not think we completely understood what we were building yet. We were trying to describe the world of a Digital Navigator: people, devices, connectivity, resources, skills, and the relationships among them. *Ontologies and Knowledge Graphs* described relationships such as a user using a device, a device connecting to a network, and a resource helping develop a skill.[^1]

That was useful work. It was also only the beginning.

What has changed over roughly the last 18 months is the scale of the question. Instead of asking only **what a Digital Navigator needs to know**, we are increasingly asking:

> **How can a community continuously construct, connect, validate, learn from, and act upon knowledge about its own digital opportunities?**

That shift helps me understand the relationship among the **Digital Opportunities Compass, Project Compass, Digital Navigation, and DOIN** much more clearly.

## 1. The Compass Was Already Pointing Toward a Learning System

The Digital Opportunities Compass established six interconnected dimensions: **Contexts, Governance, Connectivity, Skills, Applications, and Outcomes**. The important insight, however, was not simply the taxonomy.

The original Compass work described digital transformation as longitudinal. An outcome in one period can become part of the context affecting the next period. Income, education, skills, connectivity, institutional capacity, and other conditions do not sit still while programs operate around them. Communities change, and those changes alter what becomes possible next. *Digital-Opportunites-Compass-Paper-20220223* connects the Compass to longitudinal knowledge bases, learning agendas, logic models, and outcomes-based evaluation.[^2]

That seems much more important to me now than it did when we first developed the framework.

The Compass was never really just six buckets for indicators. It was beginning to describe a **dynamic system**.

## 2. Project Compass Moved the Framework Into Communities

The next important step was Project Compass.

The Compass Field Guide work shifted the framework toward practice: local assessment, stakeholder engagement, infrastructure, digital literacy, community assets, and locally appropriate interventions. *Compass Field Guide General - Draft* describes the Compass as a framework communities can use to map assets, understand their circumstances, build infrastructure and skills, and guide their broader digital transformation.[^3]

This introduced something that becomes increasingly important in the later work: **local knowledge**.

A broadband map can tell us whether infrastructure is reported as available. It cannot necessarily tell us whether residents trust the provider, whether a household can maintain a connection, whether someone knows where to receive assistance, whether a library has enough staff capacity to provide that assistance, whether an older adult is comfortable using telehealth, or whether community organizations even agree on what success should mean.

Project Compass therefore became more than measurement. It became a mechanism for **asking communities what their digital environment actually looks like**.

## 3. The Digital Navigator Ontology Was an Early Window Into a Larger Problem

Our early Digital Navigator ontology work put concepts such as `User`, `Device`, `Resource`, `Skill`, and `Connectivity` into relationships. We were thinking about classes, subclasses, properties, instances, and eventually the representation of those relationships as a knowledge graph.[^1]

At the time, the Digital Navigator was naturally near the center. I would model it differently today.

The **Digital Navigator is a role**. **Digital Navigation is a process. Digital Opportunity is the larger domain** in which that process operates.

That distinction became clearer through actual EUPConnect work. The Regional Digital Navigator role developed for the Eastern Upper Peninsula goes considerably beyond conventional technical assistance. It includes active listening, assessing client aspirations, connectivity and device assistance, coaching, community engagement, data collection, program management, partnership development, reporting, cultural competence, continuous improvement, and relationships with local and outside subject-matter experts.[^4]

Seen through the lens of DOIN, the Digital Navigator starts to look like something more interesting:

> **a boundary-spanning human node in a regional knowledge network.**

The Navigator listens, observes, teaches, refers, connects, documents, and learns.

I would therefore preserve the early ontology work but reposition it as a **Digital Navigation domain ontology within the larger DOIN ontology ecosystem**.

## 4. The Ontology Itself Has Grown Up

The newer vocabulary work shows how much broader the model has become.

*doin-vocabulary-review-v0.1* preserves the Compass dimensions while extending the vocabulary into digital literacy, information literacy, data literacy, AI literacy, computational thinking, cybersecurity awareness, stakeholders, institutions, public funding, governance mechanisms, transmission technologies, and outcome concepts.[^5]

What once looked roughly like:

**Person → Device → Connectivity → Resource → Skill**

now looks much more like:

**People + Places + Institutions + Infrastructure + Capabilities + Relationships + Evidence + Interventions + Outcomes + Time**

That is a significantly different ontology.

Increasingly, I think the **relationships** are where much of the intelligence resides. Who trusts whom? Who works with whom? Which organization serves which community? Who refers people to which resources? Who teaches whom? Which institution bridges otherwise disconnected networks? Which resource enables which intervention? Which intervention produces which outcome? Which outcome subsequently changes community context?

These are no longer just ontology questions. They become **network-science questions**. That connects directly with the more recent idea that *the network knows*.

## 5. DOIN Introduces Evidence and Provenance as First-Class Objects

This may be one of the biggest advances over the original ontology work.

If DOIN is going to become community knowledge infrastructure, storing facts is insufficient. It must also represent **how we know what we think we know**.

The *doin-provenance* work makes this explicit by introducing provenance as a first-class element of the knowledge system. Observations, indicators, analyses, and outcomes can be connected to sources, methods, contributors, and confidence.[^6]

That changes the nature of the graph.

Instead of asserting simply:

> Library X provides digital-skills training.

DOIN should ultimately be capable of representing:

> Who made that claim? Based on what observation or record? When was it true? What population did the program serve? What definition of "digital skills" was being used? What evidence supports the assertion? Has somebody else corroborated it? Has the situation subsequently changed?

This is especially important because community knowledge is temporal, situated, imperfect, and frequently contested.

The ontology therefore needs to model not just **things**, but **claims about things**.

## 6. Semantic Friction Became Part of the Problem

Another development I would not have appreciated fully during the early Digital Navigator ontology work is the importance of **semantic friction**.

Different organizations can use the same word and mean substantially different things. An ISP might understand success as service availability. A state agency may emphasize subscription or program outcomes. A school may care about student participation and learning. A community organization may care about whether technology creates genuine opportunity.

The more recent DOIN work recognizes that these differences are not noise to be eliminated. They are themselves information. *sem1* describes semantic friction as something that can be represented and potentially measured, while framing community development as movement through awareness, engagement, participation, leadership, institution building, and eventually collective intelligence.[^7]

That represents another significant evolution.

The purpose of the ontology is therefore not simply to enforce a universal vocabulary. It must help us discover **where meanings align, where meanings differ, and where those differences matter**.

## 7. The Knowledge Graph Is Not DOIN

This distinction now feels foundational.

*DOIN_Ontology_Pipeline_Policy_Learning_Synthesis* distinguishes the knowledge graph from the policy-learning system itself. Instead, the graph serves as the **governed semantic memory** of that system. The ontology pipeline provides a method for keeping that memory coherent, traceable, revisable, and reusable.[^8]

That gives us a much clearer architecture.

The **Compass** tells us the dimensions across which digital opportunity should be understood.

**Project Compass** provides a participatory process for observing those dimensions in actual communities.

**Ontologies** give the observations shared semantic structure.

**Provenance** tells us where claims came from and how much confidence we should place in them.

The **knowledge graph** remembers entities, claims, and relationships.

**Network science** helps reveal structures and relationships that are difficult to see otherwise.

**Statistical and causal methods** help test observations and hypotheses.

**DOIN** connects these components into an ongoing learning system.

That is considerably more sophisticated than the knowledge graph we imagined at the beginning.

## 8. The Cycle Is Beginning to Close

The original Compass contains an idea that now looks remarkably prescient: **outcomes become future context**.[^2]

With DOIN, we can make that concept computational and operational.

A community identifies a question. Evidence is collected. Observations become structured claims. Claims are connected through the ontology. Provenance establishes their lineage. The graph preserves the developing knowledge. Analysis identifies patterns and tests hypotheses. Communities make decisions. Programs and interventions follow. Outcomes are observed. Those outcomes change community conditions. New questions emerge. Another learning cycle begins.

This suggests a simple formulation:

> **Question → Evidence → Claim → Knowledge → Decision → Intervention → Outcome → Learning → New Question**

The graph is the memory of that process.

**DOIN is the learning process.**

## 9. Project Compass Looks Different From Here

There is an intriguing earlier clue in *BTA Plan Update - Draft - 02172024*. That work proposed combining knowledge collected through Compass with the supporting research and placing it into a knowledge graph so that relationships relevant to digital equity could be explored in local context.[^9]

We can now describe that aspiration considerably more precisely.

Project Compass can become the **participatory community-learning layer of DOIN**.

Communities are not merely subjects being measured. They participate in creating the knowledge through which their circumstances are understood.

That gives us a useful way of expressing the emerging cycle:

**Compass asks.**  
**People contribute.**  
**Evidence grounds.**  
**Ontology structures.**  
**Provenance establishes lineage.**  
**The graph remembers.**  
**Network science reveals relationships.**  
**Analysis tests hypotheses.**  
**Communities act.**  
**Outcomes produce new evidence.**  
**DOIN learns.**  
**Compass asks again.**

## 10. A Connection I Did Not See at the Beginning

Looking backward also makes the relationship to my **First Five Things to Teach a Computer** framework much more apparent.

Ontology development is, quite literally, an exercise in teaching a computer what our world means.

We tell it that a Digital Navigator is a role. We explain what a community is, what counts as evidence, what a resource does, how organizations relate, what an outcome represents, and why two apparently identical observations might have profoundly different meanings in different contexts.

But something interesting happens while doing that.

Every time the computer forces us to define a concept precisely, **we expose something we ourselves have not resolved**. Our disagreement becomes visible. Our assumptions become visible. Missing relationships become visible. Gaps in evidence become visible. Questions that have never been asked become visible.

So the learning relationship becomes reciprocal.

We teach the system about the community, and in trying to teach it, **we learn something about the community and about ourselves**.

That may ultimately be one of the deeper connections between the First Five framework, Project Compass, and DOIN.

## Working Synthesis

Where I began was something close to:

> **How do we build an ontology that helps a Digital Navigator understand people, devices, connectivity, resources, and skills?**

Where the work has arrived is much closer to:

> **How do we create a community-governed, evidence-backed, provenance-aware semantic memory that allows people and machines to learn continuously about digital opportunity, understand relationships, test assumptions, make better decisions, observe outcomes, and carry that learning into the next cycle?**

Those are related questions.

But they are not the same question.

**We have traveled a long way.**

And perhaps the most important lesson is that the ontology was never really the destination. It became part of the infrastructure that allows **Project Compass to observe, the knowledge graph to remember, the network to reveal, and DOIN to learn.**

## References

[^1]: *Ontologies and Knowledge Graphs*. Early Digital Navigator ontology and knowledge-graph work, including User, Device, Resource, Skill, and Connectivity concepts.

[^2]: *Digital-Opportunites-Compass-Paper-20220223*. Foundational Digital Opportunities Compass framework, including Contexts, Governance, Connectivity, Skills, Applications, Outcomes, and longitudinal learning.

[^3]: *Compass Field Guide General - Draft*. Translation of the Compass into community assessment, stakeholder engagement, infrastructure, skills development, and implementation practice.

[^4]: *EUPCC Program Manager- Digital Navigator*. Operational development of Digital Navigation as a regional, relational, community-facing, and continuous-improvement role.

[^5]: *doin-vocabulary-review-v0.1*. Expansion of Compass concepts into the emerging DOIN vocabulary, including literacy, governance, stakeholder, infrastructure, and outcome concepts.

[^6]: *doin-provenance*. Development of evidence lineage and provenance as first-class elements of the DOIN knowledge architecture.

[^7]: *sem1*. Development of semantic friction, developmental gradients, and collective-intelligence concepts.

[^8]: *DOIN_Ontology_Pipeline_Policy_Learning_Synthesis*. Synthesis distinguishing the policy-learning system from the knowledge graph and ontology pipeline, with the graph serving as governed semantic memory.

[^9]: *BTA Plan Update - Draft - 02172024*. Earlier proposal to combine Compass knowledge and supporting research in a knowledge graph for exploring locally meaningful relationships.
