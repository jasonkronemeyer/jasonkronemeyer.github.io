---
layout: research-note
title: "Culture, Context, and Community Knowledge: A Missing Dimension in Digital Opportunity"
author: Jason F. Kronemeyer
date: 2026-10-23
status: research
categories:
  - Digital Opportunity
  - Knowledge Science
  - Community Intelligence
  - DOIN
tags:
  - culture
  - context
  - community-engagement
  - knowledge-management
  - knowledge-modeling
  - knowledge-graphs
  - provenance
  - trust
  - place
  - digital-opportunity
  - DOIN
---

# Culture, Context, and Community Knowledge

## Research Question

As I continue developing the Digital Opportunities Intelligence Network (DOIN), I am beginning to think there is a dimension of community knowledge that our conventional data and information systems frequently fail to represent: **culture**.

We collect enormous amounts of data about communities. We measure population, income, educational attainment, broadband availability, broadband adoption, employment, infrastructure, health, housing, and other socioeconomic conditions. We increasingly connect these datasets to understand the conditions of a place.

But there is a question underneath those measurements that may be just as important:

**Do we understand the culture of the place?**

That question may have significant implications for digital opportunity, community engagement, knowledge management, and the way we design information systems intended to support communities.

## Culture and Context Are Related, but They Are Not the Same

Culture and context are deeply related, but I do not think they should be treated as interchangeable concepts.

**Culture** is the shared system of meaning through which people interpret the world. It can include values, language, identity, traditions, relationships, ways of knowing, community narratives, expectations, trust, and collective memory.

**Context** describes the circumstances in which a community and its culture exist. Context can include geography, history, economics, infrastructure, institutions, demographics, governance, policy, technology, and current events.

A useful distinction may be:

> **Culture influences what something means. Context influences what something means here and now.**

Neither exists independently of the other.

Two rural communities could have nearly identical demographic profiles, broadband availability, income levels, and infrastructure. From the perspective of a conventional dataset, the communities might appear remarkably similar.

Yet the same broadband adoption program, workforce initiative, telehealth program, or community engagement strategy could produce very different outcomes in the two places.

The difference may not be visible in the conventional data.

Part of the difference may be cultural.

Conversely, two communities may share cultural characteristics while operating under dramatically different economic, geographic, institutional, technological, or political conditions.

Understanding a community therefore requires understanding both **culture and context**.

## Culture and Context Should Not Become Simple Scores

One danger would be turning these concepts into yet another set of simplified community metrics.

I do not think DOIN should attempt to create a "culture score."

Culture is too relational, dynamic, multidimensional, and locally situated to be represented responsibly by a single number.

Instead, culture and context could be modeled as dimensions of community knowledge.

One conceptual representation might be:

    PLACE
    │
    ├── Context
    │   ├── Geography
    │   ├── Infrastructure
    │   ├── Economy
    │   ├── Institutions
    │   ├── Demographics
    │   ├── Policy
    │   └── History
    │
    ├── Culture
    │   ├── Identity
    │   ├── Language
    │   ├── Values
    │   ├── Traditions
    │   ├── Relationships
    │   ├── Ways of knowing
    │   ├── Community narratives
    │   └── Collective memory
    │
    └── Community Knowledge
        ├── Needs
        ├── Assets
        ├── Experiences
        ├── Evidence
        ├── Priorities
        └── Aspirations

This begins to describe a community in a way that conventional indicators alone cannot.

## Trust May Be the Connecting Layer

There may also be another important component sitting between culture, context, and community engagement: **trust**.

Trust is not simply a cultural characteristic. Nor is it merely contextual.

Trust emerges through relationships among people, organizations, institutions, history, experience, power, and culture.

A preliminary DOIN model might therefore be expressed as:

> **Place + Culture + Context + Relationships + Trust → Community Knowledge**

Community knowledge then helps shape whether programs, policies, technologies, or other interventions ultimately result in meaningful community participation.

This suggests that trust itself should probably be modeled relationally rather than as another simple score.

A community may trust one institution while distrusting another. Residents may trust a particular community leader, school, library, tribal institution, cooperative, nonprofit organization, local government, or healthcare provider while being skeptical of an outside organization delivering an otherwise valuable program.

That distinction matters.

## Culture as a Community Engagement Variable

This raises an important question for digital opportunity work:

**Could a lack of cultural understanding itself be a barrier to community engagement?**

I think the answer may be yes, but the causal relationship should be framed carefully.

The problem is not cultural difference.

A more useful formulation is:

> **Lack of cultural and contextual understanding → poorly designed engagement → reduced relevance or trust → lower participation → weaker evidence → poorer decisions**

This places responsibility on the system attempting to engage the community rather than treating the community itself as the problem.

Consider a familiar situation.

An organization conducts six community meetings and attendance is poor. The conclusion might be:

> The community is difficult to engage.

But that conclusion ignores a much larger collection of questions.

Where were the meetings held? At what times? Who organized them? Who invited residents? What communication channels were used? Was the language understandable and appropriate? Was transportation required? Was childcare available? Did people trust the organization conducting the meetings? Had earlier community processes resulted in meaningful action? Were trusted local organizations involved? Were residents being asked questions they had already answered before? Did participants have any actual influence over decisions?

Each of those conditions changes how the attendance data should be interpreted.

The number of people attending the meetings is **data**.

Understanding why people did or did not attend requires **contextual knowledge**.

Understanding what participation means within the community requires **cultural knowledge**.

Understanding whether residents believed their participation would matter begins to involve **trust, relationships, and institutional history**.

That distinction may be extremely important for DOIN.

## A Weakness in Conventional Information Systems

Most information systems are relatively good at representing measurable community characteristics.

For example:

    Community
      Population
      Income
      Broadband Availability
      Broadband Adoption
      Employment
      Education
      Devices
      Providers
      Programs
      Funding

These are important. They should remain part of the model.

But these systems are generally much poorer at representing relationships such as:

    Community
        ├── hasHistoryWith → Institution
        ├── trusts → Organization
        ├── identifiesWith → Place
        ├── maintains → CulturalPractice
        ├── prefers → CommunicationMethod
        ├── reliesOn → CommunityLeader
        ├── possesses → LocalKnowledge
        └── expresses → CommunityPriority

This is where knowledge graphs, semantic modeling, and provenance become particularly interesting for DOIN.

Instead of asking only:

> **What data do we have about this community?**

DOIN could ask:

> **What do we know about this community, how do we know it, who produced that knowledge, under what circumstances was it produced, and what does it mean within the community itself?**

That is a substantially different knowledge-management problem.

## Culture, Context, and Provenance

This also connects directly to provenance.

Imagine that a knowledge system contains the following assertion:

> "Community X has low interest in workforce training."

Without provenance, that statement can easily become accepted as fact.

A provenance-aware knowledge model would immediately encourage additional questions:

    Claim:
      "Community X has low interest in workforce training."

    Derived From:
      2025 Employer Survey

    Survey Population:
      Local employers

    Populations Not Represented:
      Students
      Unemployed residents
      Tribal members
      Adult learners

    Collection Method:
      Online survey

    Response Rate:
      14 percent

The meaning of the original statement changes considerably once its provenance and context become visible.

The system has not merely stored a finding. It has retained enough information about the **conditions under which the knowledge was created** to allow someone else to interpret it critically.

Culture introduces an additional question:

> **Does the evidence mean the same thing to the people being described as it does to the institution interpreting the data?**

That may be one of the most important questions for community knowledge systems.

## Data About a Community Is Not Necessarily Community Knowledge

This suggests an important distinction.

**Data about a community is not automatically community knowledge.**

Government agencies, telecommunications companies, researchers, universities, consultants, healthcare systems, nonprofits, and other organizations can possess enormous amounts of information about a place without necessarily understanding the place.

Community knowledge requires more than aggregation.

It requires context.

It requires relationships.

It requires provenance.

It requires understanding how people within a place interpret their own experiences.

And it requires culture.

A useful formulation may therefore be:

> **Data describes a place. Context helps explain the place. Culture helps us understand what the place means to the people who live there.**

This significantly expands the purpose of DOIN.

## From Data Infrastructure to Community Knowledge Infrastructure

Under this interpretation, DOIN is not simply a system for connecting digital-opportunity datasets.

It becomes infrastructure for connecting different forms of knowledge.

A preliminary knowledge progression might look like:

> **Data → Evidence → Context → Culture → Relationships → Knowledge → Action**

These stages should not necessarily be understood as a strictly linear hierarchy. They are interconnected and recursive. New action creates new experiences. Experiences create new evidence. New evidence changes context. Relationships affect how evidence is interpreted. Culture influences meaning throughout the process.

The important point is that data alone is insufficient.

This also changes what it means to preserve the community's voice in a knowledge system.

Community voice cannot simply become another field in a database. If local knowledge is stripped of the cultural, historical, relational, and contextual conditions in which it was produced, the words may remain while much of their meaning disappears.

