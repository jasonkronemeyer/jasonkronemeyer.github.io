---
layout: post
title: "The Network Knows"
subtitle: "What a Career in Signals Intelligence, Networking, and Connected Infrastructure Taught Me About Listening to the Systems We Already Have"
date: 2026-11-05
author: Jason F. Kronemeyer
status: draft
categories:
  - Connected Data Intelligence
  - Intelligent Infrastructure
  - Cybersecurity
tags:
  - network intelligence
  - signals intelligence
  - cybersecurity
  - vulnerability management
  - passive collection
  - network telemetry
  - IT and OT convergence
  - provenance
  - knowledge graphs
  - connected data intelligence
excerpt: "Before deploying another scanner, agent, or dashboard, we should first ask what the infrastructure already knows."
---

There is a moment familiar to anyone who has spent enough years troubleshooting networks. Something is not working, the explanation is not obvious, and everyone is trying to determine what changed.

You start following the evidence.

The switch learned a MAC address on a port. DHCP handed that device an address. DNS shows what it was trying to reach. The firewall saw the conversation. The wireless infrastructure knows where the client associated. Somewhere among all those observations is the story of what happened.

I have a phrase I use for this:

**The network knows.**

Not everything, of course. But usually more than we have asked of it.

There is probably a reason I have come to think about networks this way. Early in my career, I spent four years in the United States Air Force as a signals intelligence analyst. On a daily basis, I worked with highly sensitive information that had to be identified, analyzed, decrypted, interpreted, and reported. The technology mattered, but collection alone was never the objective. The work was determining what the observations meant, how they related to other observations, what could responsibly be concluded from them, and what information needed to be communicated so someone else could make a better decision.

Years later, I became a network engineer responsible for a regional network connecting nearly 6,500 students. I eventually moved into leadership with broader responsibility for information technology services supporting K-12 school districts across three counties. The technology was different. The mission was different. The consequences were different.

But something about the work felt remarkably familiar.

Once again, I was following signals.

I found myself thinking about that career arc recently while taking TEEX MGT303: Cybersecurity Vulnerability Assessment. The 16-hour course focuses on the skills needed to assess, document, remediate, and report cybersecurity vulnerabilities. Its activities include examining, analyzing, and prioritizing assets, risks, and vulnerabilities to produce an assessment that can be communicated to organizational leadership.[^1]

The official FEMA course listing makes the progression even more explicit. Its objectives include explaining the elements of a vulnerability-management program, conducting an asset inventory, prioritizing assets, analyzing a vulnerability-assessment scan, identifying corrective actions, and developing a vulnerability-assessment report.[^2]

The course brought me back to a problem that has followed me from signals intelligence through networking, cybersecurity, data science, and connected infrastructure:

**Before we can secure something, manage it, optimize it, or understand the consequences of its failure, we first have to know that it is there.**

That leads to another question:

> **Before we go looking for more information, what does the network already know?**

## The Network Is an Observer

We tend to think of networks primarily as transportation. Packets enter one interface and leave another. Applications communicate. Users connect. Data moves.

After spending much of my career around network infrastructure, I think that description is incomplete.

**A network is also an observational system.**

A switch learns which MAC addresses appear on its ports. A wireless access point knows which clients associate with it. DHCP associates devices with addresses. DNS provides evidence about the resources systems are trying to find. Routers understand paths. Firewalls observe conversations and policy decisions. Optical infrastructure provides information about physical and logical connectivity. Management platforms collect configuration, utilization, faults, performance, and changes in state.

Modern infrastructure makes many of those observations available outside the individual management console. Cisco Meraki, for example, documents Syslog, APIs and webhooks, and SNMP as reporting methods for gathering device information and events. Depending on the method and product, these interfaces can expose device flows, client connectivity, configuration changes, real-time statistics, alerts, and network- or organization-wide information.[^3]

The details matter. Cisco Meraki documents that its MX appliances can send Syslog records for events, IDS alerts, requested URLs, and flows; MR access points support similar reporting except for IDS alerts and can also produce Air Marshal events; and MS switches currently support event-log messages through Syslog. MX flow messages can include source and destination addresses, protocol and port information, and the firewall rule that matched the traffic.[^4]

