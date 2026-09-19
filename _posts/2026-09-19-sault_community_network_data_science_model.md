---
layout: research-note
title: "A Network Data Science Model for Community Health, Information Resilience, and Digital Equity in Sault Ste. Marie, Michigan"
author: "Jason Kronemeyer"
date: "2026-09-19"
location: "Sault Ste. Marie, Michigan"
document_type: "Conceptual community model"
citation_style: "APA 7th edition"
status: draft
keywords:
  - network data science
  - community health
  - information resilience
  - misinformation
  - digital equity
  - healthcare access
  - Sault Ste. Marie
  - Eastern Upper Peninsula
---

# - Conceptual - DRAFT - Not For Citation -

## Introduction

A data scientist working on this problem would build the case by combining community-health indicators, broadband and infrastructure data, institutional relationships, trusted-information flows, and local survey or engagement data into a single analytical picture of how a community functions. The task is not to reduce residents to a single score or to treat the problem as purely individual. Instead, the goal is to map who is connected to care, who is connected to reliable information, where access breaks down, and which organizations or relationships act as bridges across otherwise disconnected groups.

Spatial relationships matter here as much as social ones. Distance, travel time, water crossings, ferry schedules, bridge access, school and library access, broadband availability, and the location of clinics, tribal services, and community anchors all shape whether a resident can reach trustworthy support or remain connected during a disruption. In the Eastern Upper Peninsula, this includes not only ordinary geography but also transport isolation created by car ferries to Drummond, Neebish, and Sugar Island, the Mackinac Bridge corridor, passenger-ferry and air-dependent access on Mackinac Island, and limited-access communities such as Bois Blanc Island. These conditions change emergency response, care coordination, and information flow in ways that cannot be understood by examining people or institutions in isolation.

In network science terms, Sault Ste. Marie can be treated as a multilayer system in which clinics, schools, libraries, tribal organizations, faith communities, media channels, digital access points, and physical transport links form different kinds of relationships that influence resilience, trust, and health outcomes across both social and geographic space. This draft is intentionally exploratory: it is meant to help the reader think in systems terms about how network structure, place, and transport isolation together shape community well-being, and how a data-science lens can identify points of leverage for stronger, more equitable recovery.

This model aligns closely with the broader Digital Opportunities Intelligence Network (DOIN) framing. DOIN treats digital opportunity as a dynamic, place-based learning system rather than a static score: infrastructure, local institutions, trusted information, skills, access barriers, and lived experience all interact over time. The present model applies that same logic to community health and resilience in the Eastern Upper Peninsula by tracing how people are connected to care, to credible information, to digital infrastructure, and to practical support under conditions shaped by geography, ferry access, bridge crossings, and island isolation. In this sense, the model is not only a network-analysis exercise; it is a local example of a DOIN-style policy learning system that can help communities detect weak links, compare interventions, and update decisions as conditions change.

The sections that follow translate these ideas into a concrete model: a multilayer graph that maps healthcare, information, digital access, social support, and physical mobility; a vulnerability framework that captures how isolation and barriers change risk; and a set of measures for reach, fragmentation, resilience, and correction. In other words, the introduction frames the problem, while the rest of the document operationalizes it into a practical network analysis for community planning.

## Executive summary

Sault Ste. Marie can be modeled as a living, multilayer network of residents, healthcare organizations, public agencies, tribal organizations, schools, libraries, community groups, communications channels, and digital infrastructure. The purpose of this model is to help the community understand how healthcare access, trusted information, digital inclusion, and social support interact during periods of uncertainty or disruption. The model is designed to identify system-level opportunities for strengthening community resilience, not to judge individuals, suppress criticism, or assign people a “negativity score.”

The proposal builds on the categories in the 2025 *Community Health Needs Assessment* for MyMichigan Medical Center Sault, including chronic conditions, social determinants of health, access to care, health behaviors, behavioral health, community surveys, provider surveys, and community-partner assessment (MyMichigan Health, 2025). It also draws on Michigan’s public community-health data infrastructure, local public-health services, and Eastern Upper Peninsula work involving GIS, FCC broadband data, digital-participation metrics, community access points, and digital-equity planning (Michigan Department of Health and Human Services, n.d.; Chippewa County Health Department, n.d.; Kronemeyer, 2025a, 2025b).

## 1. Model purpose

The model is intended to help community partners answer four questions:

1. Where does reliable health information originate?
2. How does health information move through the community?
3. Where might residents experience weak connections to care, credible information, digital resources, or social support?
4. Which trusted connections could be strengthened to reduce harm and improve recovery after a disruption?

This is a conceptual and planning model. Its equations and indicators would require local validation before being used for operational decisions.

## 2. Multilayer network design

Represent the community as a time-varying multilayer graph:

$$
G_t = (V, E_t, L)
$$

where:

- $V$ is the set of community actors or anonymized population groups.
- $E_t$ is the set of relationships observed during reporting period $t$.
- $L$ is the set of network layers.

The core idea is that community well-being is influenced not by a single pathway but by several interacting layers of connection. Health access, information trust, digital inclusion, social support, and physical mobility are not separate issues; they are interdependent parts of a single system.

### 2.1 Healthcare-access layer

Potential nodes include anonymized patient groups, primary-care practices, hospital services, pharmacies, behavioral-health providers, tribal health organizations, public-health agencies, and telehealth access locations. Potential edges include referral pathways, care-transition relationships, geographic accessibility, and shared health-education activity.

The 2025 local health assessment provides an appropriate starting framework because it includes access to care, behavioral health, social determinants, health behaviors, community surveys, provider surveys, and community-partner assessment (MyMichigan Health, 2025).

### 2.2 Trusted-information layer

Potential nodes include healthcare organizations, the Chippewa County Health Department, schools, libraries, tribal organizations, local news organizations, faith and civic organizations, and public-facing social-media pages or groups. Potential edges include public information sharing, cross-posting, education partnerships, referrals to authoritative sources, and participation in community forums.

The Chippewa County Health Department publicly identifies personal and family health, environmental health, community services, emergency preparedness, school-based health, and telehealth among its service areas (Chippewa County Health Department, n.d.). These functions make the department a logical institutional node for analysis, although each actual partnership or information-sharing relationship would need to be verified locally.

### 2.3 Digital-access layer

Potential nodes include households aggregated by census geography, broadband service areas, libraries, digital navigators, training providers, and telehealth-capable community locations. Potential edges include broadband availability, device access, digital-skills assistance, training participation, and telehealth connectivity.

Existing Eastern Upper Peninsula research offers a technical foundation for this layer. Prior work has used GIS, FCC broadband data, exploratory data analysis, and random-forest modeling to examine network quality and digital inequity across the region (Kronemeyer, 2025a, 2025b). Those methods could be adapted to study whether infrastructure and digital-skills barriers limit access to credible health information or telehealth.

### 2.4 Social-support layer

Potential nodes include families, caregivers, senior groups, youth groups, faith communities, neighborhood organizations, volunteer groups, and community leaders. Potential edges include caregiving, transportation support, mutual assistance, digital help, trusted advice, and participation in shared activities.

This layer should measure access to support, not belief, character, emotion, or morality. The aim is to understand whether residents have practical pathways to assistance, reliable information, and healthcare.

### 2.5 Physical-mobility layer

This layer is especially important in the Eastern Upper Peninsula. Potential nodes include islands, ferry terminals, bridge crossings, airports, clinics, community centers, emergency-response hubs, and transport-dependent service areas. Potential edges include ferry trips, bridge crossings, road travel time, weather disruptions, emergency transfers, and scheduled access to care or services.

This layer captures a condition that is often invisible in conventional digital-equity or public-health analysis: a person may have strong support, access to broadband, and adequate health information, yet still be structurally isolated because their travel options are limited. This is especially relevant for Drummond Island, Neebish Island, and Sugar Island, where car-ferry access shapes daily life and service access; Mackinac Island, where passenger ferries and air travel create a different dependence on mobility; and Bois Blanc Island, where geographic separation alters emergency response and care continuity.

## 3. Information-flow and vulnerability model

For each anonymized population group or institutional node $i$, define:

- $T_i(t)$: exposure to trusted health information
- $M_i(t)$: exposure to misleading or unverified information
- $S_i(t)$: strength of supportive community connections
- $A_i(t)$: practical access to healthcare
- $D_i(t)$: digital access and skills
- $I_i(t)$: social isolation
- $B_i(t)$: barriers to care
- $P_i(t)$: physical access barriers caused by geography, ferry schedules, bridge crossings, weather disruptions, or limited transport options
- $R_i(t)$: estimated community-level vulnerability

A conceptual vulnerability equation is:

$$
R_i(t) = w_1M_i(t) + w_2I_i(t) + w_3B_i(t) + w_4P_i(t) - w_5T_i(t) - w_6S_i(t) - w_7A_i(t) - w_8D_i(t)
$$

The weights $w_1 \ldots w_8$ should be estimated from local outcomes or established through a transparent pilot process. In the Eastern Upper Peninsula, physical barriers are not secondary to digital or social conditions; they are a distinct layer of the network. A resident can have strong broadband access and trusted local connections but still experience high vulnerability if care requires crossing water, using seasonal ferry service, waiting for a bridge crossing, or depending on limited flights or passenger-only transportation. This equation is not a validated clinical formula. It is a proposed structure for testing whether network conditions are associated with aggregate outcomes such as delayed care, missed appointments, unresolved prescription needs, or difficulty identifying credible health sources.

