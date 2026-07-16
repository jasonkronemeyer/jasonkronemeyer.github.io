---
layout: post
title: "Setting the Bearings: What E-Rate's FY2027 Eligible Services List Is Missing — and How to Modernize It for the ICET Era"
subtitle: "The frontier is no longer reaching the schoolhouse door. It's rebuilding what happens inside the walls."
author: "Jason Kronemeyer"
role: "Community Technologist, EUPConnect Collaborative"
series: "Project Compass"
type: "op-ed"
date: 2026-07-16
location: "Eastern Upper Peninsula, Michigan"
dockets:
  - "WC Docket No. 13-184 — Eligible Services List (Draft FY2027 ESL, DA 26-647, released June 30, 2026)"
  - "WC Docket No. 26-133 — Modernizing the E-Rate Program (NPRM/FNPRM, FCC 26-41)"
comment_deadline: "2026-07-30"
reply_comment_deadline: "2026-08-14"
call_to_action: >
  The comment window on the draft FY2027 ESL (DA 26-647) is open now — comments
  due July 30, 2026; reply comments August 14, 2026. File in WC Docket Nos.
  26-133 and 13-184.
tags:
  - E-Rate
  - Universal Service Fund
  - Eligible Services List
  - FY2027 ESL
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
  - Managed Internal Broadband Services
  - Network-as-a-Service
  - Section 11x(6) consolidation
  - 10-year return on investment
  - E-Rate modernization
summary: >
  A Compass-voice position paper arguing that the FCC's draft FY2027 Eligible
  Services List (DA 26-647) freezes the list exactly when it should be
  modernizing. The Bureau proposes no changes to eligible services and asks only
  how to narrow managed services — even though, for small and rural entities,
  the capacity to design, deploy, and manage a modern network is nearly
  impossible without exactly those services (Network-as-a-Service and Managed
  Internal Broadband Services). Meanwhile the converged information,
  communications, and energy technologies (ICET) that today's school buildings
  are actually rewired around remain unnamed. Drawing on the author's Section
  11x(6) school-infrastructure feasibility studies for North Dickinson County
  Schools and Sault Area Public Schools, the piece identifies those gaps,
  explains why naming them matters, and proposes how E-Rate and the Universal
  Service Fund should be modernized — not reformed — to fund the rewiring the
  nation's schools actually need. Comments are open through July 30, 2026.
word_count_target: 1600
status: draft
---

# Setting the Bearings: What E-Rate's FY2027 Eligible Services List Is Missing — and How to Modernize It for the ICET Era

*A Compass-voice position paper for Project Compass / EUPConnect Collaborative*
*By Jason Kronemeyer*

## True North: the list is being frozen exactly when it should be modernizing

On June 30, 2026, the FCC's Wireline Competition Bureau released the draft Eligible Services List for Funding Year 2027 (DA 26-647) and opened it for public comment through July 30, with reply comments due August 14. The headline is deceptively quiet: the Bureau proposes **no changes** to what E-Rate will fund. Category One and Category Two remain substantially unchanged from FY2026, and the only pointed questions the Bureau raises are about *narrowing* — whether Managed Internal Broadband Services (MIBS) stay cost-effective enough to remain eligible, and how to handle variable-priced Network-as-a-Service (NaaS) models.

Read that against the larger backdrop and the direction becomes clear. In the companion modernization proceeding (WC Docket 26-133, FCC 26-41), the Commission is asking whether E-Rate has outlived its mission, noting that virtually all schools now reach fiber broadband. But the Commission is reading the map upside down. The frontier is no longer *reaching* the building; it is **rebuilding what happens inside the building** once the signal arrives. Freezing the eligible list — and questioning only whether to shrink it — is precisely the wrong bearing for this moment.

The Eligible Services List still sorts the world into Category One (data transmission and Internet access — leased lit fiber, dark fiber, self-provisioned networks) and Category Two (internal connections, managed internal broadband, and basic maintenance — routers, switches, access points, and cabling). That taxonomy quietly assumes that "inside the walls" is a light lift — a few switches and access points sized to a modest per-student budget. The FY2026-2030 Category Two budget is set at just $201.57 per student (floor $30,175; $66,385 for Tribal libraries). Across the Section 11x(6) school-infrastructure feasibility studies I've completed — from the smallest rural districts to full multi-building campuses — that figure doesn't come close to what a modern building actually needs, because the modern building is no longer a network with lights; it is a **converged information, communications, and energy system**.

