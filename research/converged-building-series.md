---
layout: page
title: "The Converged Building"
subtitle: "Fiber, Fault-Managed Power, DC Distribution, and the Emerging Architecture of Intelligent Infrastructure"
author: "Jason Kronemeyer"
date: 2026-10-15
status: series
---

# The Converged Building

This master file contains the ten-part publication series and shared bibliography. Each article includes its own publication front matter with `status: series`.

<!-- ARTICLE 1 -->

---
layout: post
title: "What Architects, Engineers, and Electrical Contractors Need to Know About Fault-Managed Power Today"
subtitle: "Class 4 power is becoming an infrastructure discipline"
author: "Jason Kronemeyer"
date: 2026-10-15
status: series
series: "The Converged Building"
series_order: 1
categories: [intelligent-infrastructure, fault-managed-power, buildings, engineering]
tags: [FMPS, Class 4, NEC Article 726, architects, engineers, electrical contractors]
---

# What Architects, Engineers, and Electrical Contractors Need to Know About Fault-Managed Power Today

*The Converged Building, Part 1*

Buildings are changing in a way that is easy to miss when we continue to think about electrical systems, communications networks, energy systems, and building controls as separate disciplines.

Fiber is moving deeper into buildings. Power over Ethernet is supporting more devices at the edge. Fault-Managed Power Systems, or FMPS, create another way to deliver substantial power over distance. Solar generation and battery storage introduce DC energy resources. Wireless networks, cameras, sensors, controls, distributed computing, and other connected systems continue to multiply.

Each development matters on its own. I am increasingly interested in what happens when we stop examining them separately.

> **The central question of this series is simple: What happens when we begin designing the movement of information and the movement of energy as parts of the same infrastructure problem?**

The 2023 National Electrical Code introduced Class 4 Fault-Managed Power Systems in Article 726. UL Solutions states that FMPS continually monitors for faults and limits the energy delivered into a fault; in November 2023 it announced the first certification of a Class 4 distribution system under UL 1400-1 (UL Solutions, 2023a; UL Solutions, 2023b).

The code continues to evolve. NFPA identifies the 2026 edition of NFPA 70 as the current edition and notes continued restructuring of limited-energy material (NFPA, 2026a; NFPA, 2026b).

## FMPS Is Not Simply Bigger PoE

Power over Ethernet and fault-managed power can complement one another, but they perform different jobs. PoE combines power and data for compatible Ethernet-connected devices. FMPS can transport power to a remote location, where local equipment may then distribute power in the form appropriate to the load.

One commercial distributed-edge architecture expresses this relationship as **FMPS on the power backbone and PoE at the edge** (Grigg and Rosas, 2026). That is useful evidence of one implementation model, not a universal design requirement.

My synthesis is simpler:

> **FMPS can bring power to the edge. PoE can distribute power and data from the edge.**

## Class 4 Is a Category, Not a Product

A Class 4 circuit should not be defined by the specifications of one manufacturer. UL describes Class 4 certification in technology-neutral terms focused on the system's monitoring of faults and limitation of fault energy (UL Solutions, 2023a; UL Solutions, 2023b).

The appropriate project question is therefore not merely, *Are we using fault-managed power?* It is:

> **What listed Class 4 system are we considering, what are its actual characteristics, what problem are we asking it to solve, and what requirements govern its use?**

## What Each Discipline Needs to Know

| Discipline | Key design question |
|---|---|
| Architect | What changes in rooms, pathways, ceilings, equipment locations, access, and usable building area? |
| Electrical engineer | How do source, distribution, conversion, protection, backup, grounding/bonding, and Class 4 requirements interact? |
| ICT designer | How do fiber topology, PoE, edge electronics, pathways, and remote power interact? |
| Electrical contractor | What installation, equipment, identification, commissioning, documentation, and maintenance requirements apply? |
| ICT/low-voltage contractor | Where does familiar structured cabling intersect with a separately governed electrical system? |
| Owner/commissioning team | Who accepts, documents, operates, monitors, and maintains the completed system? |

## Five Questions I Would Ask Today

1. **What problem are we actually trying to solve?**
2. **Why might Class 4 be preferable to conventional alternatives for this application?**
3. **Where will information, power, conversion, backup, and active electronics reside?**
4. **Who will design, install, commission, document, operate, and maintain each layer?**
5. **What will we measure to determine whether the architecture produced the expected result?**

