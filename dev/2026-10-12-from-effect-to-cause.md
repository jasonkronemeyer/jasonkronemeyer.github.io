---
layout: research-note
status: draft
title: "From Effect to Cause: A Better Path to AI Readiness"
subtitle: "What Judea Pearl, Toyota, and Kentaro Toyama can teach us about causality, process knowledge, and what we should teach computers first"
author: "Jason Kronemeyer"
date: 2026-10-12
description: "AI readiness may begin before AI. By connecting causal reasoning, Toyota's approach to understanding work, Kentaro Toyama's amplification theory, and the First Five Things to Teach a Computer, we can trace a path from observed effects to better interventions and organizational learning."
---

# From Effect to Cause: A Better Path to AI Readiness

## What Judea Pearl, Toyota, and Kentaro Toyama can teach us about causality, process knowledge, and what we should teach computers first

**By Jason Kronemeyer**

> ### The question that started this
>
> **How would Judea Pearl, Toyota, and Kentaro Toyama explain the pathway from effect to cause?**

We are surrounded by effects.

A new technology is introduced and performance improves. A school adopts an AI platform and some teachers embrace it while others do not. A community gains broadband, but the outcomes we expected do not automatically follow. An organization buys better tools, yet the underlying work remains stubbornly difficult.

Our instinct is often to observe the visible change and assign a cause.

But an effect is not an explanation.

I have been thinking about this distinction through three bodies of work that come from very different traditions: Judea Pearl's causal reasoning, the Toyota Production System, and Kentaro Toyama's theory of technology as an amplifier. None of these sources proposes the framework I develop here. Each contributes a different piece of the problem.

Pearl gives us a language for distinguishing association from intervention and counterfactual reasoning. Toyota gives us a model in which work is understood and improved before that understanding is incorporated into machines. Toyama reminds us that technology does not arrive in a vacuum; its effects depend on the human and institutional forces it amplifies.

When I connect those ideas, I arrive at a broader proposition:

> **The pathway to AI readiness may not begin with AI at all. It may begin with our ability to move from an observed effect toward a defensible understanding of its cause.**

That proposition is my synthesis. It provides the bridge from these established bodies of work to my own **First Five Things to Teach a Computer** framework and, more recently, to the thinking behind **Compass Next**.

---

## Pearl: Seeing Something Is Not the Same as Causing It

Judea Pearl gives us perhaps the clearest place to begin.

Pearl's causal hierarchy distinguishes three levels: **association, intervention, and counterfactuals**. He characterizes their typical activities as seeing, doing, and imagining or retrospection. At the associational level, we ask what observing one thing tells us about another. At the interventional level, we ask what would happen if we deliberately changed something. At the counterfactual level, we can ask retrospective questions such as whether *X* caused *Y* and what would have happened had we acted differently (Pearl, "Three Layer"). 【1-8472b9】

Imagine that students who use an AI tutor perform better academically.

We have observed something:

> **AI use ↔ higher performance**

But the observation alone does not establish that AI caused the improvement.

Pearl is explicit about this distinction. Statistical analysis can describe associations under observed conditions, while causal analysis asks about changes produced by treatments or external interventions. He argues that causal conclusions cannot be substantiated from associations alone; a causal conclusion necessarily depends on causal assumptions that observational data alone cannot establish (Pearl, "Causal Inference" 99–101). 【2-88096b】

That makes the next question substantially different from simply looking for another correlation:

> **What happens if we deliberately change X?**

Now we have moved from observing to intervening.

And Pearl gives us another move beyond intervention:

> **Would Y have been different had X been different?**

That is counterfactual reasoning.

Pearl's hierarchy therefore gives us a progression from observing the world toward increasingly powerful kinds of causal questions. The higher levels cannot simply be recovered from lower-level observational information alone (Pearl, "Three Layer"). 【1-8472b9】

For me, that distinction becomes particularly important in the age of AI.

A system can discover a pattern. A person can see a pattern. An organization can measure a pattern.

None of those facts, by themselves, tell us why the pattern exists.

That last observation is my interpretation of Pearl's framework and its relevance to AI readiness. Pearl provides the causal distinction. I am applying it to the problem of what organizations need to understand before using AI to make or inform decisions.

---

## Toyota: Understand the Work Before Putting It Into the Machine

Toyota approaches the relationship between people, processes, and machines from a very different direction.

