---
layout: research-note
status: review
title: "What I Learned Building My First Billion-Record Research Data Infrastructure"
subtitle: "From broadband data engineering to statistical inference, inequality, and learning infrastructure"
description: "Reflections on my contribution to an NSF Internet Measurement Research project with the University of Michigan and Merit Network, where I built my first billion-record research data infrastructure, contributed to FCC Fabric and BDC integration, and learned from Dr. Stilian Stoev how the Hájek estimator and Gini coefficient can deepen our understanding of broadband measurement and inequality."
author: "Jason F. Kronemeyer"
date: 2026-09-23
categories:
  - Data Infrastructure
  - Broadband
  - Research
  - Digital Opportunity
tags:
  - NSF
  - Internet Measurement Research
  - IMR
  - University of Michigan
  - Merit Network
  - Broadband
  - FCC Fabric
  - Broadband Data Collection
  - DuckDB
  - Parquet
  - Python
  - Data Engineering
  - Reproducible Research
  - Hájek Estimator
  - Gini Coefficient
  - Digital Opportunity
  - Public Interest Technology
  - Research Data Infrastructure
  - Statistical Inference
  - Provenance
  - Semantic Interoperability
---

# What I Learned Building My First Billion-Record Research Data Infrastructure

In 2025, I had the opportunity to contribute research data infrastructure to a National Science Foundation **Internet Measurement Research: Methodologies, Tools, and Infrastructure (IMR)** project involving researchers at the University of Michigan and Merit Network. I came into the project primarily from the data engineering side: building pipelines, organizing large datasets, working across research repositories, and figuring out how to make complex broadband data more accessible and reusable.

The experience became much more than a technical project. It was the first time I had designed and worked with a research data infrastructure containing **approximately one billion records**. It pushed me deeper into DuckDB, Parquet, Python, SQL, and R, but it also introduced me to a more important set of questions about measurement, statistical inference, inequality, provenance, and what we can responsibly claim to know from data.

A particularly valuable part of the experience was learning from **Dr. Stilian Stoev at the University of Michigan**. Dr. Stoev helped me connect the infrastructure I was building to the statistical questions the research was trying to answer. In particular, he taught me about the **Hájek estimator** and the **Gini coefficient**, two concepts that significantly changed how I think about broadband data and public-interest data infrastructure.

The project reinforced a principle that increasingly shapes my work:

> **The goal of data infrastructure should not simply be to make more data available. It should help us ask better questions, make assumptions visible, support better inference, reveal disparities, and create opportunities to learn.**

## The NSF Internet Measurement Research Project

The work was part of the NSF Internet Measurement Research program and supported research examining methods for improving how broadband availability and performance can be inferred from observational measurements, including crowdsourced speed-test data.

One resulting research paper was:

> Stuyvesant, A., Stoev, S., & Michailidis, G. (2025). *Towards unbiased inference of Internet broadband availability based on observational speed test data*. SSRN Working Paper No. 5372801. NSF Public Access Repository. https://par.nsf.gov/servlets/purl/10668222

The paper is associated with **NSF Award 2319593** and preserved in the NSF Public Access Repository as **PAR ID 10668222**.

My role was primarily on the **research data infrastructure and data engineering side**. I developed reusable infrastructure for ingesting, organizing, transforming, integrating, and analyzing large broadband and telecommunications datasets. This included work with FCC infrastructure data, DuckDB databases, Parquet-based storage, Python automation, SQL and R analytical workflows, documentation, and research repositories.

One part of that contribution was formally acknowledged in the resulting paper:

> “The authors acknowledge the technical support of Mr Jason Kronemeyer in part of the software pipeline used to join the FCC fabric and BDC data sets.”
>
> — Stuyvesant et al. (2025, p. 43)

That acknowledgment provides useful provenance for my contribution, but the more important story for me is what I learned while doing the work.

## My First Billion-Record Data Infrastructure

This project was my first experience designing and working with a research data infrastructure containing approximately **one billion records**. That scale forced me to reconsider some of the assumptions that work reasonably well with smaller datasets.

