---
layout: post
status: brainstorming
title: "The Snowflake Model in Network Science Terms"
date: 2026-11-25
author: Jason Kronemeyer
description: "A network-science explanation of the Digital Opportunity Snowflake and its relationship to Digital Citizenship, MITTEN, DOIN, Compass, the Knowledge Commons, and Holistic ROI."
categories:
  - digital-opportunity
  - community-development
  - network-science
  - EUPConnect
tags:
  - snowflake-model
  - digital-citizenship
  - MITTEN
  - DOIN
  - connected-data-intelligence
  - holistic-roi
  - opportunity-value
math: true
---

In network-science terms, the proposed **snowflake is not really a hub-and-spoke network**, even though a visual representation can initially look like one. A better description is a **multilayer, person-centered network whose communities correspond to opportunity domains and whose purpose is to increase each resident's reachable opportunities**.

That distinction is important for DOIN and MITTEN.


![Snowflake model diagram]({{ '/assets/images/IMG_4307.png' | relative_url }})


## 1. The Digital Citizen Is the Focal Node, Not the Hub

Let the regional network be:

$$
G = (V,E)
$$

where $V$ contains multiple node types:

- people;
- organizations;
- navigators;
- services;
- resources;
- skills;
- opportunities;
- places;
- evidence; and
- outcomes.

The Digital Citizen shown at the center of the snowflake is a **focal node**. The diagram is therefore an **focal-network view** of a much larger regional graph.

That citizen does not control the network. The citizen is simply the node from whose perspective we are asking:

> **What can this person reach, through which relationships, at what cost, and with what degree of confidence?**

This prevents a major design mistake. We do not want EUPConnect, MITTEN, DOIN, a library, or a navigator to become a centralized intermediary through which every interaction must pass. The citizen should ultimately develop **many independent paths into the regional network**.

## 2. The Snowflake Branches Are Network Communities

The six branches can be treated as communities or modules:

$$
C_1 = \text{Health}
$$

$$
C_2 = \text{Learning}
$$

$$
C_3 = \text{Work}
$$

$$
C_4 = \text{Government}
$$

$$
C_5 = \text{Finance}
$$

$$
C_6 = \text{Community}
$$

These communities have relatively dense internal connections. For example, the health community might contain:

$$
\begin{aligned}
&\text{Resident} \leftrightarrow \text{Navigator} \\
&\leftrightarrow \text{Library} \leftrightarrow \text{Health System} \\
&\leftrightarrow \text{Specialist} \leftrightarrow \text{Telehealth Service} \\
&\leftrightarrow \text{Remote Monitoring Service}
\end{aligned}
$$

The employment community could contain:

$$
\begin{aligned}
&\text{Resident} \leftrightarrow \text{Navigator} \\
&\leftrightarrow \text{Michigan Works!} \\
&\leftrightarrow \text{Employer} \\
&\leftrightarrow \text{Training Provider} \\
&\leftrightarrow \text{Credential} \leftrightarrow \text{Job}
\end{aligned}
$$

But these communities should **not be isolated**. Health connects to employment. Employment connects to transportation. Education connects to employment. Financial capability connects to housing. Libraries touch nearly all of them. Those cross-branch relationships are extremely important.

## 3. Digital Skills Increase Reachability

The eight competencies are:

- **Connect**
- **Identify**
- **Navigate**
- **Communicate**
- **Create**
- **Evaluate**
- **Protect**
- **Participate**

They are not simply eight topics in a curriculum. They affect the individual's ability to **traverse edges in the network**.

Suppose an opportunity exists three steps away:

$$
\begin{aligned}
&\text{Citizen} \rightarrow \text{Portal} \\
&\rightarrow \text{Provider} \rightarrow \text{Specialist}
\end{aligned}
$$

The path technically exists. But if the citizen cannot authenticate to the portal, the path is functionally broken.

> **Graph connectivity does not necessarily equal human accessibility.**

