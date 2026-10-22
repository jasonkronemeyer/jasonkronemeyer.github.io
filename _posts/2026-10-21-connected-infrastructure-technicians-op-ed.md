---
layout: post
status: op-ed
title: "Stop Training Low-Voltage Installers. Start Training Connected Infrastructure Technicians."
date: 2026-10-21
author: Jason Kronemeyer
categories:
  - workforce development
  - infrastructure
  - smart buildings
  - broadband
tags:
  - connected infrastructure
  - workforce development
  - fiber optics
  - structured cabling
  - networking
  - power over ethernet
  - smart buildings
  - fault-managed power
excerpt: "As connectivity, power, sensing, controls, and cybersecurity converge inside buildings, workforce development needs a new entry-level pathway: the Connected Infrastructure Technician."
---

For decades, we have divided the infrastructure inside a building into relatively neat occupational categories. Electricians handled power. Telecommunications installers pulled cable. Network technicians configured switches and routers. AV specialists installed displays and sound systems. Security contractors handled cameras and access control. Those distinctions made sense when the systems themselves were more separate. They make less sense every year.

The building no longer respects those boundaries.

Walk into a newly constructed school, healthcare facility, municipal building, farm operation, small business, or increasingly sophisticated home, and the convergence is difficult to miss. Fiber brings connectivity into the building. Structured copper and fiber distribute it throughout the facility. Ethernet connects devices that once operated independently. Wi-Fi provides mobility. Power over Ethernet delivers communications and electrical power through the same structured cabling plant. Cameras, environmental sensors, access-control systems, displays, and other building technologies become network endpoints. Cybersecurity becomes a concern not only for computers and servers, but for the physical building itself. IEEE's four-pair Power over Ethernet work illustrates just how far standardized Ethernet has moved toward supporting higher-power connected devices (IEEE Standards Association).

On the horizon, fault-managed power systems push this convergence even further. The point is not that electricians disappear, telecommunications trades disappear, or every worker should become an expert in every discipline. The point is that the space between these disciplines is growing, and somebody has to know how the pieces fit together.

That leads me to a simple workforce-development question: Are we still training people for the infrastructure we used to build, or for the infrastructure they will actually encounter over the next twenty years?

I think the answer requires a new occupational pathway: the **Connected Infrastructure Technician**.

## A Building Is Becoming a Network

This transition is particularly easy to see in the smart home. The structured-media enclosure was once a relatively passive piece of infrastructure. It might contain telephone distribution, coaxial cable, and a handful of Ethernet connections. Increasingly, that same part of the home has to accommodate a fiber optical network terminal, broadband gateway, router, Ethernet switching, smart-home controllers, and other active electronics. Once those components become active, enclosure space, serviceability, power, heat, cable management, and upgrade paths all become design considerations.

Better wireless does not eliminate the need for good wiring. In many cases, it makes good wiring more important. Faster wireless access points still need reliable backhaul. Cameras, access points, sensors, and other endpoints increasingly depend on both data connectivity and remote power. What looks like a Wi-Fi problem at the user's device may actually originate in the copper link, switch configuration, power budget, IP network, or broadband connection behind it.

The same pattern appears at a much larger scale in schools, hospitals, offices, public facilities, and industrial environments. The result is what I think of as the **converged building**: a place where connectivity, power, sensing, control, automation, and computing increasingly share infrastructure and depend on one another.

That convergence changes what an installer needs to know.

## Pulling Cable Is Still Essential, but It Is No Longer Enough

Physical craftsmanship remains fundamental. Someone still has to install pathways, pull cable without exceeding tension or bend limits, terminate connectors correctly, label links, maintain telecommunications spaces, preserve firestopping, and leave behind an installation that another technician can understand years later. BICSI still places these fundamentals at the beginning of its installation pathway. Its Installer 1 program requires no prior experience and emphasizes jobsite professionalism, transmission fundamentals, safety, cable pulling, terminations, and basic copper testing (BICSI, “ICT Installer 1 Training”).