A mature DOIN model should therefore preserve not only the knowledge itself but also enough provenance and context to understand **whose knowledge it is, how it was created, why it matters, and how it relates to a particular place**.

## A Potential DOIN Principle

This leads to what may become an important foundational principle for the Digital Opportunities Intelligence Network:

> **Community knowledge cannot be separated from the cultural and contextual conditions under which that knowledge is created, interpreted, and used.**

A stronger formulation may be:

> **You cannot meaningfully model digital opportunity without modeling place, and you cannot meaningfully model place without accounting for culture and context.**

This creates an important challenge for knowledge modeling.

If culture and context matter to how community knowledge is interpreted, then a community knowledge graph cannot simply model people, organizations, infrastructure, programs, indicators, and outcomes.

It must also find responsible ways to preserve the **relationships, provenance, history, meaning, and ways of knowing** that make those entities understandable.

## Implications for Community Engagement

This also changes how community engagement might be understood.

Engagement should not simply be measured by attendance, survey responses, comments collected, or number of outreach events.

Those are measures of activity.

They do not necessarily measure meaningful engagement.

A community-engagement model might need to consider at least:

1. **Access**  
   Could people participate?

2. **Representation**  
   Who participated and who was missing?

3. **Context**  
   Under what circumstances did participation occur?

4. **Culture**  
   Was the engagement compatible with local ways of communicating, gathering, deciding, and sharing knowledge?

5. **Relationships**  
   Who facilitated the engagement, and what relationships already existed?

6. **Trust**  
   Did participants believe the people and institutions involved would listen and act responsibly?

7. **Influence**  
   Could participation actually affect the outcome?

8. **Provenance**  
   Can subsequent users of the information understand where the community knowledge came from and how it was produced?

From this perspective, "lack of engagement" may sometimes be a misdiagnosis.

The community may not have failed to engage.

**The engagement system may have failed to understand the community.**

That is an important distinction for digital opportunity work.

## Questions for Further Investigation

This research note raises several questions that need additional investigation:

- How should culture be represented in a knowledge graph without reducing culture to a collection of attributes?
- How can community members define cultural context rather than having outside institutions define it for them?
- Which cultural knowledge should **not** be captured, digitized, or made broadly accessible?
- How should Indigenous data sovereignty and culturally sensitive knowledge be handled?
- How do we distinguish community knowledge from institutional knowledge about a community?
- How should trust be modeled when it exists between specific people, organizations, and institutions rather than uniformly across a community?
- Can provenance models capture not only who produced information but the social and cultural conditions under which it was produced?
- How should conflicting interpretations of the same community evidence coexist within a knowledge graph?
- Can community engagement be modeled as a relationship rather than simply measured as an activity?
- How can DOIN preserve community voice without extracting community knowledge from the context that gives it meaning?

## Working Conclusion

The more I think about digital opportunity as a knowledge problem, the more important culture becomes.

We have become increasingly sophisticated at collecting data about communities. We can map broadband infrastructure, calculate adoption rates, analyze census characteristics, identify funding programs, measure economic conditions, and connect increasingly large datasets.

What we are much less effective at doing is preserving the meaning surrounding those observations.

That meaning lives partly in context and partly in culture. It also lives in relationships, history, experience, and trust.

If those dimensions are absent from our knowledge systems, we can possess enormous amounts of data about a community while still misunderstanding the community itself.

For DOIN, that may represent both a warning and an opportunity.

The goal should not simply be to build a better database about digital opportunity. It should be to build a knowledge infrastructure capable of preserving the relationship between **evidence, place, culture, context, provenance, and community voice**.

That may be necessary if community intelligence is ultimately going to become community action.

# Five Whys

Using the “Five Whys” method on your Culture, Context, and Community Knowledge: A Missing Dimension in Digital Opportunity note, I’d start with its central claim: data about a community is not necessarily community knowledge. 1
Five Whys
1. Why isn’t data about a community sufficient to understand that community?  Because conventional indicators can describe population, income, broadband, education, infrastructure, and other conditions while failing to capture what those conditions mean to the people who live there. 1
2. Why does meaning matter for digital opportunity?  Because apparently similar communities can respond very differently to the same broadband, workforce, telehealth, or engagement intervention. Your note suggests the difference may lie partly in culture, context, relationships, history, and trust, dimensions not readily visible in conventional datasets. 1
3. Why don't our existing information systems capture those dimensions well?  Because they are generally designed to represent measurable attributes rather than relational knowledge. Your examples make the distinction particularly clear: systems readily store population or broadband adoption, but struggle with relationships such as trusts → Organization, hasHistoryWith → Institution, reliesOn → CommunityLeader, or expresses → CommunityPriority. 1
4. Why should DOIN attempt to represent those relationships instead of simply adding more datasets?  Because adding datasets can increase the amount of information without increasing understanding. Your provenance example demonstrates this well: “Community X has low interest in workforce training” means something very different once we know who was surveyed, who was excluded, how the survey was conducted, and that the response rate was 14 percent. 1
5. Why does that distinction ultimately matter?  Because decisions based on information stripped of culture, context, provenance, relationships, and community voice can misunderstand the very communities they are intended to help. That leads directly to the deeper purpose emerging from the note:

DOIN should not merely become infrastructure for data about communities. It should become infrastructure through which communities can preserve, contextualize, relate, and responsibly use knowledge about themselves. 1

What the fifth “why” reveals
I think your Five Whys exercise exposes something deeper than the note's explicit research question.
You're beginning with “How do we account for culture?”, but following the problem downward eventually produces a more fundamental question:
Who gets to determine what counts as knowledge about a place?
That reframes DOIN from primarily a data-modeling problem into a knowledge-governance problem.
And that makes one of the questions you already included in the note especially consequential: How can community members define cultural context rather than having outside institutions define it for them? 1
So I might push the emerging DOIN principle one step further:
Data infrastructure connects evidence.  Knowledge infrastructure preserves meaning.  Community knowledge infrastructure preserves meaning while also preserving the community's agency over that meaning.
That third statement may be where this note is ultimately heading.


Below is the complete revised Markdown section. It preserves your comparison prompt and table, adds source citations, and develops participation metrics as a bridge between the Digital Opportunities Compass, culture, and community knowledge infrastructure. 12
## Connecting This Question to Michigan's Digital Opportunity Frameworks

### Prompt

> **What do Michigan's Digital Equity Plan and the Digital Opportunities Compass say about this?**

This question matters because the issues raised by the Five Whys do not exist apart from Michigan's existing digital opportunity work. They extend it.

Michigan's Digital Equity Plan and the Digital Opportunities Compass both recognize that digital opportunity must be understood in community context and cannot be reduced to broadband availability alone. Michigan's plan expressly rejects a one-size-fits-all approach, states that communities know communities best, and calls for grassroots strategies in which communities lead conversations about needs and solutions.[^1] The Digital Opportunities Compass similarly moves beyond availability, affordability, and adoption by examining the larger ecosystem through which connectivity becomes meaningful opportunity.[^2]

The comparison also reveals an important gap. Both frameworks create space for local conditions, participation, community engagement, institutional capacity, and broader outcomes, but neither fully answers the knowledge-infrastructure question raised here:

> **How do we represent culture, relationships, trust, provenance, participation, and locally constructed meaning as part of what we know about a community?**

### Comparison

| This Note | Michigan's Digital Equity Plan | Digital Opportunities Compass |
|---|---|---|
| **Place and context matter** | Rejects a one-size-fits-all approach and recognizes that barriers and solutions differ among places and households.[^1] | Includes **Contexts** as one of its six components and encourages locally adapted assessment rather than a single rigid set of measures.[^2] |
| **Community knowledge matters** | Uses stakeholder engagement, community meetings, data collection, public comment, and Tribal consultation alongside quantitative evidence.[^1] | Encourages communities and institutions to assess their own conditions, identify opportunities, and select indicators relevant to local priorities.[^2] |
| **Engagement must be meaningful** | The MI Connected Future model uses community meetings, partnership roundtables, data collection, and public comment to inform planning and implementation.[^1] | Treats digital equity as an ecosystem involving governance, institutions, applications, and community outcomes rather than as a purely technical condition.[^2] |
| **Relationships and trusted intermediaries matter** | Relies on community organizations, public agencies, Tribal leaders, internet service providers, Digital Navigators, and other local partners to implement community-specific solutions.[^1][^3] | Includes **Governance** and the health of the digital-equity ecosystem among the factors that shape whether programs produce durable results.[^2] |
| **Data alone are insufficient** | Combines infrastructure, adoption, affordability, device, skills, participation, and engagement evidence in its needs assessment and measurable objectives.[^1] | Moves beyond the access triangle by connecting connectivity, skills, applications, and context to broader social and economic outcomes.[^2] |
| **Participation should be measured** | Uses a Digital Participation Score composed of specific online activities, including education, employment, healthcare, government services, communications, commerce, and content creation.[^1] | Provides a structure for relating participation to Contexts, Governance, Connectivity, Skills, Applications, and Outcomes.[^2] |
| **Participation metrics require interpretation** | The Digital Participation Score shows differences in measured digital activity, including differences between covered populations and Michigan residents generally, but it cannot by itself explain why those differences exist.[^1] | The Compass helps locate possible explanations across multiple dimensions, but local qualitative knowledge is still required to understand causal mechanisms and meaning.[^2] |
| **Culture, context, and provenance should be represented** | Partially addressed through community engagement and community-specific planning, but not fully developed as a model for preserving contextual knowledge.[^1] | Context is a formal component, but culture and provenance are not developed as complete representational or governance layers.[^2] |
| **Community knowledge should become durable knowledge infrastructure** | Not a primary function of the plan. | Not a primary function of the Compass. |
| **Communities should retain agency over how their knowledge is represented and interpreted** | Community participation informs planning, but knowledge governance and continuing community authority over collected knowledge are not the central problems being addressed.[^1] | Community-centered interpretation is compatible with the Compass, but community control over knowledge is not its primary focus.[^2] |