A separate diffusion model could estimate the probability that a public claim is reshared:

$$
P(i \text{ shares claim } c) = \sigma(\alpha F_{ic} + \eta E_{ic} + \gamma C_c + \delta Q_i - \theta L_i)
$$

where:

- $F_{ic}$ is the frequency with which node $i$ encounters claim $c$.
- $E_{ic}$ is the message’s emotional intensity, measured only in public or consented data.
- $C_c$ is exposure through trusted connections.
- $Q_i$ is structural influence within the observed network.
- $L_i$ is health and digital literacy.
- $\sigma$ is a logistic transformation.

The objective is to understand aggregate network behavior, not infer an individual’s motives, feelings, or character.

## 4. Core measures

### 4.1 Trusted reach

$$
\text{Trusted Reach} = \frac{\text{population reachable through trusted pathways}}{\text{population represented in the model}}
$$

This measure estimates how much of the represented community can receive verified health information through trusted local channels.

### 4.2 Fragmentation

Community-detection and modularity measures can identify clusters that communicate mainly within their own boundaries. High modularity is not inherently harmful, but it may indicate that credible health information is not crossing community boundaries.

### 4.3 Bridging capacity

Betweenness centrality can identify institutions that connect otherwise separated groups. Results should generally be reported by organization or organization type, rather than by private individuals.

### 4.4 Resilience under disruption

Simulate the temporary removal of a provider, clinic, communications channel, or community access site:

$$
\text{Resilience Loss} = 1 - \frac{\text{Reach after disruption}}{\text{Reach before disruption}}
$$

This can show how dependent the community is on a small number of connectors. It should not be used to determine whether an employment or personnel decision was justified.

### 4.5 Correction rate and latency

$$
\text{Correction Rate} = \frac{\text{verified corrections receiving meaningful local distribution}}{\text{material health rumors identified}}
$$

Correction latency is the time between identifying a consequential public health claim and distributing an accessible, evidence-based response.

## 5. Data sources

### 5.1 Public and institutional data

Potential sources include:

- MyMichigan Medical Center Sault’s 2025 community health needs assessment (MyMichigan Health, 2025).
- Michigan community-health tables covering areas such as hospitalization, mortality, cancer, population, births, and other health topics (Michigan Department of Health and Human Services, n.d.).
- Chippewa County Health Department service and program information (Chippewa County Health Department, n.d.).
- FCC broadband data and GIS methods consistent with existing Eastern Upper Peninsula network-quality research (Kronemeyer, 2025a, 2025b).
- Aggregated participation data from libraries, schools, clinics, digital-navigation efforts, and community programs, when legally available and appropriately governed.
- Geographic and transport data describing ferry routes, road access, bridge crossings, airports, weather disruptions, and service-area boundaries.

### 5.2 Community-generated data

Voluntary surveys could measure:

- Trusted health-information sources
- Difficulty finding or evaluating health information
- Digital-skills confidence
- Ability to reach primary care
- Care-transition experiences
- Social-support availability
- Exposure to recurring health claims
- Confidence that concerns will receive a respectful response

Regional planning materials call for a needs assessment, baseline digital-participation metrics, and expertise in tribal data sovereignty. This supports participatory measurement and local governance rather than extracting community data without meaningful oversight (Kronemeyer, 2024).

## 6. Intervention model

The model should test changes to the network rather than attempts to “fix” individuals.

### 6.1 Trusted-message coalition

A coalition could connect healthcare, public health, schools, libraries, tribal organizations, faith communities, civic groups, and local media around a common process for distributing verified health information.

**Proposed network effect:** higher trusted reach and shorter correction latency.

### 6.2 Community bridge-building

Moderated forums could allow residents to ask questions, express concerns, and hear evidence-based responses without being shamed or stereotyped. Criticism and disagreement should remain welcome, while factual claims should be sourced and discussion should preserve dignity.

**Proposed network effect:** more cross-cluster connections and reduced fragmentation.

### 6.3 Digital health navigation

Digital help could be offered through libraries, senior centers, schools, tribal programs, and community events. Possible topics include patient portals, telehealth readiness, source evaluation, scam awareness, and finding authoritative medical information.

Existing regional activity includes coordination with libraries and senior centers, planning for weekly technology-help sessions at Bayliss Public Library, youth mentoring, scam prevention, safe device use, and collaboration with the Sault Tribe Youth Education and Activities program. These activities may offer a delivery network for a clinically reviewed health-information curriculum (Daines & Kronemeyer, 2026).

### 6.4 Care-disruption protocol

When a provider, clinic, or service leaves the network, an authorized healthcare organization could track aggregate transition indicators such as:

- Patients awaiting reassignment
- Prescription-renewal continuity
- Pending referrals and tests
- Record-transfer completion
- Time to the next available appointment
- Clinically high-risk transitions handled inside authorized healthcare systems

**Proposed network effect:** fewer disconnected patients and less dependence on rumors for transition information.

### 6.5 Physical-access resilience planning

Communities with limited transport access may need separate planning strategies that treat mobility as a public-health infrastructure issue. This could include coordinated scheduling information, emergency communication plans for ferry delays or weather disruptions, transportation navigation for specialty care, and local access maps for healthcare, pharmacies, telehealth sites, and trusted community anchors.

**Proposed network effect:** reduced physical isolation and stronger continuity of care during disruptions.

### 6.6 Positive amplification

Community communication can increase the visibility of accurate answers, available services, collaborative problem-solving, recovery stories, and opportunities to participate. The goal is not artificial positivity or the suppression of valid concerns. It is to prevent anger, rumor, or conflict from becoming the only highly visible signal in the network.

## 7. Privacy-preserving dashboard

A community dashboard could report:

1. **Healthcare Reach:** Percentage of represented residents connected to at least one viable care pathway.
2. **Trusted Information Reach:** Percentage reachable through two or more independent trusted channels.
3. **Care Disruption Index:** Aggregate unresolved transitions following a service change.
4. **Correction Latency:** Time between identifying a consequential rumor and releasing verified information.
5. **Digital Inclusion Index:** Composite of connectivity, device access, skills, and assistance availability.
6. **Physical Access Index:** Travel burden, ferry dependence, bridge delay risk, and geographic isolation affecting care and information access.
7. **Community Bridge Score:** Density of relationships across healthcare, tribal, education, civic, faith, and neighborhood clusters.
8. **Isolation Risk:** Geographic areas with weak access to both health and social-support connections.
9. **Recovery Trend:** Change in reach, trust, access, and bridging measures following an intervention.

All weights, definitions, thresholds, exclusions, and limitations should be published and reviewed with community representatives.

## 8. Governance and safeguards

Because the model touches health, tribal, and social-network data, governance is as important as prediction.

- Use aggregated or de-identified information whenever possible.
- Do not identify individual patients, critics, activists, employees, or social-media users.
- Do not create a “negativity score” for people.
- Give tribal nations authority over tribal data consistent with their own governance requirements.
- Separate public-health analysis from employment discipline, law enforcement, and political targeting.
- Establish multidisciplinary oversight.
- Publish data definitions, model changes, and known limitations.
- Provide a process for challenging interpretations.
- Require human review before model outputs influence resource allocation.

## 9. Growth-mindset interpretation

The central hypothesis is that a community is not permanently defined by disruption. Network structure can change. Weak bridges can be strengthened, isolated groups can be reconnected, trusted information pathways can be improved, and care gaps can be repaired.

From a network data science perspective, hope is not merely a sentiment. It is the community’s capacity to create new edges, restore damaged connections, learn from feedback, and reorganize around shared well-being. Success does not require eliminating criticism or disagreement. It means building a network in which disagreement produces learning rather than fragmentation, accurate information travels effectively, and residents remain connected to care during difficult transitions.

A growth mindset therefore becomes a measurable community strategy: test interventions, learn from evidence, revise the model, strengthen trusted connections, and repeat. The goal is not simply to return to an earlier state. It is to become a healthier, more connected, and more resilient community network.

# References

Chippewa County Health Department. (n.d.). *Home*. Retrieved September 19, 2026, from https://www.chippewahd.com/

Daines, E., & Merchberger, M. (2025). *2024.5 4-H Tech Changemakers report EUPCC* [Internal report].

Kronemeyer, J. (2024). *EUPCC MITTEN slides* [PowerPoint slides].

Kronemeyer, J. (2025a). *Final report: Assessing network quality of experience (QoE) of Eastern Upper Peninsula of Michigan through FCC broadband data* [Unpublished report].

Kronemeyer, J. (2025b). *MADS capstone final report* [Unpublished report].

Michigan Department of Health and Human Services. (n.d.). *Community health information*. Retrieved September 19, 2026, from https://www.michigan.gov/mdhhs/inside-mdhhs/statisticsreports/community-health-information

Michigan Department of Health and Human Services. (n.d.). *Division for Vital Records & Health Statistics: Community health information*. Retrieved September 19, 2026, from https://www.mdch.state.mi.us/osr/chi/IndexVer2.asp

MyMichigan Health. (2025). *Community health needs assessment 2025: MyMichigan Medical Center Sault*. https://www.mymichigan.org/app/files/public/6239464a-325c-46ef-9b04-3d3048e28127/Sault-CHNA-2025-V3-FINAL.pdf