Those skills should not be diminished. They should be expanded.

A modern infrastructure technician should understand the complete journey between the service entering a building and the device using it: **fiber to ONT to router or firewall to Ethernet switch to structured cabling to PoE to Wi-Fi to connected device**. When a camera does not work, the technician should be able to determine whether the problem is physical cabling, a connector, available PoE power, a switch port, IP configuration, wireless connectivity, or the endpoint itself. When a fiber link underperforms, the technician should understand connector cleanliness, optical loss, inspection, testing, and when the problem needs to be escalated. When a wireless access point performs poorly, the technician should understand that Wi-Fi performance can depend on interference, placement, wired backhaul, switching, and available power.

This does not mean turning every installer into a network engineer. It means teaching installers enough about the systems attached to their cabling to understand what they are building and to troubleshoot across boundaries.

The existing credential ecosystem already gives us much of the scaffolding. BICSI's current cabling-installation pathway progresses from Installer 1 to Installer 2 Copper, Installer 2 Optical Fiber, and Technician, creating a recognizable progression from foundational installation into specialized copper, fiber, and technician capability (BICSI, “Cable Installer Certification”). Its copper training emphasizes installation, termination, and testing of structured cabling rather than termination alone (BICSI, “Installer 2, Copper”). We do not need to invent an entirely new certification universe. We need to connect existing competencies into a more coherent workforce pathway.

## Start With Employability, Not Credential Accumulation

Workforce development sometimes makes a predictable mistake: we design the perfect technician before we allow somebody to become a useful employee. In doing so, we can make the on-ramp so long and expensive that people who would thrive in the field never enter it.

I would begin with approximately **60 hours of Connected Infrastructure Technician Foundations**. At the end of those first 60 hours, a new technician should be able to work safely, identify common communications media, use basic tools, install cable supports, pull Category 6 and Category 6A cable correctly, terminate jacks and patch panels, perform basic tests, follow drawings, label work consistently, and document what was installed. These are not arbitrary starting points. They align well with the kinds of entry-level installation skills BICSI already treats as appropriate for people with little or no cabling experience (BICSI, “ICT Installer 1 Training”).

A beginner should also know what they do **not** yet know. They do not need to be an expert fusion splicer, but they should recognize fiber and understand how to handle it safely. They do not need to design a VLAN architecture, but they should understand that a network problem is not automatically a bad cable. They do not need to engineer a high-power PoE installation, but they should understand that the Ethernet cable they are installing may also be delivering power to the endpoint.

That distinction between **competency and awareness** is important. Entry-level education should produce somebody who can perform a defined set of tasks correctly and recognize when a problem has moved beyond those tasks.

Then put that person to work.

## Let Employment Become Part of the Classroom

After the foundation, I would combine paid on-the-job experience with progressively deeper technical education. The next stage could encompass roughly **240 hours of core Connected Infrastructure Technician training** covering structured copper, fiber optics, Ethernet and IP networking, Wi-Fi, Power over Ethernet, testing, troubleshooting, cybersecurity, and documentation.

Most importantly, the instruction should be hands-on. Students should encounter deliberately bad terminations. Give them a certification result and make them determine why a copper link failed. Give them a contaminated fiber connector and let them observe what poor cleanliness does to an optical link. Misconfigure a network. Create an addressing problem. Exhaust a PoE power budget. Then ask them to find the fault instead of replacing components until something works.

The goal is not memorizing a sequence of installation instructions. The goal is developing a troubleshooting mindset.

That matters because experienced technicians are rarely valuable simply because they know how to install something when everything goes according to plan. They become especially valuable because they can determine **why something is not working**.

## Networking Belongs in the Installer's Toolkit