## From Digital Equity to Community Knowledge Infrastructure

Michigan's Digital Equity Plan recognizes that digital equity cannot be achieved through a one-size-fits-all approach. Communities experience different combinations of infrastructure gaps, affordability barriers, device needs, digital skills, institutional capacity, and opportunity. The plan therefore incorporates community engagement alongside quantitative indicators of connectivity, affordability, adoption, devices, digital skills, security, accessibility, and participation.[^1]

The plan's vision is explicitly place-conscious. It observes, for example, that the Eastern Upper Peninsula faces infrastructure limitations that differ from the affordability barriers present in Detroit. It concludes that digital equity requires meeting communities where they are, learning about the problems that persist, connecting people to existing resources, and providing community-level support.[^1]

The Digital Opportunities Compass pushes this idea further. Rather than treating broadband availability or adoption as the endpoint, the Compass asks what connectivity enables people and communities to do. It organizes that inquiry around six interacting components:

1. **Contexts**
2. **Governance**
3. **Connectivity**
4. **Skills**
5. **Applications**
6. **Outcomes**[^2]

The Digital Opportunities Compass is intended as an orienting framework rather than a rigid index. Its indicators can be adapted to establish a baseline, identify areas requiring attention, monitor changes over time, and evaluate whether interventions are contributing to broader outcomes.[^2]

Together, these frameworks suggest a progression:

**Broadband infrastructure** asks whether connectivity is available.

**Digital equity** asks whether people can afford, access, and meaningfully use it.

**Digital participation** asks what people are doing with that access.

**Digital opportunity** asks what individuals and communities can accomplish through that participation.

But another question remains:

> **What do we need to know about a community to interpret participation and opportunity correctly?**

Two communities can have similar broadband availability, demographic characteristics, income levels, and device-ownership rates while exhibiting different patterns of digital participation. The explanation may reside in information that conventional datasets rarely represent well: local history, institutional relationships, trusted intermediaries, community priorities, language, identity, previous experiences, cultural practices, social networks, perceived risk, and the provenance of what we believe we know about a place.

This suggests an additional layer beneath digital opportunity: **community knowledge infrastructure**.

## Participation Metrics as a Bridge

Participation metrics provide a useful bridge between basic digital-equity conditions and the broader outcomes described by the Digital Opportunities Compass.

Michigan's Digital Equity Plan includes a **Digital Participation Score** that draws from a set of observable online activities. These include:

- using email, text messaging, social networks, and video or voice calls;
- creating or publishing original online content;
- telecommuting or working away from a usual workplace;
- searching or applying for employment;
- participating in online classes or job training;
- accessing government services;
- requesting or offering services;
- buying and selling goods;
- using online financial services;
- interacting with connected household technologies;
- accessing health or insurance records;
- communicating with healthcare professionals;
- researching health information; and
- using electronic health-monitoring services.[^1]

These measures are valuable because they move beyond asking whether a household has an internet subscription. They provide evidence about whether connectivity is being translated into actual activity in education, employment, healthcare, government, communication, commerce, and everyday life.

Michigan's plan also places its Digital Participation Score alongside an Affordability Score, Digital Government Accessibility Score, Digital Security Score, and Device Distress Score. It relates these indicator areas to economic and workforce development, educational outcomes, health outcomes, civic and social engagement, and the delivery of essential services.[^1]

Participation, in this sense, is the point at which digital-equity conditions begin to become visible as lived activity.

### Participation Metrics and the Compass

