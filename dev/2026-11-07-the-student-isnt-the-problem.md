---
layout: post
title: "The Student Isn't the Problem"
subtitle: "What Chronic Absenteeism Teaches Us About Connected Data Intelligence"
date: 2026-11-07
author: Jason F. Kronemeyer
categories:
  - connected data intelligence
  - education
  - data science
  - digital opportunity
  - community development
tags:
  - chronic absenteeism
  - connected data intelligence
  - geographic information systems
  - ZIP Codes
  - ZCTAs
  - early warning systems
  - educational data
  - rural communities
  - Eastern Upper Peninsula
  - institutional knowledge
description: "Chronic absenteeism shows why institutions must stop confusing where data is recorded with where outcomes are produced. Better intelligence requires connecting student signals to the overlapping systems, geographies, and  community conditions surrounding them."
status: draft
---

A student misses school.

The attendance system records an absence.

Another day is missed. Then another. Eventually the student crosses a threshold and becomes part of a statistic: chronically absent. Chronic absence is commonly defined as missing at least 10 percent of the school year, regardless of whether the absences are excused or unexcused.[^1]

The data is accurate. The student did, in fact, miss school.

But what exactly have we learned?

We know where the signal appeared. We do not necessarily know what produced it.

A student may miss school because of physical or mental health, housing instability, unreliable transportation, family responsibilities, bullying, school climate, academic difficulty, or some combination of conditions that no attendance record can capture by itself. Research increasingly treats chronic absence as a multidimensional indicator shaped by individual, family, school, community, health, and structural conditions, many of which schools cannot address alone.[^1][^2][^3]

Yet when the absence is recorded, the measurement attaches to the student.

That creates a subtle analytical trap. **We begin to treat the location of the measurement as the location of the problem.**

The student generates the signal. The system may generate the condition.

That distinction matters because our institutions are becoming increasingly data-driven. We are getting very good at measuring people and identifying patterns in their behavior. But measuring a person more precisely does not necessarily help us understand the conditions acting upon that person.

Chronic absenteeism therefore offers a lesson that extends well beyond education. It reveals something fundamental about how we construct data systems, choose geographic boundaries, interpret risk, and understand opportunity.

## From Records to Relationships

Most institutional information systems were designed to manage records.

A student information system records enrollment, grades, and attendance. A transportation system manages buses and routes. A municipality records parcels and addresses. A social-service organization tracks programs. A broadband provider maintains service and infrastructure data. A library defines a population or service area. A utility operates within a service territory.

Each system may be functioning exactly as intended.

The problem often exists between the systems.

Consider the difference between two questions.

How many days has this student missed?

What conditions are associated with this pattern, what systems intersect with those conditions, what resources might change them, and what happened after an intervention?

The first question requires a record.

The second requires relationships.

That difference is at the heart of what I call **Connected Data Intelligence**. The objective is not simply to collect more data or build another dashboard. It is to connect information carefully enough that we can move from records to relationships, from relationships to signals, from signals to action, and from actions and outcomes to institutional learning.

Existing early-warning practices demonstrate part of this progression. Michigan's Early Warning Intervention and Monitoring System, or MiEWIMS, organizes attendance, behavior, and course-performance data to help educators identify possible systemic improvements and students who may need support. Its process calls for teams to examine underlying causes, match needs with interventions, monitor progress, and evaluate whether those interventions are working.[^4][^5]

Chronic absenteeism provides a particularly human example of why that progression matters. But the problem is not unique to student records.

We make a remarkably similar mistake when we decide where people live analytically.

Just as we can mistake the student holding an attendance record for the source of the attendance problem, we can mistake the geographic identifier attached to a record for the community or system responsible for producing the conditions we are trying to understand.

That brings us to geography.

## The Geography Problem

ZIP Codes are extraordinarily useful. They appear in addresses, are easy to collect, and provide a convenient identifier for joining and grouping records.

But convenience should not be confused with analytical meaning.

ZIP Codes were created by the United States Postal Service to coordinate mail handling and delivery. They are associated with delivery routes and address points, not with a stable set of policy or statistical boundaries. Because point-based ZIP Code data are unsuitable for many mapping and analytical purposes, the U.S. Census Bureau constructs ZIP Code Tabulation Areas, or ZCTAs, as generalized geographic representations based on Census blocks. A ZCTA is therefore not the same thing as a USPS ZIP Code, even though the familiar five-digit codes often correspond.[^6]

That distinction is more than technical trivia. It exposes a larger problem in data analysis: **we routinely substitute available geography for meaningful geography.**

Consider what happens when a ZIP Code or ZCTA becomes a proxy for socioeconomic or educational context. Educational policy is implemented through states, intermediate and local education agencies, districts, and individual institutions. Economic conditions are also shaped through municipalities, counties, taxing authorities, development organizations, labor markets, and infrastructure systems. Transportation, broadband, electric utilities, health care, and libraries introduce still more boundaries and service territories.