The list is not wrong. It is simply **not yet modern**. And modernization — the FCC's own word in the companion NPRM — should mean aligning the list with the architecture that today's buildings are actually being designed and rewired around, not holding it static while asking only what to cut.

This is not an abstract policy timing problem. School districts across Michigan and the country are entering a capital cycle where deferred maintenance, bond refinancing, facility consolidation, and electrification pressures are converging — the same "maturity wall" that school facilities planners now describe. Most of the school buildings that will exist in 2050 already exist today; they were built or last modernized between the 1960s and 1990s, designed around analog systems, and engineered without the need for high-capacity data networks. They do not fail overnight; they fall behind until they cannot catch up. The FY2027 ESL will shape what districts can fund during that window. Freezing it now means locking in a list that treats the building as an afterthought just when the building itself is becoming the frontier — and just when the cost of delay is becoming visible in capital planning, energy use, and instructional capacity.

## What's missing from the FY2027 Eligible Services List

Every gap below traces directly to the ICET convergence work in my studies. These are the categories that a modernized ESL should name explicitly rather than leave to case-by-case eligibility fights during PIA review — and every one of them is absent from the FY2027 draft.

### 1. Whole-building structured fiber cabling as a fundable modernization, not a capped afterthought

Cabling is technically eligible under Category Two, but the $201.57/student budget was never scaled to **rewire a building**. Many of the nation's school buildings are on aging Cat5e/Cat6 copper in distributed closets that are themselves failure points and cost centers. A small building rewire runs on the order of **$120,000–$150,000** in cabling alone; a medium-sized building runs **$150,000–$750,000**; and a large building can run **$750,000–$2 million**. The ESL should recognize a **structured fiber cabling / premise re-cabling** modernization track so that the physical layer — the thing with a 20-30 year lifecycle — is fundable at the scale it actually requires.

### 2. Passive Optical LAN (POLAN) as a named architecture

POLAN — fiber to passive splitters to optical network terminals — is the single most consequential architecture missing by name from the list. It replaces power-hungry closet switches with passive splitters and a centralized optical line terminal, and pairs naturally with converged power such as Fault-Managed Power Systems (FMPS). Independent, real-world evidence points consistently in one direction: an APOLAN cost study found POLAN 40–56% cheaper across scenarios from a single building to a multi-building campus, and White Plains School District reported an initial network build roughly 30% lower after replacing legacy switches across nine buildings with POLAN. Today, ONTs are only grudgingly eligible as Category One when carrier-owned; a modernized ESL should treat POLAN electronics, splitters, and ONTs as first-class eligible internal infrastructure.

### 3. Converged power: Power-over-Ethernet and Fault-Managed Power Systems

The modern network *is* the power distribution system. PoE now drives lighting, sensors, displays, access control, and IP audio; DC Fault-Managed Power Systems (FMPS), or Class 4 power distribution, extend that convergence safely from a centralized power node. My North Dickinson study is built around exactly this architecture — a single central network and power location feeding the building over a hybrid fiber-and-copper backbone that supports Class 4 fault-managed power. A PoE lighting retrofit at one middle school used **30% fewer fixtures** and could be installed by the IT cabling team rather than licensed electricians on every run. Yet the ESL and its ineligible list still treat "electrical infrastructure" and anything "servicing only ineligible items" as off-limits. That boundary is an artifact of a pre-convergence era.

### 4. Energy-integration and resilience controls (smart microgrids, DERs)

A fiber-rich campus is the control plane for solar-plus-storage microgrids, load tiering, and grid-enabled buildings — the systems that keep communications, security, and emergency instruction alive during outages, in some documented cases for **up to 96 hours in island mode**. The ESL has no vocabulary for the ICT side of this resilience layer, even though it is inseparable from the broadband network it rides on.

### 5. The integrated safety and emergency-communications fabric