Cisco Meraki also supports SNMP polling through the cloud dashboard or directly against supported local devices. Available information can include device identity, status, last-contact time, product information, network membership, and packets or bytes on physical interfaces, although the exact data varies by product.[^5] Its webhooks can deliver JSON-formatted alerts to an HTTPS receiver for processing, storage, reporting, or automation.[^6]

FortiOS likewise supports NetFlow and sFlow. Fortinet documents that full NetFlow is supported through information maintained in the firewall session. It also warns that enabling sFlow on an interface can affect hardware offloading, an implementation trade-off that should be evaluated before deployment.[^7]

These platforms are not simply moving information.

They are observing the environment while they do it.

For me, that feels familiar.

## From Signals Intelligence to Network Intelligence

Signals Intelligence provides a useful precedent for this way of thinking, but the comparison needs to be precise.

The Office of the Director of National Intelligence defines Signals Intelligence, or SIGINT, as intelligence derived from signal intercepts. Its public definition includes communications intelligence, electronic intelligence, and foreign instrumentation signals intelligence.[^8]

The National Security Agency describes its SIGINT mission specifically as the production of foreign intelligence derived from electronic signals and systems used by foreign targets. It states that this mission is limited to international terrorists and foreign powers, organizations, or persons.[^9]

Enterprise network monitoring is not SIGINT. The missions, purposes, authorities, legal frameworks, and privacy considerations are fundamentally different. The comparison in this article concerns analytical method, not legal authority or mission.

What carried forward from my Air Force experience was not the mission.

It was the **analytical discipline**.

A signal by itself was not necessarily intelligence. Collection was only part of the process. Observations had to be evaluated, placed in context, related to other observations, interpreted, and transformed into something useful.

The Office of the Director of National Intelligence describes the intelligence cycle as moving through direction, collection, processing, exploitation, and dissemination. It also describes all-source intelligence as intelligence based on the available forms of collection rather than on only one collection discipline.[^8]

I see an important parallel in modern network operations.

A DHCP lease is an observation. A MAC address appearing on a switch port is an observation. A wireless association is an observation. A DNS request is an observation. A firewall session is an observation. A NetFlow record is an observation.

None necessarily tells us much by itself.

But suppose a switch tells us that a MAC address appeared on port 17. DHCP associates that MAC address with an IP address. The firewall observes that address communicating with particular destinations. DNS shows which services it sought. Network topology tells us that port 17 serves infrastructure in a particular building.

Now the observations begin telling a story.

That is the connection between my early signals-intelligence work and the way I later learned to troubleshoot networks.

The technologies changed.

**The analytical problem did not.**

How do we turn a collection of observations into something meaningful enough for someone to make a better decision?

## Every Observer Sees Something Different

My years in networking reinforced another lesson: no single observer necessarily sees the whole picture.

A switch sees one part of the environment. A firewall sees another. Wireless infrastructure has another perspective. DHCP and DNS contribute additional evidence. Optical infrastructure understands relationships that may be invisible at the IP layer. A building-management system may understand an operational function that the firewall knows nothing about. A vulnerability scanner may know that a device appears to be affected by a particular CVE while knowing little about the consequences if that device becomes unavailable.

The mistake would be expecting one of these systems to establish the complete truth about the environment.

Instead, I think we should treat them as observers.

Each should tell us what it actually knows. Then we should preserve those observations, determine which refer to the same assets, establish relationships among them, add context, and begin building a larger picture.

This is conceptually similar to the logic of all-source intelligence, although I use the analogy cautiously. The value comes from combining distinct sources without pretending that they all observe the same thing in the same way.

That is what I mean by **network intelligence**.

I do not mean a new formal intelligence discipline, and I do not mean another name for SIGINT. I mean intelligence developed by connecting observations produced by and about the network and placing those observations in the context of the environment the network serves.

The underlying principle is simple:

> **Collection is not intelligence. Intelligence emerges when observations are connected, contextualized, interpreted, and made useful for a decision.**

## Listen Before Interrogating

That career experience is one reason I am increasingly drawn toward a **passive-first approach to network intelligence**.

Passive-first does not mean passive-only.

