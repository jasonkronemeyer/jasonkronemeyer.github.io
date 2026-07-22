---
title: "Setting the Bearings: What E-Rate's Eligible Services List Is Missing — and How to Modernize It for the ICET Era"
subtitle: "The frontier is no longer reaching the schoolhouse door. It's rebuilding what happens inside the walls."
author: "Jason Kronemeyer"
role: "Community Technologist, EUPConnect Collaborative"
series: "Project Compass"
type: "op-ed"
date: 2026-07-16
location: "Eastern Upper Peninsula, Michigan"
dockets:
  - "WC Docket No. 26-133 — Modernizing the E-Rate Program (NPRM/FNPRM, FCC 26-41)"
  - "WC Docket No. 13-184 — Eligible Services List (FY2026 ESL, DA 25-1069)"
tags:
  - E-Rate
  - Universal Service Fund
  - Eligible Services List
  - ICET convergence
  - POLAN
  - Fault-Managed Power Systems
  - school infrastructure
  - digital equity
  - broadband policy
keywords:
  - Passive Optical LAN
  - Power over Ethernet
  - structured fiber cabling
  - Category Two budget
  - 10-year return on investment
  - E-Rate modernization
summary: >
  A Compass-voice position paper arguing that the FCC's Eligible Services List
  still describes yesterday's building. It identifies the converged information,
  communications, and energy technologies (ICET) missing from the list, explains
  why naming them matters, and proposes how E-Rate and the Universal Service Fund
  should be modernized — not reformed — to fund the rewiring the nation's schools
  actually need.
word_count_target: 1500
status: draft
---


*A Compass-voice position paper for Project Compass / EUPConnect Collaborative*
*By Jason Kronemeyer*

## True North: the list still describes yesterday's building

E-Rate was chartered in 1996 for a world in which the central problem was getting a signal *to* the schoolhouse door. That problem is largely solved — the FCC itself notes that virtually all schools now reach fiber broadband, which is precisely why it is asking in WC Docket 26-133 whether the program should be narrowed or sunset. But the Commission is reading the map upside down. The frontier is no longer *reaching* the building; it is **rebuilding what happens inside the building** once the signal arrives.

The Eligible Services List still sorts the world into Category One (data transmission and Internet access — leased lit fiber, dark fiber, self-provisioned networks) and Category Two (internal connections, managed internal broadband, and basic maintenance — routers, switches, access points, and cabling). That taxonomy quietly assumes that "inside the walls" is a light lift — a few switches and access points sized to a modest per-student budget. The FY2026-2030 Category Two budget is set at just \$201.57 per student (floor \$30,175; \$66,385 for Tribal libraries). Across the school-infrastructure feasibility studies I've completed, that figure doesn't come close to what a modern building actually needs — because the modern building is no longer a network with lights; it is a **converged information, communications, and energy system**.

The list is not wrong. It is simply **not yet modern**. And modernization — the FCC's own word — should mean aligning the list with the architecture that today's buildings are actually being designed and rewired around.

## What's missing from the Eligible Services List

Every gap below traces directly to the ICET convergence work in my studies. These are the categories that a modernized ESL should name explicitly rather than leave to case-by-case eligibility fights during PIA review.

### 1. Whole-building structured fiber cabling as a fundable modernization, not a capped afterthought

Cabling is technically eligible under Category Two, but the \$201.57/student budget was never scaled to **rewire a building**. Many of the nation's school buildings are on aging Cat5e/Cat6 copper in distributed closets that are themselves failure points and cost centers. A single building rewire runs on the order of \$120k–\$150k in cabling alone. The ESL should recognize a **structured fiber cabling / premise re-cabling** modernization track so that the physical layer — the thing with a 20-30 year lifecycle — is fundable at the scale it actually requires.

### 2. Passive Optical LAN (POLAN) as a named architecture

POLAN — fiber to passive splitters to optical network terminals — is the single most consequential architecture missing by name from the list. My studies show it delivers **30–50% capital savings and 40–60% operating savings** versus traditional copper switching, while eliminating power-hungry closet switches. In one EUP modeling scenario, a POLAN build with a utility partnership came in at **\$2.55M against \$9.6M** for traditional Ethernet — a 73% capital reduction. Today, ONTs are only grudgingly eligible as Category One when carrier-owned; a modernized ESL should treat POLAN electronics, splitters, and ONTs as first-class eligible internal infrastructure.