The Toyota Production System describes *jidoka* as "automation with a human touch." More importantly for this discussion, Toyota explains that creating such machines begins with people being able to perform the work smoothly and correctly by hand, identify abnormalities in that work, implement *kaizen*, eliminate waste and inconsistency, and only then build the appropriate understanding into machines ("Toyota Production System"). 【3-3fbcac】【4-f34b7e】

There is an important sequence embedded in that description:

**Do the work.**

**Understand the work.**

**Improve the work.**

**Recognize abnormalities in the work.**

**Then incorporate that understanding into the machine.**

Toyota's source describes those principles in a manufacturing context. It does not describe them as an AI-readiness framework.

The connection to AI is mine.

And that connection leads me to put Toyota's principle into contemporary language this way:

> **Understand the work before trying to teach the machine the work.**

Think about what happens when we reverse that sequence.

Suppose a school introduces an AI system and teachers do not use it.

The visible effect is:

> **Low AI adoption.**

We might immediately diagnose the problem as insufficient AI training.

But what if we move deeper into the work?

Perhaps teachers do not know where the AI belongs within instruction.

Perhaps that is because existing instructional processes were never examined in relation to AI.

Perhaps those processes contain knowledge that experienced educators understand intuitively but that has never been articulated.

Now we have a substantially different problem.

The initial intervention might have been:

> **Provide more AI training.**

The deeper question becomes:

> **Do we understand the instructional process well enough to determine what, if anything, should be delegated to or supported by AI?**

That school example and the questions arising from it are mine. They are not Toyota findings.

Toyota contributes something more foundational: a documented philosophy in which human understanding and improvement of work precede incorporating that understanding into machines. Toyota further states that machines, robots, and IT do not implement *kaizen* by themselves, emphasizing the continuing role of human wisdom and ingenuity ("Toyota Production System"). 【3-3fbcac】

For AI readiness, I think that is a profound idea.

---

## Toyama: Look Beneath the Technology

Kentaro Toyama gives us another way to move beneath the visible effect.

In "Technology as Amplifier in International Development," Toyama argues that information technology primarily magnifies existing human and institutional forces rather than operating as an independently transformative force. His amplification theory identifies three mechanisms associated with differences in **access, capacity, and motivation** (Toyama 75–82). 【5-0196c4】【6-a86409】

Toyama makes the argument particularly clear when describing the relationship between people and technology: people possess intent and capacity, while technology multiplies human capacity in the direction of human intent. From that premise, he argues that technology cannot substitute for missing human intent or capacity (Toyama 75–82). 【5-0196c4】

This is important because it changes the question we ask when technology appears in an explanation.

Instead of stopping with:

> **What did the technology do?**

Toyama gives us reason to ask:

> **What human or institutional forces did the technology amplify?**

That question follows directly from his amplification argument.

What I do with it next is my synthesis.

Suppose two schools adopt similar technological capabilities. One produces meaningful improvements while the other struggles.

Instead of assuming that the difference begins with the technology, I would use Toyama's amplification theory to move beneath it:

**Observed effect**

↓ What role did technology play?

**Technology**

↓ What was it amplifying?

**Existing practices**

↓ What enabled those practices?

**Organizational capacity**

↓ What makes that capacity possible?

**Human knowledge, motivation, relationships, and intent**

Toyama does not present that sequence as a formal causal pathway. I am constructing it from his amplification argument.

The distinction is important.

What Toyama establishes is the amplifier thesis: technology's effects are conditioned by underlying human and institutional forces, and technology cannot simply compensate for missing intent and capacity (Toyama 75–82). 【5-0196c4】

What I take from it is a diagnostic rule:

> **When technology appears to explain an effect, keep looking underneath the technology.**

---

# Putting Pearl, Toyota, and Toyama Together

Pearl, Toyota, and Toyama did not jointly propose an effect-to-cause framework.

I am bringing them together because each helps answer a different part of my original question.

**Pearl** establishes why observing a statistical relationship is different from making a causal claim and why intervention and counterfactual reasoning require information beyond association (Pearl, "Three Layer"; Pearl, "Causal Inference" 99–101). 【1-8472b9】【2-88096b】

**Toyota** provides a production philosophy in which people understand, improve, and learn to detect abnormalities in work before incorporating those capabilities into machines ("Toyota Production System"). 【3-3fbcac】

**Toyama** argues that technology amplifies existing human and institutional intent and capacity rather than substituting for them (Toyama 75–82). 【5-0196c4】

From those three contributions, **I propose the following pathway**:

> ## Effect → Observation → Why → System Condition → Human Capacity → Intervention → Counterfactual → Cause