Vulnerability scanners matter. Authenticated assessments matter. Endpoint telemetry matters. Packet analysis matters. Active discovery matters. TEEX MGT303 explicitly includes analyzing vulnerability-assessment scans and identifying corrective actions from the results.[^2]

I am suggesting a different sequence.

Before asking, *What can we scan?*, ask:

**What can we observe?**

Before deploying another tool to identify what is connected, ask the switches, wireless infrastructure, firewalls, DHCP servers, DNS infrastructure, optical network, and controllers already operating the environment.

In other words:

**Listen before interrogating.**

There is an established cybersecurity foundation for the broader idea. NIST Special Publication 800-137, *Information Security Continuous Monitoring for Federal Information Systems and Organizations*, describes continuous monitoring as a way to provide visibility into organizational assets, awareness of threats and vulnerabilities, and visibility into the effectiveness of security controls. It also emphasizes providing the information needed to respond to risk in a timely manner when observations indicate that controls may be inadequate.[^10]

My extension of that principle comes directly from my experience with infrastructure:

**Treat the infrastructure itself as a source of evidence.**

## What Is It?

Asset intelligence begins with identity, but identity rarely lives in one field in one database.

A switch might know a MAC address and the port where it appeared. DHCP can associate that MAC address with an IP address. DNS may provide evidence about a hostname or the resources that address is trying to find. A firewall observes sessions originating from the address. Other systems may identify a manufacturer or classify the endpoint as a workstation, camera, printer, access-control system, building controller, or another form of IoT or OT equipment.

Individually, these are observations.

Together, they begin describing an asset.

My Air Force experience taught me early not to confuse an observation with a conclusion. My network-engineering experience reinforced why that matters. Networks change constantly. Devices move. Addresses change. Equipment gets replaced. Wireless clients roam.

I do not necessarily need one platform to declare itself the keeper of absolute truth.

I need multiple authoritative observers to tell me what they actually observed, and I need a way to determine when those observations describe the same thing.

Instead of beginning with *What is the authoritative inventory?*, I increasingly want to ask:

> **What evidence do we have that this thing exists, and what does each observer know about it?**

## Where Is It?

Location adds another layer.

An IP address gives us logical location, but network infrastructure can often take us much further. Switch ports, wireless associations, VLANs, OLTs and ONTs, telecommunications spaces, and network topology can help connect digital identities back to the physical environment.

That has become increasingly important as my work has expanded beyond traditional IT into broadband, intelligent buildings, Passive Optical LAN, energy systems, IoT, OT, and the larger convergence between information technology and operational technology.

A device might be associated with a campus, then a building, then telecommunications infrastructure, a switch or OLT, a particular port or ONT, and ultimately a physical space or operational system.

Now the MAC address is not simply an address.

It is a camera on this port in this building. It is an access-control system serving these doors. It is a sensor associated with this space. It is a device supporting an energy or building-management function.

The network is helping us connect the **logical environment to the physical environment**.

That is where network data begins becoming organizational context.

## What Is It Talking To?

Networks also observe relationships particularly well.

Flow telemetry, firewall sessions, DNS activity, routing information, application identification, and event data can help establish which systems communicate, which services they rely upon, which protocols are involved, and how those communications change over time.

This is not merely theoretical. Cisco Meraki's documented flow records can contain source and destination addresses, protocol, source and destination ports, available MAC information, and the firewall rule applied to the traffic.[^4] FortiOS NetFlow is generated from information maintained in firewall sessions, making the security gateway another source of relationship evidence.[^7]

A single flow is an observation.

A recurring pattern begins establishing a relationship.

A device **connects to** a switch. A switch **serves** a building. A device **communicates with** a service. A service **depends upon** another system. A device **supports** an operational function.

The longer I have worked with technology, the more interested I have become in those relationships.

As a network engineer, understanding relationships was how I troubleshot connectivity. As an IT leader, relationships helped explain how a failure in one system affected teachers, students, staff, and services. As my work moved into broadband and intelligent infrastructure, those relationships expanded to buildings, communities, physical systems, and institutional missions.

Data science later gave me another vocabulary and another set of tools for working with those relationships. In 2024, after a career-long pattern of continuing education, I earned a Master of Applied Data Science from the University of Michigan.