Those systems generally do not organize themselves around postal delivery routes.

Yet ZIP Code frequently becomes the unit of analysis because it is the geographic identifier available in the dataset.

That matters because different geographic aggregations can produce different statistical patterns. This is known as the **modifiable areal unit problem**, or MAUP. The scale, shape, and placement of geographic units can affect mapped patterns, correlations, and other analytical results. Researchers also risk the ecological fallacy when they assume that an individual has the characteristics of the aggregate area in which that person resides.[^7][^8][^9]

Two students can share a ZIP Code while attending different school districts or living in different municipalities and experiencing different transportation options, public services, taxation, broadband availability, or community resources. Conversely, two households on opposite sides of a ZIP or ZCTA boundary may participate in the same school system, use the same library, travel the same roads, depend on the same regional institutions, and participate in essentially the same local economy.

The postal or statistical boundary can divide people who functionally share a community while grouping together people who interact with substantially different systems.

That does not mean ZIP Codes or ZCTAs should never be used in research. ZCTAs can be useful for mapping and analyzing conditions at a ZIP-like scale. The problem is treating them as though they necessarily represent the institutions, service areas, policy jurisdictions, or social relationships producing the outcome being studied.

The better principle is simple:

**Geography should follow the question.**

Before selecting a geographic unit, we should ask who makes the relevant decision, where the policy applies, and through what geography the service is actually delivered. A study of education policy should have some relationship to educational governance. A study of broadband opportunity should recognize serviceable locations, provider footprints, and network availability. A study of transportation barriers should consider routes, distance, and travel time. A study of workforce opportunity may need to follow commuting patterns and labor markets rather than postal or municipal borders.

Researchers should also test whether their conclusions survive across more than one reasonable geography. Because spatial results can change with aggregation scale and boundary configuration, sensitivity analysis across school districts, Census tracts, counties, travel-time areas, or other relevant units can help reveal whether an apparent pattern is robust or partly a product of the chosen map.[^7][^8][^9]

**The appropriate geography is a property of the question, not merely a field in the dataset.**

## People Do Not Live Inside One Boundary

That does not mean we simply need to replace ZIP Codes with a better universal geography.

There is no single boundary capable of representing every system that shapes a person's opportunities.

A student lives at an address inside a municipality or township, within a county and a school district. The household may be served by an electric utility and one or more broadband providers. The student may cross several jurisdictions on the way to school. The family may use a library outside its municipality, receive health care in another community, and work in another county. Programs available to the family may operate within eligibility or service boundaries that resemble none of these.

This becomes especially important in rural places, where schools, employment, health care, utilities, transportation, and community institutions may serve large or overlapping territories. The geography of daily life can be much larger and more complex than the geography suggested by a mailing address.

In Michigan's Eastern Upper Peninsula, for example, the functional community is often better understood as a **network of places, institutions, service areas, and relationships** than as one neatly bounded place. That is my practitioner interpretation of the region's structure, not a claim that every rural community functions identically. But it illustrates the methodological point: treating one postal or administrative geography as though it represents an entire lived environment can conceal relationships that matter.

These overlapping boundaries are not inconvenient exceptions to our data model.

**They are the data model.**

The world is relational. Our information systems simply have difficulty representing it that way.

## Where Is Risk Being Produced?

Once we acknowledge that outcomes emerge from overlapping systems rather than isolated individuals, the purpose of prediction begins to change too.

The conventional analytical question might be:

**Which students are at risk of becoming chronically absent?**

There are legitimate reasons to ask that question. Data systems using attendance, behavior, and academic indicators can support earlier and more targeted interventions. Evidence reviews find that such systems can help schools identify students needing additional support, although effective responses still depend on understanding causes and matching students with appropriate interventions.[^3][^4][^5]

But concentrating only on the individual leads easily toward another question: Which students are most likely to fail?

We should ask something else too:

**Where is risk being produced?**

Or, put more directly:

**Which systems are showing evidence that they may be failing students?**

Imagine that several students begin accumulating absences. A predictive system might identify those students as increasingly at risk. A connected system could ask what relationships they share.

Perhaps they have little demographic similarity but live along the same transportation corridor. Perhaps students experiencing increasing absences reside beyond reliable transportation options. Perhaps another pattern overlaps with housing instability. Perhaps a community program appears alongside improved outcomes for students receiving a particular form of support.

These are plausible hypotheses, not automatic explanations. Research does establish that health, housing, transportation, school belonging, and other social and structural conditions can influence attendance. Research also indicates that accessible transportation, physical and mental health supports, mentoring, family communication, and partnerships with public agencies and community organizations can improve or support attendance.[^1][^2][^3]

But finding a geographic or statistical relationship does not establish what caused an individual student's absence.