> ### Provenance Check
> **Evidence:** NEC Article 726, UL 1400-1, and UL Class 4 certification establish a formal code and safety framework (NFPA, 2026a; UL Solutions, 2023a; UL Solutions, 2023b).
>
> **My synthesis:** These developments justify examining information transport and energy transport as increasingly related infrastructure problems.
>
> **Hypothesis:** Designing these layers together could produce measurable advantages under particular conditions. That proposition still needs to be tested.

---

**Next:** *Power That Manages the Fault*

**Evidence → Synthesis → Hypothesis → Test → Evidence**

<!-- ARTICLE 2 -->

---
layout: post
title: "Power That Manages the Fault"
subtitle: "Why Class 4 is better understood by what happens during a fault than by voltage or wattage alone"
author: "Jason Kronemeyer"
date: 2026-10-16
status: series
series: "The Converged Building"
series_order: 2
categories: [intelligent-infrastructure, fault-managed-power]
tags: [FMPS, Class 4, UL 1400-1, NEC Article 726]
---

# Power That Manages the Fault

*The Converged Building, Part 2*

The easiest way to misunderstand fault-managed power is to define it primarily by voltage, wattage, or distance. Those characteristics matter when evaluating a particular system, but they do not capture the idea that makes Class 4 distinct.

The important concept is in the name:

> **The system manages the fault.**

UL Solutions describes FMPS as technology that continually monitors for faults and limits the energy delivered into a fault. It can automatically shut off after a detected fault that could cause shock or fire hazards (UL Solutions, 2023a).

## Think System, Not Wire

UL's Class 4 guidance describes a certified system as including a transmitter, a receiver, and Class 4 cable (UL Solutions, 2023b). That changes the mental model from a conductor carrying electricity to a **power-delivery system whose monitored behavior contributes to its safety architecture**.

| Traditional question | FMPS adds another question |
|---|---|
| Where does power go? | What conditions does the system monitor? |
| What conductor carries it? | What equipment forms the listed system? |
| What is the connected load? | What happens during a detected fault? |
| What protects the circuit? | How is fault energy limited? |

## Safety Intelligence Is Not Operational Intelligence

I distinguish between two concepts. **Safety intelligence** is the monitoring and response necessary to manage fault energy. **Operational intelligence** may include additional product-dependent measurements, events, alarms, configuration, or integrations.

Those concepts should not be conflated. Class 4 tells us something important about the way a power system manages faults. It does not by itself specify a complete intelligent-building analytics platform.

That distinction opens a larger question: if power can become an actively managed infrastructure layer, how should it relate to the communications network?

---

**Previous:** *What Architects, Engineers, and Electrical Contractors Need to Know About Fault-Managed Power Today*  
**Next:** *Between PoE and Conventional Power*

**Evidence → Synthesis → Hypothesis → Test → Evidence**

<!-- ARTICLE 3 -->

---
layout: post
title: "Between PoE and Conventional Power"
subtitle: "Finding the architectural role for Class 4 at the building edge"
author: "Jason Kronemeyer"
date: 2026-10-17
status: series
series: "The Converged Building"
series_order: 3
categories: [intelligent-infrastructure, networks, power]
tags: [FMPS, PoE, distributed edge, Class 4]
---

# Between PoE and Conventional Power

*The Converged Building, Part 3*

Power over Ethernet changed something fundamental about the relationship between power and communications. For compatible devices, an endpoint can receive both information and power through network cabling.

But PoE does not solve every building-power problem. FMPS occupies another part of the design space.

A commercial distributed-edge design reviewed for this series explicitly proposes FMP for long-distance backbone power and PoE for local device distribution (Grigg and Rosas, 2026). My shorthand is:

> **FMPS can be the highway. PoE can be the local road.**

That is my synthesis, not a standards definition.

## Stop Designing From the Maximum Number

Vendor literature can contain useful product specifications but should not define the category. Grigg and Rosas describe particular power, distance, material, and energy claims for their AGILE-CORE architecture; those claims should remain tied to that commercial design unless independently demonstrated elsewhere (Grigg and Rosas, 2026).