The technologies and scale changed.

Again, the fundamental question remained remarkably consistent:

**How are these things connected?**

## What Is It Doing?

Time adds behavior.

A camera behaves differently from a laptop. A building controller behaves differently from a printer. An access-control system behaves differently from a server. Environmental sensors, wireless access points, EV chargers, and DC Fault Managed Power Systems each develop characteristic communication patterns.

We do not necessarily have to retain the contents of every packet to begin understanding those patterns. Metadata can tell us what communicated, when it communicated, where the conversation went, which protocol was involved, and approximately how much data moved.

Infrastructure contributes another layer through utilization, latency, interface errors, wireless conditions, optical measurements, security events, and configuration changes. Cisco Meraki's documented reporting interfaces illustrate this distinction: flows are available through Syslog, client connectivity and detailed statistics are available through API or SNMP mechanisms, and alerts can be delivered through webhooks.[^3][^6]

Given enough observations over time, we can move from asking:

**What is this device doing?**

to:

**Is what this device is doing consistent with what we normally observe it doing?**

That transition interests me because it follows an analytical progression that has accompanied me from signals intelligence through networking and into data science.

The individual observation matters.

**The pattern often matters more.**

## Provenance: How Do We Know?

There is another connection to my Air Force experience that has become increasingly important as I think about Connected Data Intelligence: provenance.

Suppose an inventory says:

> Camera 01 is connected to port 17 on Switch 01.

I want to know more than that.

**How do we know?**

Perhaps the switch observed the camera's MAC address on port 17 at 10:17 that morning. DHCP associated that MAC address with a particular IP address. The firewall subsequently saw traffic originating from that address. Another system associated the device with a manufacturer and device type.

Those observations collectively support an assertion.

That is different from recording the assertion as permanent truth.

My signals-intelligence work required understanding where information came from and what could responsibly be concluded from it. My years troubleshooting networks taught me the operational version of the same lesson. Information has a source, a time, a context, and limitations.

That principle carries directly into how I think about data systems today.

A useful network-intelligence architecture should preserve not just conclusions, but the **observation, observer, timestamp, source, relationship, and confidence** supporting them.

New information can supersede an earlier observation. Multiple independent observers can corroborate it. Contradictory observations can indicate either a data problem or something in the environment worth investigating.

A claim becomes much more useful when we can trace it to the evidence supporting it.

The objective is not simply to create more data.

It is to create **defensible knowledge**.

## The Graph and the Timeline

Not everything the network knows belongs in the same database.

Flows, events, logs, interface statistics, measurements, performance data, and security telemetry are temporal. They help answer questions such as when something changed, how often an event occurs, or how communication patterns evolved.

Other questions are relational.

Which devices in this building depend upon this infrastructure? Which communicate externally? Which support important operational functions? Which are associated with products or firmware containing known vulnerabilities?

Those questions lend themselves to graph thinking.

A building contains a space. The space is served by infrastructure. The infrastructure connects a device. The device corresponds to a product. The product runs firmware. The firmware may be affected by a vulnerability. The vulnerability may be known to be actively exploited.

The analytical layer describes **what happened through time**.

The graph describes **how things relate**.

Provenance tells us **why we believe those relationships exist**.

That combination is where my early experience with signals, career in networking, and later work with data begin converging into what I think of as **Connected Data Intelligence**.

## Vulnerability Is Not the Same as Risk

This is where my experience in TEEX MGT303 brought much of this thinking together.

The course is not simply about finding vulnerabilities. It includes examining and prioritizing assets, risks, and vulnerabilities and translating an assessment into something organizational leadership can use.[^1][^2]

That distinction matters.

Consider two identical devices running identical firmware with the same CVE.

One sits in an isolated training environment.

The other supports physical security, building automation, communications, or critical energy infrastructure.

The vulnerability may be identical.

The CVSS severity may be identical.

**The consequence is not.**

The CISA Known Exploited Vulnerabilities Catalog adds another important dimension. CISA describes the catalog as the authoritative source for vulnerabilities known to have been exploited in the wild and recommends that organizations use it as an input to their vulnerability-management prioritization frameworks.[^11]