We can represent a capability-weighted edge as:

$$
w_{ij} = f(A_{ij}, S_i, T_{ij}, C_{ij}, R_{ij})
$$

where:

- $A_{ij}$ represents access;
- $S_i$ represents the person's relevant skill or capability;
- $T_{ij}$ represents trust;
- $C_{ij}$ represents cost or burden; and
- $R_{ij}$ represents reliability.

A broadband connection might physically exist, but the effective edge weight could still be poor because the person lacks a suitable device, cannot authenticate, distrusts the platform, cannot navigate it, or cannot afford the service.

Here, $w_{ij}$ is a conceptual **traversability score**: a larger value means that the relationship is more usable for this person and purpose. The function $f$ is not a standard network-science formula; it is a reminder that physical access alone does not determine whether an edge works in practice. Its inputs would need consistent definitions and scales before calculating a score. In particular, $w_{ij}$ is a measure of effective strength, not a path length or cost. A shortest-path model needs a separate cost for each edge.

Digital Citizenship can improve the effective traversability of some connections. It does not necessarily change the underlying physical network: it may instead change whether a person can use a path that already exists.

## 4. Navigators Are Brokers

In network science, the Digital Navigator is especially interesting. Navigators occupy **brokerage positions** between otherwise weakly connected parts of the network.

Consider:

$$
\begin{aligned}
&\text{Citizen} \rightarrow \text{Navigator} \\
&\rightarrow \text{Health System}
\end{aligned}
$$

or:

$$
\begin{aligned}
&\text{Citizen} \rightarrow \text{Navigator} \\
&\rightarrow \text{Michigan Works!}
\end{aligned}
$$

or:

$$
\begin{aligned}
&\text{Citizen} \rightarrow \text{Navigator} \\
&\rightarrow \text{Government Service}
\end{aligned}
$$

The navigator may have high **betweenness centrality** because many shortest paths initially pass through that navigator. For a node $v$, the unnormalized betweenness centrality is:

$$
B(v) = \sum_{\substack{s,t \in V \setminus \{v\} \\ s \ne t}} \frac{\sigma_{st}(v)}{\sigma_{st}}
$$

Here, $\sigma_{st}$ is the number of shortest paths from $s$ to $t$, and $\sigma_{st}(v)$ is the number of those paths on which $v$ is an **intermediate** node, not an endpoint. This version counts ordered pairs $(s,t)$; in an undirected graph, one can instead count each unordered pair once. If several shortest paths tie, a pair contributes a fraction: for example, if 2 of 4 shortest paths pass through $v$, that pair contributes $2/4=0.5$. Normalized betweenness divides this total by the number of eligible pairs, using a convention that depends on whether the graph is directed or undirected.

High betweenness can be useful, but it also presents a danger. If every pathway permanently requires the navigator, we have unintentionally created a **bottleneck**.

The objective of navigation should therefore be unusual:

> **The navigator should intentionally reduce the resident's dependence on the navigator.**

The desired transition is:

### Assisted

$$
\text{Citizen} \rightarrow \text{Navigator} \rightarrow \text{Resource}
$$

### Guided

$$
\text{Citizen} \rightarrow \text{Resource}
$$

with the navigator available as a supporting connection.

### Independent

$$
\text{Citizen} \rightarrow \text{Resource}
$$

The navigator initially brokers an edge and then helps the citizen establish a **direct edge**. That is capacity building.

## 5. MITTEN Becomes the Network-Weaving Layer

MITTEN has a different network function. Its question is not:

> What services should the Hub deliver?

It is:

> **Which nodes need to become connected so that opportunity can flow through the regional network?**

That is network weaving.

Suppose DOIN reveals two nodes that exist but lack a meaningful connection:

$$
\text{Library} \qquad \text{Health System}
$$

MITTEN might facilitate:

$$
\text{Library} \leftrightarrow \text{Health System}
$$