The more useful design question is:

> **Where should switching, transformation, conversion, backup, and distribution occur to produce the best complete building system?**

Technology selection should follow the building's requirements. Once we begin asking where active equipment should be centralized and where it should remain distributed, fiber becomes part of the same conversation.

---

**Previous:** *Power That Manages the Fault*  
**Next:** *When Fiber and Power Travel Together*

**Evidence → Synthesis → Hypothesis → Test → Evidence**

<!-- ARTICLE 4 -->

---
layout: post
title: "When Fiber and Power Travel Together"
subtitle: "Why deep fiber and remotely delivered power invite us to rethink the telecommunications room"
author: "Jason Kronemeyer"
date: 2026-10-18
status: series
series: "The Converged Building"
series_order: 4
categories: [intelligent-infrastructure, fiber, networks]
tags: [POLAN, FMPS, Passive Optical LAN, distributed edge]
---

# When Fiber and Power Travel Together

*The Converged Building, Part 4*

Fiber and fault-managed power solve fundamentally different problems. **Fiber transports information. FMPS transports energy.** Yet the two can support complementary architectures.

My earlier work on distributed-edge POLAN explored zone-based ONT placement, fiber backbones, and the possibility of coordinating those designs with remote power (Kronemeyer, 2025). That earlier article contains several product-level performance statements that should be treated cautiously; this series preserves the architectural idea while applying stricter provenance to performance claims.

## Does This Eliminate the IDF?

Not automatically.

My current synthesis is more precise:

> **Deep fiber can change the networking equipment traditionally concentrated in distributed telecommunications spaces. Remotely delivered power can change the electrical and backup requirements associated with active equipment at the edge.**

Commercial distributed-edge material explicitly proposes reducing or eliminating conventional IDF rooms, but that outcome is a feature claimed for a specific architecture, not an inherent result of Class 4 itself (Grigg and Rosas, 2026).

The better approach is to redesign the space from first principles:

- What equipment actually needs to reside here?
- What requires power or backup?
- What generates heat?
- What requires technician access?
- What should remain operational during an outage?
- What should be centralized?
- What should remain distributed for resilience?

These questions move the conversation beyond individual technologies toward infrastructure layers.

---

**Previous:** *Between PoE and Conventional Power*  
**Next:** *The Building Becomes Layered*

**Evidence → Synthesis → Hypothesis → Test → Evidence**

<!-- ARTICLE 5 -->

---
layout: post
title: "The Building Becomes Layered"
subtitle: "A systems model for bringing information, power, energy, and operational intelligence into one architecture"
author: "Jason Kronemeyer"
date: 2026-10-19
status: series
series: "The Converged Building"
series_order: 5
categories: [intelligent-infrastructure, systems-thinking]
tags: [FMPS, intelligent infrastructure, layered architecture, POLAN]
---

# The Building Becomes Layered

*The Converged Building, Part 5*

The more I study convergence, the less useful I find the idea of treating "the network" and "the electrical system" as two enormous, self-contained boxes. A layered model is more useful.

| Layer | Examples | Primary question |
|---|---|---|
| Energy sources | Grid, solar, storage, generator | Where does energy originate? |
| Energy and conversion | AC, DC, UPS, microgrid | In what form should energy move? |
| Managed power | Class 4 FMPS | How can power be delivered while fault energy is managed? |
| Transport | Fiber, Class 4 pathways | How do information and energy reach the edge? |
| Edge distribution | Receivers, ONTs, switches, PoE | Where should final distribution occur? |
| Building loads | Wi-Fi, DAS, cameras, lighting, sensors, controls | What consumes the infrastructure? |
| Operational intelligence | Measurement, events, monitoring, automation | What can operators understand and act upon? |

> **Provenance note:** This layered model is **my synthesis**. It is not an architecture prescribed as a whole by NFPA, UL, NECA, or a manufacturer.

The underlying components are real. UL identifies transmitters, receivers, and Class 4 cable as elements of listed Class 4 systems, and commercial distributed-edge designs demonstrate FMPS, fiber, receivers, switching, and PoE in combined implementations (UL Solutions, 2023b; Grigg and Rosas, 2026).

The act of connecting those components into the larger model above is my contribution.