Connected data does not magically turn correlation into causation. Spatial aggregation can itself alter observed associations, and group-level relationships should not be assumed to describe every person within the group.[^7][^8][^9]

What connected data can do is reveal relationships worth investigating, allow competing explanations to be tested, and direct scarce human attention toward places where further inquiry or intervention may be warranted.

**Intelligence isn't knowing the answer before asking the question. It is knowing where to ask the next question.**

That leads to an ethical principle that I believe should accompany increasingly powerful analytical systems:

**Use data to identify conditions requiring support, not people requiring judgment.**

## The Measurement Belongs to the Student. The Cause Might Not.

Traditional information systems are extraordinarily good at answering questions about entities.

Who is this student? What school does the student attend? How many days has the student missed? What grades has the student received?

Connected systems help us understand what happens **among entities**.

What school does this student attend? What district governs that school? What transportation options connect the student's location to it? What community resources serve the surrounding area? What programs are available? What infrastructure reaches the household? What intervention was attempted? Which organizations participated? What changed afterward?

Suddenly, the data is no longer describing only the student.

It is beginning to describe the system around the student.

That framing is consistent with emerging public-health research that treats chronic absence as an early-warning signal of unmet developmental, social, and health needs rather than only an education-sector problem. That research calls for coordinated action across education, health, public health, and other community systems because many determinants of attendance lie outside a school's direct control.[^1][^10]

The distinction applies far beyond education. We encounter the same analytical problem when studying broadband adoption, workforce participation, economic development, housing, transportation, health, and digital opportunity. When the measured outcome belongs to an individual, our instinct is often to collect increasingly detailed information about that individual.

Sometimes we need to look in the other direction.

The missing variables may not be attributes of the person at all.

They may be attributes of the systems surrounding the person.

## From Dashboards to Intelligence

Over the past decade, institutions have become remarkably good at building dashboards.

That is progress. Visibility matters.

But visibility is not intelligence.

A dashboard can tell us:

**Here is what is happening.**

Connected Data Intelligence should help us ask:

**What is this connected to?**

Then:

**What can we do about it?**

And finally:

**Did it work?**

That final question turns intervention into institutional knowledge. Michigan's EWIMS guidance, for example, does not end with identifying a student or assigning an intervention. Its seven-step process includes monitoring interventions and student progress, followed by evaluating and refining the overall process.[^4][^5]

Communities repeatedly encounter problems, respond to them, observe the results, and then lose some of what they learned because the intervention itself was never represented as reusable knowledge. We preserve the original statistics, perhaps even final outcomes, while losing the reasoning and relationships in between.

What condition did we observe? What evidence led us to act? Who became involved? What resources were available? What intervention was attempted? What happened afterward? What did we learn?

If we can preserve those relationships, an institution does more than accumulate data.

It learns.

And when those connections can appropriately be understood across institutions, a community can learn too.

## No Institution Sees the Whole Community

A school district sees one part of the picture. A municipality sees another. A broadband provider sees another. A library sees another. A workforce organization, health provider, community nonprofit, transportation agency, or utility may each possess another piece.

No single institution needs to possess all of the data to recognize that the relationships matter.

That is an important distinction.

Connected Data Intelligence does not require building one enormous database containing everything known about everyone. Such a system could produce serious privacy, security, governance, and proportionality concerns, particularly when it includes student, health, housing, or other sensitive information.

What institutions need instead is the ability to describe what their information means, what it relates to, what uncertainty it contains, and under what legal, ethical, and governance conditions those relationships may appropriately be used.

A school, road, broadband location, library, public program, municipality, and household do not need to live inside the same database to be understood as parts of the same community.

That is partly a technical challenge involving semantics, interoperability, privacy, and governance. Before it becomes a technical problem, however, it is a conceptual one.

**We have to agree that the relationships matter.**

The same insight should change the way we think about public data.

We have traditionally justified public data using the language of transparency. Communities should be able to see what institutions are doing and understand how public resources are being used.

That remains important.

Connected Data Intelligence suggests a more ambitious purpose. Communities should also be able to understand how their institutions, infrastructure, resources, and conditions relate to one another.

**Transparency lets a community see. Connected data can help a community act.**

That transforms data from merely a reporting mechanism into a form of community infrastructure.

## The Student Isn't the Problem

Return to the student who missed school.

The attendance record was never wrong.

The mistake was assuming that because the measurement belonged to the student, the explanation did too.

The same is true of geography. A ZIP Code can accurately describe part of an address without accurately describing the systems shaping the person who lives there. A school district, transportation network, broadband footprint, labor market, utility territory, or community organization may each reveal a different part of the story.

None is universally correct because **people do not live inside datasets. They live inside overlapping systems of relationships.**

That is the promise I see in Connected Data Intelligence. Not collecting more data so institutions can make increasingly precise judgments about people, but connecting data responsibly so communities can better understand the conditions surrounding them.