so the library can become a Digital Health Navigator site. MITTEN has not necessarily created either resource. It has created **an edge**.

The same logic applies to relationships such as:

$$
\text{School} \leftrightarrow \text{Employer}
$$

$$
\begin{aligned}
&\text{Tribal Health System} \\
&\leftrightarrow \text{Community Navigator}
\end{aligned}
$$

$$
\text{Library} \leftrightarrow \text{Michigan Works!}
$$

$$
\text{College} \leftrightarrow \text{Healthcare Provider}
$$

Community development becomes partly the intentional act of **creating valuable relationships among existing regional assets**.

## 6. Structural Holes Represent Opportunity Gaps

A **structural hole**, in the sense used in social-network analysis, is a gap between otherwise disconnected or weakly connected contacts or groups. It can create an opportunity for a broker to connect them. Not every missing edge is a structural hole: the gap matters when connecting the sides could provide value.

For example:

- a telehealth service is available;
- a resident needs that service; but
- the resident cannot successfully access it.

The conventional interpretation might be: "The person needs digital-literacy training."

A graph perspective asks a better question:

> **Where is the path broken?**

Possibilities include:

- no broadband edge;
- no affordable-device edge;
- no identity or authentication capability;
- no knowledge of the service;
- no connection between navigator and provider;
- no private community access location;
- no transportation;
- no reimbursement mechanism; or
- no trust relationship.

Different broken edges require completely different interventions. That is substantially more useful than treating everything as a generalized digital divide.

## 7. DOIN Makes the Graph Observable

MITTEN helps **change the graph**. DOIN helps us **observe and understand the graph**.

Conceptually, DOIN records assertions such as:

$$
\begin{aligned}
&\text{Organization A} \\
&\xrightarrow{\text{PROVIDES}} \text{Service X}
\end{aligned}
$$

$$
\text{Service X} \xrightarrow{\text{REQUIRES}} \text{Capability Y}
$$

$$
\begin{aligned}
&\text{Navigator B} \\
&\xrightarrow{\text{SUPPORTS}} \text{Capability Y}
\end{aligned}
$$

$$
\text{Community C} \xrightarrow{\text{LACKS}} \text{Resource Z}
$$

$$
\begin{aligned}
&\text{Intervention D} \\
&\xrightarrow{\text{PRODUCED}} \text{Outcome E}
\end{aligned}
$$

And, importantly:

$$
\text{Assertion} \xrightarrow{\text{SUPPORTED BY}} \text{Evidence}
$$

That is where provenance enters. DOIN does not merely tell us that two nodes are connected. It should tell us **why we believe that relationship exists, where the evidence came from, when it was observed, and how confident we should be in it**.

That fits closely with the broader Connected Data Intelligence concept: relationships, context, meaning, time, and provenance turn separate observations into usable understanding.

## 8. Redundancy Creates Resilience

A healthy regional snowflake should avoid single points of failure.

Suppose the only route to a service is:

$$
\text{Resident} \rightarrow \text{Navigator A} \rightarrow \text{Service}
$$

If Navigator A becomes unavailable, the path disappears.

A more resilient structure might provide several paths:

$$
\text{Resident} \rightarrow \text{Navigator A} \rightarrow \text{Service}
$$

$$
\text{Resident} \rightarrow \text{Library} \rightarrow \text{Service}
$$

$$
\begin{aligned}
&\text{Resident} \rightarrow \text{Health Center} \\
&\rightarrow \text{Service}
\end{aligned}
$$

$$
\text{Resident} \rightarrow \text{Portal} \rightarrow \text{Service}
$$

Now the network has **alternative paths**.

The same ideas used to understand broadband resilience also apply to community development:

> **A resilient community network should have multiple viable paths to important resources.**

Redundancy is not necessarily inefficiency. Sometimes redundancy is resilience.

## 9. Bridging Capital Matters as Much as Bonding Capital