Districts are converging PA, intercom, E911, panic initiation, and mass notification onto the IP network. In my North Dickinson work, this convergence was not a luxury — it was the reason the district engaged at all, since it was the only district in its ISD not yet integrated into shared emergency notification and badge-access systems. Much of this fabric is stranded as "ineligible" because it touches safety systems, even though it is delivered over — and depends entirely on — the eligible internal network.

## Why this matters: the 10-year return the current list leaves on the table

The strongest modernization argument is fiscal, and it is one the FCC should welcome — especially as it professes concern in the FY2027 notice about cost-effectiveness. When a building is re-architected around converged fiber/POLAN rather than patched copper, the district captures a **10-year-plus return**: 30–50% lower ICT energy use, closets decommissioned and **repurposed for instruction**, active-switch refresh cycles (5-7 years) replaced by passive splitters that don't need replacing, and simplified operations.

The scale is real, and it holds across very different districts. My Section 11x(6) feasibility work for **North Dickinson County Schools** — a small, rural district consolidating shared services with the Dickinson-Iron ISD on a $108,394 grant — identified **$6.95M in 10-year repair needs**, roughly $2.67M in HVAC and $1.69M in electrical/power systems: precisely the systems a converged ICET design lets you plan and pay for once. At the other end of the spectrum, my 11x(6) consolidation Master Plan for **Sault Area Public Schools** positions that larger, multi-building district to pursue on the order of **$32.5M** in state consolidation funding — grounded in the 2025 State Facilities Study repair estimates, facility dispossession, and the case for consolidating into modern, converged campuses. Two districts, two scales, one lesson: the building itself is the frontier, and the returns compound whether you are retiring four data closets or several aging schools.

Multiply that by the **101,500 schools and 11,600 libraries** E-Rate serves, and the picture is clear: the nation's school buildings need to be rewired, and a list that only funds thin internal connections — and now proposes to freeze even that — forces districts to defer the very modernization that would pay for itself.

There is also an equity and workforce return. Converged ICET buildings become **living laboratories** for CTE programs in energy, networking, and building systems — turning the infrastructure investment into a skills investment, consistent with the Compass principle that technology amplifies capacity rather than substituting for it.

## The small-entity reality: managed services are the on-ramp, not the loophole

Here is where the FY2027 draft gets its priorities backward. For a small, rural district or library — the kind that fills the Eastern Upper Peninsula, and the kind North Dickinson represents — the capacity to **design, deploy, and manage** a modern converged network is nearly impossible in-house. These entities do not have a CCIE on staff, a network operations center, or a facilities engineer who also happens to understand optical LAN, PoE lighting, and fault-managed power. The technical talent that a modern ICET building demands is exactly the talent that is scarcest in the places E-Rate exists to serve.

That is precisely why **Managed Internal Broadband Services (MIBS)** and **Network-as-a-Service (NaaS)** matter. They are not a cost-control problem to be regulated down; they are the **on-ramp** that lets a district with two IT generalists operate infrastructure it could never design, staff, or maintain alone. A managed model converts an impossible capital-and-talent lift into a predictable operating relationship — bringing enterprise-grade architecture, monitoring, and lifecycle management within reach of the smallest entity. It is also how small districts capture the consortium and shared-services efficiencies that make consolidation viable in the first place.

So when the Bureau spends its FY2027 question time asking whether MIBS should remain eligible, whether it should be capped by applicant size, or whether reimbursement should be nickel-and-dimed to hours worked, it is aiming the scrutiny at the wrong target — and at the wrong entities. Limiting MIBS "by applicant size" would fall hardest on the small applicants who depend on it most. The same logic applies to NaaS: because the FCC forms are built around a fixed monthly cost, the answer is to **modernize the forms** to accommodate variable, usage-based pricing — not to strand the districts that can only afford infrastructure as a service. Cost-effectiveness for a small entity is not the lowest line item; it is the ability to run a modern network at all.

## How E-Rate and the Universal Service Fund should be modernized

I deliberately use *modernize*, not *reform* — it aligns with the Commission's own framing in the NPRM and keeps the conversation about **fitness for the current era**, not retrenchment.

1. **Recognize ICET convergence in the ESL taxonomy.** Add explicit, named categories for structured fiber cabling, POLAN electronics/ONTs, PoE/FMPS (Class 4) converged power distribution, and the ICT layer of resilience/energy-integration systems. Where a component serves both the eligible network and a converged function, adopt clear **cost-allocation guidance** rather than blanket ineligibility.

