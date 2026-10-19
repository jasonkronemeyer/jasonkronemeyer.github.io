---
layout: research-note
title: "From Data to Digital-Opportunity Intelligence: A Learning Roadmap for Query Languages, Knowledge Graphs, and Network Science"
author: "Jason F. Kronemeyer"
date: 2026-10-19
description: "A hands-on learning roadmap spanning relational algebra, SQL, first-order logic, Prolog, Datalog, RDF, SPARQL, Cypher, GQL, Gremlin, path querying, and network science, organized around a reusable Michigan digital-opportunity knowledge graph project."
tags:
  - graph databases
  - query languages
  - knowledge graphs
  - network science
  - SQL
  - SPARQL
  - Cypher
  - GQL
  - Gremlin
  - Datalog
  - digital opportunity
  - DOIN
  - MiGreatDataLake
status: draft
---

# From Data to Digital-Opportunity Intelligence

## Executive Summary

Learning graph and network query languages is most useful when it is treated as a progression in ways of thinking about information rather than as an exercise in memorizing syntax. For my work with MiGreatDataLake, the Digital Opportunities Intelligence Network (DOIN), knowledge graphs, research data, and causal analysis, the objective is not simply to become familiar with several database products. The objective is to learn how the same real-world system can be represented and interrogated as tables, logical statements, semantic triples, property graphs, traversals, paths, and ultimately networks whose structure can be analyzed.

This roadmap therefore uses one continuing hands-on project: a small **Michigan Digital Opportunity Knowledge Graph**. The project begins as a set of relations and SQL tables and evolves through logic programming, RDF and SPARQL, property graphs and Cypher, standardized graph concepts in GQL, Gremlin traversals, path querying, and network science. Reusing the same underlying domain makes the differences among the languages visible. Instead of learning isolated syntax, I repeatedly ask similar questions and observe how each information model changes what is easy to express, infer, or analyze.

The highest priorities are **SQL, RDF/SPARQL, Cypher, path and pattern querying, and network science**. Datalog provides an important bridge into recursive reasoning and inference; GQL provides a standards-oriented perspective on property graphs; Gremlin develops traversal-oriented thinking; and first-order logic and Prolog provide enough theoretical grounding to understand facts, rules, variables, recursion, and inference. The PostgreSQL Global Development Group describes its official tutorial as an introduction to PostgreSQL, relational database concepts, and SQL that provides hands-on experience. Apache TinkerPop describes Gremlin as its graph traversal language and explains that a traversal consists of a sequence of potentially nested steps (PostgreSQL Global Development Group; Apache Software Foundation, “Graph Query Language”).

The destination is larger than graph querying. The progression is **data engineering → semantic modeling → knowledge graphs → graph querying → network science → statistical modeling → causal research**. For DOIN in particular, this allows the graph to become an analytical environment for examining how communities, institutions, programs, infrastructure, research, and resources connect, where structural gaps appear, and which hypotheses deserve rigorous statistical or causal investigation.

## The Continuing Hands-On Project

Rather than using unrelated tutorial datasets at each stage, I will build one deliberately small digital-opportunity ecosystem and repeatedly represent it in different ways. The first version does not need to be comprehensive. Its purpose is to create enough heterogeneity and interconnectedness to make different query paradigms meaningful.

The model can include:

- Communities and counties
- Schools and intermediate school districts
- Libraries
- Nonprofits
- Tribal Nations
- Broadband providers
- Workforce organizations
- State agencies
- Universities and research organizations
- Programs
- Grants and funding sources
- Infrastructure projects

Representative relationships might include:

```text
Community → LOCATED_IN → County
Organization → SERVES → Community
School → LOCATED_IN → Community
ISP → PROVIDES_SERVICE_TO → Community
Organization → PARTNERS_WITH → Organization
Agency → FUNDS → Program
Program → SUPPORTS → Community
Organization → PARTICIPATES_IN → Program
```

This dataset should remain intentionally manageable during the learning process. The goal is not to build a definitive Michigan ontology on the first pass. The goal is to make increasingly sophisticated questions possible while preserving enough familiarity with the underlying entities that I can concentrate on what each language is doing.

