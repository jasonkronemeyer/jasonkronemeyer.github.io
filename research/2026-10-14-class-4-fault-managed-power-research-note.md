# Research Note: From “Digital Electricity” to Class 4 Fault-Managed Power

**Updated October 14, 2026**

## Research question

How have the capabilities originally promoted as the “Advantages of Digital Electricity” changed as the technology moved from a proprietary remote-power solution into the standards-based category now known as **Class 4 Fault-Managed Power Systems**, or FMPS?

## Summary finding

The early Belden and VoltServer Digital Electricity value proposition has largely survived: safe remote power, longer reach than Power over Ethernet, reduced dependence on conventional branch-circuit infrastructure, centralized backup, operational monitoring, and flexible deployment. What has changed is the **technical and regulatory foundation beneath those claims**.

In 2018, Digital Electricity was explained primarily as a proprietary packetized-power technology and evaluated through telecommunications and ICT equipment safety standards. By 2022–2023, fault-managed power had acquired dedicated equipment and cable requirements under UL 1400-1 and UL 1400-2, along with recognition as Class 4 under NEC Article 726. By 2026, the field had advanced again through changes in the 2026 NEC, continuing standards work, broader application development, and publication of NECA 726-2026, an installation, commissioning, documentation, and maintenance standard.

> Digital Electricity began as a particular vendor’s implementation of intelligent remote power. Class 4 FMPS is now the larger, technology-neutral category within which packetized, pulsed, continuous-DC, AC, and combined-waveform systems may be evaluated.

UL Solutions describes Class 4 systems in technology-neutral terms: the system monitors its circuit for faults and controls power so that energy delivered into a fault remains limited. Its requirements are not restricted to packetized power or to a single vendor’s implementation.

## 1. Safety: from voltage limitation to active fault-energy management

### Original claim

The original material described Digital Electricity as “safe power where, when, and how you need it,” citing RFT-V classification under IEC 60950-1, IEC 60950-21, and IEC 62368-1 and recognition as a Limited Power Source under NEC Article 830.

### What changed

The present code framework does not define Class 4 primarily by calling it low voltage, limited power, or telecommunications power. It defines the category by **what happens during a fault**.

UL 1400-1 states that fault-managed systems monitor the circuit for faults and control transmitted power to limit the energy delivered into a fault. Unlike Class 2 and Class 3 systems, Class 4 systems are not necessarily power-limited at the source during normal operation. Their protection is based on limiting shock and fire risk between the Class 4 transmitter and receiver.

Eaton explains that a typical pulsed-DC implementation analyzes each pulse for short circuits, overcurrent conditions, line-to-line faults, line-to-ground faults, component failures, and other conditions that could present a fire or shock risk. When an unacceptable condition is detected, the transmitter stops sending power.

NECA 726-2026 similarly describes a continuously monitored circuit in which the transmitter stops power flow within milliseconds following detected contact, faults, or other abnormal conditions, thereby limiting fault energy and reducing fire and electric-shock risks.

### Updated research statement

**Class 4 FMPS achieves its distinctive safety characteristics through active monitoring and fault-energy limitation, not merely through a low source-power ceiling.** The system can deliver substantial normal operating power while limiting the energy that reaches a detected fault.

This wording is more accurate than calling all Class 4 circuits “low voltage” or “inherently safe.” Safety depends on the performance and listing of the complete system, including the transmitter, receiver, cabling, control logic, and associated utilization equipment.

## 2. Standards: from ICT equipment certification to a dedicated FMPS framework

The publication of the first issue of UL 1400-1 on December 19, 2022, established dedicated safety requirements for fault-managed equipment. The outline applies to Class 4 equipment and circuits installed under NEC Article 726 and also requires compliance with applicable portions of UL 62368-1.

UL Solutions reported the first certification of a Class 4 distribution system to UL 1400-1 in November 2023. A March 2025 UL Solutions update reported three completed UL 1400-1 certifications and ten UL 1400-2 cable certifications. It also identified continuing work on a second issue of UL 1400-1 and noted that the July 2023 issue of UL 1400-2 added requirements for CL4Z outdoor cables.

The standards history can be summarized as follows:

1. **Pre-Class 4 period:** proprietary systems evaluated through existing ICT, remote-feeding, and equipment-safety frameworks.
2. **2020–2022:** development and publication of UL 1400-1 requirements for systems and equipment.
3. **2023:** NEC Article 726 formally recognizes Class 4 circuits; UL 1400-2 adds cable requirements, including CL4Z outdoor cable provisions.
4. **2023–2025:** first system certifications and a growing number of cable certifications.
5. **2026:** publication of NECA 726-2026, providing an installation and workmanship framework covering transmitters, receivers, Class 4 cabling, labeling, programming, commissioning, documentation, and maintenance.

## 3. Wiring and pathways: from “communications wiring methods” to a listed system

FMPS can support less-intensive wiring arrangements than conventional Class 1 distribution. However, the older “no conduit” wording should not be interpreted as permission to use any ordinary communications cable or to omit pathway, separation, support, firestopping, grounding, labeling, or local licensing requirements.