### 3. Converged power: Power-over-Ethernet and Fault-Managed Power Systems

The modern network *is* the power distribution system. PoE now drives lighting, sensors, displays, access control, and IP audio; DC Fault-Managed Power Systems (FMPS) extend that convergence safely. A PoE lighting retrofit at one middle school used **30% fewer fixtures** and could be installed by the IT cabling team rather than licensed electricians on every run. Yet the ESL and its ineligible list still treat "electrical infrastructure" and anything "servicing only ineligible items" as off-limits. That boundary is an artifact of a pre-convergence era. Modernization means recognizing that the low-voltage backbone carrying broadband is the same backbone carrying power to end devices.

### 4. Energy-integration and resilience controls (smart microgrids, DERs)

A fiber-rich campus is the control plane for solar-plus-storage microgrids, load tiering, and grid-enabled buildings — the systems that keep communications, security, and emergency instruction alive during outages, in some documented cases for **up to 96 hours in island mode**. The ESL has no vocabulary for the ICT side of this resilience layer, even though it is inseparable from the broadband network it rides on.

### 5. The integrated safety and emergency-communications fabric

Districts are converging PA, intercom, E911, panic initiation, and mass notification onto the IP network. Much of this is stranded as "ineligible" because it touches safety systems, even though it is delivered over — and depends entirely on — the eligible internal network.

## Why this matters: the 10-year return the current list leaves on the table

The strongest modernization argument is fiscal, and it is one the FCC should welcome. When a building is re-architected around converged fiber/POLAN rather than patched copper, the district captures a **10-year-plus return**: 30–50% lower ICT energy use, closets decommissioned and **repurposed for instruction**, active-switch refresh cycles (5-7 years) replaced by passive splitters that don't need replacing, and simplified operations.

The scale is real. My North Dickinson feasibility work identified **\$6.95M in 10-year repair needs** for a single small district — roughly \$2.67M in HVAC and \$1.69M in electrical/power systems — precisely the systems that a converged ICET design lets you plan and pay for once. Multiply that by the **101,500 schools and 11,600 libraries** E-Rate serves, and the picture is clear: the nation's school buildings need to be rewired, and a list that only funds thin internal connections forces districts to defer the very modernization that would pay for itself.

There is also an equity and workforce return. Converged ICET buildings become **living laboratories** for CTE programs in energy, networking, and building systems — turning the infrastructure investment into a skills investment, consistent with the Compass principle that technology amplifies capacity rather than substituting for it.

## How E-Rate and the Universal Service Fund should be modernized

I deliberately use *modernize*, not *reform* — it aligns with the Commission's own framing in the NPRM and keeps the conversation about **fitness for the current era**, not retrenchment.

1. **Recognize ICET convergence in the ESL taxonomy.** Add explicit, named categories for structured fiber cabling, POLAN electronics/ONTs, PoE/FMPS converged power distribution, and the ICT layer of resilience/energy-integration systems. Where a component serves both the eligible network and a converged function, adopt clear **cost-allocation guidance** rather than blanket ineligibility.

2. **Create a capital modernization track distinct from the annual Category Two budget.** A \$201.57/student allowance cannot rewire a building. A lifecycle-based modernization category — evaluated on **10-year total cost of ownership and ROI** — would fund the physical layer at the scale and cadence it actually requires.

3. **Keep — and modernize — special construction and self-provisioned/dark fiber.** The NPRM questions whether these remain necessary given BEAD. For border, island, and rural regions like the Eastern Upper Peninsula, they remain essential; the answer is to **coordinate** E-Rate with BEAD and IRA energy incentives through fund stacking and utility partnerships, not to withdraw support.

4. **Make ROI and resilience explicit eligibility lenses.** Reward architectures that demonstrably lower long-run cost, cut energy use, and sustain emergency communications — the outcomes USF exists to advance.

5. **Modernize by outcomes, using the Compass frame.** Evaluate USF investments against Connectivity, Skills, Application, and Outcomes — so that "modern infrastructure" is measured by the human and institutional capacity it unlocks, not just megabits delivered.

## Bearing forward

The Commission is right that the original "get a signal to the door" mission is largely accomplished. The modern mission — the one the ESL has **not yet** caught up to — is to help the nation's schools **rewire the building itself** around converged information, communications, and energy technology, and to capture the decade-long return that convergence makes possible. Modernizing the Eligible Services List to name these technologies isn't an expansion of E-Rate's purpose. It's fidelity to it.