The snowflake also exposes an important social-network distinction.

Within a community, strong **bonding relationships** may exist among:

- neighbors;
- families;
- tribal communities;
- professional peers;
- local organizations;
- faith communities; and
- existing service networks.

Those relationships create trust.

But opportunity often comes from **bridging relationships** that connect one community to another. Examples include:

$$
\begin{aligned}
&\text{Local Resident} \leftrightarrow \text{Library} \\
&\leftrightarrow \text{University}
\end{aligned}
$$

$$
\begin{aligned}
&\text{Tribal Health System} \\
&\leftrightarrow \text{Regional Hospital} \\
&\leftrightarrow \text{Distant Specialist}
\end{aligned}
$$

$$
\begin{aligned}
&\text{Student} \leftrightarrow \text{School} \\
&\leftrightarrow \text{Regional Employer}
\end{aligned}
$$

$$
\begin{aligned}
&\text{Entrepreneur} \\
&\leftrightarrow \text{Local Organization} \\
&\leftrightarrow \text{Statewide Capital Network}
\end{aligned}
$$

MITTEN should therefore value both:

- **Bonding capital**, which supports strong communities; and
- **Bridging capital**, which opens access to new opportunities.

One purpose of the snowflake is to create **bridges between branches**.

## 10. Opportunity Value Becomes Measurable as Network Expansion

This relates directly to the fourth Holistic ROI category: **Opportunity Value**.

In network terms, an intervention creates Opportunity Value when it increases the set of meaningful things reachable by a person or community.

Let:

$$
R_i(t)
$$

represent the set of useful opportunities reachable by citizen $i$ at time $t$.

An intervention creates Opportunity Value when:

$$
\left|R_i(t+1)\right| > \left|R_i(t)\right|
$$

But a simple count is insufficient because some opportunities are technically reachable but impractical. We can instead define effective opportunity reach as:

$$
R_i^{*}(t;\tau) = \left\{o \in O : d_{io}^{*}(t) \le \tau \right\}
$$

where:

- $O$ is the set of opportunities;
- $d_{io}^{*}(t)$ is the effective distance from person $i$ to opportunity $o$ at time $t$; and
- $\tau$ is an acceptable threshold of burden.

The threshold turns a continuous burden score into a practical yes/no rule: an opportunity is counted as reachable if its score is at or below $\tau$. For comparisons over time, use the same definition of an opportunity, scoring method, and threshold; otherwise a change in the count may reflect a changed measurement rule rather than a changed network. The threshold is a policy choice, so it is useful to check whether conclusions hold for nearby values of $\tau$.

Effective distance might combine time, cost, physical distance, skill requirements, trust, administrative friction, and the number of intermediaries:

$$
\begin{aligned}
d_{io}^{*} &= \alpha \widetilde{T}_{io} + \beta \widetilde{C}_{io} + \gamma \widetilde{D}_{io} \\
&\quad + \delta \widetilde{S}_{io} + \epsilon \widetilde{U}_{io} + \zeta \widetilde{F}_{io} + \eta \widetilde{H}_{io}
\end{aligned}
$$

The tildes indicate that each factor has been put on a comparable scale (for example, normalized to the range $0$ to $1$). Here, $\widetilde{U}_{io}$ is a **trust deficit**: higher values mean less trust, and therefore greater burden. The coefficients are nonnegative weights representing the relative importance of travel time, monetary cost, geographic distance, skill burden, trust deficit, administrative friction, and network hops. One possible convention is to make the weights sum to $1$; that makes the result a weighted average on the same scale. The choices of scales and weights are modeling decisions, not universal constants. They should be selected with residents and validated against whether people can actually use the opportunities. Without normalization, adding minutes, dollars, miles, and hops directly would not have a meaningful interpretation.

