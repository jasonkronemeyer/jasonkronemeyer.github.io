---
layout: null
---

# Technical Specification: Repository-Wide Contribution and Threaded Discussion Framework

**Repository:** `jasonkronemeyer/jasonkronemeyer.github.io`  
**Prototype branch:** `prototype/contribution-framework`  
**Delivery:** Draft pull request only, with no automatic merge  
**Status:** Prototype specification

## 1. Purpose

Prototype a reusable contribution and discussion framework for Jason Kronemeyer's Jekyll-based public knowledge repository. The framework will make eligible articles, research notes, development notes, maps, prototypes, frameworks, and other documents open to structured review, correction, evidence submission, discussion, and revision.

The initial implementation must add a context-aware contribution panel to the bottom of eligible rendered pages. It must also establish the architecture for expandable, nested, newsgroup-style discussions that can remain associated with the document and, when technically practical, be explored without leaving the page.

The site should evolve from a publication pipeline into a versioned participation and provenance system:

```text
Idea -> Note -> Evidence -> Discussion -> Issue -> Pull Request -> Revision -> Publication
```

## 2. Scope

### 2.1 Phase 1: Required in this prototype

- Inspect and document the existing Jekyll architecture.
- Build a reusable contribution panel.
- Generate document-aware links for editing, issues, evidence, discussions, source, and history.
- Add site defaults and page-level front-matter controls.
- Add intellectual-property review safeguards.
- Create contribution documentation, issue forms, and a pull-request template.
- Demonstrate the framework on a small representative sample.
- Establish the data model and accessible interface shell for nested discussions.
- Use GitHub as the system of record.
- Build, validate, and open a draft pull request.

### 2.2 Phase 2: Architect now, implement only if feasible and explicitly approved

- Retrieve discussion data from an appropriate GitHub interface.
- Render expandable top-level threads and nested replies on the document page.
- Provide branch-level expand and collapse behavior.
- Support in-context reading while preserving canonical links to GitHub.
- Add authenticated reply behavior only through a secure GitHub-supported flow.

### 2.3 Out of scope for the initial prototype

- A custom comments database.
- A custom identity or account system.
- Client-side private tokens.
- Automatic repository-wide front-matter migration.
- Automatic enabling of GitHub Discussions.
- Automatic merging into the default branch.
- Public release of content marked for intellectual-property review.

## 3. Recommended GitHub Copilot Model Strategy

Use the strongest reasoning and coding model available in the GitHub Copilot model picker for the initial architecture and implementation. Prefer a model that is optimized for agentic software development, repository-wide reasoning, terminal use, multi-file editing, and test-driven verification.

Because GitHub Copilot model availability varies by plan, client, policy, and release date, do not hard-code an unverified model identifier. In Visual Studio Code, use the custom-agent `model:` autocomplete to choose an available model. If the project-specific custom agent must remain portable, omit `model:` so it inherits the selected or default model.

### Required model competencies

The selected model should be demonstrably strong at:

- multi-file repository analysis;
- Jekyll and Liquid templating;
- YAML front matter and configuration inheritance;
- GitHub URLs, Issues, Discussions, and pull requests;
- accessible HTML, CSS, and JavaScript;
- API capability analysis and graceful degradation;
- branch-based Git workflows;
- build, test, and link verification;
- security and secret-management reasoning; and
- documenting assumptions, limitations, and rollback procedures.

Use a faster, lower-cost model only for bounded follow-up work such as wording changes, repetitive metadata updates, or minor CSS adjustments.

## 4. Required Agent Competencies

The coding agent must understand:

### 4.1 Jekyll

- layout inheritance;
- Liquid templates, filters, conditionals, and variable precedence;
- `_includes`, `_layouts`, `_data`, `_config.yml`, and custom collections;
- YAML front matter and defaults;
- user sites versus project sites;
- `url`, `baseurl`, permalinks, canonical URLs, and GitHub Pages constraints;
- local and GitHub Actions build workflows.

### 4.2 GitHub collaboration

- branch-based development;
- document-aware edit, blob, and history URLs;
- Issues and issue forms;
- GitHub Discussions;
- pull requests and review workflows;
- query-string construction and URL encoding;
- repository permissions and settings;
- authentication boundaries and rate limits;
- graceful behavior when Issues or Discussions are unavailable.

### 4.3 Content and metadata

The agent must distinguish among published articles, research notes, development notes, maps, datasets, prototypes, frameworks, early-stage ideas, archived documents, and documents closed to public contribution.

### 4.4 Accessibility