# Stage 1: Sets, Relations, and Relational Algebra

Before learning another query syntax, I need to understand the mathematical ideas underneath relational databases. The important concepts are sets, tuples, relations, selection, projection, union, intersection, difference, Cartesian products, joins, keys, and cardinality.

### Hands-On Exercise

Create three small relations by hand:

**Community**

| ID | Name | County |
|---|---|---|
| C1 | Community A | County X |
| C2 | Community B | County Y |

**Organization**

| ID | Name | Type |
|---|---|---|
| O1 | Library A | Library |
| O2 | Nonprofit B | Nonprofit |

**Serves**

| Org | Community |
|---|---|
| O1 | C1 |
| O2 | C1 |
| O2 | C2 |

Without using software, answer: **Which organizations serve Community A?** Work through the relationship using joins rather than simply reading the answer from the table.

> **Learning objective:** Recognize that relationships can themselves be represented as data and understand the operations used to combine relations.

# Stage 2: SQL

SQL should become the relational foundation for everything that follows. The official PostgreSQL tutorial introduces relational database concepts and SQL. Its contents include creating and populating tables, querying, joins, aggregate functions, views, foreign keys, transactions, and window functions (PostgreSQL Global Development Group).

I should become comfortable with:

```text
SELECT
FROM
WHERE
JOIN
GROUP BY
HAVING
ORDER BY
WITH
CASE
UNION
```

Then move into common table expressions, recursive CTEs, window functions, views, and integrity constraints.

### Hands-On Exercise

Build the first version of the digital-opportunity dataset in PostgreSQL. Create separate tables for communities, organizations, programs, and relationships.

Ask progressively harder questions:

```sql
SELECT o.name
FROM organization o
JOIN serves s
  ON o.id = s.organization_id
JOIN community c
  ON s.community_id = c.id
WHERE c.name = 'Community A';
```

Then investigate:

- Which counties have the most organizations serving them?
- Which organizations serve communities in more than one county?
- Which communities do not have a participating workforce organization in the dataset?
- Which programs are associated with organizations serving multiple communities?

### Critical Exercise

Represent a chain such as:

```text
A → B → C → D → E
```

in relational tables and use a recursive CTE to traverse it. This exercise is particularly valuable because it exposes the difference between storing relationships relationally and treating paths as first-class graph concepts.

# Stage 3: First-Order Logic

At this stage, temporarily step away from database products. Learn predicates, variables, constants, quantification, conjunction, disjunction, implication, and existential statements. The purpose is to distinguish facts from rules about facts.

For example:

> Every community served by an organization participating in a particular program is connected to that program.

can be conceptualized as:

```text
Serves(O,C)
Participates(O,P)
→
Connected(C,P)
```

### Hands-On Exercise

Write at least 20 statements about the digital-opportunity ecosystem in predicate form. Include statements about location, service, participation, funding, partnerships, and program support.

Then classify each statement as one of the following:

- Observed fact
- Relationship
- Rule
- Derived statement
- Hypothesis requiring evidence

> **Learning objective:** Build the discipline of separating what is explicitly stored or observed from what is inferred, derived, or hypothesized. This is directly relevant to provenance in future knowledge-graph work.

# Stage 4: Prolog

The goal here is not necessarily to become an expert Prolog developer. The value is in making facts, rules, variables, recursion, unification, and backtracking executable.

### Hands-On Exercise

Represent a few facts:

```prolog
serves(library_a, community_a).
serves(nonprofit_b, community_a).
participates(nonprofit_b, workforce_program).
```

Then create a rule:

```prolog
connected_to_program(Community, Program) :-
    serves(Organization, Community),
    participates(Organization, Program).
```

Ask:

```prolog
connected_to_program(community_a, X).
```

The important conceptual shift is from retrieving only stored information toward asking what can be **derived from facts plus rules**.

# Stage 5: Datalog

Datalog deserves particular attention because it connects logic, databases, recursion, graph reachability, and rule-based reasoning.

### Hands-On Exercise

Create a small partnership network:

```text
partner(A,B)
partner(B,C)
partner(C,D)
```

Then define reachability conceptually:

```text
reachable(X,Y) ← partner(X,Y)

reachable(X,Y) ←
partner(X,Z),
reachable(Z,Y)
```

Ask:

- Is D reachable from A?
- Which organizations are indirectly connected?
- Which organizations could connect a community to a program through a chain of partnerships?

### DOIN Connection

This is the first stage at which indirect institutional relationships become a central object of inquiry. Rather than merely storing who directly works with whom, I can begin representing rules about connectivity, eligibility, reachability, and institutional pathways.

# Stage 6: RDF

Before learning SPARQL, learn the RDF way of representing information as subject-predicate-object statements.

```text
Subject → Predicate → Object
```

For example:

```text
EUPISD → serves → ChippewaCounty
LibraryA → locatedIn → CommunityA
CommunityA → locatedIn → CountyX
ProgramA → fundedBy → AgencyB
```

Important concepts include IRIs, triples, resources, literals, predicates, namespaces, vocabularies, Turtle, and RDF Schema.

### Hands-On Exercise

Take roughly 50 facts from the PostgreSQL version of the project and rewrite them as RDF/Turtle statements.

```turtle
:communityA
    :locatedIn :countyX .

:libraryA
    :serves :communityA .
```

Then identify places where the relational schema and RDF representation encourage different modeling choices. The important question is not simply whether the same data can be represented. It is whether semantic identifiers and explicit predicates change how I think about interoperability and meaning.

# Stage 7: SPARQL

SPARQL introduces graph-pattern querying over RDF. Rather than treating it as SQL with different punctuation, I should concentrate on triple patterns, optional relationships, graph construction, and property paths.

Learn:

```text
SELECT
WHERE
FILTER
OPTIONAL
UNION
VALUES
BIND
GROUP BY
CONSTRUCT
ASK
```

Then move into property paths.

### Hands-On Exercises

**Exercise 1: Direct relationships**  
Find every organization serving Community A.

**Exercise 2: Multi-hop semantics**  
Find organizations serving communities located in the same county.

**Exercise 3: Institutional pathways**  
Find paths corresponding to:

```text
Community
 → servedBy
 → Organization
 → participatesIn
 → Program
 → fundedBy
 → Agency
```

**Exercise 4: Construct new knowledge**  
Write a `CONSTRUCT` query producing a graph containing organizations and communities connected to workforce programs.

> **Learning objective:** Move beyond retrieving records toward discovering and constructing meaningful semantic subgraphs.

# Stage 8: Property Graphs and Cypher

Now remodel the same ecosystem as a property graph. Instead of starting with rows or RDF triples, work with labeled nodes, relationships, and properties.

```text
(:Community)
(:Organization)
(:Program)
(:County)

(:Organization)-[:SERVES]->(:Community)
(:Organization)-[:PARTICIPATES_IN]->(:Program)
```

### Hands-On Exercise

Implement the dataset in a property-graph environment and begin with direct patterns:

```cypher
MATCH (o:Organization)-[:SERVES]->(c:Community)
RETURN o, c;
```

Then query multi-hop patterns:

```text
Community
   ↑
 SERVES
   |
Organization
   |
PARTICIPATES_IN
   ↓
Program
```

Advance to questions such as:

- Which organizations connect otherwise separate groups of communities?
- Which programs have relationships with organizations serving several counties?
- Which communities appear isolated from particular categories of resources in this modeled network?

At this point, I should consciously stop asking only about attributes and start asking about **structure**.

# Stage 9: GQL

GQL should be approached as a standards-oriented layer rather than simply another syntax to memorize. The goal is to understand the general concepts behind property-graph querying and separate those concepts from the conventions of any one vendor implementation.

Focus on:

- Graph patterns
- Paths
- Labels
- Properties
- Matching
- Filtering
- Graph types

### Hands-On Exercise

Choose ten Cypher queries created during Stage 8. For every query, document:

1. What graph concept is being expressed?
2. Which parts are specific to Cypher syntax?
3. What is the underlying property-graph operation?
4. How would I describe the same intent using GQL concepts?

> **Learning objective:** Understand the abstraction under the syntax well enough to move among implementations without confusing a product's language conventions with graph theory itself.

# Stage 10: Gremlin