Networking should be part of the core pathway, not a separate universe encountered after the physical installation is complete. Cisco's current CCST Networking certification is explicitly aimed at foundational, entry-level networking capability. Its objectives include copper and fiber media, Wi-Fi, Internet of Things endpoints, Ethernet switching, routing concepts, addressing, PoE, troubleshooting commands, documentation, and even basic packet capture with Wireshark (Cisco, “Cisco Certified Support Technician (CCST) Networking”; Cisco, “CCST Networking Exam Topics”). The exam currently costs $125 and Cisco positions it as a first step toward CCNA (Cisco, “Cisco Certified Support Technician Networking”).

That makes CCST Networking an unusually useful companion credential for a Connected Infrastructure Technician. A student learning to terminate a cable should also understand what a link light means. A student installing a switch should understand the difference between switching and routing. A student connecting an endpoint should understand DHCP, DNS, private addressing, default gateways, and basic diagnostic commands. They do not need to become a network architect to use that knowledge every day.

The combination is more important than either competency by itself: **physical installation plus network understanding**.

## Fiber Belongs Earlier in the Pathway

Fiber should no longer be treated as an exotic technology reserved for telecommunications carriers or senior specialists. Fiber-to-the-home, institutional networks, broadband infrastructure, optical LANs, wireless backhaul, and other applications are making optical infrastructure increasingly common across the connected environment.

At the entry level, technicians should understand single-mode and multimode fiber, optical safety, connector inspection and cleaning, attenuation, basic loss concepts, and the importance of bend radius and physical protection. As they progress, they can add fusion splicing, optical loss testing, and OTDR interpretation.

The Fiber Optic Association's CFOT credential provides a useful model. FOA describes CFOT as its primary fiber-technician certification and expects training to address applications, components, premises and outside-plant cable, splicing, termination, testing, and hands-on laboratory work (Fiber Optic Association, “CFOT Certification”). FOA also organizes advanced specialist credentials around skills and applications such as splicing, testing, FTTx, data centers, optical LANs, and fiber for wireless, allowing technicians to specialize after establishing a foundation (Fiber Optic Association, “Certification Training Curriculum Requirements”).

Again, the objective is not to make every beginning installer a master fiber technician. It is to eliminate the increasingly artificial assumption that copper installers, fiber technicians, and network technicians inhabit unrelated worlds.

The building needs people who understand how those worlds connect.

## Then Comes Power

Perhaps the most important convergence is between communications and power. Power over Ethernet has already changed what we expect from structured cabling. IEEE 802.3bt expanded standardized PoE by using all four pairs and increasing the power available to powered devices, while extending classification information for power management (IEEE Standards Association). That means the communications pathway is increasingly also a power-delivery pathway.

Technicians consequently need practical electrical concepts: voltage, current, resistance, watts, voltage drop, available power, cable heating, and the relationship between the power sourcing equipment and the powered device. A technician does not need to become an electrical engineer to understand that eight 25-watt access points represent 200 watts of endpoint demand before we have added cameras, sensors, losses, or design margin.

Fault-managed power systems push that trajectory further. As Class 4 power and other intelligent distribution approaches mature, the old mental model of “data over here and power over there” becomes less useful. That does not erase licensing requirements, electrical codes, or traditional trades. It creates a growing competency space between them.

That is precisely where workforce-development programs should be looking.

## This Matters in Rural Michigan

For the Eastern Upper Peninsula, this approach offers something more durable than training workers for a single construction cycle. The same foundational capabilities support fiber broadband, schools, healthcare facilities, municipal infrastructure, smart homes, agriculture, security systems, wireless networks, building automation, data infrastructure, industrial connectivity, and emerging power-delivery systems.

A rural workforce cannot always depend on hyper-specialization because there may not be enough local projects in any one specialty to sustain continuous employment. Convergence can become an advantage. A technician who can install structured copper on Monday, troubleshoot a Wi-Fi problem on Tuesday, assist with fiber splicing on Wednesday, and commission PoE endpoints on Thursday has skills that transfer across employers and sectors.

That is not dilution of the trades. It is workforce resilience built on a common technical foundation.