The agent must implement semantic HTML, keyboard operation, visible focus states, sufficient contrast, descriptive labels, responsive rendering, screen-reader support, reduced-motion compatibility, and accessible loading and error states.

### 4.5 Security and intellectual property

The agent must not expose secrets, add tokens to client-side code, change repository visibility, publish private content, enable protected content for contribution, add unreviewed third-party scripts, or represent technical controls as legal patent protection.

## 5. Branch and Delivery Requirements

Use branch:

```text
prototype/contribution-framework
```

If it already exists, use:

```text
prototype/contribution-framework-v2
```

The agent must:

1. inspect the repository before editing;
2. summarize the current architecture;
3. create the prototype branch;
4. make small, logical commits;
5. run the documented build and tests;
6. push the branch;
7. open a draft pull request;
8. include screenshots or previews where feasible;
9. list required manual settings separately; and
10. stop without merging.

Suggested commits:

```text
feat: add reusable contribution panel
feat: add contribution metadata and defaults
feat: add threaded discussion interface shell
feat: add issue forms and pull request template
docs: add contribution and intellectual property guidance
test: add contribution link and rendering validation
style: add responsive contribution and discussion styles
```

## 6. Discovery Phase

Inspect at minimum:

```text
_config.yml
Gemfile
Gemfile.lock
.github/
_includes/
_layouts/
_data/
_sass/
assets/
_posts/
all custom collection directories
```

Identify:

- default branch and publishing source;
- Jekyll theme or remote theme;
- layout inheritance;
- custom collections and defaults;
- permalink, URL, and base URL behavior;
- CSS or Sass conventions;
- existing components and scripts;
- GitHub Actions and Pages deployment;
- existing issue, PR, contribution, license, and code-of-conduct files;
- whether Discussions are enabled;
- pages that must not display contribution controls;
- whether Content Security Policy or JavaScript restrictions apply.

Include the findings in the draft pull request.

## 7. Functional Requirements

### FR-1: Reusable contribution include

Create:

```text
_includes/contribution-panel.html
```

Render it from site defaults, page front matter, and discoverable repository metadata. Avoid hard-coding the current repository when a reliable configurable value is available.

### FR-2: Layout integration

Insert the component into the lowest appropriate shared layout so it appears after substantive content and before the global footer. Do not edit hundreds of Markdown files individually.

```liquid
{% unless page.contributions.enabled == false %}
  {% include contribution-panel.html %}
{% endunless %}
```

### FR-3: Contribution actions

Support configurable actions for:

- Suggest an edit
- Report a correction
- Propose evidence or a citation
- Ask a question
- Discuss this work
- View source
- View history

### FR-4: Document-aware URLs

Generate links for the current source document:

```text
https://github.com/OWNER/REPOSITORY/edit/BRANCH/PATH
https://github.com/OWNER/REPOSITORY/blob/BRANCH/PATH
https://github.com/OWNER/REPOSITORY/commits/BRANCH/PATH
```

Issue links should prepopulate the document title, public URL, source path, contribution category, privacy warning, and relevant checklist.

### FR-5: Safe URL encoding

URL-encode all dynamic titles, paths, labels, and query values. Test spaces, apostrophes, colons, ampersands, question marks, parentheses, and Unicode.

### FR-6: Status display

Optionally display document type, maturity, version, last-reviewed date, contribution status, peer-review status, and applicable license or terms.

### FR-7: Content-specific language

Use contribution prompts appropriate to the document type:

- **Article:** corrections and supported alternative interpretations.
- **Research note:** evidence, citations, methodological critiques, and alternative interpretations.
- **Development note:** code corrections, reproducibility findings, and improved technical approaches.
- **Prototype:** defects, accessibility concerns, unexpected behavior, and proposed improvements.
- **Map:** location errors, missing context, data-quality concerns, and relevant source data.
- **Framework:** terminology, assumptions, relationships, evidence, and practical applications.
- **Early-stage idea:** limited contribution pending authorship, disclosure, or IP review.

### FR-8: Front-matter controls

Support:

```yaml
contributions:
  enabled: true
  edit: true
  issues: true
  evidence: true
  questions: true
  discussions: true
  source: true
  history: true
  peer_review: true
  status: open
```

Allow individual actions or the entire component to be disabled.

### FR-9: Intellectual-property controls

Support:

```yaml
intellectual_property:
  review_required: false
  public_disclosure_approved: true
```

If `review_required` is `true` or `public_disclosure_approved` is `false`, suppress public edit, issue, and discussion prompts by default and display a neutral closed-contribution notice. This is a workflow safeguard, not legal protection or patent advice.