Current CISA guidance also emphasizes risk-based prioritization rather than treating all vulnerabilities and systems equally. Its 2026 federal directive focuses rapid remediation on high-risk known exploited vulnerabilities affecting certain publicly exposed assets, while CISA encourages organizations outside the federal scope to adopt risk-based vulnerability management and prioritize KEV remediation.[^12]

But external threat intelligence is still only part of the equation.

Our network can potentially supply local context.

Where is the vulnerable device? What does it communicate with? What infrastructure does it depend upon? What depends upon it? Has its behavior changed? What organizational or operational function does it support?

Those observations allow us to move toward something far more useful than a vulnerability count.

I think about the relationship this way:

**Vulnerability + Identity + Topology + Behavior + Operational Function + Threat Intelligence = Contextual Risk**

That is my synthesis, not a formal risk equation. It does not replace a structured risk assessment.

It describes the evidence I want available when making one.

For leadership, the useful question is not simply:

*How many vulnerabilities do we have?*

It is:

> **Which vulnerabilities matter most here, in our environment, and why?**

## The Same Problem, Seen Through Different Careers

Looking back, what once appeared to be several different chapters in my career increasingly looks like one continuous line of inquiry.

In the Air Force, I learned to work with signals and turn observations into intelligence that could be communicated and acted upon.

As a network engineer, I learned to listen to infrastructure. A switch table, route, firewall event, DHCP lease, or packet trace was not simply technical output. It was evidence that helped explain what was happening.

As an IT leader, the question expanded from *What is happening technically?* to *What does this mean for the organization and the people depending upon these systems?*

As my work expanded into broadband and intelligent infrastructure, the boundary between digital and physical systems became increasingly indistinct.

Data science added another layer, giving me methods for organizing observations at scale, identifying patterns, modeling relationships, and extracting useful information from complex datasets.

Connected Data Intelligence brings those experiences together.

The challenge has remained surprisingly consistent:

**Observe. Connect. Interpret. Communicate. Act.**

The tools change.

The work evolves.

The responsibility to understand what the evidence actually tells us remains.

## Passive First, Not Passive Only

None of this means we stop scanning.

There will always be questions the network cannot answer through ordinary observation. Authenticated vulnerability assessments, endpoint interrogation, configuration analysis, packet analysis, and active discovery remain necessary.

I simply want to change where they appear in the process.

Begin with what configuration tells us **should exist**.

Listen to the infrastructure to determine what **is connected**.

Observe what those things **are doing**.

Correlate observations from multiple sources to establish what we reasonably know.

Preserve the provenance supporting those conclusions.

Enrich the observations with external product, vulnerability, exploitation, and threat intelligence.

Then identify what remains unknown.

**That is when we interrogate.**

The sequence becomes:

**Configuration → Observation → Correlation → Context → Enrichment → Interrogation**

That approach becomes especially important as networks extend farther into the physical world. Building automation, IoT, OT, cameras, access control, sensors, communications infrastructure, and energy systems do not necessarily conform to management models designed around traditional PCs and servers.

But they communicate.

And when they communicate:

**The network sees something.**

## From Signals to Connected Data Intelligence

The longer I have worked with technology, the less interested I have become in individual technologies in isolation.

A broadband network is not simply fiber.

An intelligent building is not simply sensors.

Cybersecurity is not simply a firewall.

A data platform is not simply a database.

Digital opportunity is not simply connectivity.

The interesting problems increasingly live **between things**.

My Air Force experience taught me that a collected signal is not automatically intelligence.

My networking career taught me that a device appearing in a table is not automatically understanding.

Leadership taught me that technical understanding does not automatically tell us organizational consequence.

Data science taught me that an abundance of data does not automatically produce knowledge.

That is why I keep coming back to relationships, context, and provenance.

A MAC address is data. Associating it with a camera gives us identity. Knowing the camera connects through port 17 of a particular switch in a particular building gives us context. Knowing what it normally communicates with establishes relationships and a behavioral pattern. Observing a change provides evidence of a changing condition. Connecting that change to a vulnerability known to be actively exploited, while understanding that the camera supports an important operational function, gives us something on which someone can make a decision.

The progression becomes:

**Signal → Observation → Identity → Relationship → Context → Knowledge → Action**

That progression captures more than a network architecture for me.