When data is relatively small, it is easy to develop a workflow around loading a dataset into memory, manipulating it, producing an output, and moving on. At much larger scales, those assumptions begin to break down. Storage formats, query execution, data types, joins, intermediate transformations, reproducibility, provenance, and update processes become architectural concerns rather than implementation details.

This was where **DuckDB and Parquet** became particularly valuable. Instead of assuming that billion-record analytics automatically required a large proprietary platform or distributed computing environment, I learned how much could be accomplished with lightweight, open tools when the underlying architecture was designed appropriately.

The experience taught me an important lesson: **large data does not necessarily require large infrastructure; it requires thoughtful infrastructure**.

Some of the capabilities I developed or supported included:

- Reusable **Python and DuckDB pipelines** for ingesting and managing FCC broadband infrastructure data.
- Disk-based analytical workflows using **DuckDB and Parquet** rather than requiring complete datasets to reside in memory.
- Reusable **SQL, Python, and R workflows** for research exploration and analysis.
- Structured organization of datasets, notebooks, analytical assets, and research code.
- Repeatable processes for incorporating future dataset releases rather than treating each update as a one-time exercise.
- Technical documentation and repository stewardship to improve reproducibility and knowledge transfer.
- Data infrastructure supporting downstream broadband analysis using FCC, Ookla, and related datasets.

The technical accomplishment mattered, but working at this scale also taught me that **making a billion records queryable is not the same thing as making a billion records meaningful**.

## Data Engineering Is Part of the Research Method

One of my most important lessons from the project was that data engineering is not simply preparation for research. It is part of the research method.

My work included developing part of the software pipeline used to integrate the **FCC Broadband Serviceable Location Fabric with Broadband Data Collection (BDC) datasets**. The publication acknowledgment documents that contribution directly (Stuyvesant et al., 2025, p. 43).

Building that pipeline made the relationship between engineering decisions and research outcomes tangible. Choices about identifiers, joins, transformations, missing values, geographic units, temporal alignment, and data organization influence what researchers can subsequently observe and analyze.

A technically successful join does not necessarily mean that the resulting data is conceptually valid. FCC Fabric data, BDC data, crowdsourced speed tests, geographic data, provider information, and other broadband datasets are created for different purposes. They can have different definitions, collection processes, spatial units, temporal characteristics, incentives, and limitations.

Getting two datasets to join is a technical problem. Determining whether the things being joined actually represent comparable concepts is a much harder problem.

That distinction strengthened my interest in **provenance, semantic interoperability, shared vocabulary, and semantic friction**. As datasets become larger and more interconnected, understanding what the data means becomes at least as important as understanding how to process it.

## Learning From Dr. Stoev

One of the most valuable aspects of the project was the opportunity to learn directly from **Dr. Stilian Stoev**. I entered the project primarily thinking about how to engineer systems capable of working with very large datasets. Dr. Stoev helped me understand what comes after the infrastructure is built: determining what we can responsibly infer from the observations.

Two concepts he taught me became especially important: the **Hájek estimator** and the **Gini coefficient**.

These were not simply new statistical terms for me. They helped connect data engineering to questions I increasingly care about in broadband and digital opportunity work: Who is represented in the data? Who is missing? How much confidence should we place in an estimate? How is opportunity distributed within a community? What can an average conceal?

That mentorship helped move my thinking from simply processing data toward understanding the relationship among **scale, measurement, inference, and distribution**.

## A Billion Records Can Still Be Biased

The **Hájek estimator** became particularly meaningful in the context of observational broadband speed-test data.

Crowdsourced speed tests are not generated through random sampling. Some households test frequently, while others may never test. Some geographic areas generate large numbers of observations, while other places remain sparsely represented. The decision to conduct a speed test may itself be related to broadband performance or other characteristics of the household, location, or network.

That means a very large collection of speed tests is not automatically representative of the population researchers want to understand.

Dr. Stoev helped me understand how propensity-based weighting and the **Hájek estimator** could be used to reason about this problem and improve inference from observational data. For someone coming from the infrastructure side, this was an important conceptual shift.

