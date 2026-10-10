# Research Brief: From Data Infrastructure to Learning Infrastructure

Connecting DIKW, MiGreatDataLake, the Digital Opportunities Compass, Project Compass, and DOIN

**Jason F. Kronemeyer**  
October 2026

---

## Executive Summary

Michigan is building increasingly sophisticated infrastructure for bringing previously fragmented data together. MiGreatDataLake, led through the Michigan Association of Intermediate School Administrators (MAISA), provides a particularly important example. MAISA describes the initiative as a statewide effort to unify data management, storage, and advanced analytics across Michigan's educational landscape through a modernized cloud platform downstream from MiDataHub (Michigan Association of Intermediate School Administrators, Annual Report).[^1]

But a data platform raises a larger question:

> What happens after the data have been integrated?

This research brief uses the Data-Information-Knowledge-Wisdom tradition, commonly abbreviated DIKW, as a conceptual lens for exploring that question. DIKW is not a single settled theory. Its intellectual lineage includes work by Cleveland, Milan Zeleny, and Ackoff, among others. Ackoff's influential formulation actually included an additional level, understanding, between knowledge and wisdom (Ackoff 3).[^2][^3]

Building on that lineage, I propose reframing DIKW not as a pyramid but as a learning loop:

> Data → Information → Knowledge → Understanding → Judgment → Action → Outcomes → New Data

This adaptation helps connect three bodies of work that have increasingly converged in my own research: MiGreatDataLake as data infrastructure, the Digital Opportunities Compass and Project Compass as frameworks for organizing context and community knowledge, and the Digital Opportunities Intelligence Network (DOIN) as my proposed architecture for connecting evidence, provenance, relationships, interventions, and outcomes.

The central proposition of this brief is straightforward:

> The next challenge in digital transformation is not simply building infrastructure that stores and processes more information. It is building trustworthy knowledge infrastructure that helps institutions and communities learn from evidence, act on that understanding, evaluate what happens, and learn again.

---

## 1. The Problem Has Changed

For much of the digital transformation era, the problem was access to data.

Information existed in different systems, used different formats, followed different governance practices, and often required significant technical effort before it could be combined meaningfully.

MiGreatDataLake demonstrates how that problem is beginning to change in Michigan education.

MAISA describes the initiative as a statewide strategic effort to unify data management, storage, and analytics across Michigan's educational landscape. Its 2025-26 annual report says the architecture operates downstream from MiDataHub and is intended to integrate structured Student Information System data with unstructured assets such as student artifacts and teacher observations. The report also identifies predictive analytics, early-warning interventions, and automated reporting among the intended uses of the resulting environment (Michigan Association of Intermediate School Administrators, Annual Report).[^1]

MAISA separately describes MiGreatDataLake as an extension of earlier MiDataExchange work involving MiRead, MiEWIMS, and student information systems (Michigan Association of Intermediate School Administrators, "MiGreatDataLake").[^4]

These are important data-infrastructure developments.

But they also expose the next problem.

Once information becomes integrated, governed, and accessible, how do we convert it into understanding that improves decisions?

That is no longer principally a storage problem.

**It is a knowledge problem.**

---

## 2. DIKW and Its Provenance

The familiar DIKW sequence is often represented as:

> Data → Information → Knowledge → Wisdom

Its history, however, is more complicated.

Frické's review of the DIKW literature identifies strands leading to the model through Cleveland, Mortimer Adler, Milan Zeleny, and Ackoff. Frické identifies the work of Zeleny in 1987 and Ackoff in 1989 among the traditional sources of the model (Frické 33-35).[^3]

Nikhil Sharma's historical reconstruction identifies Cleveland's 1982 "Information as Resource" as an important information-science precursor and traces still earlier conceptual antecedents while recognizing that these earlier formulations were not identical to the modern four-level DIKW model (Sharma).[^5]

Zeleny's 1987 work explicitly developed a data-information-knowledge-wisdom hierarchy. Sharma describes Zeleny's treatment as associating its levels with progressively different kinds of knowing (Sharma).[^5]

Ackoff's 1988 presidential address, published the following year as "From Data to Wisdom," introduced a particularly useful variation:

> Data → Information → Knowledge → Understanding → Wisdom (Ackoff 3).[^2]

