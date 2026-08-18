---
layout: post
title: "Why the Building Itself Is the Next Frontier: The Case for POLAN and Fault-Managed Power"
subtitle: "The network stopped being a data pipe with lights attached. It became the power system. Here is why that matters for schools and the communities they anchor."
author: "Jason Kronemeyer"
role: "Community Technologist, EUPConnect Collaborative"
series: "Project Compass"
type: "essay"
date: 2026-08-17
location: "Eastern Upper Peninsula, Michigan"
tags:
  - Project Compass
  - POLAN
  - Fault-Managed Power Systems
  - Class 4 power
  - converged infrastructure
  - smart buildings
  - school modernization
  - digital opportunity
keywords:
  - Passive Optical LAN
  - Power over Ethernet
  - NEC Article 726
  - UL 1400-1
  - converged information communications and energy technologies
---

For most of a generation, the story of connectivity was a story about *arrival*. The frontier was the schoolhouse door, and the goal was to get a fast enough signal across it. That frontier has largely been settled. Fiber now reaches nearly every school in the country. And so the interesting question has quietly moved indoors, from the property line to the wiring in the walls. **The building itself is the next frontier**, and two technologies are redrawing its map: Passive Optical LAN and Fault-Managed Power Systems.

They sound like plumbing. They are closer to a change in worldview. The old model treated a building as a data network with an electrical system bolted alongside it, each on its own budget, its own crew, its own closet. The converged model treats the two as one thing. *In a converged building, the network is also the power distribution system.* Once you see a school that way, the reasons to care become hard to unsee.

## Rethinking the network

Start with **POLAN**, or Passive Optical LAN. The name hides an elegant idea. Instead of stacking powered switches in a telecom closet on every floor and hall, a single optical line terminal at the core sends light down a strand of glass to *passive* splitters, which fan the signal out to the classrooms. Passive is the operative word. Those splitters need **no power, no cooling, no software updates, and no maintenance visits**, and a single fiber can reach up to *20 kilometers, roughly 12 miles*, from that central point. One district, or a whole campus, can run on electronics housed in a single location.

The reason to care is partly, bluntly, *money*. The independent evidence is remarkably consistent. The Association for Passive Optical LAN found POLAN **40 to 56 percent less expensive** than traditional category-cabled networks across scenarios ranging from a single four-story building to a four-building campus. Industry analyses point to total cost of ownership as much as **50 percent lower** over five years. And this is not a laboratory number. White Plains School District reported its initial network build came in **roughly 30 percent lower** after it replaced legacy switching across nine buildings with POLAN.

But the deeper reason to care is what POLAN *frees up*. When the closets full of switches disappear, so do the recurring costs that came with them: the power, the air conditioning, the rip-and-replace cabling cycle every five to seven years. The reclaimed rooms become storage, or small-group instruction space, or simply stop being points of failure. One fiber backbone can carry **data, voice, video surveillance, building automation, Wi-Fi, and even public-safety radio** at once, replacing a tangle of separate systems with a single, encrypted, long-lived spine. In a small rural district, that consolidation is not a luxury. It is the difference between an infrastructure a lean staff can actually manage and one that quietly manages them.

## Rethinking the power

Now the second half of the map, and the part most people have never heard of. **Fault-Managed Power Systems**, formally *Class 4 power*, are the first genuinely new category of electrical power the code has recognized in decades. This is not a vendor's marketing term or an experiment. It was written into the **2023 National Electrical Code as new Article 726**, and it is governed by real safety standards, **UL 1400-1** for the systems and **UL 1400-2** for the cable. When the National Fire Protection Association gives something its own article, the industry is telling you it intends to build on it.

What makes Class 4 remarkable is *how* it stays safe. Traditional wiring limits danger by capping how much power the source can push. Fault-managed power does the opposite. It sends energy in continuously monitored packets and watches the circuit in real time. The instant it detects a short, an arc, a damaged cable, or a human hand, it **shuts the power off within milliseconds**, before harm can occur. The conductor is, in effect, *touch-safe*. You get the reach and strength of real power distribution with a shock-and-fire profile closer to a low-voltage doorbell circuit.

That safety unlocks reach that Power over Ethernet simply cannot match. PoE, the workhorse behind our cameras and access points, tops out near **90 watts over 100 meters** and delivers only about 71 watts at that full distance. Fault-managed power, by validated contrast, pushes **hundreds of watts per copper pair over more than a kilometer**, with the underlying technology rated for far higher loads still. And because the code treats touch-safe Class 4 cable more like signal wiring than branch-circuit power, it usually **needs no conduit** and can be pulled in the same pathway as the fiber.