Gremlin changes the mental model from primarily describing a graph pattern to explicitly composing a traversal. Apache TinkerPop describes Gremlin as its graph traversal language and characterizes a traversal as a sequence of potentially nested steps (Apache Software Foundation, “Graph Query Language”).

### Hands-On Exercise

Take the conceptual path:

```text
Community
 → Organization
 → Program
 → Agency
```

Express the same intent in Cypher and Gremlin. Then document the difference in reasoning:

- What did the Cypher version ask the system to match?
- Where did the Gremlin traversal start?
- Which edges did it traverse?
- Where did filtering happen?
- What did each expression return?

The objective is not simply syntactic translation. It is learning the difference between **pattern-oriented** and **traversal-oriented** thought.

# Stage 11: Path Querying

Path querying deserves its own stage because paths are fundamental to many questions that make graphs valuable. Study path, simple path, shortest path, reachability, cycles, repeated relationships, bounded paths, unbounded traversal, and regular path expressions.

### Hands-On Exercise

Starting from one rural community, ask:

- Which organizations are reachable within one relationship?
- Which are reachable within two relationships?
- Which are reachable within three?
- What paths connect Community A and Community B?
- Which organizations function as possible bridges between them?

Then introduce relationship constraints:

```text
Community
 → SERVED_BY
 → Organization
 → PARTNERS_WITH*
 → Organization
 → PARTICIPATES_IN
 → Program
```

The repeated `PARTNERS_WITH` portion introduces the idea of a variable-length pathway rather than a fixed set of joins.

# Stage 12: Network Science

Graph querying establishes what is connected. Network science asks what the structure of those relationships may tell us. At this stage, querying becomes the foundation for analysis rather than the endpoint.

Begin with:

- Degree
- Betweenness centrality
- Closeness centrality
- Connected components
- Community detection
- Shortest paths
- PageRank
- Clustering
- Similarity
- Link prediction
- Network flows

### Hands-On Exercises

**Degree:** Which entities have the most direct relationships in the modeled network?

**Betweenness:** Which entities sit on many paths between otherwise separated parts of the network?

**Connected components:** Which portions of the modeled ecosystem are disconnected from one another?

**Community detection:** What clusters emerge from the recorded relationships?

**Shortest paths:** What modeled institutional pathways connect two communities?

**PageRank:** Which nodes gain structural prominence because of the network positions of nodes linking to them?

These measures should initially be treated as structural descriptions, not automatic evidence of importance, effectiveness, influence, or causality. Interpretation requires domain knowledge and, where causal claims are contemplated, appropriate research design.

# Capstone: A DOIN Digital-Opportunity Knowledge Graph

The capstone is a deliberately bounded but real digital-opportunity ecosystem. A learning dataset of approximately **100–250 entities** is a practical target I am proposing for the exercise: large enough to create interesting paths and network structure, but intentionally small enough to inspect manually while learning. This figure is a project-design recommendation rather than a requirement from an external source.

Possible entity classes include:

```text
People
Organizations
Communities
Counties
Schools
Libraries
ISPs
Tribal Nations
State Agencies
Universities
Nonprofits
Programs
Funding Sources
Infrastructure
Research Projects
```

Possible relationships include:

```text
SERVES
LOCATED_IN
FUNDS
PARTNERS_WITH
EMPLOYS
RESEARCHES
OPERATES
PARTICIPATES_IN
PROVIDES_SERVICE_TO
SUPPORTS
```

## Capstone Query Ladder

The capstone should be evaluated through increasingly sophisticated questions rather than by the number of nodes loaded into a database.

### Descriptive

> What organizations operate in this county?

### Relational

> Which organizations serve the same communities?

### Path

> How is this community connected to this state program in the modeled data?

### Deductive

> Under explicitly defined rules, which communities could be connected to workforce resources through partner organizations?

### Structural

> Where does this modeled network contain bridges, clusters, or disconnected components?

### Comparative

> How does the observed institutional network surrounding rural communities differ structurally from the network represented around urban communities?

### Research Hypothesis

> Is greater observed institutional network connectivity associated with stronger digital-opportunity outcomes?

