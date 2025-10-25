---
layout: post
title: "Building a Library of Skills for Community Training"
date: 2025-10-25
author: Jason Kronemeyer
tags: [skills.md, digital-equity, community-training, AI-curriculum, broadband]
---

Over the past few months, I’ve been thinking a lot about how we package what we know—how we make it reusable, shareable, and scalable. In our work with EUPConnect and the Compass series, we’ve built training modules, digital equity plans, and AI curriculum frameworks. But the question keeps coming up: how do we make these resources easier to use, remix, and deploy across communities?

That’s where I’ve been exploring something called `skills.md`.

## What Is `skills.md`?

Originally introduced by Anthropic for their Claude AI models, `skills.md` is a way to define a skill—like “Digital Literacy 101” or “Broadband Planning Basics”—in a structured folder. It’s not just a markdown file. It’s a whole package: instructions, templates, scripts, and even automated tests. Think of it like a recipe box for community knowledge.

Each skill lives in its own folder, and the `SKILL.md` file acts as the table of contents. It tells you what the skill is, who created it, what it’s for, and how to use it. It’s a simple idea, but it opens up a world of possibilities.

## Why It Matters for Us

In our region, we’re not just building networks—we’re building capacity. We’re helping schools, libraries, and local leaders understand the digital tools they need to thrive. But every time we run a workshop or write a guide, we’re starting from scratch. What if we didn’t have to?

By turning our training modules into `skills.md` folders, we can create a library of reusable, remixable knowledge. These skills can be loaded into AI agents, shared across GitHub, or used by educators and technologists to jumpstart their own programs.

## A Simple Structure

Here’s how I’ve started organizing our skills:


community-training-modules/ ├── README.md ├── .gitignore └── skills/ ├── digital-literacy/ │   └── SKILL.md ├── ai-curriculum/ │   └── SKILL.md ├── broadband-planning/ │   └── SKILL.md └── community-engagement/ └── SKILL.md

Each folder is a standalone skill. Inside, you’ll find a `SKILL.md` file with metadata, an overview, prerequisites, usage instructions, and links to resources. It’s clean, it’s simple, and it’s built for sharing.

## What’s Next?

I’m working on turning this into a public GitHub repository. The goal is to make it easy for others to contribute, remix, and deploy these skills in their own communities. Whether you’re a teacher in North Dickinson, a planner in Chippewa County, or a technologist in a rural library, you’ll be able to grab a skill, tweak it, and put it to work.

If you’re curious about how to build your own skills, or want to collaborate on this library, let’s talk. The power of “not yet” is alive and well—and this is just the beginning.