The six components of the Digital Opportunities Compass provide a way to interpret participation metrics without treating participation as an isolated behavioral score.

| Compass component | Relationship to participation | Illustrative questions |
|---|---|---|
| **Contexts** | Identifies the demographic, geographic, social, economic, institutional, and cultural conditions surrounding participation. | Who is participating, in what place, under what conditions, and with what prior experiences? |
| **Governance** | Examines the institutions, policies, partnerships, accountability structures, and decision-making processes that enable or constrain participation. | Are community members involved in setting priorities? Are trusted local organizations included? Who controls the resulting data? |
| **Connectivity** | Establishes whether reliable and affordable service and appropriate devices make participation technically possible. | Can residents connect consistently, afford service, and use a device suited to the activity? |
| **Skills** | Examines whether people have the knowledge, confidence, support, and safety awareness needed to participate. | Do residents know how to complete the activity, recognize risks, recover from errors, and obtain trusted assistance? |
| **Applications** | Examines whether useful, accessible, secure, culturally appropriate, and locally relevant services are available. | Does the application meet a locally recognized need? Is it accessible, understandable, safe, and worth using? |
| **Outcomes** | Examines what changes because participation occurred. | Did participation improve education, employment, health, community connection, civic life, access to services, or another locally valued outcome? |

Participation therefore should not be positioned as a single point on a linear path. It sits at the intersection of all six Compass components.

A person may have connectivity but lack the skills to use a telehealth platform. A person may have both connectivity and skills but avoid the platform because of privacy concerns. A platform may be secure and technically accessible but fail to reflect the person's language or expectations about care. A resident may use a service once but derive little benefit from it. Another resident may rely on a trusted librarian, educator, family member, Tribal organization, faith community, or Digital Navigator before deciding to participate at all.

The measurable activity is participation. The conditions that make the activity possible, meaningful, safe, and worthwhile are distributed across the Compass.

## Participation Is More Than Attendance or Use

Participation metrics should operate at several levels.

### 1. Reach

Reach asks whether an opportunity reached the people and communities it was intended to serve.

Possible measures include:

- number of residents contacted;
- number and geographic distribution of engagement events;
- representation of covered populations;
- number of community organizations involved;
- availability of remote, in-person, multilingual, and accessible participation options; and
- comparison between participants and the population the initiative intended to reach.

Reach is necessary, but it does not establish that participation was meaningful.

### 2. Engagement

Engagement asks what people actually did.

Possible measures include:

- attendance and return-participation rates;
- survey, interview, listening-session, or focus-group participation;
- completion of digital-skills training;
- use of Digital Navigator services;
- enrollment in affordability programs;
- device acquisition and activation;
- use of telehealth, online learning, employment, government, or financial tools; and
- contributions to local priority setting or program design.

Engagement provides stronger evidence than reach, but it still may not establish influence.

### 3. Influence

Influence asks whether participation affected a decision, program, investment, representation, or allocation of resources.

Possible measures include:

- community recommendations incorporated into a plan;
- program modifications made in response to participant feedback;
- funding priorities changed because of local evidence;
- community-defined indicators included in evaluation;
- residents or local organizations given continuing decision-making roles;
- identified barriers resolved after community input; and
- explanations provided when recommendations were not adopted.

Influence distinguishes participation from consultation conducted merely to satisfy a procedural requirement.

### 4. Continuity

Continuity asks whether participation can be sustained after a meeting, survey, grant, or pilot ends.

Possible measures include:

- repeat participation over time;
- continued operation of local working groups;
- retention and support of Digital Navigators;
- durability of institutional partnerships;
- transfer of knowledge when staff or leaders change;
- preservation of community-generated evidence and decisions; and
- continued community access to the information produced through the initiative.

Continuity is where participation begins to become infrastructure.

### 5. Outcomes

Outcome measures ask whether participation contributes to improvements that people and communities value.

Possible measures might include:

- successful use of online public services;
- completion of education or workforce credentials;
- improved access to employment;
- use of telehealth and patient portals;
- increased ability to recognize and respond to cyber risks;
- greater connection to family or community networks;
- increased civic participation;
- improved delivery of essential services; and
- stronger local capacity to plan, fund, and sustain digital-inclusion work.

Outcome measures should not assume that the same result is equally important to every community. Part of the participation process should be determining which outcomes matter locally.

## Culture Shapes Participation

Culture should not be treated as a demographic variable added after the measurement framework has been designed. Culture helps shape whether participation occurs, what form it takes, how it is interpreted, and whether an intervention is considered legitimate.