2. **Create a capital modernization track distinct from the annual Category Two budget.** A $201.57/student allowance cannot rewire a building. A lifecycle-based modernization category — evaluated on **10-year total cost of ownership and ROI** — would fund the physical layer at the scale and cadence it actually requires, and would let E-Rate stack cleanly with state consolidation funding like Michigan's Section 11x/12e programs rather than working at cross purposes with it.

3. **Protect MIBS and NaaS as the small-entity on-ramp, and answer the cost questions with a convergence lens.** The FY2027 draft's real energy goes into whether managed and usage-based services are cost-effective, whether MIBS should be capped by applicant size, and how to handle variable NaaS pricing. But for small and rural entities, these services are the only realistic way to design, deploy, and manage a modern converged network — capping or shrinking them would fall hardest on the applicants who depend on them most. The right answer isn't to narrow these models; it is to (a) **modernize FCC Forms 470 and 471** to accommodate variable, usage-based pricing rather than penalizing it, and (b) require that managed-service and NaaS bids be evaluated against **lifecycle-owned converged infrastructure** — making cost-effectiveness a comparison of architectures and of realistic in-house capacity, not a reason to strand small entities.

4. **Keep — and modernize — special construction and self-provisioned/dark fiber.** The NPRM questions whether these remain necessary given BEAD. For border, island, and rural regions like the Eastern Upper Peninsula, they remain essential; the answer is to **coordinate** E-Rate with BEAD and IRA energy incentives through fund stacking and utility partnerships, not to withdraw support.

5. **Modernize by outcomes, using the Compass frame.** Evaluate USF investments against Connectivity, Skills, Application, and Outcomes — so that "modern infrastructure" is measured by the human and institutional capacity it unlocks, not just megabits delivered.

## Bearing forward

The Commission is right that the original "get a signal to the door" mission is largely accomplished. The modern mission — the one the draft FY2027 list has **not yet** caught up to — is to help the nation's schools **rewire the building itself** around converged information, communications, and energy technology, and to capture the decade-long return that convergence makes possible. Across a small rural district like North Dickinson and a full multi-building system like Sault Area Public Schools, the finding is the same. Modernizing the Eligible Services List to name these technologies isn't an expansion of E-Rate's purpose. It's fidelity to it.

The window is open now. Comments on the draft FY2027 ESL (DA 26-647) are due July 30, 2026, with reply comments due August 14, filed in WC Docket Nos. 26-133 and 13-184. If the list is going to be revisited this year anyway, let's make sure it's pointed toward True North.

---

**Related reading:**

- [The School Building Reckoning](https://www.jasonkronemeyer.com/compass%20series/infrastructure/schools/digital%20opportunity/2026/06/23/fmp-michigan-school-infrastructure.html) — on the capital cycle, the retrofit imperative, and why the buildings we inherited were never designed for the digital systems they are now expected to carry.
- [WCB Seeks Comment on E-Rate Eligible Services List for FY 2027](https://www.fcc.gov/document/wcb-seeks-comment-e-rate-eligible-services-list-fy-2027) — FCC public notice releasing the draft FY2027 ESL (DA 26-647) and opening the comment window.
- [FCC ECFS: WC Docket No. 13-184 — Modernizing the E-rate Program for Schools and Libraries](https://www.fcc.gov/ecfs/search/search-filings?dockets=13-184) — official docket for the Eligible Services List and E-Rate program.
- [FCC ECFS: WC Docket No. 26-133 — Ensuring Children's Safe Use of Screens and E-Rate-Funded Services](https://www.fcc.gov/ecfs/search/search-filings?dockets=26-133) — official docket for the E-Rate modernization proceeding.
- [FCC Fact Sheet: Ensuring Children's Safe Use of Screens and E-Rate-Funded Services / Modernizing the E-Rate Program (June 4, 2026)](https://docs.fcc.gov/public/attachments/DOC-422168A1.pdf) — PDF summary of the NPRM/FNPRM in WC Docket Nos. 26-133, 13-184, 21-93, and 21-455.