I had spent considerable effort making very large datasets computationally accessible. The Hájek estimator helped me understand that accessibility and representativeness are fundamentally different questions.

> **A billion records can still be biased.**

That simple observation has stayed with me. More data can improve our analytical possibilities, but volume alone does not eliminate selection effects, measurement problems, missing observations, or systematic bias.

Data engineering asks whether we can process the observations. Statistical inference asks what we are justified in concluding from them. A well-engineered pipeline can efficiently process biased observations, so the first does not guarantee the second.

This is where I began to see research data infrastructure differently. Its purpose is not simply to process more records. Its purpose is to create a reliable computational foundation upon which more rigorous questions and methods can operate.

## Learning to Look Beyond the Average

Dr. Stoev also taught me about the **Gini coefficient** and how it could be applied to broadband conditions.

I had previously associated the Gini coefficient primarily with economics and income inequality. Applying the same underlying concept to broadband gave me a new way to think about digital opportunity.

An average can tell us something useful about a community, but it cannot necessarily tell us **how broadband conditions are distributed within that community**. Two communities might have similar average broadband performance while having dramatically different internal distributions. One might have relatively consistent connectivity across locations, while another might combine excellent connectivity in some places with very poor connectivity in others.

Averages can hide those differences.

I supported data workflows that Dr. Stoev subsequently used to generate **broadband-proportion, broadband-index, and Gini-coefficient maps**. Seeing those analytical ideas connected back to the DuckDB infrastructure I had helped develop made the lesson tangible.

It changed the questions I wanted to ask. Instead of only asking, *How much broadband does this community have?*, I became increasingly interested in asking:

> **How is broadband opportunity distributed across the community?**

That is a different question, and for digital opportunity work, I believe it is often the more important one.

## From Broadband Availability to Broadband Opportunity

The distinction between averages and distributions matters because broadband availability and digital opportunity are related, but they are not synonymous.

A community-level average can make conditions appear acceptable while masking substantial differences among neighborhoods, households, institutions, or geographic areas. Likewise, a coverage percentage can tell us whether infrastructure is reported as available without necessarily telling us about performance, reliability, affordability, adoption, accessibility, or the distribution of those conditions across a community.

The **Hájek estimator** gave me a framework for thinking about **representativeness and inference**. The **Gini coefficient** gave me a framework for thinking about **distribution and inequality**. The billion-record data infrastructure gave researchers the computational foundation needed to operationalize those questions across very large datasets.

Together, those experiences changed how I think about broadband intelligence.

A broadband map or index should not be treated as a final statement about a community. It is a model built from particular observations, definitions, assumptions, and methods. Its value comes from understanding those assumptions and being willing to test the model against additional evidence.

## More Data Does Not Automatically Create More Legibility

Perhaps the most counterintuitive lesson from working with my first billion-record infrastructure was that **more data does not necessarily make a problem easier to understand**.

We can have enormous quantities of data and still struggle to understand a community. We can have precise measurements and still misunderstand what they represent. We can have sophisticated models and still overlook the assumptions embedded within them. We can have a billion records and still be missing the people, places, or experiences that matter most.

This is where the project began connecting with my broader interest in **legibility**. Data systems make aspects of the world visible by reducing complexity into categories, variables, geographic units, measurements, and models. That reduction is necessary, but it is never complete.

More records can create greater statistical precision while simultaneously creating an illusion of certainty if we do not understand the provenance and meaning of the underlying observations.

A model is not reality. A map is not the community. A broadband index is not broadband opportunity itself.

These are representations that help us reason about complex systems. Their value comes from our ability to test them, challenge them, compare them with other evidence, and revise them when reality tells us something different.

## Reproducibility Is Infrastructure

The project also deepened my understanding of reproducibility. Reproducibility requires much more than putting code in a repository.

At billion-record scale, reproducibility depends on an ecosystem of decisions. We need to know where the data originated, which version was used, how it was transformed, which identifiers were selected, how datasets were joined, which intermediate products were retained, and whether the pipeline can be rerun when a new FCC dataset becomes available.