Culture can influence participation through at least six mechanisms.

### Trust

People are more likely to participate when an invitation comes through a person or institution they recognize as trustworthy. The same survey, training program, or public meeting may receive very different responses depending on whether it is offered by an unfamiliar outside organization or through a local library, school, Tribal organization, faith community, cooperative, healthcare provider, extension office, or respected community leader.

### Relevance

Participation depends on whether people see a relationship between an activity and a need they recognize. A digital-skills program framed around abstract technological proficiency may attract different participants than one organized around access to healthcare, managing a farm or small business, communicating with family, protecting against scams, completing schoolwork, or obtaining government services.

### Communication

Language matters, but cultural communication involves more than translation. It includes terminology, examples, storytelling practices, communication channels, assumptions about expertise, and expectations about who speaks, who listens, and how disagreement is expressed.

### Risk and prior experience

A community's previous experiences with government, research institutions, technology providers, healthcare organizations, data collection, or outside programs can affect current participation. Low participation may represent distrust, fatigue, fear of surveillance, concern about data use, inaccessible processes, or a rational judgment that participation has not produced meaningful results in the past.

### Relationships and reciprocity

Participation is more likely to be meaningful when relationships continue beyond a single request for information. Communities may reasonably expect institutions that collect knowledge to return findings, explain decisions, share benefits, acknowledge contributors, correct misinterpretations, and remain accountable after the engagement process ends.

### Community definitions of success

The outcomes valued by a state agency, funder, researcher, service provider, or technology company may not fully match the outcomes valued locally. Culture influences what a community considers progress, which trade-offs it accepts, whose experiences receive priority, and how benefits and harms are distributed.

For these reasons, participation levels should never be interpreted without context. A low rate of participation does not necessarily indicate a lack of interest, motivation, or need. It may indicate that an opportunity was offered through the wrong institution, at the wrong time, in an inaccessible format, using unfamiliar language, without adequate trust, or without evidence that participation would influence anything.

Likewise, a high participation count does not necessarily demonstrate meaningful engagement. Attendance can be high while influence remains low. A program can reach many residents while failing to include those most affected by a decision. A survey can generate a large dataset while omitting the people who lack the time, connectivity, trust, literacy, language access, or institutional relationships needed to respond.

Culture is therefore not simply another influence on participation. It is part of the interpretive framework required to understand what participation metrics mean.

## From Participation Measurement to Participation Provenance

A participation metric should record more than a count. It should preserve enough provenance to support responsible interpretation.

For a survey, meeting, training program, or community-engagement process, that provenance might include:

- who organized the activity;
- who helped design it;
- who invited participants;
- which organizations or community leaders served as intermediaries;
- who was eligible to participate;
- who actually participated;
- which groups were underrepresented or absent;
- how participants were recruited;
- when and where participation occurred;
- whether transportation, childcare, connectivity, disability access, or compensation was provided;
- which languages and formats were available;
- what participants were told about the purpose of the activity;
- how their information would be stored and used;
- whether participants could review or correct interpretations;
- which recommendations emerged;
- which recommendations influenced decisions; and
- what was returned to the community afterward.

Consider the statement:

> **Community X has low interest in workforce training.**

Without participation provenance, this can appear to be a factual description of the community.

With provenance, the statement might instead become:

> **Fourteen percent of invited residents responded to an online-only survey distributed primarily through partner email lists. Respondents reported low interest in the training options presented. Residents without reliable connectivity, people unaffiliated with the partner organizations, and individuals who preferred in-person engagement may have been underrepresented.**

The second statement does not discard the survey result. It makes the result interpretable.

This is one place where DOIN could add value. Rather than storing only a participation rate or a generalized conclusion, it could connect the metric to its method, participants, context, limitations, cultural setting, responsible organizations, affected communities, and subsequent decisions.

## Relating the Three Frameworks

The relationship among these ideas can be expressed this way:

- **Michigan's Digital Equity Plan:** What conditions is Michigan trying to improve, and what measurable objectives will guide that work?
- **Digital Opportunities Compass:** What interacting dimensions should be examined to understand whether connectivity is becoming meaningful opportunity?
- **Participation metrics:** Who is taking part, what are they doing, whether they influence decisions, and what outcomes follow?
- **Culture:** What makes participation trusted, relevant, legitimate, meaningful, and sustainable in a particular community?
- **DOIN:** What do we know about this place that helps explain these conditions, where did that knowledge come from, whose knowledge is represented, and under what cultural and contextual conditions should it be interpreted?

