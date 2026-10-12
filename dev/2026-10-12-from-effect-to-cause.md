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

We are surrounded by effects. A new technology is introduced and performance improves. A school adopts an AI platform and some teachers embrace it while others do not. A community gains broadband, but the outcomes we expected do not automatically follow. An organization buys better tools, yet the underlying work remains stubbornly difficult. Our instinct is often to observe the visible change and assign a cause, but an effect is not an explanation.

I have been thinking about this distinction through three bodies of work from very different traditions: Judea Pearl's causal reasoning, the Toyota Production System, and Kentaro Toyama's theory of technology as an amplifier. None proposes the framework I develop here; each contributes a different piece. Pearl helps distinguish association from intervention and counterfactual reasoning. Toyota describes why people should understand and improve work before incorporating that understanding into machines. Toyama reminds us that technology's effects depend on the human and institutional forces it amplifies.

I connect these ideas to a question that has become central to my own work: **what should we understand about a system before we teach a computer about it?** That question links the sources to my original **First Five Things to Teach a Computer** framework and, more recently, to my thinking about Compass Next.

When I connect the sources, I arrive at a broader proposition:

> **The pathway to AI readiness may not begin with AI at all. It may begin with our ability to move from an observed effect toward a defensible understanding of its cause.**

That proposition is my synthesis. In the sections that follow, I use Pearl, Toyota, and Toyama to explore what it takes to understand the system behind an observed effect.

---

## Pearl: Seeing Something Is Not the Same as Causing It

Judea Pearl's causal hierarchy distinguishes three levels: **association, intervention, and counterfactuals**—or, in his shorthand, seeing, doing, and imagining or retrospection. At the associational level, we ask what observing one thing tells us about another. At the interventional level, we ask what would happen if we deliberately changed something. At the counterfactual level, we ask whether *X* caused *Y* and what might have happened had we acted differently (Pearl, "Three Layer"). 【1-8472b9】

Imagine that students who use an AI tutor perform better academically. We have observed an association:

> **AI use ↔ higher performance**

But the observation alone does not establish that AI caused the improvement. Statistical analysis can describe associations under observed conditions, while causal analysis asks about changes produced by treatments or external interventions. Pearl argues that causal conclusions depend on assumptions that observational data alone cannot establish (Pearl, "Causal Inference" 99–101). 【2-88096b】 So the next question is not simply whether the association appears again:

> **What happens if we deliberately change X?**

This moves the inquiry from observing to intervening. Pearl also gives us another kind of question:

> **Would Y have been different had X been different?**

That is counterfactual reasoning. Pearl's hierarchy describes a progression toward increasingly powerful causal questions; higher-level answers cannot simply be recovered from lower-level observational information alone (Pearl, "Three Layer"). 【1-8472b9】 This distinction matters in the age of AI: a system can discover a pattern, a person can see one, and an organization can measure one, but none of those facts alone explains why it exists. That application to AI readiness is mine; Pearl provides the causal distinction, which I apply to what organizations need to understand before using AI to make or inform decisions.

---

## Toyota: Understand the Work Before Putting It Into the Machine

Toyota approaches the relationship between people, processes, and machines from a different direction. The Toyota Production System describes *jidoka* as "automation with a human touch." Toyota explains that creating such machines begins with people able to perform work smoothly and correctly by hand, identify abnormalities, implement *kaizen*, and eliminate waste and inconsistency before incorporating the appropriate understanding into machines ("Toyota Production System"). 【3-3fbcac】【4-f34b7e】 In short: **do the work, understand it, improve it, recognize abnormalities, and only then incorporate that understanding into a machine.**

Toyota describes these principles in manufacturing, not as an AI-readiness framework. The connection to AI is mine, and it leads me to restate the principle this way:

> **Understand the work before trying to teach the machine the work.**

Consider what happens when we reverse that sequence. Suppose a school introduces an AI system and teachers do not use it. The visible effect is:

> **Low AI adoption.**