That model leads naturally to another question: what happens when more generation, storage, and end-use equipment involve DC?

---

**Previous:** *When Fiber and Power Travel Together*  
**Next:** *The DC-Native Question*

**Evidence → Synthesis → Hypothesis → Test → Evidence**

<!-- ARTICLE 6 -->

---
layout: post
title: "The DC-Native Question"
subtitle: "When does hybrid AC/DC distribution make sense in a modern building?"
author: "Jason Kronemeyer"
date: 2026-10-20
status: series
series: "The Converged Building"
series_order: 6
categories: [intelligent-infrastructure, energy, buildings]
tags: [DC power, microgrids, FMPS, energy efficiency]
---

# The DC-Native Question

*The Converged Building, Part 6*

Look closely at a modern building and an interesting convergence appears. Photovoltaics produce DC. Batteries store energy as DC. Solid-state lighting and consumer electronics are among the DC end uses identified in national-laboratory research examining renewed interest in DC building distribution (Vossos et al., 2022).

That invites a tempting question:

> **Why not make the building DC?**

We should resist answering too quickly.

Vossos and colleagues evaluate technology and market readiness, efficiency, cost, resilience, implementation barriers, field deployments, and adoption pathways. They conclude that significant technology and market barriers have kept broader DC distribution largely in the demonstration phase while identifying specific applications they consider viable (Vossos et al., 2022).

"DC loads exist" is evidence. "Therefore every building should distribute DC" is not.

> ### Hypothesis
> **Buildings with sufficiently large concentrations of compatible DC loads, DC generation, storage, and remotely powered digital infrastructure may present conditions in which hybrid AC/DC architectures outperform otherwise comparable conventional architectures at the system level.**

That is my hypothesis, not a conclusion of Vossos et al.

## Define "Better"

| Measure | What a comparative study could examine |
|---|---|
| Energy | Total measured system consumption and conversion losses |
| Cost | Complete installed architecture, not isolated components |
| Material | Copper, fiber, pathways, electronics, supporting infrastructure |
| Space | Electrical and telecommunications-room requirements |
| Resilience | Behavior under source, equipment, and grid failures |
| Maintenance | Labor, replacement, troubleshooting, and service requirements |
| Lifecycle | Cost and performance over an agreed study period |
| Adaptability | Moves, additions, changes, and technology refreshes |

A component can be more efficient without making the entire building more efficient. The building therefore needs to be evaluated as a system.

---

**Previous:** *The Building Becomes Layered*  
**Next:** *The Resilient Building*

**Evidence → Synthesis → Hypothesis → Test → Evidence**

<!-- ARTICLE 7 -->

---
layout: post
title: "The Resilient Building"
subtitle: "The bigger question may not be efficiency, but what continues to work when normal power does not"
author: "Jason Kronemeyer"
date: 2026-10-21
status: series
series: "The Converged Building"
series_order: 7
categories: [intelligent-infrastructure, resilience, energy]
tags: [FMPS, resilience, microgrids, backup power]
---

# The Resilient Building

*The Converged Building, Part 7*

We often discuss new energy infrastructure in terms of efficiency. For schools, public buildings, community facilities, and other important infrastructure, a more consequential question may be:

> **What still works when normal power doesn't?**

My October 14 research note identifies centralized backup as one architectural possibility for Class 4 systems while also cautioning that FMPS status alone does not confer an emergency-power classification (Kronemeyer, 2026a).

That distinction matters.

## Centralization Is Not Automatically Resilience

Centralization can simplify some infrastructure while increasing the consequence of particular failures. The right question is therefore not whether everything should be centralized. It is:

> **What should be centralized, what should remain distributed, and how should the system behave when something fails?**

Independent DC-building research also identifies resilience as a potential benefit worthy of study while documenting barriers to deployment (Vossos et al., 2022).

For a real building, the design team must decide which functions are critical and which power architecture is appropriate to applicable codes and operational requirements. FMPS does not make that decision for us.

My hypothesis is narrower: coordinating energy resources, communications, controls, and managed distribution may create new ways to preserve selected building functions during an interruption. That proposition should be tested rather than assumed.

---

**Previous:** *The DC-Native Question*  
**Next:** *The Intelligent Power Layer*

