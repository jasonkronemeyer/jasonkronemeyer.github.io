---
layout: post
status: brainstorming 
title: "The Model Is Not the Database: Why Learning Systems Should Think in Graphs Before They Store Them"
date: 2026-11-12
author: Jason Kronemeyer
description: "A graph model defines how a learning system represents entities and relationships, while a graph database is one possible technology for storing and traversing them. This article explains why DOIN should adopt graph modeling before committing to graph infrastructure."
categories:
  - knowledge-infrastructure
  - educational-technology
  - data-architecture
tags:
  - DOIN
  - Common Cartridge
  - graph model
  - graph database
  - knowledge graph
  - continuous open courseware
  - RDF
  - PostgreSQL
  - Neo4j
---

As I have been thinking through the architecture for a Common Cartridge importer for the Digital Opportunities Intelligence Network, one distinction keeps becoming more important: **a graph model and a graph database are not the same thing**. Confusing the two can lead either to premature technical complexity or, in the opposite direction, to a data model that cannot express the relationships we eventually want the system to understand.

The distinction is fairly simple. A **graph model is a way of representing knowledge**. A **graph database is a technology for storing, querying, and traversing knowledge represented as a graph**. That means we can, and I think should, begin modeling learning content as a graph long before we decide that DOIN needs a dedicated graph database.

## Start With the Learning Content, Not the Database

Consider what happens when we import a course packaged using 1EdTech Common Cartridge. Common Cartridge is an open interoperability standard for packaging and exchanging digital learning materials and assessments among learning-management systems, learning-object repositories, publishers, and other platforms.

A cartridge might give us a structure that looks something like this:

```text
Connected Infrastructure Fundamentals
|
+-- Module: Optical Networking
|   |
|   +-- Lesson: Fiber Optic Fundamentals
|   +-- Lab: Fiber Inspection
|   +-- Assessment: Fiber Basics
|
+-- Module: Passive Optical Networks
```

There is nothing particularly graph-like about that at first glance. It looks like a hierarchy, much like a directory tree. Common Cartridge performs an important job here: it provides a standardized mechanism for packaging and moving the instructional resources and their organization. 1EdTech also supports metadata, assessments, LTI-linked resources, and extensible resource types within different versions and profiles of the standard.

But moving a course and understanding a course are different problems.

Suppose the lesson “Fiber Optic Fundamentals” teaches the concept **optical fiber**. That concept is used in **Passive Optical Networking**, supports a particular **competency**, and that competency is relevant to the role of a **Connected Infrastructure Technician**. Another course elsewhere in the repository might teach the same concept.

Our original tree has suddenly become a network:

```text
[Connected Infrastructure Fundamentals]
                 |
              CONTAINS
                 v
        [Optical Networking]
                 |
              CONTAINS
                 v
      [Fiber Optic Fundamentals]
                 |
               TEACHES
                 v
          [Optical Fiber]
           /           \
    RELATED_TO        USED_IN
        /                 \
 [Ethernet]              [PON]
                           |
                        SUPPORTS
                           v
                      [Competency]
                           |
                      REQUIRED_BY
                           v
             [Connected Infrastructure
                   Technician]
```

That is the point at which the graph **model** becomes useful.

## A Graph Is a Way of Describing the World

A graph model describes information primarily through **entities and their relationships**.

In a property-graph model, entities are represented as nodes and connections between them as relationships. Both can have properties. Neo4j, for example, describes its property-graph model in terms of nodes representing entities, typed and directed relationships connecting those nodes, and key-value properties describing nodes and relationships.

For a learning system, our graph could contain entities such as:

```text
Course
Module
Lesson
Resource
Assessment
Concept
Competency
Standard
Credential
Occupation
Organization
```

And relationships such as:

```text
CONTAINS
TEACHES
ASSESSES
ALIGNS_TO
REQUIRES
PRECEDES
PART_OF
SUPPORTS
RELATED_TO
```

We can therefore express knowledge in a simple form:

```text
Lesson-101  --TEACHES---->  PON
Quiz-003    --ASSESSES--->  PON
PON         --RELATED_TO->  Optical-Fiber
Course-001  --CONTAINS--->  Lesson-101
```

Those relationships constitute a graph whether or not they are stored in a graph database.

## JSON Can Contain a Graph

For the first DOIN Common Cartridge importer, there is no technical requirement to install a graph database simply because we want a graph model.

We could represent the same relationships in ordinary JSON:

```json
{
  "relationships": [
    {
      "subject": "lesson-101",
      "predicate": "teaches",
      "object": "concept-pon"
    },
    {
      "subject": "quiz-003",
      "predicate": "assesses",
      "object": "concept-pon"
    },
    {
      "subject": "concept-pon",
      "predicate": "relatedTo",
      "object": "concept-optical-fiber"
    }
  ]
}
```

That file contains graph-structured information even though it is just JSON.

We could store that representation in GitHub. We could write it to ordinary files. We could put it into PostgreSQL. PostgreSQL's `jsonb` type stores JSON in a decomposed binary representation designed for efficient processing and supports indexing; PostgreSQL also provides operators and GIN indexes for working with structured JSON data.

So the early architecture can remain remarkably simple:

```text
Common Cartridge
       |
       v
     Parser
       |
       v
DOIN Course Model
       |
       v
   course.json
       |
       +-- entities
       +-- relationships
```

We gain the semantics of a graph without taking on the operational complexity of another database platform.

That is an important engineering choice. **Data modeling should not be confused with product selection.**

## So What Does a Graph Database Add?

The answer becomes clearer as the collection grows.

Suppose DOIN eventually knows about thousands of courses, lessons, concepts, assessments, competencies, credentials, standards, occupations, organizations, and communities. We may want to ask:

> Which courses teach concepts associated with competencies required by a particular occupation?

That question involves a path:

```text
Course
  | TEACHES
  v
Concept
  | SUPPORTS
  v
Competency
  | REQUIRED_BY
  v
Occupation
```

Or perhaps we want to know:

> What is the shortest learning pathway from the competencies someone already has to the competencies necessary for a Connected Infrastructure Technician role?

Now the *connections* among records are becoming at least as important as the records themselves.

This is where a graph database starts earning its place. In a property graph such as that used by Neo4j, relationships are explicitly stored as typed connections between nodes rather than being merely reconstructed conceptually by the application. The graph model makes queries over connected entities a natural part of the database design.

That does not mean a relational system cannot answer such questions. It can. We might construct relational tables such as:

```text
courses
lessons
concepts
competencies
occupations

course_lessons
lesson_concepts
concept_competencies
competency_occupations
```

Then we use joins to reconstruct the connections.

A graph database changes the center of gravity. The relationship is no longer only something we reconstruct through foreign keys and joining tables. It becomes a first-class element of the stored model.

A practical rule follows:

> **Relational databases are often strongest when our primary concern is the records and transactions. Graph databases become increasingly compelling when our primary questions concern paths and relationships among records.**

That is not an argument for replacing relational databases with graph databases. It is an argument for choosing storage technology according to the questions the system actually needs to answer.

## The Threshold Is Cross-Course Intelligence

For DOIN, I would draw the boundary at **cross-course intelligence**.

We do not need a graph database to answer:

> What resources are contained in this course?

The canonical course model can answer that easily.

We become much more interested in graph infrastructure when we start asking:

> What resources across every course teach this concept?

Or:

> What assessments provide evidence of this competency?

Or:

> Which credentials incorporate competencies associated with this occupation?

Or:

> Which learning resources could fill a gap between two stages of a learning pathway?

The graph might then look like this:

```text
[Course]
    |
  TEACHES
    v
[Concept]
    |
 SUPPORTS
    v
[Competency]
    |
 ALIGNS_TO
    v
[Standard]
    |
 SUPPORTS
    v
[Credential]
    |
 PREPARES_FOR
    v
[Occupation]
```

At that point the system has moved beyond **course interchange** into **knowledge discovery**.

That is when I would revisit whether Neo4j, an RDF store, a graph extension for an existing data platform, or some other graph architecture is justified. The decision should follow the demonstrated query requirements, rather than precede them.

## Property Graphs Are Not the Only Graphs

There is another reason not to choose a graph database too early: we have not yet decided what kind of knowledge graph DOIN ultimately needs.

The property-graph model is intuitive:

```text
(Course)-[TEACHES]->(Concept)
```

Nodes and relationships can carry properties, making the approach particularly approachable for application development and connected-data traversal. Neo4j is a prominent example of this approach.

But another possibility is the Resource Description Framework, or RDF.

The World Wide Web Consortium defines RDF graphs as sets of **subject-predicate-object triples** used to describe resources.

That maps remarkably well to our conceptual representation:

```text
Course123   teaches       PON
PON         relatedTo     OpticalFiber
Quiz456     assesses      PON
```

RDF is particularly interesting when the objective is not only application navigation but **semantic interoperability**, shared vocabularies, linked data, and machine-readable knowledge that can connect across organizational or system boundaries. The W3C's RDF model is explicitly an abstract data model, underscoring the same distinction between how information is modeled and the particular technology used to persist it.