We might immediately diagnose the problem as insufficient AI training and respond by providing more training. But what if teachers do not know where AI belongs in instruction because the existing processes have never been examined in relation to it? Perhaps those processes contain knowledge that experienced educators understand intuitively but have never articulated. Rather than assuming the remedy, we need to ask:

> **Do we understand the instructional process well enough to determine what, if anything, should be delegated to or supported by AI?**

The school example and the questions it raises are mine, not Toyota findings. Toyota contributes the more foundational philosophy: human understanding and improvement of work precede incorporating that understanding into machines. Toyota also emphasizes that machines, robots, and IT do not implement *kaizen* by themselves; human wisdom and ingenuity remain essential ("Toyota Production System"). 【3-3fbcac】 I see that as a profound idea for AI readiness.

---

## Toyama: Look Beneath the Technology

Kentaro Toyama gives us another way to look beneath a visible effect. In "Technology as Amplifier in International Development," he argues that information technology primarily magnifies existing human and institutional forces rather than operating as an independently transformative force. His amplification theory identifies three mechanisms associated with differences in **access, capacity, and motivation** (Toyama 75–82). 【5-0196c4】【6-a86409】

Toyama makes the argument particularly clear when describing the relationship between people and technology: people possess intent and capacity, while technology multiplies human capacity in the direction of human intent. From that premise, he argues that technology cannot substitute for missing human intent or capacity (Toyama 75–82). 【5-0196c4】

This changes the question we ask when technology appears to explain an outcome. Instead of stopping with:

> **What did the technology do?**

Toyama gives us reason to ask:

> **What human or institutional forces did the technology amplify?**

Suppose two schools adopt similar technological capabilities, but one achieves meaningful improvements while the other struggles. Rather than assuming that the difference begins with the technology, I would ask what existing practices and organizational capacities each system has, and what human knowledge, motivation, relationships, and intent those capacities depend on. Toyama does not present this as a formal causal pathway; it is my application of his amplification argument.

What Toyama establishes is that technology's effects are conditioned by underlying human and institutional forces, and technology cannot simply compensate for missing intent and capacity (Toyama 75–82). 【5-0196c4】 What I take from it is a diagnostic rule:

> **When technology appears to explain an effect, keep looking underneath the technology.**

---

## From Effects to Process Knowledge

Pearl, Toyota, and Toyama did not jointly propose an effect-to-cause framework. I bring their ideas together because each helps answer a different part of the question. Pearl distinguishes observing an association from intervening and reasoning counterfactually; Toyota emphasizes understanding and improving work before incorporating that understanding into machines; Toyama explains how technology can amplify existing human and institutional intent and capacity. 【1-8472b9】【2-88096b】【3-3fbcac】【5-0196c4】

From those contributions, I propose a diagnostic sequence of my own:

> **Effect → Evidence → Process → Human Capacity → Intervention → Learning**

We begin by describing what happened and what evidence supports the observation. We then ask how the work actually happens, what conditions and human capabilities shape it, and which of those conditions might be changed. After an intervention, we examine what changed and what the evidence allows us to conclude. Pearl's framework is especially important here: an observed association is not proof of causation, and causal claims require assumptions and evidence beyond the association itself.

This sequence is not a causal model supplied by any of the three sources, nor does following it automatically establish cause. It is my way of using their distinct insights to guide inquiry: look beyond the visible effect, understand the system in which it occurs, and treat intervention as an opportunity to learn rather than a guarantee of improvement.

---

## Before We Teach the Computer

The three perspectives converge on a question I think is missing from many conversations about AI readiness: **Do we understand what we do?** Organizations often begin with “What can AI do?” But knowing that a process exists is not the same as understanding it. A procedure may document expected steps, a workflow may show how information moves, and a dataset may record what happened; process knowledge goes further.

To understand a process, we need to know what information people rely on, how decisions are made, where judgment and exceptions enter, what relationships matter, what outcomes we seek, and why the process behaves differently under different conditions. This is my framing of process knowledge. Pearl helps show why causal questions cannot be answered simply by extracting patterns from observed data (Pearl, "Causal Inference" 99–101). 【2-88096b】 Toyota offers a practical analogue in its emphasis on understanding and improving work before embedding capabilities in machinery ("Toyota Production System"). 【3-3fbcac】 Toyama adds that technology's contribution depends on the human and institutional intent and capacity it amplifies (Toyama 75–82). 【5-0196c4】 The sources establish those respective ideas; the connection I make among them is mine.

