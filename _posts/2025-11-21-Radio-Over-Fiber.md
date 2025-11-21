---
layout: post
title: "Are Public Safety Radios Moving to Radio over Fiber?"
date: 2025-11-21
categories: [Public Safety, RF Technology, RoF, DAS, POLAN]
status: research 
---

**Short answer:** Yes, but not for the entire network. Radio over Fiber (RoF) is being adopted primarily for **in-building coverage** and **distributed antenna systems (DAS)** rather than replacing outdoor macro networks. When combined with **Passive Optical LAN (POLAN)**, RoF becomes even more powerful for sites like schools where the central node is located at an **emergency services facility** such as a police or fire station.

---

### **Why RoF is Being Adopted**

#### **Regulatory Mandates**
Public safety codes are driving RoF adoption:
- **NFPA 72** and **IFC Section 510** require reliable indoor coverage for first responders
- Many jurisdictions now mandate **95% in-building coverage** with minimum signal strength (-95 dBm for 700 MHz, -100 dBm for 800 MHz)
- New construction and major renovations must demonstrate compliance before certificate of occupancy
- Schools, hospitals, high-rises, and large commercial buildings face stricter requirements

#### **Technical Advantages**
- **Coverage Challenges:** Traditional coaxial runs between donor antennas and bi-directional amplifiers (BDAs) suffer from high RF losses over long distances (6-7 dB per 100 feet).
- **RoF Advantage:** Fiber links eliminate these losses, enabling long-distance connections between donor antennas, BDAs, and DAS headends without degrading signal quality. Fiber can run miles with negligible loss. This is critical in large campuses, high-rise buildings, and tunnels.

---

### **POLAN Integration for Geographically Separated Nodes**
Schools and municipal buildings often connect to a **centralized emergency services hub** (police/fire station or EOC). Using **POLAN**, the same fiber backbone that delivers IT services can also transport RF signals for public safety DAS:
- **Shared Fiber Infrastructure:** POLAN uses single-mode fiber to connect remote Optical Network Terminals (ONTs) in buildings to an Optical Line Terminal (OLT) at the emergency services facility.
- **RoF Overlay:** RF signals for 700/800 MHz public safety bands can ride on dedicated wavelengths or separate fibers within the same cable plant. Think of it like different colors of light traveling through the same fiber—data uses one wavelength, voice uses another, and public safety radio uses a third, all without interfering with each other.
- **Power Integration:** ONTs typically include PoE+ ports that can power DAS equipment, access points, and IoT sensors. With **NEC 2026 updates** for fault-managed power systems (Class 4 circuits), higher-power DAS components can be safely powered through the same low-voltage infrastructure.
- **Benefits:** Reduced trenching costs, simplified maintenance, future-proof scalability for both IT and life-safety systems, and centralized backup power at the emergency services facility ensures resilience during outages.

#### **Typical Architecture**
```
[Fire Station/EOC]                    [School Campus]
      OLT                                  Building A
       |                                    ONT → DAS
       |                                    |
       |--- Single Fiber (>12 miles) ----  Building B
       |                                    ONT → DAS
       |                                    |
    Headend                                Building C
  (Donor Antenna)                         ONT → DAS
```
*This single multi-strand fiber run carries both IT network traffic and public safety radio signals to multiple buildings.*

---
### **Cost-Benefit of POLAN + RoF**

| Factor | Traditional LAN + DAS | POLAN + RoF Hybrid |
|--------|----------------------|---------------------|
| **Cabling** | Multiple copper runs + coax | Single fiber backbone |
| **Telecom Closets** | Required per building/floor | Minimal (ONT only) |
| **Power & Cooling** | Distributed UPS for switches | Centralized at OLT |
| **Maintenance** | Multiple active devices | Fewer points of failure |
| **Scalability** | Limited by copper distance | Fiber supports gigabit+ |
| **Integration** | Separate networks for IT & DAS | Shared infrastructure |


**Bottom Line:** POLAN reduces costs by:
- Eliminating multiple telecom rooms and active switches
- Lowering power and cooling requirements
- Reducing trenching and conduit for separate networks
- Providing a future-proof backbone for IT and public safety systems

#### **Case Study: K-12 Campus Integration**
Consider a typical school district with a 5-building campus located 12 miles from the central fire station:

**Traditional Approach:**
- 5 telecom rooms ($15K equipment each = $75K)
- Separate DAS headend at school ($40K)
- 5 UPS systems for switches ($3K each = $15K)
- Annual cooling costs for 5 rooms (~$5K/year)
- **Total initial cost: ~$130K + ongoing OpEx**

**POLAN + RoF Approach:**
- Single OLT at fire station (shared with IT)
- 5 ONTs at school buildings ($2K each = $10K)
- Minimal telecom closets (ONT only, no active cooling)
- RoF DAS integrated with existing fiber
- **Total initial cost: ~$50K + minimal OpEx**

**Net savings: $80K upfront + $5K annually in cooling/maintenance costs**

---

### **Current Use Cases**
- **In-Building Public Safety DAS:** Vendors such as Honeywell and ADRF offer fiber-based DAS solutions for 700/800 MHz public safety bands. These systems are UL 2524 certified and comply with fire and building codes.
- **Campus Deployments:** Schools and municipal buildings increasingly leverage POLAN for IT and DAS integration, reducing complexity and improving resilience.
- **Healthcare Facilities:** Hospitals use RoF to maintain reliable emergency communications throughout complex, multi-building campuses with challenging RF environments.

---

### **Future Trends**
- **Hybrid Architectures:** Expect more integration of RoF in distributed public safety networks as agencies upgrade for interoperability and resilience.
- **Mission-Critical Fiber DAS:** Fiber-based DAS is becoming the standard for new construction projects due to code compliance and performance benefits.
- **NEC 2026 Alignment:** The consolidation of low-energy system requirements under NEC Chapter 7 and expanded provisions for fault-managed power systems (Class 4) simplify the electrical design for POLAN + RoF deployments, enabling higher power delivery to DAS equipment while maintaining safety standards.
- **Centralized Resilience:** By locating OLTs at emergency services facilities with backup generators and UPS systems, POLAN + RoF ensures public safety communications remain operational during power outages—when they're needed most.
- **Not a Full Migration:** Outdoor macro networks for 800 MHz public safety still rely on traditional RF infrastructure; RoF is mainly a transport layer for indoor and extended coverage scenarios.

---

### **Related Topics**

For deeper understanding of RoF and POLAN integration in public safety contexts, consider exploring:

- **Architectural Design Patterns:** Detailed fiber topology designs for school-to-emergency services connectivity, including redundancy and failover strategies
- **Performance Comparisons:** Quantitative analysis of RoF versus traditional coaxial systems across cost, signal quality, and operational metrics
- **Compliance Frameworks:** Comprehensive overview of NFPA 72, IFC 510, and UL 2524 testing requirements and certification processes
- **SMART Building Integration:** How POLAN supports convergence of IT infrastructure, building automation, and life-safety systems (see reference 8 below)

---

### **References**

1. **NFPA 72: National Fire Alarm and Signaling Code**
   - National Fire Protection Association
   - [https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=72](https://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards/detail?code=72)

2. **International Fire Code (IFC)**
   - International Code Council
   - Section 510: Emergency Responder Radio Coverage
   - [https://www.iccsafe.org/products-and-services/i-codes/2021-i-codes/ifc/](https://www.iccsafe.org/products-and-services/i-codes/2021-i-codes/ifc/)

3. **UL 2524: Standard for In-Building 2-Way Emergency Radio Communication Enhancement Systems**
   - UL Solutions
   - [https://www.ul.com/](https://www.ul.com/)

4. **ADRF Technologies - Distributed Antenna Systems**
   - Public Safety and Commercial DAS Solutions
   - [https://www.adrftech.com/](https://www.adrftech.com/)

5. **Honeywell Building Technologies - Emergency Communications**
   - Public Safety DAS and In-Building Wireless Solutions
   - [https://buildings.honeywell.com/](https://buildings.honeywell.com/)

6. **CommScope - Passive Optical LAN Solutions**
   - Enterprise Networks and POLAN Architecture
   - [https://www.commscope.com/solutions/enterprise-networks/](https://www.commscope.com/solutions/enterprise-networks/)

7. **Tellabs - Passive Optical LAN (POL) Technology**
   - Fiber-based networking architecture for enterprise and smart building deployments
   - [https://www.tellabs.com/pol](https://www.tellabs.com/pol)

8. **SMART Building Certifications: A Technical and Programmatic Framework**
   - Related post exploring Passive Optical LAN in smart building contexts
   - [SMART Building Certifications](/2025/11/05/SMART-Building-Certifications.html)