For example, suppose a path to telehealth has normalized burdens of $0.2$ for time, $0.1$ for cost, $0.0$ for geographic distance, $0.4$ for skill, $0.1$ for trust deficit, $0.2$ for administrative friction, and $0.3$ for hops. With weights $(0.15,0.15,0.05,0.15,0.25,0.15,0.10)$ in that same order, the effective distance is:

$$
d_{io}^{*} = 0.15(0.2)+0.15(0.1)+0.05(0.0)+0.15(0.4)+0.25(0.1)+0.15(0.2)+0.10(0.3)=0.19
$$

If the acceptable threshold is $\tau=0.25$, this path qualifies under the chosen model. This is an illustration of the method, not a claim that these particular scores or weights are appropriate for a real community.

This gives us a practical interpretation of rural development:

> **Development expands the effective opportunity neighborhood of the resident.**

Telehealth illustrates this well. Before an intervention, cardiology expertise may be 150 miles away. After an intervention, the same expertise may be three reliable network hops away through a trusted local access point.

The geography has not changed. **The network distance has.**

## 11. The Snowflake Should Become Less Snowflake-Like Over Time

The snowflake is an excellent **conceptual starting topology** because it helps identify domains. But a mature network should not actually look like six isolated spokes.

Initially, relationships may look like:

$$
\text{Citizen} \rightarrow \text{Health}
$$

$$
\text{Citizen} \rightarrow \text{Education}
$$

$$
\text{Citizen} \rightarrow \text{Work}
$$

$$
\text{Citizen} \rightarrow \text{Finance}
$$

As the regional network develops, cross-domain relationships emerge:

$$
\text{Health} \leftrightarrow \text{Employment}
$$

$$
\text{Education} \leftrightarrow \text{Employment}
$$

$$
\text{Finance} \leftrightarrow \text{Entrepreneurship}
$$

$$
\text{Libraries} \leftrightarrow \text{All Domains}
$$

$$
\text{Transportation} \leftrightarrow \text{Health} \leftrightarrow \text{Work}
$$

$$
\text{Broadband} \leftrightarrow \text{All Domains}
$$

The topology gradually becomes a **meshed network**.

The snowflake therefore describes the **domains of opportunity**, not the topology we ultimately want. The end state is not a prettier snowflake. The end state is a **dense, resilient, navigable opportunity network**.

## What We Should Measure

This model suggests stronger metrics for MITTEN and DOIN than program counts alone.

### Degree

How many useful direct relationships does a resident or community organization have?

For node $i$:

$$
k_i = \sum_j A_{ij}
$$

For a simple, undirected, unweighted graph, $A_{ij}=1$ when $i$ and $j$ have a direct relationship and $0$ otherwise; the diagonal is $0$, so a node is not counted as connected to itself. For example, if a resident has direct ties to a navigator, library, and clinic, then $k_i=3$. The formula counts ties, not their quality or usefulness; those need to be defined in the data. In a directed graph, distinguish in-degree from out-degree. In a weighted graph, $\sum_j A_{ij}$ is usually called strength rather than degree.

### Betweenness Centrality

Which navigators or organizations are becoming bottlenecks or critical brokers?

$$
B(v) = \sum_{\substack{s,t \in V \setminus \{v\} \\ s \ne t}} \frac{\sigma_{st}(v)}{\sigma_{st}}
$$

This is the same unnormalized measure described above: it counts how often a node lies between other nodes on shortest paths. High betweenness can indicate brokerage, but it does not by itself prove that a node is a bottleneck or that removing it would disrupt service. To assess that risk, examine what reachable paths remain if the node or relationship is unavailable. Also specify whether shortest paths mean fewest hops or lowest total cost.

### Path Length

How many steps must a resident traverse to reach a resource?

For a connected graph with $N$ nodes, the average path length over ordered pairs is:

$$
L = \frac{1}{N(N-1)} \sum_{i \ne j} d(i,j)
$$

