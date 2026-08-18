---
layout: post
title: "The Building Itself: A Candid Case for Converged Networks and Power"
subtitle: "Optical LAN and fault-managed power can reshape how a school is wired, and where the money goes. But the honest version of this story includes the conditions under which it doesn't pencil out."
author: "Jason Kronemeyer"
role: "Community Technologist, EUPConnect Collaborative"
type: "op-ed"
date: 2026-08-17
location: "Eastern Upper Peninsula, Michigan"
tags:
  - Passive Optical LAN
  - Fault-Managed Power Systems
  - Class 4 power
  - converged infrastructure
  - school modernization
  - digital opportunity
keywords:
  - Optical LAN
  - Power over Ethernet
  - NEC Article 726
  - UL 1400
  - converged information and energy infrastructure
---

For most of a generation, the story of connectivity was a story about *arrival*. The frontier was the schoolhouse door, and the goal was to get a fast enough signal across it. That frontier has largely been settled. Fiber now reaches nearly every school in the country. And so the interesting question has quietly moved indoors, from the property line to the wiring in the walls.

Two shifts are redrawing the map inside the building. **Passive Optical LAN** changes how the network is built. **Fault-managed power**, now recognized in code as *Class 4*, changes how power is delivered. Together they suggest a different way of thinking about a school: not as a data network with an electrical system bolted alongside it, but as one converged system. That idea is worth taking seriously. It is also worth taking *skeptically*, because the most useful thing anyone can do with a promising technology is describe not only when it works, but when it doesn't.

## Rethinking the network

Passive Optical LAN, or POLAN, rests on an elegant idea. Instead of stacking powered switches in a telecom closet on every floor, a single optical line terminal at the core sends light down a strand of glass to *passive* splitters, which fan the signal out to classrooms. Passive is the operative word. Those splitters need **no power, no cooling, and no software updates**, and fiber can reach many kilometers from that central point. A whole campus can run on electronics housed in one location.

The mechanism behind the savings is easy to state and hard to argue with: a converged optical design **reduces the number of powered network closets a district must build, staff, cool, and eventually replace**. Fewer distributed active electronics means less recurring cost, less heat, and fewer points of failure to chase. That is a structural property of the architecture, not a claim about any one building.

The dollar figures are where honesty matters most. Published cost studies and district reports generally point toward savings, but most originate with vendors or the industry's trade association and should be read with that interest in mind. The reasonable synthesis is directional, not precise: **optical LAN can lower first-cost and recurring cost** in the right building, largely by eliminating distributed active electronics, but *the exact figure depends entirely on the building, the labor market, and the replacement timeline*. Anyone quoting you a single confident percentage is selling something.

## Rethinking the power

Fault-managed power, formally *Class 4*, is the first genuinely new category of electrical power the code has recognized in decades. This is not a marketing term. It was written into the **2023 National Electrical Code as new Article 726**, and it is governed by safety standards **UL 1400-1** for systems and **UL 1400-2** for cable. When the National Fire Protection Association gives a technology its own article, it signals an intent to build on it.

What makes Class 4 notable is *how* it stays safe. Traditional wiring limits danger by capping how much power the source can push. Fault-managed power instead sends energy in continuously monitored packets and watches the circuit in real time, shutting off **within milliseconds** when it detects trouble. The conductor is, in effect, touch-safe. That safety unlocks reach ordinary low-voltage cabling cannot match: fault-managed power can deliver **hundreds of watts over more than a kilometer**, well beyond the roughly 90 watts and 100 meters that Power over Ethernet allows.

That touch-safe promise is not a marketing claim. It is earned by the transmitter's ability to detect and interrupt specific fault conditions before harmful energy can transfer. Industry summaries of the UL 1400-1 and Article 726 requirements generally group these into **six fault conditions a Class 4 system must catch**:

1. **Short circuit / overcurrent** — a sudden, abnormal surge in current.
2. **Ground fault (line-to-ground)** — current leaking to ground, a shock and fire risk.
3. **Line-to-line fault** — an unintended connection between conductors.
4. **Arc fault** — the characteristic electrical signature of an arc.
5. **Human contact (touch fault)** — the impedance change of a person contacting a conductor.
6. **Cable damage or faulty wiring** — changes in the line's electrical characteristics from a cut, crush, or degraded run.

*A note of precision: the standards do not publish these as a single tidy numbered list, and authoritative sources group them slightly differently (some collapse line-to-line and ground faults, others add component failure of the transmitter or receiver itself). The point is not the exact count but the principle: the system's safety case rests on continuously testing every energy packet against a defined set of fault signatures and refusing to transmit when any one is present.*

A related efficiency claim circulates in the market and is worth citing carefully rather than adopting at face value. A manufacturer study has reported that a Power-over-Ethernet lighting design can use roughly **30 percent fewer fixtures** than a conventional layout, in part because networked luminaires can be zoned and controlled more granularly. That figure is a *manufacturer's result, not an independent finding*, and belongs in the same directional, read-with-interest category as any other vendor number. The general and better-established point stands on its own: because touch-safe PoE and Class 4 cabling are treated more like signal wiring than branch-circuit power, they can often be installed by the technology cabling team rather than requiring licensed electricians on every run, which changes the labor math for a small district.

## A signal to the optical equipment makers

If the converged building is where this is headed, then fault-managed power is a signal, and the manufacturers of optical networking equipment should read it. Here is the argument, offered as an informed inference rather than a settled fact.

Today's optical network terminals, the endpoints that sit in the classroom and hand off Ethernet to devices, were largely designed for a *data-first* world. Their power budgets and their Power-over-Ethernet capabilities are often modest, sized for a phone and an access point. But in a converged building, that same endpoint is being asked to feed lighting, cameras, displays, sensors, and access control. The endpoint is becoming a *local power distribution point*, not just a data drop.