It captures much of my career.

## Listen to the Infrastructure

I went into TEEX MGT303 thinking about vulnerability assessment.

I came out thinking about something I first learned in a very different environment more than two decades ago:

**Signals tell stories, but only if we learn how to listen to them.**

In the Air Force, those signals existed within a particular mission, governed by the authorities and practices of Signals Intelligence. Formal SIGINT should not be confused with the enterprise network intelligence I am describing here. The National Security Agency's public description makes clear that its SIGINT mission concerns foreign intelligence, is limited to specified foreign targets, and operates under legal authorities and civil-liberties requirements.[^9][^13]

What stayed with me was the discipline of turning observation into understanding.

Years later, as a network engineer, I found myself doing something conceptually familiar. Something was happening. The infrastructure had observed pieces of it. My job was to find those pieces, determine what they meant together, and act.

Today, the environment is far more complex.

The switch knows something. The access point knows something. The router knows something. The firewall knows something. The optical infrastructure knows something. DHCP knows something. DNS knows something. The vulnerability platform knows something. The building system knows something.

None knows everything.

**That is precisely why connecting them matters.**

For years, we have tended to leave those observations trapped in the systems where they originated. We open one dashboard for switching, another for wireless, another for cybersecurity, another for the optical network, another for building systems, and another for vulnerability management.

They are different windows into the same environment.

What becomes possible when we begin treating their observations as evidence about that shared environment?

That question is where the different parts of my career converge.

Signals intelligence taught me to respect the difference between collection and intelligence.

Networking taught me to listen to infrastructure.

Leadership taught me to connect technical conditions to organizational consequences.

Intelligent infrastructure taught me that the network increasingly sits at the boundary between digital and physical systems.

Data science gave me additional methods for analyzing patterns and relationships.

Connected Data Intelligence gives me a way to think about bringing those observations together without losing where they came from.

NIST SP 800-137 provides an established cybersecurity foundation for maintaining visibility into organizational assets, threats, vulnerabilities, controls, and changing conditions.[^10] TEEX MGT303 reinforced the equally fundamental vulnerability-management principle that we must understand our assets if we are going to meaningfully understand their vulnerabilities and risk.[^1][^2]

My career experience leads me to add one more principle:

**Before going out to discover everything again, listen to the infrastructure we have already built.**

Do not begin with:

*What new technology can collect more data?*

Begin with:

> **What does the network already know?**

Then ask:

> **What evidence supports what we think we know?**

Then:

> **What can we learn by connecting observations from systems that each see a different part of the environment?**

And ultimately:

> **How do we turn those observations into knowledge that helps someone make a better decision?**

More than two decades ago, I learned to work with signals.

Since then, the signals have changed. The systems have changed. The scale has changed. My role has changed.

The fundamental challenge has not.

**The network knows. Our job is to learn how to listen.**

## Provenance Statement

**“The Network Knows”** is my practitioner framing. It is informed by my Air Force service, network-engineering and IT-leadership experience, continuing work with broadband and intelligent infrastructure, graduate study in applied data science, and current exploration of Connected Data Intelligence.

The following formulations are my synthesis and should not be attributed to the external institutions or vendors cited in this article:

- **The Network Knows**
- **Listen before interrogating**
- **Passive-first, not passive-only**
- Network infrastructure as an **observational system**
- **Network intelligence** as intelligence developed by correlating observations produced by and about enterprise network infrastructure
- **Configuration → Observation → Correlation → Context → Enrichment → Interrogation**
- **Signal → Observation → Identity → Relationship → Context → Knowledge → Action**
- **Vulnerability + Identity + Topology + Behavior + Operational Function + Threat Intelligence = Contextual Risk**
- The connection among network observations, provenance, graph relationships, and **Connected Data Intelligence**

The Signals Intelligence discussion is an analogy of analytical method grounded in my career experience. This article does not claim that enterprise network monitoring constitutes formal SIGINT.

The external sources establish the factual foundation: the purpose and objectives of MGT303, public definitions and boundaries of SIGINT, NIST's continuous-monitoring guidance, network-telemetry capabilities documented by Cisco Meraki and Fortinet, and CISA's guidance on known exploited vulnerabilities. They do not establish the larger thesis of this article.