Another researcher should be able to understand what happened. Ideally, an analytical result should be traceable backward through the transformations and source data that produced it.

This is why **provenance** became increasingly important to me. A research system should help us understand the chain of evidence behind an analytical result.

That is not merely good data management. It is part of making research **inspectable, challengeable, reproducible, and learnable**.

## Open Tools and the Architecture of Scale

The project reinforced my preference for open and interoperable analytical tools. My experience with **DuckDB, Parquet, Python, SQL, and R** demonstrated that sophisticated research infrastructure does not always require a massive centralized platform.

There is something powerful about an architecture in which data can remain in open formats while different analytical tools interact with the same underlying evidence. That approach can reduce unnecessary duplication, improve portability, lower infrastructure barriers, and make it easier for researchers with different technical backgrounds to participate.

It also aligns with a broader principle that has become increasingly important in my work:

> **Public-interest data infrastructure should maximize our ability to learn from data without unnecessarily locking the data, knowledge, or analytical process into a particular vendor or platform.**

Open infrastructure does not solve every problem, but it can create better conditions for transparency, reuse, collaboration, and long-term stewardship.

## Interoperability Is Ultimately About Meaning

The project also reinforced that interoperability has multiple layers. Technical interoperability asks whether systems can exchange data. Syntactic interoperability asks whether they can understand its structure. Semantic interoperability asks the harder question: **Do we agree about what the data means?**

A common identifier can solve a join. It cannot resolve a disagreement about definitions.

This is where my experience on the project began connecting with my broader interests in provenance, shared vocabulary, semantic interoperability, legibility, and semantic friction. The more datasets we combine, the more important those questions become.

At billion-record scale, semantic ambiguity does not disappear. It scales with the data.

That realization has influenced how I think about community data systems and public-sector analytics. The challenge is not simply to connect more datasets. It is to create enough shared understanding that the connections we make are meaningful.

## From Data Infrastructure to Learning Infrastructure

The most important thing I took away from the project may be the distinction between **data infrastructure** and **learning infrastructure**.

A data system is often designed around questions such as:

- How do we collect the data?
- Where do we store it?
- How do we query it?
- How do we integrate it?
- How do we visualize it?

Those questions matter, but a learning system asks additional questions:

- What do we think the data tells us?
- What assumptions produced that conclusion?
- How representative are the observations?
- What does the distribution look like?
- What evidence contradicts our model?
- What are we unable to observe?
- What do communities themselves know that our datasets do not capture?
- How should new evidence change what we believe?

That is a fundamentally different orientation.

The billion-record infrastructure taught me about **scale**. The FCC Fabric and BDC integration taught me about **data engineering and interoperability**. Crowdsourced speed-test data taught me about **selection and measurement bias**. Dr. Stoev's instruction on the Hájek estimator taught me about **inference**. His instruction on the Gini coefficient taught me about **distribution and inequality**.

Together, those lessons taught me that scale, inference, distribution, provenance, and meaning are different dimensions of the same research problem.

## Technology Is an Enabler

The experience reinforced a principle that runs through much of my work today: **technology is not the solution; technology is an enabler**.

DuckDB did not solve broadband inequality. Python did not solve measurement bias. Parquet did not make FCC data inherently meaningful. The Hájek estimator does not eliminate every limitation of observational data, and the Gini coefficient does not explain why disparities exist.

Each provides a capability.

The real value emerges when those capabilities are combined with research methods, domain knowledge, collaboration, critical questioning, and a willingness to revise our understanding when the evidence changes.

That is the kind of infrastructure I increasingly want to help build: not systems that simply accumulate data, but systems that help people **learn together**.

## Why This Experience Matters to My Work Today

Looking back, the NSF IMR project sits at the intersection of many things I now care deeply about:

- Broadband intelligence and digital opportunity.
- Open and interoperable data infrastructure.
- Reproducible research and provenance.
- Statistical inference and measurement bias.
- Distributional inequality.
- Semantic interoperability and shared vocabulary.
- Community data and public-interest technology.
- Policy learning and evidence-informed decision-making.