**Evidence → Synthesis → Hypothesis → Test → Evidence**

<!-- ARTICLE 8 -->

---
layout: post
title: "The Intelligent Power Layer"
subtitle: "What changes when power distribution becomes increasingly observable?"
author: "Jason Kronemeyer"
date: 2026-10-22
status: series
series: "The Converged Building"
series_order: 8
categories: [intelligent-infrastructure, data, power]
tags: [FMPS, telemetry, operational intelligence, intelligent buildings]
---

# The Intelligent Power Layer

*The Converged Building, Part 8*

Networks have taught us to expect observability. We do not simply move information through communications infrastructure and hope for the best. Power infrastructure likewise has mature traditions of protection, monitoring, metering, and control.

What interests me about FMPS is the opportunity to examine how monitoring and response become integral to a remotely distributed power system. UL Solutions explicitly describes continuous fault monitoring and limitation of the energy delivered into a fault (UL Solutions, 2023a).

That does not mean every Class 4 product provides comprehensive analytics, APIs, historical dashboards, or building-management integration. Those are product-specific questions.

## From Data to Knowledge

I use the following conceptual progression:

| Stage | Question |
|---|---|
| Data | What was measured? |
| Information | What does the measurement describe? |
| Context | What else was happening? |
| Knowledge | What does the relationship tell us? |
| Action | What should we do about it? |

> **Measurement → Context → Information → Knowledge → Action**

This is my synthesis, not an FMPS standard.

A connected building has systems capable of communicating. An intelligent building should increasingly help people understand what the building is doing, how conditions relate, and what decisions those conditions support.

Technology alone does not create that intelligence. Architecture, data, people, and operations have to work together.

---

**Previous:** *The Resilient Building*  
**Next:** *Who Builds the Converged Building?*

**Evidence → Synthesis → Hypothesis → Test → Evidence**

<!-- ARTICLE 9 -->

---
layout: post
title: "Who Builds the Converged Building?"
subtitle: "Why Class 4 creates a case for cross-disciplinary infrastructure literacy"
author: "Jason Kronemeyer"
date: 2026-10-23
status: series
series: "The Converged Building"
series_order: 9
categories: [workforce, intelligent-infrastructure, education]
tags: [FMPS, workforce development, electrical contractors, ICT, Class 4]
---

# Who Builds the Converged Building?

*The Converged Building, Part 9*

Technology convergence creates a workforce challenge long before it becomes a workforce shortage.

Our occupational boundaries developed around systems that were easier to separate. Electrical trades handled power. ICT professionals handled structured cabling. Network professionals handled communications. Controls professionals occupied still another territory.

Those professions are not disappearing. Their systems are increasingly intersecting.

## The Design-Team Problem Comes First

| Role | Emerging literacy |
|---|---|
| Architect | Infrastructure topology, spaces, pathways, accessibility |
| Electrical engineer | Class 4, conventional power, DC, backup, interfaces |
| ICT designer | Fiber, PoE, edge architecture, power dependencies |
| Electrical contractor | Class 4 installation, safety, commissioning, documentation |
| ICT contractor | Structured cabling plus awareness of Class 4 interfaces |
| Commissioning professional | Cross-system interfaces and performance |
| Owner/operator | Monitoring, documentation, maintenance, lifecycle planning |

NECA-hosted material demonstrates that Class 4 is already being presented to electrical contractors as a distinct technical and business topic. The 2023 NECA/BICSI session identified Class 4 with NEC Article 726 and fault-energy limitation; because the presenter was the founder and CEO of VoltServer, the presentation should be treated as industry/vendor evidence rather than independent NECA policy (Eaves, 2023).

> **Convergence should not mean everyone does everyone else's job. It means everyone needs enough understanding of adjacent systems to recognize where coordination is required.**

I call this **cross-disciplinary infrastructure literacy**. It is my workforce-development synthesis.

The opportunity for organizations such as the Cloverland Training & Technology Center is larger than teaching another product. Practitioners need strong fundamentals in their own disciplines and enough knowledge of adjacent infrastructure to recognize interfaces, scope limits, commissioning dependencies, and documentation requirements.

---

**Previous:** *The Intelligent Power Layer*  
**Next:** *Build One and Measure Everything*