The credential strategy should reflect that reality. An entry-level worker might begin with local CIT Foundations training and move toward BICSI Installer 1. With experience, the worker can specialize through BICSI's copper or optical-fiber tracks and eventually Technician. Fiber-focused workers can pursue FOA's CFOT and later specialist certifications. Networking competency can be validated through Cisco CCST Networking, with CCNA available later for those moving further into network administration or engineering (BICSI, “Cable Installer Certification”; Fiber Optic Association, “Certification Training Curriculum Requirements”; Cisco, “Cisco Certified Support Technician Networking”).

This creates a stack rather than a gate. The worker does not need every credential before receiving a paycheck. The paycheck, field experience, classroom learning, and credentials become reinforcing parts of the same career pathway.

## The Name Matters

Words communicate expectations. “Low-voltage installer” describes an occupational category shaped largely by the characteristics of yesterday's infrastructure. “Cable installer” describes a task. “Smart-home installer” ties the worker to one market segment.

I would choose something more durable: **Connected Infrastructure Technician**.

The title communicates that the work is ultimately about connecting systems, not merely installing a particular kind of wire. Underneath it are four intersecting areas of competency: **connectivity, power, controls, and cybersecurity**.

Start with safety and craftsmanship. Teach copper and fiber. Add Ethernet and IP networking. Introduce Wi-Fi and PoE. Teach technicians to test, document, commission, and troubleshoot their work. Then create advanced pathways into broadband, cybersecurity, building automation, optical networking, and fault-managed power.

Most importantly, make the first step short enough that somebody can take it.

A 60-hour foundation can lead to employment. Employment can lead to a 240-hour technical core. The core can lead to recognized credentials. Those credentials can lead to specialization, leadership, and eventually infrastructure design.

That is more than a training program. It is a **career ladder**.

As our homes, schools, businesses, farms, healthcare facilities, and public buildings become increasingly connected, we should make sure the people building that infrastructure have a ladder of their own.

## Works Cited

BICSI. “Cable Installer Certification.” *BICSI*, https://www.bicsi.org/education-certification/certification/cabling-installation/installers-landing-page_li. Accessed 21 Oct. 2026.

BICSI. “BICSI ICT Installer 1 Training.” *BICSI*, https://www.bicsi.org/trainings-career-advancement/training-catalog/bicsi-ict-installer-1-training/. Accessed 21 Oct. 2026.

BICSI. “Installer 2, Copper.” *BICSI*, https://shop.bicsi.org/courses/face-to-face/installer-2-copper. Accessed 21 Oct. 2026.

Cisco. “CCST Networking Exam Topics.” *Cisco Learning Network*, https://learningnetwork.cisco.com/s/ccst-networking-exam-topics. Accessed 21 Oct. 2026.

Cisco. “Cisco Certified Support Technician Networking.” *Cisco*, https://www.cisco.com/site/us/en/learn/training-certifications/exams/ccst-networking.html. Accessed 21 Oct. 2026.

Cisco. “Cisco Certified Support Technician (CCST) Networking.” *Cisco*, https://www.cisco.com/site/us/en/learn/training-certifications/training/courses/ccst-networking.html. Accessed 21 Oct. 2026.

Fiber Optic Association. “The Fiber Optic Association CFOT Certification.” *The Fiber Optic Association*, https://thefoa.org/cfot.htm. Accessed 21 Oct. 2026.

Fiber Optic Association. “The Fiber Optic Association Certification Training Curriculum Requirements.” *The Fiber Optic Association*, https://www.thefoa.org/instructors/class-reqs.htm. Accessed 21 Oct. 2026.

IEEE Standards Association. “IEEE 802.3bt-2018: IEEE Standard for Ethernet Amendment 2: Physical Layer and Management Parameters for Power over Ethernet over 4 Pairs.” *IEEE Standards Association*, https://standards.ieee.org/standard/802_3bt-2018.html. Accessed 21 Oct. 2026.
