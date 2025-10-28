# Capitalizing on Class Four Power in Optical LAN Applications | Panduit Webinar

## Webinar Recap and In-Depth Overview

### Introduction
Thank you to everyone who joined our webinar, "**Capitalizing on Class Four Power in Optical LAN Applications**." We were excited to welcome outstanding speakers from Tellabs and Panduit to discuss the latest advancements in Optical LAN and the introduction of a new Class Four Power Solution, highlighting its applications and benefits in optical LAN environments.
---
### Challenges in Designing Smart Building Networks
*Presented by John Hoover, Marketing Director, Tellabs*
John Hoover began by addressing the key challenges faced when implementing smart buildings and campuses. He identified five primary obstacles in designing and deploying these networks:
- **Scale and Reach:** The exponential growth in the number and capacity of Internet of Things (IoT) devices within smart buildings and across campuses presents a major challenge for network scalability. Keeping up with this demand is a constant hurdle.
- **Security:** The proliferation of connected devices increases the corporate attack surface, making smart buildings more vulnerable to security threats. Ensuring robust security for data in transit and at rest is essential.
- **Reliability:** Network downtime can disrupt critical services, including security endpoints. Redundancy and failover mechanisms are crucial to maintaining uninterrupted operations.
- **Sustainability:** Energy usage, cooling requirements, and the accumulation of plastics and electronic waste all impact the building’s carbon footprint. Addressing these issues is vital for sustainable operations and achieving net-zero goals.
- **Power Management:** Managing the power needs of numerous IoT endpoints, including power over Ethernet and backup solutions, is critical for the smooth operation of smart buildings. Reliable and scalable power delivery is increasingly important as networks expand.
---
### Innovations for Smart Building Network Design
John highlighted that passive optical LAN (POL) and innovations like Class Four Fault Managed Power are key solutions to these challenges:
- **Scale and Reach:** Fiber-based networks can support five times the device density—and, in some cases, up to 128 times the Ethernet density—across a single-mode fiber. These networks also offer 100 times the reach, supporting up to 10, 40, and even 100 gigabit speeds.
- **Security:** Optical LANs can eliminate known security gaps by replacing legacy Ethernet switches, thus reducing the attack surface and supporting zero trust architectures.
- **Reliability:** Originating from the carrier world, optical LANs deliver carrier-grade stability and uptime, lowering operational costs and reducing human error, a major cause of outages and security breaches.
- **Sustainability:** By using fiber networks, both embodied and operational carbon impacts are reduced—less plastic, materials, and lower energy use for cooling, aiding organizations on their journey to net zero.
- **Powering Innovations:** Class Four Fault Managed Power enables longer-distance, higher-capacity, and safer power delivery to IoT endpoints, supporting the growth of smart buildings and campuses.
---
### Evolution of Power Delivery in Optical LAN
John explained the progression of power delivery methods in passive optical LANs:
1. **Local Powering:** Initially, optical line terminals (OLTs) and optical network terminals (ONTs) were powered locally, enabling up to 12 miles of reach. ONTs were responsible for delivering power over Ethernet to IoT devices.
2. **Class Two Remote Powering:** With centralized or distributed architectures, class two remote powering allowed DC power to be pushed up to 2,000 feet using composite cabling. ONTs still delivered power to edge devices.
3. **Class Four Fault Managed Power:** The latest advancement allows ONTs to be powered over distances exceeding one mile. This system supports direct connections or integration with class two systems for higher endpoint density, enabling safe, reliable, and scalable power distribution in smart buildings.
---
### Overview of Passive Optical LAN Networks
*Presented by Ian Merrill, Enterprise Account Executive, Tellabs*
Ian Merrill provided a comprehensive comparison between traditional Ethernet networks and passive optical LAN (POL) solutions.
#### **Traditional Ethernet Networks**
- Consist of a main switch in the data center, riser fiber connections, and point-to-point copper cabling to endpoints.
- Each access switch must be individually managed, requiring significant time and personnel.
#### **Passive Optical LAN Topology**
POL networks use a point-to-multipoint topology with four main components:
- **Optical Line Terminal (OLT):** The central controller in the main data center, managing the entire system and connecting to the core network.
- **Optical Splitters:** Split the signal (up to 64 times for 10G networks or 32 times for 1G networks) and distribute it throughout the building.
- **Optical Network Terminals (ONTs):** Media converters that connect fiber to copper for end devices, available in various configurations (in-wall, zone enclosure, rackmount).
- **Software:** The Panorama software manages all network devices centrally, drastically simplifying operations.
Single-mode fiber allows thousands of devices to connect to a centralized OLT, extending network reach up to 18 miles—ideal for campus-wide deployments.
---
### Key Benefits of Passive Optical LAN
- **Simplicity:** Centralized management reduces the required staff and streamlines moves, adds, and changes, freeing up IT resources for more strategic work.
- **Scalability:** Fiber infrastructure supports easy upgrades and mixed 1G/10G transmissions, accommodating future technologies like Wi-Fi 6/7 without major cable replacements.
- **Security:** Fiber is inherently difficult to tap, and only the OLT console port needs physical security. ONTs have no console ports or IP addresses, making them useless to intruders. The system uses AES 128-bit encryption with a 60-second rotating key for enhanced data protection.
- **Reliability:** Born from carrier-grade technology (e.g., Verizon FiOS), POL systems deliver five nines (99.999%) reliability, with advanced redundancy options (port, card, dual-chassis protection) further boosting uptime to six nines.
- **Sustainability:** POL significantly reduces physical footprint, energy use, and cooling requirements. Single-mode fiber lasts decades, minimizing landfill waste. Large-scale deployments, like Sandia National Labs, have reported up to 65% energy savings and millions in operational cost reductions.
---
### Class Four Power and Fault Managed Power Systems
*Presented by Mahmoud Ibrahim, Commercial Lead, Panduit*
Mahmoud Ibrahim introduced Panduit’s Fault Managed Power System (FMPS), the market's first and only Class Four listed system, and detailed the evolution and standards behind Class Four power.
#### **Understanding NEC Power Classes**
- **Class One:** No power limit, up to 600 volts, requires conduit and electrician installation—common in today’s buildings.
- **Class Two:** Limited to 100 watts and 60 volts, considered safe for low-voltage installations without conduit, but with distance and power limits.
- **Class Three:** Limited to 100 watts and 150 volts, requires electrician installation, but is less commonly deployed.
- **Class Four:** Combines the safety of Class Two with the high power and voltage of Class One. Up to 450 volts can be pushed safely over copper, with built-in fault detection and energy limitation for safe operation. Enables low-voltage installation practices with higher power and longer distances.
#### **Class Four System Standards and Adoption**
- Class Four systems are governed by UL 1400-1 (systems) and UL 1400-2 (cables), covered by NEC Article 726 and 722, respectively.
- The technology is new, with adoption accelerating as more states update to the 2023 NEC code.
- Seven states have adopted Class Four, and twelve more are considering it.
#### **Class Four System Architecture and Safety**
- A Class Four deployment includes a transmitter and receiver connected by Class Four cable, with constant monitoring for faults.
- The system instantly disables power in case of a fault, then self-heals and restarts when safe.
- Compared to GFCI and AFCI outlets, Class Four covers a broader range of fault types, making it safer for distribution than conventional building wiring.
#### **Class Four Cable Specifications**
- Class Four cables are rated for at least 450 volts and come in various gauges, pair counts, and configurations (plenum, riser, indoor/outdoor, hybrid).
- They are typically twisted for installation ease, and termination is vendor-specific.
---
### Panduit Fault Managed Power System (FMPS) Overview
The Panduit FMPS consists of:
- **Transmitter Unit:** Converts AC to pulsed current for Class Four circuits, with network management for monitoring and control.
- **Power Supply Unit:** IT-friendly, rack-mounted, and hot-swappable transmitter modules, each delivering up to 600 watts.
- **Receiver Unit:** Wall or rack-mounted, converts Class Four input to 48V DC, with up to three input channels for aggregated power delivery at long distances.
- **Cabling:** Three-pair, 16-gauge Class Four cable, optimized for the receiver’s three-channel topology.
Centralized power enables backup with a single UPS, centralized monitoring, remote control, scalability, and easy moves, adds, and changes. The system is suitable for a wide range of applications, with particular value in smart buildings and optical LANs.
---
### Panduit FMPS in Optical LAN Applications
Panduit’s FMPS integrates seamlessly with optical LAN architectures. It allows long-distance, high-power delivery alongside fiber—either directly powering ONTs or supplying Class Two power distribution at the edge. This provides flexibility for various deployment scenarios and supports efficient, safe, and scalable power delivery throughout the building or campus.
---
### Conclusion
This webinar provided an in-depth look at the challenges of smart building network design, the benefits and architecture of passive optical LAN, and the new possibilities unlocked by Class Four Fault Managed Power systems. Both Tellabs and Panduit are available to assist with project design and answer further questions regarding the integration and benefits of these technologies.
---
> **Watch the Original Video:**
> [YouTube video, "Capitalizing on Class Four Power in Optical LAN Applications," presented by Tellabs and Panduit. Accessed 10/28/2025. https://youtu.be/OX1P7SaA2RQ?si=3f2VrNye26duK8nN]
>
> [![Watch the webinar]([URL]])