**Evidence → Synthesis → Hypothesis → Test → Evidence**

<!-- ARTICLE 10 -->

---
layout: post
title: "Build One and Measure Everything"
subtitle: "Turning the converged building from an architectural proposition into a research program"
author: "Jason Kronemeyer"
date: 2026-10-24
status: series
series: "The Converged Building"
series_order: 10
categories: [research, intelligent-infrastructure, buildings]
tags: [FMPS, research, provenance, causal inference, intelligent infrastructure]
---

# Build One and Measure Everything

*The Converged Building, Part 10*

This series began with a practical question: **What should architects, engineers, electrical contractors, ICT professionals, and owners understand about FMPS today?**

I want to end with a harder one:

> **How much of what we believe about the converged building have we actually measured?**

The underlying technologies are real. Class 4 has a code framework, UL certification requirements, and certified commercial systems (NFPA, 2026a; UL Solutions, 2023a; UL Solutions, 2023b). Independent researchers are also studying DC distribution, efficiency, cost, resilience, and implementation barriers in buildings (Vossos et al., 2022).

From those facts, I have developed a broader synthesis:

> **Fiber can become an information backbone. Fault-managed power can provide a managed power layer. PoE can provide local power and data distribution where appropriate. Generation, storage, controls, networking, and operational telemetry can increasingly be considered as parts of one building-infrastructure architecture.**

That is **my synthesis**. It does not prove the architecture is better. It gives us hypotheses worth testing.

## The Hypotheses

| ID | Hypothesis | Candidate measures |
|---|---|---|
| H1: Space | Convergence may reduce some distributed infrastructure space. | Room area, equipment count, supporting MEP requirements |
| H2: Materials | Deep fiber and remote power may reduce some copper and pathway requirements. | Cable quantities, conduit/tray, material mass |
| H3: Energy | Coordinating AC/DC infrastructure may improve energy performance in suitable applications. | Input/output energy, conversion losses, cooling |
| H4: Resilience | Managed distribution and centralized energy resources may improve continuity of selected functions. | Outage behavior, runtime, failure domains, recovery |
| H5: Operations | Greater observability may improve troubleshooting and maintenance. | Events, resolution time, labor, maintenance history |
| H6: Economics | Savings elsewhere may offset specialized-system costs. | First cost, engineering, commissioning, maintenance, replacement |

Commercial material advances much stronger claims about copper, conduit, energy, real estate, and equipment life. Those figures should remain tied to the AGILE-CORE commercial architecture unless independently validated in comparable conditions (Grigg and Rosas, 2026).

## Build the Demonstration

The next step should not be another assertion that FMPS is better. It should be a demonstration capable of telling us **whether, where, and by what measure** a converged architecture produces a better result.

Candidate measures include:

- equipment quantities;
- copper and fiber quantities;
- pathway requirements;
- telecommunications-room area;
- electrical distribution requirements;
- engineering and construction labor;
- commissioning effort;
- first cost;
- conversion stages and measured energy;
- cooling associated with active infrastructure;
- battery and backup requirements;
- outage behavior;
- faults and alarms;
- moves, additions, and changes;
- equipment replacement;
- maintenance effort;
- training requirements; and
- lifecycle cost.

The measurements should follow the hypothesis.

## The Provenance Loop

> **Evidence → Synthesis → Hypothesis → Test → Observation → New Evidence**

Evidence establishes what reliable sources or measurements support. Synthesis makes my interpretation explicit. A hypothesis converts that interpretation into something capable of being challenged. Testing creates observations, and those observations become new evidence.

> ### The Research Question
> **Under what conditions does a converged architecture outperform an appropriate conventional alternative, according to which measures, and why?**

That is a more useful question than asking whether FMPS is simply "better."

# From Connected Buildings to Intelligent Infrastructure

Broadband taught us to think seriously about connecting buildings. Fiber demonstrated how information could move across extraordinary distances. Networks allowed devices to communicate. Sensors made physical environments increasingly observable.

I do not think the important story is that Class 4 will replace conventional electrical distribution, that Passive Optical LAN will replace every switched Ethernet network, or that every facility should become a DC microgrid.

My argument is narrower:

> **The boundaries among information, power, sensing, control, and energy are becoming permeable enough that we should begin designing the relationships among them intentionally.**