For DOIN, that deserves careful consideration.

## The Architecture Should Preserve the Choice

Rather than deciding today that DOIN “is a Neo4j application” or “is an RDF system,” I would establish a neutral semantic boundary.

```text
                       DOIN SEMANTIC MODEL
                               |
                    Entities + Relationships
                               |
              +----------------+----------------+
              v                v                v
            JSON           PostgreSQL       Graph Store
                                                  |
                                        +---------+---------+
                                        v                   v
                                  Property Graph           RDF
```

The canonical model should tell us what something **is** and how it **relates** to other things.

Storage should remain an implementation choice below that boundary.

That protects us from an easy architectural mistake: embedding one database vendor's way of thinking into the fundamental representation of educational knowledge.

## From Course Packages to Knowledge Infrastructure

This also clarifies the role of Common Cartridge.

1EdTech defines Common Cartridge as a mechanism for packaging and exchanging digital learning resources and assessments and for supporting interoperability among learning systems. That makes it an excellent interchange layer. It does not need to become our entire knowledge model.

I envision the layers this way:

```text
+---------------------------------+
|       INTERCHANGE LAYER         |
|                                 |
| Common Cartridge                |
| Git/Open Courseware             |
| Future educational formats      |
+----------------+----------------+
                 v
+---------------------------------+
|        CANONICAL LAYER          |
|                                 |
| Courses                         |
| Resources                       |
| Assessments                     |
| Relationships                   |
| Provenance                      |
+----------------+----------------+
                 v
+---------------------------------+
|         SEMANTIC LAYER          |
|                                 |
| Concepts                        |
| Competencies                    |
| Standards                       |
| Credentials                     |
| Occupations                     |
| Organizations                   |
+----------------+----------------+
                 v
+---------------------------------+
|       INTELLIGENCE LAYER        |
|                                 |
| Discovery                       |
| Learning pathways               |
| Gap analysis                    |
| Semantic search                 |
| Recommendations                 |
| AI and agents                   |
+---------------------------------+
```

The Common Cartridge importer serves the first transition. It gets learning content into a predictable representation.

The graph model prepares the second. It gives us a way to say what those resources mean in relationship to one another.

A graph database may eventually help power the third and fourth layers at scale.

Those are related architectural decisions, but they are not the same decision.

## Teach the Relationships Before Choosing the Database

This distinction also connects directly to my **First Five Things to Teach a Computer** framework. If we want a computer to do something meaningful with institutional knowledge, identifying the things is only the beginning. The system also needs properties, relationships, context, and rules.

An educational resource called “Fiber Optic Fundamentals” is useful.

Knowing that it:

```text
TEACHES -> Optical Fiber
SUPPORTS -> Fiber Installation Competency
PRECEDES -> Passive Optical Networking
CONTRIBUTES_TO -> Connected Infrastructure Technician Pathway
```

makes it considerably more useful.

The graph model gives us the language to express those relationships.

The graph database is simply one possible machine for operating on them.

That leads to what I think should be a foundational principle for DOIN and for the Continuous Open Courseware architecture:

> **Model the knowledge as a graph before deciding whether you need to store it in a graph database.**

For the first Common Cartridge importer, that means keeping the engineering modest. Parse the cartridge. Normalize the course. Preserve identifiers and provenance. Represent relationships explicitly. Store the result in JSON or a conventional database if that is sufficient.

Then pay attention to the questions people begin asking.

When those questions stop being primarily “What's in this course?” and increasingly become “How is this connected to everything else?”, we will know why we need the graph database rather than merely having one because graph databases sounded like the right architecture.

And that difference matters. It lets DOIN develop from **course interchange into knowledge infrastructure** without requiring us to pretend that we already know exactly what its final database will look like.

## References

1. [1EdTech: Common Cartridge](https://www.1edtech.org/standards/cc)
2. [1EdTech Common Cartridge 1.4 Implementation Guide](https://www.imsglobal.org/spec/cc/v1p4/impl/)
3. [Neo4j Documentation: Graph Database Concepts](https://neo4j.com/docs/getting-started/graph-database/)
4. [W3C: RDF 1.2 Concepts and Abstract Data Model](https://www.w3.org/TR/rdf12-concepts/)
5. [PostgreSQL Documentation: JSON Types](https://www.postgresql.org/docs/current/datatype-json.html)
6. [PostgreSQL Documentation: GIN Indexes](https://www.postgresql.org/docs/current/gin.html)
