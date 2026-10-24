---
layout: page
title: "DOIN Continuous Open Courseware Pilot"
subtitle: "Building Reproducible, Interoperable Learning Infrastructure on MiGreatDataLake"
author: "Jason Kronemeyer"
status: brainstorm
date: 2026-10-24
---

# DOIN Continuous Open Courseware Pilot

## Project Summary

The Digital Opportunities Intelligence Network (DOIN) proposes a pilot to demonstrate a new model for developing, sharing, delivering, and continuously improving open educational resources using MiGreatDataLake as shared learning infrastructure.

Today, digital courseware is often developed as collections of documents, LMS pages, presentations, assessments, videos, and links. Once assembled inside a learning management system, those resources can become difficult to version, reproduce, adapt, move between platforms, or improve systematically. The proposed pilot treats courseware differently: **as open, versioned, testable, interoperable learning infrastructure that can be continuously improved through evidence and community participation.**

The pilot will combine Git-based development and continuous integration/continuous delivery (CI/CD), Calkit-inspired reproducibility and provenance, Common Cartridge for portable course packaging, LTI 1.3 for learning-tool interoperability, Tsugi for interactive learning applications, Moodle for initial delivery, and MiGreatDataLake for governed data, metadata, provenance, and analytical infrastructure.

DOIN will provide the connective intelligence layer, organizing relationships among people, organizations, communities, learning resources, concepts, competencies, tools, adaptations, and evidence.

## Pilot Use Case

The initial proof of concept will use one openly distributable module from **CS204 Web Page Design / Responsive Web Design at Bay Mills Community College**.

The pilot module will focus on semantic and accessible HTML and will include instructional content, learning objectives, activities, assessment criteria, accessibility guidance, and a Tsugi/WebGrader activity providing deterministic HTML assessment and formative feedback.

The complete development cycle will demonstrate:

**Need → Objective → Resource → Git Commit → CI Validation → Human Review → Release → Common Cartridge → Moodle → LTI/Tsugi → Learning Evidence → MiGreatDataLake → Human Interpretation → Revision → New Release**

The objective is not simply to build an HTML autograder. The pilot will test whether an open learning resource can move through an auditable cycle of development, validation, deployment, use, evaluation, and improvement without losing accessibility, licensing, local context, interoperability, privacy, or provenance.

## Technical Architecture

The authoritative source for the courseware will reside in a version-controlled Git repository rather than inside Moodle. Course specifications, instructional content, assessments, rubrics, accessibility resources, metadata, and provenance will be maintained as structured source artifacts.

A CI pipeline will automatically validate:

- course and module structure;
- objective-to-assessment alignment;
- HTML and link integrity;
- accessibility requirements;
- licensing and attribution;
- provenance;
- WebGrader test fixtures; and
- Common Cartridge packaging.

Successful builds will create versioned Common Cartridge release artifacts. Human approval will remain required before publication or deployment.

Moodle will serve as the initial learning-delivery environment. Interactive learning activities will connect through LTI 1.3, initially using Tsugi/WebGrader. PostgreSQL will manage operational application state, while DuckDB will support analytical exploration of governed learning evidence. The architecture will remain compatible with a future DuckLake-based longitudinal analytical layer if scale and research requirements justify it.

MiGreatDataLake will provide shared infrastructure for resource registration, metadata, lineage, governed storage, access control, and approved learning-event data. DOIN will provide the semantic and participation model required to understand how resources, concepts, competencies, communities, adaptations, and evidence relate to one another.

## Open Courseware and Local Adaptation

The pilot will treat Common Cartridge as a **portable release artifact**, not the canonical authoring format.

Each released resource will have a persistent identity and machine-readable information describing its creator, steward, version, license, learning objectives, concepts, accessibility status, technical dependencies, source repository, build provenance, and derivative history.

The model will explicitly support local adaptation. A resource developed at one institution could be forked and contextualized by another while retaining attribution and its relationship to the original resource.

This creates an important distinction between **shared infrastructure and standardized content**. DOIN should make open learning resources easier to discover, adapt, improve, and contribute back without requiring communities to surrender local context or knowledge.

## Governance

The pilot will use a small multidisciplinary governance model with clear accountability for:

- pilot/product stewardship;
- instructional quality;
- technical architecture;
- MiGreatDataLake infrastructure;
- DOIN information stewardship;
- privacy and data governance;
- accessibility;
- OER licensing; and
- community review.

No single role may unilaterally override privacy, licensing, accessibility, security, or instructional-quality controls.

AI may assist with course development, metadata, formative feedback, accessibility drafts, and alternative explanations, but it will not autonomously determine student grades or make consequential student decisions. Objectively testable requirements will use deterministic assessment wherever practical.

Identified learner information will remain within institutionally controlled systems unless an explicitly approved purpose requires otherwise. Shared analytical evidence will use pseudonymous identifiers and data minimization by default.

## Pilot Roadmap

The proposed MVP can be completed in approximately **16 weeks**.

1. **Governance and Scope:** confirm the module, infrastructure, licensing, privacy requirements, and implementation team.
2. **Course Source and Specification:** establish the Git repository, learning objectives, semantic relationships, rubrics, metadata, and provenance.
3. **CI/CD Pipeline:** implement structural, accessibility, licensing, provenance, assessment, and Common Cartridge validation.
4. **Moodle and Tsugi Integration:** demonstrate LTI launch, WebGrader assessment, formative feedback, and grade passback.
5. **DOIN and MiGreatDataLake Integration:** register the resource, its versions and relationships, and ingest approved pseudonymous learning events.
6. **Evidence and Improvement:** analyze the pilot through DuckDB, conduct human review, make one evidence-informed improvement, and release the next version.

## Success Measures

The MVP will be considered successful when it demonstrates:

- 100% traceability from an approved release to its Git commit, build, Common Cartridge artifact, registry record, and Moodle deployment;
- 100% resolved licensing for publicly distributed resources;
- 100% mapping between assessed criteria and identified learning objectives;
- at least 95% successful LTI launch and grade-passback reliability in controlled testing;
- no known critical accessibility or security issues at release;
- correct grading of valid alternative solutions rather than comparison against a single reference solution;
- at least a 30% reduction in instructor grading and repetitive feedback time for the selected activity;
- at least one locally adapted derivative that retains attribution and provenance;
- at least one contribution beyond the original author; and
- at least one documented courseware revision informed by pilot learning evidence.

The most important success measure is the final one: **the system must demonstrate that evidence from one release can responsibly inform a subsequent human-reviewed release.**

## Expected Outcome

The pilot will establish whether DOIN and MiGreatDataLake can support something more consequential than another repository of educational files.

The intended outcome is an open learning infrastructure in which educational resources can be **discovered, forked, adapted, validated, packaged, deployed, evaluated, and continuously improved while preserving their accessibility, licensing, provenance, interoperability, and community context**.

In this model, Git provides versioning and collaboration; CI/CD provides reproducible development; Common Cartridge provides courseware portability; LTI provides learning-tool interoperability; Tsugi provides reusable interactive learning applications; Moodle provides local learning delivery; MiGreatDataLake provides governed statewide infrastructure; and DOIN connects resources to people, communities, concepts, evidence, and meaning.

The pilot therefore represents a practical step from **data infrastructure toward learning infrastructure**: an environment in which open educational resources are not merely published once, but become continuously improvable public knowledge resources shaped by evidence and community participation.