That sequence is mine.

The sources inform it, but none of them should receive attribution for the combined framework.

The pathway works by repeatedly changing the question.

### Effect

**What happened?**

We begin with the visible outcome.

↓

### Observation

**What appears to be associated with it?**

Pearl warns us not to treat that association as sufficient evidence of causation.

↓

### Why

**What conditions are producing what we observe?**

Here I borrow the Toyota habit of looking more deeply into the work rather than treating the visible manifestation as the whole problem.

↓

### System Condition

**How does the work actually happen?**

Now the inquiry moves from the symptom into the system.

↓

### Human Capacity

**What knowledge, capability, intention, or institutional condition exists beneath the technology?**

This is where Toyama's amplification theory becomes especially useful.

↓

### Intervention

**What happens if we deliberately change the condition we believe matters?**

Here we return to Pearl.

↓

### Counterfactual

**Would the outcome have been different had that condition been different?**

Again, Pearl provides the causal vocabulary.

↓

### Cause

We now have something stronger than the pattern that originally attracted our attention.

We have a causal explanation that can be stated, examined, challenged, tested where possible, and improved.

That last description is also my synthesis rather than a proposition attributable to any one source.

---

# The Missing Layer: Process Knowledge

This leads me to something I think is missing from many conversations about AI readiness:

**process knowledge.**

Organizations frequently begin their AI journey with a version of this question:

> **What can AI do?**

I increasingly think another question has to come first:

> **Do we understand what we do?**

Knowing that a process exists is not necessarily the same as understanding it.

A procedure might document the steps people are expected to follow. A workflow might show how information moves. A dataset might record what previously occurred.

Process knowledge requires something deeper.

We need to understand what information people rely upon, how decisions are made, where judgment enters the process, where exceptions occur, what relationships matter, what outcomes we are seeking, and why the process behaves differently under different conditions.

This definition of process knowledge is my framing for this article.

Pearl helps sharpen the distinction because causal questions require knowledge that cannot simply be extracted from observed statistical distributions (Pearl, "Causal Inference" 99–101). 【2-88096b】

Toyota provides a practical analogue because its production philosophy calls for people to understand and improve work before incorporating the resulting capabilities into machinery ("Toyota Production System"). 【3-3fbcac】

Toyama adds an institutional dimension because technology's contribution depends on the intent and capacity already present for it to amplify (Toyama 75–82). 【5-0196c4】

Those sources establish their respective propositions.

**I make the connection between them and process knowledge.**

And that connection gives me a new pathway:

> **Effect → Cause → Process Knowledge**

That is where this line of reasoning intersects with my **First Five Things to Teach a Computer**.

---

# Before We Teach the Computer

The **First Five Things to Teach a Computer** is my original framework.

It should not be attributed to Pearl, Toyota, Toyama, Seymour Papert, STEAM scholarship, UNESCO, or another source. Other bodies of work can help contextualize or illuminate it, but the framework and its intellectual development are my own.

The First Five begins with a deceptively simple question:

> **What are the first things we should teach a computer?**

The work in this article exposes a question that I now see as logically prior to it:

> **Do we understand the human system well enough to know what should be taught?**

Consider what happens if the answer is no.

We may teach the machine patterns without knowing what produces them.

We may encode procedures without understanding why those procedures exist.

We may automate inherited practices without asking whether they still make sense.

We may interpret statistical associations as causal relationships.

We may give an AI access to enormous quantities of organizational information while failing to provide the process knowledge necessary to interpret what that information means.

These are implications I am drawing from the synthesis, not claims made by Pearl, Toyota, or Toyama.

And they lead me to extend the First Five lineage:

> ### Process Knowledge → Causal Knowledge → First Five → AI → Intervention → Observation → Learning

Again, **this sequence is mine**.

The important shift is that teaching the computer is no longer the beginning of the pathway.

Understanding comes first.

---

# From Teaching Machines to Learning Systems

Once we make that shift, something else happens.

The First Five doesn't have to end when the computer has been taught.

Suppose we understand a process well enough to make part of that knowledge legible to an AI system.

The system helps us identify something.

Humans make an intervention.

We observe the effect.

Now we have new evidence.

And that evidence can challenge what we thought we knew about the process.

The progression becomes cyclical:

> **Effect → Cause → Process Knowledge → First Five → AI → Intervention → Observation → Learning → New Understanding**

This is my proposed learning loop.

Pearl's framework is especially useful at the latter end of the cycle because it distinguishes among observations, interventions, and counterfactual questions (Pearl, "Three Layer"). 【1-8472b9】