That final question should not be answered from graph structure alone. It establishes a hypothesis that can lead into statistical modeling and, if the research question supports it, a separate causal-inference design.

# Recommended Priority

I would not allocate equal learning effort to every language. For my current work, the priorities should be:

| Priority | Topic | Target |
|---|---|---|
| ★★★★★ | SQL | Fluent |
| ★★★★★ | RDF/SPARQL | Fluent |
| ★★★★★ | Cypher | Fluent |
| ★★★★★ | Path and pattern querying | Deep conceptual understanding |
| ★★★★★ | Network science | Strong |
| ★★★★☆ | Datalog | Conceptually strong |
| ★★★★☆ | GQL | Working knowledge |
| ★★★☆☆ | Gremlin | Working competency |
| ★★★☆☆ | First-order logic | Conceptually strong |
| ★★☆☆☆ | Prolog | Enough to understand logic programming |

This prioritization reflects my intended application rather than a universal curriculum. Someone focused primarily on traversal-oriented applications, RDF interoperability, or deductive databases would reasonably weight the languages differently.

# The Full Learning Progression

```text
                DATA
                  │
        ┌─────────▼─────────┐
        │ Sets & Relations  │
        │Relational Algebra │
        └─────────┬─────────┘
                  │
                 SQL
                  │
            First-Order Logic
                  │
          ┌───────▼───────┐
        Prolog          Datalog
                          │
                         RDF
                          │
                       SPARQL
                          │
              ┌───────────┴───────────┐
              │                       │
        Property Graphs          Traversals
              │                       │
           Cypher                  Gremlin
              │
             GQL
              │
        Path Querying
              │
       Graph Algorithms
              │
       Network Science
              │
       Statistical Models
              │
       Causal Inference
              │
              ▼
     DIGITAL-OPPORTUNITY
        INTELLIGENCE
```

# A Practical Learning Method

For every stage, I should preserve four artifacts in the project repository:

1. **The data model** used at that stage.
2. **Ten or more working queries or rules** ranging from direct retrieval to multi-hop questions.
3. **A query journal** explaining in plain language what each query asks and what assumptions it makes.
4. **A comparison note** recording what became easier, harder, or conceptually different from the previous representation.

This structure turns the repository into more than a code collection. Over time it becomes a record of how the same community system looks through relational, logical, semantic, graph, traversal, network, and statistical lenses. It also creates a provenance habit: each analytical result can be tied back to a data model, query, rule, and assumption rather than presented as unexplained output.

# Conclusion

The real objective of this roadmap is not to be able to say that I know SQL, SPARQL, Cypher, GQL, Gremlin, Datalog, and Prolog. It is to learn to recognize **what kind of question I am actually asking**. Some questions are relational. Others are semantic, deductive, structural, navigational, statistical, or causal. Choosing a language begins with understanding that distinction.

For MiGreatDataLake, this creates a pathway from integrating and organizing data toward expressing shared meaning across sources. For DOIN, it creates a pathway from cataloging organizations and programs toward examining relationships among communities, institutions, capabilities, resources, and knowledge. Network science then makes possible a different class of questions about the structure represented by those relationships, while statistical and causal methods provide the discipline necessary when moving from description and association toward explanation.

The knowledge graph, therefore, should not be viewed as the end product. It can become the connective analytical layer between raw data and more sophisticated inquiry. The progression is ultimately **data → relationships → semantics → knowledge → structure → hypotheses → evidence**. Learning these query languages in sequence makes each transition explicit and gives me a practical way to build, interrogate, and critically evaluate the information systems behind digital-opportunity research and practice.

## Works Cited

Apache Software Foundation. “Graph Query Language: Gremlin.” *Apache TinkerPop*, https://tinkerpop.apache.org/gremlin.html. Accessed 19 Oct. 2026.

Apache Software Foundation. “TinkerPop Documentation.” *Apache TinkerPop*, https://tinkerpop.apache.org/docs/current/reference/. Accessed 19 Oct. 2026.

PostgreSQL Global Development Group. “Part I. Tutorial.” *PostgreSQL 18.6 Documentation*, https://www.postgresql.org/docs/current/tutorial.html. Accessed 19 Oct. 2026.