The consequences show up on real job sites. In one 20-location security deployment, combining fault-managed power and fiber in a single pathway produced **51 percent material savings, 42 percent labor savings, and a 78 percent reduction in maintenance**, largely by eliminating conduit and distributed backup units. My own **North Dickinson** feasibility work found the same logic in a school. A Power-over-Ethernet lighting retrofit at one middle school used **30 percent fewer fixtures** and, tellingly, *could be installed by the IT cabling team rather than requiring licensed electricians on every run*. When the people who already manage your network can also deploy your power, the economics of modernization change for a small district in a way that is easy to underestimate.

## Why they matter together

Here is the part worth slowing down for, because it is the whole point. POLAN and fault-managed power are not two upgrades. They are *two halves of one idea*, though they work at *different scales*. Fiber can carry data astonishing distances, up to *20 kilometers* from the core, which lets a single optical terminal serve an entire district. Class 4 power reaches a shorter but still transformative range, roughly *one to two kilometers*, far enough to cover a building or a campus from a centralized node. The point is not that power travels as far as light. It is that within the footprint of a school or campus, **the two can share a single pathway and a single origin**, with fiber extending data outward for miles and fault-managed power energizing the edge over that same hybrid backbone. Put them together and you get a building with **one place where the data and the power both begin**, feeding intelligent devices over one converged fiber-and-copper spine.

That converged spine is what makes everything downstream possible: PoE lighting and sensors and displays, access control and IP audio, and eventually the solar-plus-storage and grid-enabled resilience that keeps a school's communications and emergency systems alive during an outage. It is also, not incidentally, the physical foundation for edge computing and the data-rich, community-serving campus that so much of the **Project Compass** work imagines. You cannot build a smart, resilient, community-anchoring building on a network and a power system that don't know each other exist.

So why should people care about fault-managed power and POLAN? Because the return is measured in *decades, not budget cycles*. Because a converged building is a safer building, a cheaper building to run, and a building whose reclaimed space and spare capacity can be turned back toward students and community. And because our public funding programs, from E-Rate on down, still describe school infrastructure in a vocabulary written for a pre-convergence world. **Naming these technologies is the first step to funding them.** The frontier moved indoors. It is time our maps caught up.

---

## What these ideas are based on

**Passive Optical LAN, cost and architecture**
- Association for Passive Optical LAN (APOLAN), *Passive Optical LAN Cost Comparison* study, finding 40% savings for a four-story building, 55% for a seven-story building, and 56% for a four-building campus.
- eSchool News, "Optical LAN: The silent hero of modern learning" (2025), citing up to 50% lower five-year total cost of ownership versus traditional LAN.
- White Plains School District POLAN deployment, ~30% lower initial network build across nine buildings (referenced in author's FY2027 E-Rate ESL comments).
- Tellabs, *Saving K-12 Schools Money with Optical LAN*, on passive splitters, IDF elimination, and up-to-20 km reach.
- Author's North Dickinson County Schools Section 11x(6) feasibility study, POLAN technical architecture (OLT, splitters, ONTs, PoE+ over Category 6a).

**Fault-Managed Power / Class 4**
- National Electrical Code (NFPA 70), 2023 edition, **Article 726, Class 4 Fault-Managed Power Systems**.
- UL 1400-1 (fault-managed power systems) and UL 1400-2 (Class 4 cable) safety standards.
- Panduit, *Fault Managed Power Systems Technology Brief*, on NEC power classes and Class 4 characteristics.
- Cisco / Panduit, *FMPS and Cisco Implementation Guide*, on delivering hundreds of watts per pair over distances exceeding 1 km.
- NECA / VoltServer, *Intro to Class 4 Fault-Managed Power Systems*, on PoE limits (90W / 100m, ~71W at max distance with Cat6A) and FMPS reach.
- Electrical Contractor Magazine and Low Voltage Nation overviews of Article 726, packet energy transfer, and touch-safe operation.
- Panduit government-facility case study: 51% material, 42% labor, and 78% maintenance savings from combined fiber-and-Class-4 pathways.

**The converged-building argument**
- Author's Comments on the Draft FY2027 Eligible Services List and E-Rate Modernization (WC Docket Nos. 26-133 and 13-184), Section III, "What the Eligible Services List Fails to Name."
- Author's North Dickinson County Schools feasibility work: PoE lighting retrofit using 30% fewer fixtures, installable by IT cabling staff; single central network-and-power node over a hybrid fiber-and-copper backbone.

*Project Compass is a series on building digital opportunity in rural communities. DOIN and the converged-infrastructure framing here build on ideas developed in the author's E-Rate and school-modernization work.*