### FR-10: Site defaults

Add site-level defaults through `_config.yml` or an appropriate data file:

```yaml
github_repository:
  owner: jasonkronemeyer
  name: jasonkronemeyer.github.io
  default_branch: main
  discussions_enabled: false

contribution_defaults:
  enabled: true
  edit: true
  issues: true
  evidence: true
  questions: true
  discussions: true
  source: true
  history: true
  peer_review: false
  status: open
```

First determine whether equivalent data already exists.

### FR-11: Cross-repository portability

Support future project repositories and page-level source overrides:

```yaml
source_repository:
  owner: jasonkronemeyer
  name: another-repository
  branch: main
  path: docs/example.md
```

Do not assume every page belongs to `jasonkronemeyer.github.io`.

### FR-12: Expandable Nested Discussion Interface

The framework must establish a threaded discussion experience modeled on classic Internet newsgroups. Conversations must be represented as trees, not deliberately flattened into a single chronological stream.

#### FR-12.1 Interaction model

Readers should be able to remain on the document while exploring its conversation:

```text
Discuss this work
7 threads · 23 replies

▼ Evidence supporting this claim
   Initial message

   └─ Reply
      └─ Nested reply
         [Reply]

▶ Question about the methodology     4 replies
▶ Application to rural schools       7 replies

[Start a new discussion]
```

#### FR-12.2 Required capabilities

The architecture and interface shell must support:

- expandable and collapsible top-level threads;
- nested replies preserving parent-child relationships;
- independent expansion and collapse of reply branches;
- a reply action associated with the message being answered;
- thread and reply counts;
- author and timestamp display;
- permanent links to individual contributions;
- keyboard-accessible disclosure controls;
- mobile-readable rendering;
- graceful handling of deleted, hidden, locked, or moderated content;
- loading, empty, unavailable, and error states;
- a canonical link to the full conversation on GitHub;
- optional controls for Expand all, Collapse all, Newest, Oldest, and Most active.

#### FR-12.3 Progressive disclosure

Render long conversations in a collapsed summary by default. Expanding a thread must not navigate away from the document. Expanding one reply branch should not require expanding every branch.

#### FR-12.4 Deep nesting

Preserve logical reply depth, but cap visual indentation after approximately three or four levels. At greater depths, use styling such as connector lines, compact labels, or branch markers rather than continuing to reduce content width.

#### FR-12.5 Progressive enhancement

JavaScript may enhance the discussion interface, but:

- the document and core contribution links must work without JavaScript;
- a failed discussion request must not block page rendering;
- accessible loading and error states are required;
- failure must fall back to the canonical GitHub Discussion;
- no framework should be introduced unless justified by the existing site architecture.

#### FR-12.6 System of record

Do not build a custom discussion database. Use GitHub as the preferred identity, moderation, notification, and discussion system of record. Before implementing embedded synchronization or replies, investigate and document the actual capabilities, reply-depth behavior, authentication requirements, rate limits, and constraints of the selected GitHub interface.

If the provider cannot preserve arbitrary nested replies, document that limitation and do not simulate false hierarchy.

#### FR-12.7 Authentication and secrets

Never embed a personal access token, private API token, repository credential, or secret in Jekyll configuration, rendered HTML, JavaScript, CSS, or public repository files. If authenticated writing is required, use a secure GitHub-supported authentication flow or send the user to the canonical GitHub interface.

#### FR-12.8 Document association

Every discussion must be traceable to its originating document. Support metadata such as:

```yaml
discussion:
  enabled: true
  provider: github
  id:
  category:
  embedded: true
  threading: nested
```

Avoid manual identifiers when they can be derived or managed reliably.

#### FR-12.9 Prototype boundary

Phase 1 must implement the accessible discussion summary/interface shell and canonical links. Full embedded retrieval and reply behavior should be implemented only if repository discovery confirms a clean, secure, maintainable approach and the pull request clearly separates optional work from the baseline contribution panel.

### FR-13: Discussion as Provenance

Treat meaningful discussions as part of the intellectual provenance of a document.

The architecture must support eventual relationships among:

```text
Claim -> Question -> Discussion -> Evidence -> Issue -> Pull Request -> Revision
```

#### FR-13.1 Distinct semantics

- **Discussion:** interpretation, questions, reasoning, and exploration.
- **Issue:** a defined correction, evidence gap, defect, or requested work.
- **Pull request:** a concrete proposed modification.
- **Revision:** an accepted change incorporated into repository history.

Do not collapse these objects into one workflow.

#### FR-13.2 Cross-references