That is what I mean by **intelligent infrastructure**.

The answer to how a building should work should not come from a vendor, enthusiasm for new technology, or attachment to the systems we have always built. It should come from evidence.

We establish what we know. We connect the evidence and make our synthesis explicit. We turn that synthesis into testable hypotheses. Then we build, measure, learn, and allow the results to become the next generation of evidence.

---

<!-- SHARED BIBLIOGRAPHY -->

---
layout: page
title: "The Converged Building: Shared Bibliography"
author: "Jason Kronemeyer"
date: 2026-10-15
status: series
series: "The Converged Building"
---

# Shared Bibliography

## Citation and Provenance Policy

The series uses **author-date citations in the text** and a consistently formatted **MLA 9-style bibliography** below. The two work together: short author-date references keep the articles readable, while the bibliography provides the complete source record and public links where they are available.

The source classes are deliberately preserved:

| Class | Role |
|---|---|
| Authoritative | Code, certification, or formal standards information |
| Independent research | Peer-reviewed or independent empirical evidence |
| Industry/vendor | Product, architecture, or implementation evidence whose commercial context remains visible |
| Author research | My earlier writing or research notes used to establish intellectual lineage |
| Author synthesis | A conclusion I draw by connecting evidence; not a separate external source |
| Hypothesis | A proposition that remains to be tested |

## Works Cited

### Authoritative and Standards Sources

