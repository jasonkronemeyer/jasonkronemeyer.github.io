---
layout: post
title: "Are Public Safety Radios in the 800 MHz Band Moving to Radio over Fiber?"
date: 2025-11-21
categories: [Public Safety, RF Technology, DAS, POLAN]
status: research 
---

## Are Public Safety Radios in the 800 MHz Band Moving to Radio over Fiber?

**Short answer:** Yes, but not for the entire network. Radio over Fiber (RoF) is being adopted primarily for **in-building coverage** and **distributed antenna systems (DAS)** rather than replacing outdoor macro networks. When combined with **Passive Optical LAN (POLAN)**, RoF becomes even more powerful for sites like schools where the central node is located at an **emergency services facility** such as a police or fire station.

---

### **Why RoF is Being Adopted**
- **Coverage Challenges:** Public safety codes like **NFPA 72** and **IFC 510** require reliable indoor coverage for first responders. Traditional coaxial runs between donor antennas and bi-directional amplifiers (BDAs) suffer from high RF losses over long distances.
- **RoF Advantage:** Fiber links eliminate these losses, enabling long-distance connections between donor antennas, BDAs, and DAS headends without degrading signal quality. This is critical in large campuses, high-rise buildings, and tunnels.

---

### **POLAN Integration for Geographically Separated Nodes**
Schools and municipal buildings often connect to a **centralized emergency services hub** (police/fire station or EOC). Using **POLAN**, the same fiber backbone that delivers IT services can also transport RF signals for public safety DAS:
- **Shared Fiber Infrastructure:** POLAN uses single-mode fiber to connect remote Optical Network Terminals (ONTs) in buildings to an Optical Line Terminal (OLT) at the emergency services facility.
- **RoF Overlay:** RF signals for 700/800 MHz public safety bands can ride on dedicated wavelengths or separate fibers within the same cable plant.
- **Benefits:** Reduced trenching costs, simplified maintenance, and future-proof scalability for both IT and life-safety systems.

---

### **Cost-Benefit of POLAN + RoF**
| **Factor**                | **Traditional LAN + DAS** | **POLAN + RoF Hybrid** |
|---------------------------|---------------------------|-------------------------|
| **Cabling**              | Multiple copper runs + coax | Single fiber backbone |
| **Telecom Closets**      | Required per building/floor | Minimal (ONT only) |
| **Power & Cooling**      | Distributed UPS for switches | Centralized at OLT |
| **Maintenance**          | Multiple active devices | Fewer points of failure |
| **Scalability**          | Limited by copper distance | Fiber supports gigabit+ |
| **Integration**          | Separate networks for IT & DAS | Shared infrastructure |

**Bottom Line:** POLAN reduces costs by:
- Eliminating multiple telecom rooms and active switches
- Lowering power and cooling requirements
- Reducing trenching and conduit for separate networks
- Providing a future-proof backbone for IT and public safety systems

---

### **Current Use Cases**
- **In-Building Public Safety DAS:** Vendors such as Honeywell (Fiplex) and ADRF offer fiber-based DAS solutions for 700/800 MHz public safety bands. These systems are UL 2524 certified and comply with fire and building codes.
- **Campus Deployments:** Schools and municipal buildings increasingly leverage POLAN for IT and DAS integration, reducing complexity and improving resilience.

---

### **Future Trends**
- **Hybrid Architectures:** Expect more integration of RoF in distributed public safety networks as agencies upgrade for interoperability and resilience.
- **Mission-Critical Fiber DAS:** Fiber-based DAS is becoming the standard for new construction projects due to code compliance and performance benefits.
- **Not a Full Migration:** Outdoor macro networks for 800 MHz public safety still rely on traditional RF infrastructure; RoF is mainly a transport layer for indoor and extended coverage scenarios.

---

#### **Want to Learn More?**
Next steps could include:
- Mapping out a **typical RoF + POLAN architecture for a school connected to an emergency services hub**
- Comparing **RoF vs coaxial for cost and performance**
- Summarizing **compliance requirements (NFPA, IFC) driving RoF adoption**

---

### **References**
- NFPA 72 and IFC 510 Coverage Requirements
- Honeywell Public Safety DAS Solutions
- ADRF Fiber DAS Overview
- UL 2524 Certification for Public Safety DAS
- Passive Optical LAN Overview – Tellabs