But the complete loop itself should not be called Pearl's framework.

Nor is it Toyota's.

Nor is it Toyama's.

It is the synthesis I am developing by connecting their work to my ideas about process knowledge, First Five, AI readiness, and Compass Next.

That provenance boundary matters because synthesis is itself intellectual work. We should neither claim another author's ideas as our own nor give another author credit for connections they never made.

---

# AI Readiness Is Also Learning Readiness

This brings me to what may be the larger point.

We often talk about AI readiness in technological terms.

Do we have the infrastructure?

Do we have the data?

Do we have appropriate AI systems?

Do people know how to use them?

Those are useful questions.

But the effect-to-cause pathway suggests another dimension of readiness:

> **Can an organization learn about itself?**

An organization moving toward AI readiness should be able to ask:

1. **What happened?**
2. **What evidence do we have for it?**
3. **What do we think caused it?**
4. **What assumptions support that explanation?**
5. **How does the underlying process actually work?**
6. **What human or institutional capabilities matter?**
7. **What should we teach the computer about that system?**
8. **What could we change?**
9. **What happened when we changed it?**
10. **What did we learn?**

That ten-question sequence is my own formulation.

It changes the starting question from:

> **Can we deploy AI?**

to:

> **Do we understand our work well enough to know where AI can help?**

And eventually to:

> **Can humans and machines learn enough about the system to make better interventions together?**

That, for me, gets much closer to what **AI ready** should mean.

---

# From Effect to Cause and Back Again

This is where I see a deeper connection to **Compass Next**.

The important movement is not simply toward more data, more powerful models, or more capable AI.

It is toward better organizational learning.

Pearl helps us understand that observing relationships, intervening in a system, and reasoning about what would have happened otherwise constitute fundamentally different kinds of causal inquiry (Pearl, "Three Layer"). 【1-8472b9】

Toyota shows us a production philosophy in which human beings learn the work, improve it, identify abnormalities, and then incorporate appropriate capabilities into machines ("Toyota Production System"). 【3-3fbcac】

Toyama shows us why the technology itself cannot be the whole explanation: technology magnifies underlying intent and capacity rather than replacing what is missing (Toyama 75–82). 【5-0196c4】

Those are their contributions.

The connection I make among them is this:

> ## Effect → Cause → Understanding → Teaching → Intervention → Learning

And the First Five introduces the question that sits at the center:

> **Once we understand the system, what should we teach the computer about it?**

That gives me a different way of thinking about the pathway to AI.

Not simply:

> **data → model → AI**

but:

> **effect → cause → process knowledge → teaching → intervention → learning**

The first pathway begins with the machine.

The second begins with understanding.

That difference may be more consequential than it first appears.

Because the deepest challenge of AI readiness is not simply teaching machines to recognize patterns.

It is making sure **we understand what those patterns mean before we ask machines to reason or act on them**.

Perhaps that is the line between an organization that merely **has AI** and one that is becoming genuinely **AI ready**.

And perhaps the journey from effect to cause is not merely a way of diagnosing problems.

It is part of how we learn what is worth teaching a computer in the first place.

---

## About the Author

**Jason Kronemeyer** is a community technologist and advisor working at the intersection of broadband, data infrastructure, artificial intelligence, knowledge management, intelligent infrastructure, and community development. His work focuses on how communities and institutions build the human, technical, and organizational capacity needed to use emerging technologies meaningfully. He is the originator of the **First Five Things to Teach a Computer** framework and is developing **Compass Next** as part of his broader work on AI readiness, process knowledge, organizational learning, and the relationship between human and machine intelligence.

---

## Works Cited

Pearl, Judea. "Causal Inference in Statistics: An Overview." *Statistics Surveys*, vol. 3, 2009, pp. 96–146. https://doi.org/10.1214/09-SS057.

Pearl, Judea. "The Three Layer Causal Hierarchy." *UCLA Computer Science*, https://web.cs.ucla.edu/\~kaoru/3-layer-causal-hierarchy.pdf. Accessed 12 Oct. 2026.

Toyota Motor Corporation. "Toyota Production System." *Toyota Motor Corporation*, https://global.toyota/en/company/vision-and-philosophy/production-system/. Accessed 12 Oct. 2026.

Toyama, Kentaro. "Technology as Amplifier in International Development." *Proceedings of the 2011 iConference*, Association for Computing Machinery, 2011, pp. 75–82. https://doi.org/10.1145/1940761.1940772.