Where practical, preserve links among related objects:

```text
Discussion #42 -> Issue #57 -> Pull Request #63 -> Document version 0.5
```

Do not automatically delete or close the originating discussion when a revision is accepted. The conversation may explain why the document changed.

#### FR-13.3 Provenance metadata

Design for optional metadata such as:

```yaml
provenance:
  discussions: []
  issues: []
  pull_requests: []
  supersedes:
  revised_from:
```

Do not require manual duplication when relationships can be derived reliably through GitHub references or build-time data.

#### FR-13.4 Future graph representation

Keep identifiers stable enough that future systems can express document, claim, evidence, discussion, issue, pull request, contributor, and revision relationships as connected data. Do not require a graph database in this prototype.

## 8. Representative Front Matter

```yaml
---
layout: research-note
title: "Example Research Note"
description: "A concise description."

document:
  type: research-note
  status: active-research
  version: "0.4"
  last_reviewed: 2026-10-22

contributions:
  enabled: true
  edit: true
  issues: true
  evidence: true
  questions: true
  discussions: true
  source: true
  history: true
  peer_review: true
  status: open

discussion:
  enabled: true
  provider: github
  embedded: true
  threading: nested

intellectual_property:
  review_required: false
  public_disclosure_approved: true
---
```

Demonstrate on a small sample: one article, research note, development note, prototype, map, contribution-disabled page, and IP-review page.

## 9. GitHub Collaboration Files

Create or revise:

```text
CONTRIBUTING.md
.github/ISSUE_TEMPLATE/correction.yml
.github/ISSUE_TEMPLATE/evidence.yml
.github/ISSUE_TEMPLATE/question.yml
.github/ISSUE_TEMPLATE/technical-problem.yml
.github/ISSUE_TEMPLATE/config.yml
.github/pull_request_template.md
```

`CONTRIBUTING.md` must address accepted contributions, small edits, evidence and citations, conceptual discussions, review expectations, respectful participation, authorship, attribution, contribution licensing, material AI assistance, confidentiality, and patent-sensitive submissions.

Recommend manual Discussion categories:

- Announcements
- Questions
- Ideas and Frameworks
- Research and Evidence
- Prototypes and Technical Work
- Maps and Spatial Data
- Show and Tell
- General

Do not assume categories can be configured through repository files.

## 10. Visual and Interaction Requirements

The contribution area should be distinct but restrained, inherit the site's typography and colors, avoid unnecessary dependencies, provide usable mobile tap targets, print cleanly, and remain functional without JavaScript.

Suggested structure:

```text
Contribute to this work
[status, version, review state]
[context-specific invitation]
[Suggest an edit] [Report a correction] [Propose evidence]
[Ask a question] [Discuss] [View source] [View history]

Discuss this work
[thread summaries with expandable nested replies]

Contribution guidelines | Code of conduct | License
```

## 11. Testing Requirements

### 11.1 Build

Run the repository's documented build. If none exists, attempt the appropriate equivalent of:

```bash
bundle exec jekyll build
```

Document exact environmental failures rather than masking them.

### 11.2 Component tests

Verify:

- eligible pages show the panel exactly once;
- excluded pages do not show it;
- source paths, repositories, and branches are correct;
- site and page overrides work;
- IP-review pages suppress public actions;
- no raw Liquid appears in output;
- issue data is correctly encoded;
- discussion shell renders all defined states.

### 11.3 Threading and accessibility tests

Verify:

- threads and branches expand and collapse independently;
- `aria-expanded`, labels, focus order, and keyboard behavior are correct;
- logical hierarchy is preserved where the provider supports it;
- deep threads do not create unusable indentation;
- mobile rendering remains readable;
- reduced-motion preferences are respected;
- failures fall back to the canonical discussion;
- no credentials appear in generated files or network calls.

### 11.4 Regression tests

Confirm no breakage to navigation, pagination, collections, maps, prototypes, syntax highlighting, feeds, sitemap, SEO metadata, canonical URLs, or Pages deployment.

## 12. Acceptance Criteria

The prototype is complete when:

1. A reusable contribution include exists.
2. It renders on representative content types.
3. Page-level settings can disable it or individual actions.
4. Edit, source, and history links target the correct file.
5. Issue links retain document context.
6. IP-review metadata suppresses public contribution actions.
7. The component is accessible and responsive.
8. Contribution guidance and GitHub templates are present.
9. A discussion interface shell is present on eligible pages.
10. Threads can be expanded and collapsed independently in the implemented shell.
11. Nested parent-child relationships are preserved where supported.
12. Deep nesting does not cause excessive indentation.
13. Discussion controls work by keyboard.
14. Discussion loading failure does not affect article rendering.
15. No private credential is exposed client-side.
16. Every discussion is associated with its originating document.
17. Users can reach the canonical GitHub conversation.
18. The design can trace discussion to issue, pull request, and revision.
19. The Jekyll build succeeds or the exact environmental limitation is documented.
20. The branch is pushed and a draft pull request is opened.
21. The pull request contains architecture findings, previews, tests, limitations, manual settings, rollback instructions, and next-phase recommendations.
22. No automatic merge occurs.

## 13. Custom Copilot Agent

Create:

```text
.github/agents/jekyll-collaboration-architect.agent.md
```

Suggested profile:

```markdown
---
name: Jekyll Collaboration Architect
description: Designs, implements, tests, and documents contribution and threaded discussion features for this Jekyll knowledge repository.
# Select an available agentic coding model with repository-wide reasoning,
# or omit model to inherit the current/default model.
---

You are the collaboration architect for Jason Kronemeyer's Jekyll-based public knowledge repository.

Inspect the repository before editing. Prefer reusable includes, shared layouts, site defaults, and page-level overrides. Preserve existing content, authorship, attribution, MLA citations, design conventions, and build behavior.

Implement document-aware contribution features and an accessible shell for expandable nested discussion. Use GitHub as the system of record. Do not build a custom comments database. Do not flatten reply relationships that the provider exposes. Do not invent nesting the provider does not support.

Never expose credentials, private content, or patent-sensitive material. Pages marked for intellectual-property review must not invite public contribution. Do not change repository visibility, enable Discussions automatically, merge, or publish protected material.

Build and test the site. Validate URLs, keyboard behavior, responsive rendering, error handling, and graceful fallback. Make small commits and open a draft pull request with findings, previews, test results, limitations, manual settings, rollback instructions, and next-phase recommendations. Stop before merge.
```

GitHub custom agents are repository-level Markdown profiles with YAML front matter. The `model` property is optional; if omitted, the agent inherits the default model.

## 14. Repository-Wide Copilot Instructions

Create or update:

```text
.github/copilot-instructions.md
```

Include repository purpose, Jekyll conventions, content-preservation requirements, Jason Kronemeyer's authorship of the First Five framework, MLA 9 preservation, contribution controls, discussion architecture, IP safeguards, branch workflow, build commands, tests, and the prohibition against automatic merge.

## 15. Agent Execution Prompt

```text
Using the Jekyll Collaboration Architect custom agent, implement the repository-wide contribution and threaded discussion prototype described in the technical specification.

Work only in a new branch named prototype/contribution-framework. Do not merge changes into the default branch.

Begin by inspecting and documenting the current Jekyll architecture, collections, layouts, includes, theme, styles, builds, repository metadata, collaboration files, and GitHub Discussions status.

Implement a reusable, accessible contribution panel at the bottom of eligible documents. Generate document-aware actions for edits, corrections, evidence, questions, discussions, source, and history. Use site defaults and page-level overrides. Include document status, maturity, version, peer-review status, and intellectual-property controls. Content requiring IP review must not display public contribution actions.

Implement the accessible interface shell and data model for expandable top-level threads and nested replies. Preserve parent-child relationships, support independent branch expansion, cap visual indentation, retain canonical GitHub links, and fail gracefully. Use GitHub as the system of record. Do not build a custom comments database or expose credentials. Fully embedded retrieval or reply behavior is optional and must only be added if repository investigation confirms a secure, maintainable provider capability.

Create or update CONTRIBUTING.md, issue forms, the pull-request template, the custom Copilot agent, repository Copilot instructions, and supporting documentation. Recommend manual Discussion categories but do not enable settings automatically.

Demonstrate the system on a small representative sample. Do not perform a repository-wide front-matter migration.

Build and test the site. Validate generated URLs, responsive behavior, keyboard operation, nested discussion states, error fallback, and regression safety. Make small commits, push the branch, and open a draft pull request containing architecture findings, screenshots or previews, tests, limitations, manual settings, rollback instructions, and next-phase recommendations.

Stop after opening the draft pull request. Do not merge it.
```

## 16. Implementation Principle

The smallest successful prototype should establish a stable foundation for:

```text
Document
  -> Contribution panel
  -> Discussion summary and canonical link
  -> Expandable nested conversation interface
  -> Evidence and issue relationships
  -> Pull request and revision provenance
```

The discussion layer is not a generic comment section. It is part of the documented evolution of the knowledge itself.