Seen this way, DOIN does not need to replace either Michigan's Digital Equity Plan or the Digital Opportunities Compass. It can complement them by providing a knowledge layer capable of connecting conventional data and participation metrics with relationships, culture, context, provenance, and locally generated knowledge.

That distinction is especially important because community engagement produces forms of knowledge that are difficult to capture in conventional datasets. Listening sessions, interviews, community meetings, surveys, and collaborative planning can reveal who residents trust, why previous initiatives succeeded or failed, which organizations actually reach particular populations, what residents identify as priorities, and what local assets may be invisible in statewide datasets.

Project Compass demonstrates this community-centered orientation in practice. Its work in rural Michigan uses the Digital Opportunities Compass framework to understand local needs, develop digital-skills strategies, organize community groups, connect communities with experts and resources, and assist with funding opportunities.[^4] That activity generates knowledge about participation, relationships, needs, trust, and local capacity that may be as important as the resulting program counts.

If those insights remain only in meeting notes, reports, presentations, survey exports, or institutional memory, much of their value can disappear between projects. A community knowledge infrastructure could help preserve those insights while retaining information about their source, context, perspective, limitations, and appropriate use.

This leads to an important distinction:

> **Data infrastructure connects evidence.**
>
> **Knowledge infrastructure preserves meaning.**
>
> **Community knowledge infrastructure preserves meaning while also preserving community agency over that meaning.**

That last requirement matters. The goal should not be to convert culture, trust, relationships, community identity, or participation into another collection of scores. Doing so could reproduce the same abstraction problem this work is trying to address.

Instead, the challenge is to combine quantitative participation metrics with qualitative and relational evidence while preserving provenance, uncertainty, perspective, context, limitations, and appropriate community control.

The Digital Opportunities Compass can help identify **where to look** for digital opportunity.

Michigan's Digital Equity Plan can help establish **what conditions and outcomes require attention**.

Participation metrics can help show **who is taking part and what they are doing**.

Cultural context can help explain **why participation takes the form it does**.

DOIN may be able to preserve **what a community knows about itself, how that knowledge was produced, and why it matters**.

This suggests a broader research proposition:

> **A digital-opportunity measurement framework can tell us that communities differ. Participation metrics can show where those differences appear in practice. A community knowledge infrastructure may help us understand why those differences exist without reducing culture, participation, or community identity to another score.**

The deeper question for DOIN, then, may not simply be how to incorporate culture and context into a data model. It may be:

> **How can we build knowledge infrastructure that allows communities to describe themselves, preserves the context and provenance of participation and community knowledge, connects that knowledge to other forms of evidence, and retains community agency over how it is interpreted and used?**

That moves the problem from **data integration toward knowledge governance**, from counting participation toward understanding participation, and from building infrastructure *about* communities toward building knowledge infrastructure *with* them.

## References

[^1]: Michigan High-Speed Internet Office. *State of Michigan Digital Equity Plan*. Michigan Department of Labor and Economic Opportunity, July 2024. https://www.michigan.gov/leo/-/media/Project/Websites/leo/Documents/MIHI/MIHI-Digital-Equity-Plan.pdf?rev=0bcd2c37d52b40a1bf476e72ea7c65db&hash=E1181B05337C998B398C49E6B5BEF441

[^2]: Rhinesmith, Colin, Pierrette Renée Dagg, Johannes M. Bauer, Greta Byrum, and Aaron Schill. *Digital Opportunities Compass: Metrics to Monitor, Evaluate, and Guide Broadband and Digital Equity Policy*. Merit Network and Quello Center, Michigan State University, 2023. https://mccmeetingspublic.blob.core.usgovcloudapi.net/hartfordmi-meet-e3dbd234ead145f9ae972630e4298ed8/ITEM-Attachment-001-2cdac5e024924cc39630b3cc0203b574.pdf

[^3]: Michigan High-Speed Internet Office. “Michigan Digital Equity and Inclusion.” Michigan Department of Labor and Economic Opportunity. https://www.michigan.gov/leo/bureaus-agencies/mihi/michigan-digital-inclusion-resources

[^4]: Merit Network. “Project Compass.” https://www.merit.edu/research/project-compass/
What changed
The revised section distinguishes digital participation from community participation in planning. It introduces a five-level model of reach, engagement, influence, continuity, and outcomes, maps participation to all six Compass components, and treats culture as an interpretive layer rather than another demographic field. It also introduces participation provenance, which gives DOIN a concrete role: connecting participation measurements to the people, methods, relationships, cultural conditions, limitations, and decisions that give those measurements meaning.