Ackoff distinguished data as representations of observable properties, information as data transformed into useful form, and knowledge as know-how. Importantly for the argument developed here, he separated understanding from knowledge and connected it with explanation, learning, and adaptation. Wisdom went further, concerning effectiveness, values, judgment, and consequences (Ackoff 3-5).[^2]

DIKW should nevertheless not be treated as settled theory. Frické describes the hierarchy as widespread in information science and knowledge management while also reviewing substantial theoretical criticisms of the model and disagreement over the meanings of its underlying concepts (33-35).[^3]

That limitation is important.

I use DIKW here as a conceptual scaffold, not as a literal architecture or claim that data automatically transforms into wisdom.

---

## 3. From Hierarchy to Learning Loop

For the problems addressed by MiGreatDataLake, Project Compass, and DOIN, I believe DIKW becomes more useful when transformed from a hierarchy into a feedback process:

> Data → Information → Knowledge → Understanding → Judgment → Action → Outcomes → New Data

This is my adaptation of the DIKW tradition, not a model proposed by Ackoff, Zeleny, MAISA, Merit Network, or Cloudwick.

The addition of an explicit feedback cycle matters because institutions and communities do not reach wisdom and stop.

They observe conditions. They organize evidence. They develop explanations. They decide. They intervene.

Something happens.

Those outcomes create new observations, which become evidence for the next decision.

This changes the fundamental question from:

> How do we get more value from our data?

to:

> **How do we build institutional capacity to learn continuously from evidence?**

---

## 4. MiGreatDataLake as a Foundation for Learning

The documented architecture of MiGreatDataLake addresses important portions of the lower part of this learning cycle.

A 2026 MAISA job posting describes AWS-native environments leveraging Cloudwick Amorphic for data and analytics and identifies responsibility for implementing and optimizing data-lake and analytics solutions using the platform (Michigan Association of Intermediate School Administrators, "Cloud DevOps Manager"). This provides evidence of the project's implementation direction, though not a comprehensive technical specification.[^6]

According to Cloudwick, Amorphic supports data ingestion and integration, cataloging, metadata tagging, lineage, role-based access, governance, workflow automation, and deployment within a customer's AWS account (Cloudwick). These are vendor-published descriptions of platform capabilities rather than independent assessments of system performance.[^7]

Those capabilities address a critical problem: before organizations can reason reliably over information, they need mechanisms for discovering, governing, connecting, and tracing the underlying data.

But that does not complete the learning process.

A data catalog can establish that data exist.

Metadata can describe them.

Lineage can help establish where data originated and how they moved through a technical system.

The more difficult questions concern meaning:

- How are these observations related?
- Why might those relationships exist?
- What additional evidence would strengthen or weaken an explanation?
- What should we do in response?

Those questions begin moving from data infrastructure toward knowledge infrastructure.

---

## 5. The Digital Opportunities Compass as a Framework for Context

The Digital Opportunities Compass, developed by Colin Rhinesmith, Pierrette Renée Dagg, Johannes M. Bauer, Greta Byrum, and Aaron Schill, offers a useful model for thinking about that transition.

The authors organize digital opportunity across six components: contexts, governance, connectivity, skills, applications, and outcomes (Rhinesmith et al.).[^8]

A later paper by the authors emphasizes that advanced broadband ecosystems are highly interconnected and argues that their relevant interdependencies need to be represented more completely. They propose integrating insights from the Compass and statistical analysis toward what they describe as a dynamic broadband policy learning system in which evidence can improve understanding of interventions over time (Bauer et al.).[^9]

This provides an important bridge to DIKW.

My interpretation is that the Compass can function as a map for organizing meaning.

Connectivity alone rarely explains an outcome. Connectivity exists within contexts. Governance shapes decisions. Skills affect people's ability to use technology. Applications determine what people can accomplish through it. Outcomes provide evidence about whether conditions actually changed.

The Compass therefore gives us a way to ask not just what data exist, but which relationships we need to investigate.

---

## 6. Project Compass Adds Community Context

Project Compass brings this framework into community practice.

Merit Network describes Project Compass as a USDA Broadband Technical Assistance-funded initiative applying the Digital Opportunities Compass framework in eight rural Michigan communities to understand local needs, develop digital-skills strategies, support infrastructure planning, and provide technical assistance (Merit Network, "Projects").[^10]

Merit Network also describes listening to residents, identifying connectivity and digital-skills barriers, supporting community education, organizing groups, connecting residents with resources, and assisting communities with funding opportunities and grant applications (Merit Network, "Project Compass").[^11]