## References

[^1]: Texas A&M Engineering Extension Service. “Cybersecurity Vulnerability Assessment.” *MGT303*. [https://teex.org/class/MGT303/](https://teex.org/class/MGT303/).

[^2]: Federal Emergency Management Agency. “Cybersecurity Vulnerability Assessment.” *MGT-303*. [https://www.fema.gov/emergency-managers/national-preparedness/training/course/mgt-303](https://www.fema.gov/emergency-managers/national-preparedness/training/course/mgt-303).

[^3]: Cisco Meraki. “How to Configure Meraki Device Reporting via Syslog, SNMP, and API.” [https://documentation.meraki.com/Platform_Management/Dashboard_Administration/Operate_and_Maintain/Monitoring_and_Reporting/Meraki_Device_Reporting_-_Syslog%2C_SNMP%2C_and_API](https://documentation.meraki.com/Platform_Management/Dashboard_Administration/Operate_and_Maintain/Monitoring_and_Reporting/Meraki_Device_Reporting_-_Syslog%2C_SNMP%2C_and_API).

[^4]: Cisco Meraki. “Syslog Server Overview and Configuration.” [https://documentation.meraki.com/Platform_Management/Dashboard_Administration/Operate_and_Maintain/Monitoring_and_Reporting/Syslog_Server_Overview_and_Configuration](https://documentation.meraki.com/Platform_Management/Dashboard_Administration/Operate_and_Maintain/Monitoring_and_Reporting/Syslog_Server_Overview_and_Configuration).

[^5]: Cisco Meraki. “How to Set Up SNMP Monitoring for Meraki Devices.” [https://documentation.meraki.com/Platform_Management/Dashboard_Administration/Operate_and_Maintain/Monitoring_and_Reporting/SNMP_Overview_and_Configuration](https://documentation.meraki.com/Platform_Management/Dashboard_Administration/Operate_and_Maintain/Monitoring_and_Reporting/SNMP_Overview_and_Configuration).

[^6]: Cisco Meraki. “How to Set Up Webhooks in the Meraki Dashboard.” [https://documentation.meraki.com/Platform_Management/Dashboard_Administration/Operate_and_Maintain/How-Tos/Webhooks](https://documentation.meraki.com/Platform_Management/Dashboard_Administration/Operate_and_Maintain/How-Tos/Webhooks).

[^7]: Fortinet. “sFlow and NetFlow and Hardware Acceleration.” *FortiGate/FortiOS 7.4.0 Documentation*. [https://docs.fortinet.com/document/fortigate/7.4.0/hardware-acceleration/631057/sflow-and-netflow-and-hardware-acceleration](https://docs.fortinet.com/document/fortigate/7.4.0/hardware-acceleration/631057/sflow-and-netflow-and-hardware-acceleration).

[^8]: Office of the Director of National Intelligence. “What Is Intelligence?” [https://www.odni.gov/index.php/what-we-do/what-is-intelligence?highlight=WyJhdCIsImF0cyJd](https://www.odni.gov/index.php/what-we-do/what-is-intelligence?highlight=WyJhdCIsImF0cyJd).

[^9]: National Security Agency. “Signals Intelligence Overview.” [https://www.nsa.gov/Signals-Intelligence/Overview/](https://www.nsa.gov/Signals-Intelligence/Overview/).

[^10]: Dempsey, Kelley, et al. *Information Security Continuous Monitoring for Federal Information Systems and Organizations*. NIST Special Publication 800-137, National Institute of Standards and Technology, Sept. 2011. [https://doi.org/10.6028/NIST.SP.800-137](https://doi.org/10.6028/NIST.SP.800-137).

[^11]: Cybersecurity and Infrastructure Security Agency. “Known Exploited Vulnerabilities Catalog.” [https://www.cisa.gov/known-exploited-vulnerabilities-catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog).

[^12]: Cybersecurity and Infrastructure Security Agency. “BOD 26-04: Prioritizing Security Updates Based on Risk.” [https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk).

[^13]: National Security Agency. “Signals Intelligence.” [https://www.nsa.gov/Signals-Intelligence/](https://www.nsa.gov/Signals-Intelligence/).