Here, $d(i,j)$ is the length of a shortest path from $i$ to $j$. In an unweighted graph, length is the number of edges; in a weighted graph, it is the minimum sum of edge costs. For example, in a three-node chain $A-B-C$, the ordered-pair distances are $1,1,2,2,1,1$, so $L=8/6=4/3$ edges. If the graph is disconnected, some distances are infinite, so this all-pairs formula is not a finite average. One option is to average only over reachable ordered pairs, dividing by the number of such pairs; another is to report averages for each connected component. State which convention is used, since the results answer different questions.

### Network Density

Are organizations within and across domains actually becoming connected?

For an undirected graph:

$$
D = \frac{2|E|}{|V|(|V|-1)}
$$

This is the fraction of all possible distinct node pairs that have an edge, ranging from $0$ (no edges) to $1$ (every pair is connected). It assumes a simple undirected graph with no self-loops. Density says how many direct ties exist, not whether they are accessible, trusted, or resilient. For directed, weighted, or multilayer networks, use a definition appropriate to the layer and edge type rather than combining unlike relationships into one denominator.

### Modularity

Are health, education, workforce, and other domains becoming isolated silos, or are meaningful cross-domain bridges emerging?

A common modularity expression is:

$$
Q = \frac{1}{2m}\sum_{i,j}\left(A_{ij}-\frac{k_i k_j}{2m}\right)\delta(c_i,c_j)
$$

Here, $A_{ij}$ is the binary adjacency matrix, $m$ is the number of edges, $k_i$ and $k_j$ are node degrees, and $\delta(c_i,c_j)=1$ when $i$ and $j$ are assigned to the same community and $0$ otherwise. The sum considers all ordered pairs; the factor $1/(2m)$ accounts for each undirected edge appearing twice. The term $k_i k_j/(2m)$ is the expected connection under a degree-based random-graph baseline. Thus, $Q$ compares the number of within-community edges with what that baseline would predict. A higher value indicates stronger-than-expected within-community clustering for that particular partition; it does not automatically mean the network is healthier. This expression is for an undirected, unweighted graph; directed and weighted networks use variants.

### Bridges

Which relationships connect otherwise separate communities? These relationships may have disproportionate community-development value even if they are few in number.

### Redundancy

Are alternative pathways available when one resource, organization, navigator, or communication channel fails?

### Reachability

What opportunities can residents actually access, not merely discover?

### Edge Strength

Are relationships theoretical referral links, or are they trusted, current, and routinely used connections?

### Temporal Change

Is the community network improving?

DOIN should not merely represent a static graph $G$. It should eventually allow comparison across time:

$$
G_t \rightarrow G_{t+1}
$$

This notation means the graph observed at one time is compared with the graph observed later. It is descriptive, not by itself evidence that an intervention caused the change: other events may also have changed the network. The practical question is:

> **How did the community network change because we intervened?**

## The Deeper Interpretation

The overall model can be summarized in network-science terms:

| Model element | Network-science interpretation |
|---|---|
| Digital Citizen | Ego node whose opportunity set we want to expand |
| Snowflake branches | Modular opportunity communities |
| Digital skills | Capabilities affecting edge traversability |
| Navigator | Broker who helps establish and strengthen edges |
| MITTEN | Network-weaving intervention system |
| DOIN | Observable, provenance-aware representation of the network |
| Knowledge Commons | Shared informational resources available through the network |
| Compass | Mechanism for identifying where intervention may create value |
| Structural holes | Potential opportunities for network weaving |
| Opportunity Value | Increase in meaningful opportunities reachable through the network |

The snowflake model can therefore be stated concisely:

> **The snowflake model treats community development as the intentional expansion, strengthening, and diversification of the pathways through which people can reach meaningful opportunities.**

That is more than a metaphor. It supplies a network model that DOIN can represent, MITTEN can intentionally change, Compass can help analyze, the Knowledge Commons can resource, and Holistic ROI can evaluate.