That shift argues for a new generation of optical network terminals built deliberately for smart buildings: **endpoints with larger aggregate power budgets, more powered ports, and the intelligence to negotiate and deliver the full range of PoE standards, port by port**. An ONT should be able to serve a 15-watt sensor on one port and a 90-watt display on the next, sensing each device's class and modulating delivery accordingly, all fed upstream by fault-managed power that carries the energy the long distance from a central node. In effect, the optical endpoint becomes the graceful handoff between Class 4 power on the backbone and Class 2 PoE at the edge.

This is where I think the market should go, and I would encourage the optical equipment makers to build toward it. It is also fair to name the caveat: this is a direction of travel, not a shipping product line, and standards for how fault-managed power and optical endpoints interoperate cleanly are still maturing. Districts should ask for a roadmap, not assume one exists.

## Where this doesn't pencil out

An argument that cannot describe its own limits is a pitch, not an analysis. Here is where a district should slow down or say no.

**We do not yet have a built proof of concept.** This is the honest heart of the matter. The convergence case rests today on standards, design logic, and projections, not on a measured demonstration site. What communities need now is a district willing to build a converged pilot and an independent, ideally peer-reviewed, evaluation of what it actually costs, saves, and requires to operate. Until then, we are reasoning from design and code, not from measured outcomes, and we should say so.

**Vendor concentration is a real dependency.** Optical LAN, in particular, tends to be a *single-vendor ecosystem*: the terminals, the endpoints, and the management software often do not interoperate across manufacturers. For a district making a twenty-year infrastructure decision, that is a strategic risk worth naming out loud. Ask hard questions about open standards, second-source availability, and what happens to support if a vendor exits the market.

**Class 4 is young, and the workforce is younger.** Article 726 dates only to 2023. The installed base is thin, and in rural regions especially, contractors who have actually *worked with* fault-managed power may be scarce. The advantage that technology staff can pull touch-safe cabling is real, but it also raises questions of liability, inspection, and code familiarity when a novel power system is energized in an occupied school. Do not treat immaturity as a detail.

**Centralization concentrates risk.** Collapsing distributed closets into a single network-and-power node is efficient, but it also creates a more consequential point of failure. That is manageable with redundancy, backup power, and disciplined design, but it is a cost and a responsibility, not a free byproduct of convergence.

**And sometimes the old way is simply right.** A building already slated for replacement, a district with ample in-house electrical labor, or a site with no local Class 4 expertise may be better served by conventional switching and standard power. Convergence is a strong default in *new construction and deep renovation*. It is a weaker case as a mid-life retrofit.

## Why it still matters

With those caveats honestly on the table, the core idea holds. POLAN and fault-managed power work at *different scales*, fiber reaching many kilometers to carry data across a district, Class 4 reaching a shorter one-to-two-kilometer range to energize the edge, but *within the footprint of a school or campus they can share a single pathway and a single origin*. That convergence is what makes a genuinely modern building possible: lighting, sensors, access control, and communications fed from one place, over one backbone, with power and data managed as a single system.

The moment to act on this is specific. A district opening its walls for a consolidation or a major renovation faces exactly the decision point where convergence deserves serious study, because the backbone is being chosen and a converged design is far cheaper to build in now than to retrofit later. For that district, this is a foundation worth studying seriously, and if the projections hold, the return would be measured in *decades, not budget cycles*. Whether they hold is precisely what a demonstration site would tell us.

The policy point survives the skepticism too, though it needs stating precisely. Our public funding programs still describe school infrastructure in a vocabulary written for a pre-convergence world. Naming converged technologies in something like the E-Rate Eligible Services List will not, and should not, guarantee funding. But eligibility frameworks that cannot even *name* a technology cannot evaluate it on cost-effectiveness or subject it to competitive bidding. **The first step is not funding. It is recognition, followed by honest scrutiny.** That is a standard convergence should have to meet, not evade.

The frontier moved indoors. Our maps should follow, with eyes open.

---

## What these ideas are based on

**Standards and code (independent)**
- National Electrical Code (NFPA 70), 2023 edition, Article 726, Class 4 Fault-Managed Power Systems, and Article 100 definition of Fault-Managed Power.
- UL 1400-1 (fault-managed power systems / equipment) and UL 1400-2 (Class 4 cable) safety requirements.
- UL Solutions and ATIS technical summaries of UL 1400-1, describing the monitored fault categories (short circuit, ground fault, arcing fault, touch fault, and faulty wiring) and packet-based fault testing.
- IEEE 802.3 Power over Ethernet standards, for the ~90W / 100m comparison baseline and the PoE classes an optical endpoint would negotiate.

**Industry and vendor material (directional, read with interest in mind)**
- Manufacturer study reporting a ~30% reduction in fixtures for a Power-over-Ethernet lighting design. Cited as a vendor result, not an independent finding. *[Add exact manufacturer and title.]*
- Association for Passive Optical LAN (APOLAN) cost-comparison studies, cited as directional rather than definitive because the association exists to promote the technology.
- Other manufacturer technology briefs and case studies on optical LAN and fault-managed power, useful for mechanism and range but subject to selection bias.

*A note on sourcing: much of the published cost and efficiency evidence for these technologies originates with vendors or their trade association, and is flagged as directional here. This op-ed argues from independent standards and code, and from the engineering properties of the two technologies, rather than from any single built or peer-reviewed deployment. The six-fault list is an industry synthesis of the UL 1400-1 / Article 726 requirements, not a verbatim clause. The argument about next-generation optical network terminals is the author's forward-looking inference. Readers weighing a real decision should seek independent references and, ideally, a demonstration site with an independent evaluation.*