My first billion-record infrastructure taught me how to think about **scale without assuming scale itself creates knowledge**. The FCC Fabric and BDC pipeline taught me how engineering decisions become part of the research process. The Hájek estimator taught me to question whether observations are representative. The Gini coefficient taught me to look beyond averages and examine how opportunity is distributed.

Most importantly, the project taught me to ask a better question. Instead of asking only, *How much data do we have?*, I increasingly ask:

> **What can we responsibly learn from the evidence we have, what might we still be missing, and how should that uncertainty shape what we do next?**

That question now influences how I approach broadband, digital opportunity, community intelligence, and public-interest data systems.

## A Documented Contribution

I am grateful that my technical contribution was formally recognized in the resulting research. On page 43 of *Towards unbiased inference of Internet broadband availability based on observational speed test data*, the authors acknowledge my technical support for part of the software pipeline used to integrate the FCC Fabric and BDC datasets (Stuyvesant et al., 2025).

That acknowledgment provides external provenance for the work, but what I value most is what happened around that contribution: the opportunity to work alongside researchers, operate at a scale I had not previously experienced, encounter unfamiliar statistical ideas, and develop a more mature understanding of what research data infrastructure is actually for.

For me, the accomplishment was not simply **building infrastructure capable of working with approximately one billion records**. It was learning that the billion records were only the beginning of the question.

The harder—and much more interesting—work is figuring out **what we can responsibly learn from them**.

## Acknowledgment

I am especially grateful to **Dr. Stilian Stoev of the University of Michigan** for the opportunity to contribute to this research and for taking the time to teach me the statistical ideas behind the work, particularly the **Hájek estimator and Gini coefficient**. His mentorship helped me connect data engineering with statistical inference and distributional analysis, and that connection continues to influence how I think about broadband intelligence and public-interest data infrastructure.

## Project Contribution at a Glance

**NSF Internet Measurement Research (IMR) Project**  
**Research Data Infrastructure Contributor** | University of Michigan & Merit Network | 2025

Selected contributions and learning outcomes include:

- Built and worked with my first research data infrastructure operating at approximately **one billion records**.
- Developed reusable **Python and DuckDB pipelines** for large FCC broadband datasets.
- Contributed to the software pipeline integrating the **FCC Broadband Serviceable Location Fabric and Broadband Data Collection datasets**.
- Used **DuckDB and Parquet** to support scalable, disk-based analytics.
- Developed reusable **SQL, Python, and R workflows** for research and data exploration.
- Supported reproducibility through structured data organization, documentation, and repository stewardship.
- Supported analytical workflows associated with broadband proportion, broadband indices, and **Gini-coefficient mapping**.
- Learned from **Dr. Stilian Stoev** how the **Hájek estimator** can help address representativeness in observational data and how the **Gini coefficient** can illuminate distributional inequality.
- Deepened my understanding of measurement bias, statistical inference, provenance, semantic interoperability, and the distinction between data infrastructure and learning infrastructure.
- Contributed technical infrastructure to NSF-supported research examining methods for improving inference from observational broadband speed-test data.

## Citation-Ready Contribution Statement

> **Acknowledged technical contributor to NSF-supported Internet Measurement Research conducted by the University of Michigan and Merit Network, providing research data infrastructure and technical support for the software pipeline integrating FCC Broadband Serviceable Location Fabric and Broadband Data Collection datasets used in broadband-availability research (Stuyvesant et al., 2025, p. 43).**

## Reference

Stuyvesant, A., Stoev, S., & Michailidis, G. (2025). *Towards unbiased inference of Internet broadband availability based on observational speed test data*. SSRN Working Paper No. 5372801. NSF Public Access Repository. https://par.nsf.gov/servlets/purl/10668222

**NSF Public Access Repository ID:** 10668222  
**Associated NSF Award:** 2319593  
**Acknowledgment of Jason Kronemeyer:** p. 43.