**Class 4 FMPS can use limited-energy-style pathways and cabling practices in qualifying installations, but it must be treated as a listed system rather than as an arbitrary combination of power equipment and standard communications cable.**

Project requirements remain dependent on the system listing, the cable’s Class 4 designation and environmental rating, adopted NEC provisions, building and fire codes, manufacturer instructions, and authority-having-jurisdiction interpretations. “No conduit” is therefore a potential design advantage, not a universal condition.

## 4. Power and distance: the “20 times PoE” proposition

Belden’s 2018 explanation said that contemporary PoE could supply up to 100 watts over 100 meters, whereas the referenced Digital Electricity implementation could supply up to 2,000 watts or reach up to 2,000 meters. That produced the marketing shorthand of 20 times the power or 20 times the distance.

The “20 times” statement is valid as a comparison between the specific products and PoE assumptions used in that material. It should not be treated as a universal FMPS performance ratio. Class 4 is a safety and code classification, not a guarantee that every qualifying system will deliver 2 kW over 2 km.

> **Class 4 can occupy the design space between PoE and conventional branch power by carrying substantially more power over substantially greater distances than Class 2 PoE in appropriately engineered systems.**

PoE and FMPS should be treated as complementary. FMPS can transport power to a remote zone, while a receiver may provide the voltage or power format required by local equipment, including equipment subsequently served through PoE.

## 5. Speed and flexibility: from faster cabling to lifecycle adaptability

The emergence of purpose-built Class 4 cabling, integrated receivers, hybrid fiber-and-power assemblies, system-level listings, and a formal installation standard strengthens the argument that FMPS can support modular deployment and reconfiguration.

**FMPS may improve the adaptability of distributed power infrastructure by separating the centralized transmitter, pathway, receiver, and local load into manageable components.** This can make selected moves, additions, and changes less dependent on extending conventional branch circuits.

The evidence does not support a universal promise that later changes require “no electrician work.” Licensing, permitting, maintenance responsibility, and scope-of-work rules vary by jurisdiction.

## 6. Cost: from component savings to total installed architecture

Potential savings may come from reduced Class 1 branch-circuit infrastructure, fewer intermediate electrical-distribution components, smaller conductors for long-distance distribution, coordinated pathways for fiber and power, centralized backup, fewer distributed UPS units, and reduced cooling or floor-space demands at some remote equipment locations.

Offsetting costs can include specialized transmitters and receivers, listed Class 4 cable, system engineering, commissioning, training, software or management components, and the risks associated with a still-maturing vendor ecosystem.

> **The correct economic comparison is FMPS versus the complete conventional architecture it may replace, not FMPS cable versus ordinary electrical cable.**

## 7. Centralized backup and power continuity

The original architectural principle remains valid: a centralized transmitter can receive AC or DC input, and a receiver can convert the Class 4 waveform into the electrical form required by the load.

```text
Grid, generator, storage, or DC source
                    ↓
        Central Class 4 transmitter
                    ↓
             Class 4 circuit
                    ↓
        Remote receiver or load
```

This can allow multiple distributed loads to be supported from a centrally managed source rather than from separate UPS devices at every remote location. FMPS status alone, however, does not grant an emergency-power classification.

## 8. Space: from bypassing IDFs to rethinking equipment-room density

Class 4 does not, by itself, eliminate IDFs. It creates another design option for reducing the equipment normally concentrated in those rooms.

When combined with deep fiber or Passive Optical LAN, FMPS can potentially relocate or centralize Ethernet switching, branch electrical distribution, distributed UPS equipment, power conversion, cooling loads, and local monitoring equipment.

The better claim is that converged fiber and Class 4 architectures can **reduce dependence on traditional full-size IDFs**, not that they universally remove them.

## 9. Intelligence and operational visibility

The contemporary FMPS framework treats monitoring as part of the safety architecture, not merely as an optional building-management feature. Beyond required protection, products may add telemetry, event histories, remote configuration, power measurement, load control, alarm reporting, or policy-based operation.

Class 4 therefore creates two distinct forms of intelligence:

1. **Safety intelligence**, required to identify and limit fault energy.
2. **Operational intelligence**, which may include telemetry, event histories, remote configuration, power measurement, load control, alarm reporting, or policy-based operation where the selected product documents those capabilities.

These categories should not be conflated. Every qualifying Class 4 system must manage fault energy, but products do not necessarily provide identical user-facing analytics, integrations, APIs, or policy controls.

## 10. Sustainability: a plausible benefit that requires project evidence

A defensible sustainability claim is:

> **FMPS can support material-efficient and DC-oriented designs by reducing selected distributed electrical components, enabling smaller conductors in appropriate applications, accepting AC or DC source power, and supporting centralized conversion and backup architectures.**

A project should not be labeled greener without analyzing conductor mass and length, pathway materials, conversion efficiency, standby consumption, cooling effects, equipment service life, repairability, battery architecture, and end-of-life recovery.

## 11. Applications: from telecommunications loads to converged infrastructure

Current applications are better organized into five groups:

### Digital connectivity

- Passive Optical LAN and ONT infrastructure
- remote PoE switches
- Wi-Fi access points
- DAS and private wireless equipment
- 4G and 5G radios

### Smart-building infrastructure

- sensors and controls
- security devices
- lighting systems
- building automation
- selected motor and HVAC applications

### Distributed computing

- edge-computing nodes
- remote IT equipment
- selected data-center distribution applications
- AI rack expansion in qualifying vendor designs

### Industrial and transportation systems

- automation equipment
- communications and operational systems
- distributed equipment in warehouses, factories, airports, and transportation facilities

### Energy and resilience

- centralized UPS arrangements
- battery-supported critical ICT loads
- DC distribution
- renewable and generator integration
- microgrid-connected intelligent loads

Each proposed load still requires engineering confirmation of receiver output, starting current, load behavior, cable distance, voltage drop, protection, environmental ratings, listing compatibility, and applicable code requirements.

## 12. New capabilities and developments visible by 2026

### Technology-neutral Class 4 systems

UL 1400-1 was developed to accommodate multiple waveform types, including continuous DC, pulsed DC, sinusoidal AC, AC plus DC, and pulsed DC plus DC. Class 4 is therefore broader than VoltServer’s packetized implementation.

### Integrated receivers

The Class 4 receiver may operate as a standalone device or be integrated into utilization equipment.

### Dedicated outdoor cabling

The July 2023 issue of UL 1400-2 added requirements for CL4Z cables intended for outdoor use.

### Residential eligibility under the 2026 NEC

Eaton reports that the 2023 NEC prohibition on Class 4 FMPS in dwelling units was removed in the 2026 edition, subject to local adoption and applicable listing and installation requirements.

### Installation and maintenance standardization

NECA 726-2026 addresses installation, equipment handling, cabling, transmitters, receivers, labeling, system programming, startup, commissioning, safety, documentation, and long-term maintenance.

### Convergence with deep-fiber networks

Fiber can move data deep into a building while FMPS moves centrally managed power to the same zones. Local receivers can then serve suitable DC, PoE, network, control, or building-system loads. This is an interpretive synthesis from the underlying technical capabilities, rather than a universal standards claim.

## Research conclusion

The technology has moved through three stages:

### Stage 1: Proprietary innovation

Digital Electricity demonstrated that substantial power could be packetized, monitored, transmitted over long distances, and interrupted rapidly when faults were detected.

### Stage 2: Code and certification category

UL 1400-1, UL 1400-2, and NEC Article 726 established the larger category of Class 4 Fault-Managed Power. Safety became formally associated with monitored and limited fault energy rather than with a proprietary packet format.

### Stage 3: Infrastructure platform

By 2026, FMPS was developing into a fuller infrastructure discipline with listed systems and cables, outdoor cable classifications, installation and maintenance practices, residential eligibility under the 2026 NEC, integrated receivers, diverse waveform possibilities, and growing application interest in campuses, smart buildings, wireless networks, industrial systems, data centers, electrification, and DC energy architectures.

> **Class 4 Fault-Managed Power is a managed power-distribution layer that can deliver substantial power over extended distances while actively limiting energy under fault conditions. Its emerging importance lies not only in replacing selected conventional circuits, but in enabling power, communications, fiber, controls, backup energy, and operational telemetry to be designed as parts of one converged infrastructure system.**

The first sentence is directly supported by Class 4 safety and standards sources. The second is Jason Kronemeyer’s synthesis from his work on Passive Optical LAN, smart campuses, DC systems, and intelligent infrastructure, and should not be attributed to NEC, UL, NECA, Belden, or VoltServer.

## Selected sources

- Belden. “Digital Electricity: 5 Things You Need to Know.” 29 Nov. 2018.
- Eaton. “NEC 2026: Fault Managed Power.”
- National Electrical Contractors Association. *NECA 726-2026: Standard for Installing and Maintaining Class 4 Fault-Managed Power Systems.* 2026.
- Panduit. *Fault Managed Power Systems / Class 4 Power Technology Brief.* Rev. 5, Sept. 2026.
- UL Solutions. “Fault-Managed Equipment and Cables: UL 1400-1 and UL 1400-2 Update.” Mar. 2025.
- UL Solutions. “UL 1400-1 and 2023 NEC Updates for Fault-Managed Equipment.” 2023.
- UL Standards & Engagement. *UL 1400-1: Outline of Investigation for Fault-Managed Power Systems, Part 1.* 19 Dec. 2022.
- UL Solutions. “First Certification for a Fault-Managed Power System.” 21 Nov. 2023.
- VoltServer. “Powering the Future with Digital Electricity.”
- Vicor. “VoltServer Digital Electricity.”

## Editorial note

This research note separates historical marketing claims from current code-supported capabilities, distinguishes the Class 4 category from the VoltServer implementation, qualifies universal assertions such as “no conduit,” “green,” and “no electrician,” and identifies the converged-infrastructure interpretation as Jason Kronemeyer’s synthesis rather than an assertion by the technical standards.