National Fire Protection Association. *NFPA 70, National Electrical Code*. 2026 ed., National Fire Protection Association, 2025. **Current-edition record:** [NFPA 70 Code Development](https://www.nfpa.org/codes-and-standards/nfpa-70-standard-essentials/70).

National Fire Protection Association. “What Changed in the 2026 NEC?” *NFPA*, 29 Jan. 2026, https://www.nfpa.org/news-blogs-and-articles/blogs/2026/01/29/2026-nec-key-changes. Accessed 15 Oct. 2026.

National Electrical Contractors Association. *NECA 726-2026: Standard for Installing and Maintaining Class 4 Fault-Managed Power (FMP) Systems*. National Electrical Contractors Association, 2026. **Verification note:** the complete standard is not freely reproduced online; use the purchased/current NECA publication for enforceable wording rather than summaries.

UL Solutions. *Outline of Investigation for Fault-Managed Power Systems—Part 1: General Requirements*. UL 1400-1, 2022.

UL Solutions. *Outline of Investigation for Fault-Managed Power Systems—Part 2: Requirements for Class 4 Cables*. UL 1400-2, 2023.

UL Solutions. “NEC 230.46 Line Side Connectors Update and Fault Managed Equipment.” *UL Solutions Question Corner*, 2023, https://code-authorities.ul.com/wp-content/uploads/sites/46/2023/08/UL-QC-230.46-and-Fault-Managed-Equipment_Spring-2023.pdf. Accessed 15 Oct. 2026.

UL Solutions. “UL Solutions Issues First Certification for a Fault-Managed Power System to Panduit.” *UL Solutions*, 21 Nov. 2023, https://www.ul.com/news/ul-solutions-issues-first-certification-fault-managed-power-system-panduit. Accessed 15 Oct. 2026.

### Independent Research

Vossos, Vagelis, et al. “Adoption Pathways for DC Power Distribution in Buildings.” *Energies*, vol. 15, no. 3, 2022, article 786, https://doi.org/10.3390/en15030786.

### Industry and Implementation Sources

Eaves, Stephen. “Intro to Class 4 Fault Managed Power Systems.” *NECA/BICSI Summit 2023*, National Electrical Contractors Association and BICSI, 26 June 2023, https://www.necanet.org/docs/2023necabicsisummitlibraries/default-document-library/powerpoints/intro-to-class-4-fault-managed-power-systems---stephen-eaves.pdf. Accessed 15 Oct. 2026. **Source note:** Eaves was identified by NECA as founder and CEO of VoltServer; product and performance claims in this presentation are treated as industry/vendor evidence.

Grigg, David, and Aaron Rosas. *Designing IT Network Infrastructures with Fault Managed Power and Power over Ethernet*. Sinclair Digital, 24 Mar. 2026. Presentation. **Source note:** commercial distributed-edge design material; quantitative savings and performance claims are not generalized beyond the presented architecture without independent evidence.

### Jason Kronemeyer Research Lineage

Kronemeyer, Jason. “Distributed Edge, POLAN, and Fault Managed Power.” *Jason Kronemeyer*, 16 Dec. 2025. Earlier research brief. **Provenance note:** used to document the development of my distributed-edge and convergence synthesis; it is not independent corroboration of my later claims.

Kronemeyer, Jason. “The Building Itself: A Candid Case for Converged Networks and Power.” *Jason Kronemeyer*, 17 Aug. 2026. Earlier essay. **Provenance note:** direct intellectual predecessor to *The Converged Building* series. Claims carried forward from this piece have been narrowed where later research established a more precise provenance boundary.

Kronemeyer, Jason. “Research Note: From ‘Digital Electricity’ to Class 4 Fault-Managed Power.” 14 Oct. 2026. Unpublished research note. **Provenance note:** principal author research synthesis used to distinguish proprietary Digital Electricity implementations from the broader standards-based Class 4 category.

## Verification Notes

1. **NFPA 70:** NFPA currently identifies the 2026 NEC as the current edition. The 2023 edition introduced Article 726; the 2026 edition continues the broader NEC restructuring.
2. **UL 1400 titles and years:** NFPA's 2026-development material identifies UL 1400-1-2022 as *Fault-Managed Power Systems—Part 1: General Requirements* and UL 1400-2-2023 as *Fault-Managed Power Systems—Part 2: Requirements for Class 4 Cables*.
3. **First Class 4 certification:** UL Solutions' 21 Nov. 2023 release expressly states that Panduit received the first Class 4 power-distribution-system certification to UL 1400-1.
4. **Vossos et al.:** the journal record verifies the author list, *Energies* volume 15, issue 3, article 786, and DOI 10.3390/en15030786.
5. **NECA 726-2026:** because the full standard is not freely available, the series does not quote or paraphrase detailed requirements that could not be verified from an authoritative public record. Project teams should use the purchased/current standard and the code adopted by the authority having jurisdiction.
6. **Commercial presentations:** AGILE-CORE, VoltServer, Panduit, and other commercial claims remain identified as vendor/industry evidence rather than independent findings.

## Claim-to-Source Map

| Topic | Preferred source | Evidence class |
|---|---|---|
| Current NEC edition | NFPA 70 | Authoritative |
| Class 4 / Article 726 | NFPA and UL | Authoritative |
| FMPS fault-management principle | UL Solutions / UL 1400-1 | Authoritative |
| Class 4 system components | UL Solutions | Authoritative |
| Class 4 cable requirements | UL 1400-2 | Authoritative |
| DC distribution in buildings | Vossos et al. | Independent research |
| FMPS + PoE distributed edge | Grigg and Rosas | Industry/vendor |
| Early Class 4 industry framing | Eaves | Industry/vendor |
| POLAN + FMPS convergence | Kronemeyer | Author synthesis |
| Layered Converged Building model | Kronemeyer | Author synthesis |
| Intelligent power layer | Kronemeyer | Author synthesis |
| Cross-disciplinary infrastructure literacy | Kronemeyer | Author synthesis |
| Comparative performance of a converged building | Future demonstration | Hypothesis / test |

## Research Questions Still Open

1. Under what conditions does convergence materially reduce telecommunications and supporting building space?
2. How do copper, fiber, pathway, and equipment quantities change in a genuinely comparable design?
3. When does a hybrid AC/DC architecture create net system-level efficiency improvements?
4. Does managed centralized power improve continuity of selected building functions, and what new failure domains does it create?
5. Does increased power-system observability measurably reduce troubleshooting or maintenance effort?
6. What competencies are actually required across electrical, ICT, engineering, commissioning, and operations roles?
7. Under which building types, load profiles, and lifecycle assumptions does the complete converged architecture outperform an appropriate conventional alternative?

> **These are research questions, not findings.**

## The Converged Building Research Method

> **Evidence → Synthesis → Hypothesis → Test → Observation → New Evidence**

The bibliography is not the end of the research process. It is the start of an auditable chain between what the evidence establishes, what I infer from it, what I think should happen next, and what a real-world test eventually shows.