That community dimension matters because not every relevant fact about a place appears in an administrative dataset.

Local experience, institutional relationships, community priorities, and people's descriptions of barriers can contribute evidence that quantitative datasets alone do not provide.

The forward-looking opportunity, in my view, is not to substitute community knowledge for quantitative evidence or vice versa.

**It is to connect them while preserving the provenance and context of both.**

---

## 7. DOIN as Knowledge and Learning Infrastructure

This is the problem I am exploring through the Digital Opportunities Intelligence Network.

DOIN is my developing framework. It is not an official component of Project Compass, Merit Network, MAISA, MiGreatDataLake, or the original Digital Opportunities Compass.

I have described DOIN through three related concepts: the Compass as the map, a semantic network as the structure, and intelligence as the learning engine (Kronemeyer, "Digital Opportunities Intelligence Network").[^12]

The idea is straightforward.

A community problem rarely fits neatly within one database.

Relevant evidence may be distributed among demographic data, infrastructure records, broadband measurements, community observations, workforce information, schools, policies, program evaluations, institutions, and funding sources.

A semantic knowledge system could provide a way to represent relationships across those evidence sources.

That changes the questions we can ask.

Instead of only asking:

> Where is broadband unavailable?

we can begin exploring:

> Where do connectivity limitations intersect with digital skills, affordability, workforce needs, institutional capacity, community priorities, and available resources?

That movement from retrieval toward relationships is where I see knowledge infrastructure becoming important.

---

## 8. Provenance Must Be Part of the Architecture

There is a consequence to connecting more data, community knowledge, analytical methods, and AI.

The resulting system must also become more accountable for what it claims to know.

If an AI-assisted learning system produces a recommendation, we should be able to investigate where its supporting evidence originated, who contributed it, what methodology produced it, what transformations occurred, what limitations accompany it, and how the recommendation relates to the evidence.

My developing DOIN provenance framework treats this chain from evidence through interpretation and outcomes as part of the knowledge system itself (Kronemeyer, "DOIN Provenance Framework").[^13]

This sits alongside, rather than replaces, technical data lineage.

Cloudwick documents metadata, lineage, access-control, governance, and observability capabilities within Amorphic (Cloudwick).[^7]

I distinguish that kind of technical lineage from knowledge provenance.

Technical lineage can help answer:

> Where did this data come from and how did it move?

Knowledge provenance needs to help answer:

> Why do we believe this claim, and what evidence supports it?

That distinction is my synthesis.

Both become increasingly important as AI systems move closer to public decision-making.

---

## 9. A Research Agenda for the Next Layer

The convergence of data infrastructure, semantic technologies, AI, community knowledge, provenance, and policy learning suggests a research agenda rather than a finished architecture.

One question concerns **semantics**. Once governed data becomes available, what ontology or semantic model should connect observations across institutional and community contexts?

A second concerns **provenance**. How should a knowledge system preserve the chain connecting a recommendation to datasets, community observations, analytical methods, assumptions, and previous interventions?

A third concerns **community evidence**. How can qualitative and place-based knowledge participate in a computational knowledge system without being stripped of the people, circumstances, and uncertainty that give it meaning?

A fourth concerns **policy learning**. The Compass authors envision communities learning from interventions and peer communities (Bauer et al.). How could the conditions surrounding an intervention, the intervention itself, its observed outcomes, and subsequent interpretation remain connected as evidence for future decisions?[^9]

And finally, there is the question of **human judgment**.

Ackoff's distinction between knowledge, understanding, and wisdom becomes especially relevant here. His framework places values and judgment at the level of wisdom rather than treating greater quantities of information as sufficient (Ackoff 3-5).[^2]

That suggests an important design principle for future knowledge infrastructure:

> The objective should not be to automate wisdom. It should be to improve the evidence, context, memory, and feedback available to people exercising judgment.

That final statement is my proposed principle, grounded in but not claimed by Ackoff's work.

---

## 10. Conclusion: The Infrastructure That Helps Us Learn

We have spent decades building networks that move bits.

Then we built systems that move and integrate data.

Now platforms such as MiGreatDataLake demonstrate the possibility of creating shared environments in which information from previously disconnected sources can support analytics and applications across Michigan education (Michigan Association of Intermediate School Administrators, Annual Report).[^1]