That connection matters to my **First Five Things to Teach a Computer**, my original framework. The First Five should not be attributed to Pearl, Toyota, or Toyama; their work helps me contextualize my own. The familiar question is, “What are the first things we should teach a computer?” The logically prior question is: **Do we understand the human system well enough to know what should be taught?**

If we do not, we risk teaching machines patterns without understanding what produces them, encoding procedures without knowing why they exist, automating inherited practices without asking whether they still make sense, or treating statistical associations as causes. We might give AI access to vast organizational information without the process knowledge needed to interpret what that information means. These are implications I draw from the synthesis, not claims made by the cited sources.

The shift is not away from teaching computers; it is toward putting understanding first. Once people understand a process well enough to make relevant knowledge legible to an AI system, the system may help them notice something, inform an intervention, or raise a new question. People then examine the effects and learn from the evidence. New observations may challenge the original understanding, sending inquiry back through the process. This is my proposed learning loop—not Pearl's, Toyota's, or Toyama's:

> **Effect → Evidence → Process Knowledge → First Five → AI → Intervention → Observation → Learning → New Understanding**

The loop also clarifies what I mean by organizational AI readiness. Infrastructure, data, suitable systems, and operational skills matter, but an organization must also be able to learn about itself. In practical terms, can it describe what happened and the evidence for it; identify assumptions and possible causes; explain how the work actually happens and what human capacities matter; decide what, if anything, to teach the computer; and evaluate what changed after an intervention?

This sequence of questions is my formulation, not a standardized readiness model. It shifts the starting question from **“Can we deploy AI?”** to **“Do we understand our work well enough to know where AI can help?”** The larger question is whether humans and machines can help us learn enough about the system to make better interventions together.

---

## From Effect to Cause and Back Again

This is where I see a deeper connection to **Compass Next**: the important movement is not simply toward more data, more powerful models, or more capable AI, but toward better organizational learning. The First Five brings the central question into focus: **Once we understand the system, what should we teach the computer about it?**

That is a different starting point from **data → model → AI**. It begins with an observed effect, asks what produced it, develops process knowledge, and uses technology within an ongoing cycle of intervention and learning. The deepest challenge of AI readiness is not simply teaching machines to recognize patterns; it is making sure **we understand what those patterns mean before we ask machines to reason or act on them**. The journey from effect to cause is part of how we learn what is worth teaching a computer in the first place.

---

## About the Author

**Jason Kronemeyer** is a community technologist and advisor working at the intersection of broadband, data infrastructure, artificial intelligence, knowledge management, intelligent infrastructure, and community development. His work focuses on how communities and institutions build the human, technical, and organizational capacity needed to use emerging technologies meaningfully. He is the originator of the **First Five Things to Teach a Computer** framework and is developing **Compass Next** as part of his broader work on AI readiness, process knowledge, organizational learning, and the relationship between human and machine intelligence.

---

## Works Cited

Pearl, Judea. "Causal Inference in Statistics: An Overview." *Statistics Surveys*, vol. 3, 2009, pp. 96–146. https://doi.org/10.1214/09-SS057.

Pearl, Judea. "The Three Layer Causal Hierarchy." *UCLA Computer Science*, https://web.cs.ucla.edu/\~kaoru/3-layer-causal-hierarchy.pdf. Accessed 12 Oct. 2026.

Toyota Motor Corporation. "Toyota Production System." *Toyota Motor Corporation*, https://global.toyota/en/company/vision-and-philosophy/production-system/. Accessed 12 Oct. 2026.

Toyama, Kentaro. "Technology as Amplifier in International Development." *Proceedings of the 2011 iConference*, Association for Computing Machinery, 2011, pp. 75–82. https://doi.org/10.1145/1940761.1940772.