**The student isn't the problem to be modeled. The system around the student is the thing we need to learn how to see.**

## Provenance Statement

"The Student Isn't the Problem" is my practitioner framing. It is informed by my work in education technology, broadband, digital opportunity, community development, data science, institutional knowledge, and Connected Data Intelligence.

The following formulations are my synthesis and should not be attributed to the external institutions or researchers cited in this article:

- The student generates the signal. The system may generate the condition.
- We begin to treat the location of the measurement as the location of the problem.
- Geography should follow the question.
- The appropriate geography is a property of the question, not merely a field in the dataset.
- Overlapping boundaries are the data model.
- Where is risk being produced?
- Use data to identify conditions requiring support, not people requiring judgment.
- Intelligence isn't knowing the answer before asking the question. It is knowing where to ask the next question.
- Transparency lets a community see. Connected data can help a community act.
- The connection among chronic absenteeism, geographic fit, community systems, institutional learning, and Connected Data Intelligence.

The external sources establish the factual foundation: definitions and causes of chronic absenteeism, evidence-based attendance interventions, Michigan's EWIMS process, the distinction between USPS ZIP Codes and Census ZCTAs, and the methodological risks associated with spatial aggregation and ecological inference. They do not establish the larger thesis of this article.

## References

[^1]: Falconer, Catherine, et al. "Chronic Absence as a Public Health Priority: A Framework for Coordinated Action." *The Milbank Quarterly*, vol. 104, special issue, 2026. [https://www.milbank.org/quarterly/articles/chronic-absence-as-a-public-health-priority-a-framework-for-coordinated-action/](https://www.milbank.org/quarterly/articles/chronic-absence-as-a-public-health-priority-a-framework-for-coordinated-action/).

[^2]: Robert Wood Johnson Foundation. "The Relationship Between School Attendance and Health." September 2016. [https://files.eric.ed.gov/fulltext/ED592870.pdf](https://files.eric.ed.gov/fulltext/ED592870.pdf).

[^3]: Gottfried, Michael, Lindsay Page, and Danielle Edwards. "Reducing Student Absenteeism." *EdResearch for Action*, May 2023. [https://files.eric.ed.gov/fulltext/ED647452.pdf](https://files.eric.ed.gov/fulltext/ED647452.pdf).

[^4]: Michigan Department of Education. "Early Warning Intervention and Monitoring System (EWIMS)." [https://www.michigan.gov/mde/services/school-performance-supports/early-warning](https://www.michigan.gov/mde/services/school-performance-supports/early-warning).

[^5]: Michigan Department of Education. *EWIMS Implementation Guide*. Adapted 2023. [https://www.michigan.gov/-/media/Project/Websites/mde/EWIMS/Michigan_EWIMS_Implementation_Guide.pdf](https://www.michigan.gov/-/media/Project/Websites/mde/EWIMS/Michigan_EWIMS_Implementation_Guide.pdf).

[^6]: U.S. Census Bureau. "ZIP Code Tabulation Areas (ZCTAs)." [https://www.census.gov/programs-surveys/geography/guidance/geo-areas/zctas.html](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/zctas.html).

[^7]: Bradley, Jonathan R., Christopher K. Wikle, and Scott H. Holan. "Regionalization of Multiscale Spatial Processes by Using a Criterion for Spatial Aggregation Error." *Journal of the Royal Statistical Society: Series B*, vol. 79, no. 3, 2017, pp. 815-832. [https://academic.oup.com/jrsssb/article/79/3/815/7040667](https://academic.oup.com/jrsssb/article/79/3/815/7040667).

[^8]: Tuson, M., et al. "Incorporating Geography into a New Generalized Theoretical and Statistical Framework Addressing the Modifiable Areal Unit Problem." *International Journal of Health Geographics*, vol. 18, article 6, 2019. [https://pmc.ncbi.nlm.nih.gov/articles/PMC6437958/](https://pmc.ncbi.nlm.nih.gov/articles/PMC6437958/).

[^9]: Mennis, Jeremy. "Problems of Scale and Zoning." *The Geographic Information Science & Technology Body of Knowledge*, 2019. [https://gistbok-ltb.ucgis.org/current/concept/FC-07-026](https://gistbok-ltb.ucgis.org/current/concept/FC-07-026).

[^10]: Attendance Works. "A New Public Health Challenge: Chronic Absence." June 17, 2025. [https://www.attendanceworks.org/a-new-public-health-challenge-chronic-absence/](https://www.attendanceworks.org/a-new-public-health-challenge-chronic-absence/).

---

🔬 **Learning in Public** — This site is my digital laboratory, a space for curiosity, experimentation, and evolving ideas. The content here reflects my ongoing experimentation and learning process and may be revised as my understanding deepens over time.