The Digital Opportunities Compass gives us a framework for examining relationships among contexts, governance, connectivity, skills, applications, and outcomes (Rhinesmith et al.).[^8]

Project Compass takes that framework into rural Michigan communities through local engagement, digital-skills work, infrastructure planning, and technical assistance (Merit Network, "Projects"; Merit Network, "Project Compass").[^10][^11]

The Compass authors' subsequent research points toward continuous policy learning from data, interventions, and peer communities (Bauer et al.).[^9]

DOIN asks what infrastructure might help make that kind of learning durable, connected, explainable, and auditable.

The DIKW tradition provides a useful conceptual starting point, provided that we also recognize its contested history and theoretical limitations.

I would take it one step further.

Data gives us observations.

Information places observations into usable form.

Knowledge connects what we know.

Understanding helps us explain relationships.

Judgment helps us choose what to do.

Then we act.

The results become new evidence.

And we learn again.

That is why I increasingly believe the next frontier is not a bigger data lake.

**It is learning infrastructure.**

Infrastructure that helps us remember what we knew, understand why we believed it, trace the evidence behind our decisions, observe what happened next, and improve the next decision we make.

The real opportunity is not simply to build systems that know more.

**It is to help communities learn better together.**

---

## Works Cited

[^1]: Michigan Association of Intermediate School Administrators. MiGreatDataLake 12c-Consolidation Grant 2025-26 Annual Report. 2026.

[^2]: Ackoff, Russell L. "From Data to Wisdom." *Journal of Applied Systems Analysis*, vol. 16, 1989, pp. 3-9. Accessed 10 Oct. 2026.

[^3]: Frické, Martin. "The Knowledge Pyramid: The DIKW Hierarchy." *Knowledge Organization*, vol. 46, no. 1, 2019, pp. 33-46.

[^4]: Michigan Association of Intermediate School Administrators. "MiGreatDataLake." MAISA. Accessed 10 Oct. 2026.

[^5]: Sharma, Nikhil. "The Origin of Data Information Knowledge Wisdom (DIKW) Hierarchy." Updated 4 Feb. 2008.

[^6]: Michigan Association of Intermediate School Administrators. "MiGreatDataLake Cloud DevOps Manager." 4 Aug. 2026.

[^7]: Cloudwick. "Amorphic Data Platform: The Foundation for AI-Powered Automation." Cloudwick. Accessed 10 Oct. 2026.

[^8]: Rhinesmith, Colin, et al. *Digital Opportunities Compass: Metrics to Monitor, Evaluate, and Guide Broadband and Digital Equity Policy*. Merit Network and Quello Center, 24 Feb. 2023.

[^9]: Bauer, Johannes M., et al. "A Comprehensive Framework to Monitor, Evaluate, and Guide Broadband and Digital Equity Policy." SSRN, 30 Aug. 2023.

[^10]: Merit Network. "Projects." Merit Network. Accessed 10 Oct. 2026.

[^11]: Merit Network. "Project Compass." Merit Network. Accessed 10 Oct. 2026.

[^12]: Kronemeyer, Jason. "Digital Opportunities Intelligence Network: The 'Policy Learning Machine.'" Jason Kronemeyer, 7 Nov. 2025.

[^13]: Kronemeyer, Jason. "The DOIN Provenance Framework: Extending the Digital Opportunities Compass Toward a Verifiable Policy Learning Machine." Jason Kronemeyer. Accessed 10 Oct. 2026.

---

## Provenance Note

This brief intentionally distinguishes source findings from synthesis. MAISA supports the statements about MiGreatDataLake; Cloudwick's own documentation supports only the capabilities it claims for Amorphic; the Compass authors support the Digital Opportunities Compass and policy-learning concepts; Merit Network supports the descriptions of Project Compass; and the DIKW discussion separates historical formulations from this adaptation.

The learning-loop formulation, the distinction between data infrastructure and knowledge infrastructure, the extension from technical lineage to knowledge provenance, and the proposed convergence of MiGreatDataLake, Compass, Project Compass, and DOIN are my synthesis. They should be read as a research direction, not as claims that the organizations or original authors cited here have adopted that architecture.

**Writing changes**: The article has been recast as a research brief with an executive argument, literature-grounded conceptual framework, explicit research agenda, and forward-looking conclusion. Tables were omitted because the relationships are interpretive rather than comparative, and narrative paragraphs were used so the provenance and evolution of the argument remain visible.