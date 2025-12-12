---
layout: post
title: "HTML has come a long way since 1997"
date: 2025-11-08
author: Jason Kronemeyer
status: story
categories: [Technology, Web Development, Personal Story]
tags: [HTML, Web Development, Personal Story, Technology]
excerpt: "From a Hawaii Air Force dorm room and a fantasy football website on aloha.net to semantic HTML5, CSS Grid, and the modern web—how curiosity and experimentation taught me I could learn anything."
---

As I sit here writing in a modern editor—syntax highlighting, auto-completion, and collaboration baked in—I keep thinking about 1997.

I was in the U.S. Air Force then, working as a Signals Intelligence Analyst in Hawaii. My shifts were spent analyzing signals and reporting intelligence from a facility tucked beneath a pineapple field—a surreal detail that still sounds like fiction. But when my shift ended and I walked back to the dorm, I entered a different kind of intelligence work: learning the early web when the *semantic web* (and even semantic HTML) was still in its infancy.

The breakthrough wasn’t a specific tutorial. It was a pattern: the World Wide Web + curiosity + experimentation meant I could teach myself almost anything I was willing to wrestle with.

### Curiosity and Experimentation (the real stack)

Curiosity fueled every late-night tweak and every broken layout I had to fix. Experimentation was the method: view source, change a tag, refresh, repeat. I kept notes on what worked, what didn’t, and why—small iterations that built confidence and momentum.

To anyone learning today:
- Ask “what if?” and try it immediately.
- Break things on purpose to see how they fail.
- Keep a changelog of experiments and outcomes.
- Rebuild the same component three ways to compare approaches.
- Share drafts early; feedback is a force multiplier.

Curiosity sets direction. Experimentation delivers progress.

## Discovery in the Dorm

During my free time, I began experimenting with HTML. The internet was still relatively new to most people, and the idea that I could create my own corner of this digital frontier was exhilarating. Armed with nothing more than a text editor and a dial-up connection, I started teaching myself the basics: `<html>`, `<head>`, `<body>`, `<table>` (oh, so many tables for layout), and the ever-temperamental `<font>` tag.

My first real project? A website to run a fantasy football league—long before ESPN Fantasy Sports or Yahoo! made that kind of thing turnkey. I wanted a central place where league members could check scores, view rosters, and talk some trash. So I built it.

I hosted it on aloha.net under the username “Kroney3268”—a digital address that felt like home in more ways than one. The site was nothing fancy by today’s standards: static HTML pages, maybe a GIF or two (likely animated, because that was the style), and basic forms for interaction. But to me and my league members, it was revolutionary. We had our own little slice of the internet.

## The Web in 1997: A Different Era

Looking back, the web in 1997 was a fundamentally different place. HTML 3.2 was the standard, and creating a webpage meant:

- Using `<table>` elements for layout, nesting them multiple levels deep
- Relying on `<font>` tags with attributes like `color` and `size` to style text
- Employing transparent GIF images as spacers to control layout
- Working with limited color palettes (216 "web-safe" colors)
- Accepting that websites would look different across the handful of browsers available
- Dealing with slow dial-up connections that made every image a careful consideration

There was no separation of content and presentation. Your HTML was your design, and your design was your HTML. Maintenance was a nightmare—changing the color scheme meant editing every single page manually.

And yet, that constraint had a gift in it: it made the web feel *learnable*. It was just text, rendered into something real.

That mindset is exactly why I later wrote [The First 5 Things to Teach a Computer](%7B%25%20post_url%202024-08-30-first-5-things-to-teach-computer%20%25%7D). Those five “first lessons” (communication, sequence, art, math, and play) were all in the room with me in 1997—HTML just gave them a new medium.

## The Evolution Begins: Separation of Concerns

The late 1990s and early 2000s brought significant changes. CSS (Cascading Style Sheets) emerged as a way to separate content from presentation. Suddenly, you could change the entire look of a website by editing a single stylesheet. JavaScript became more sophisticated, enabling dynamic interactions without page refreshes.

The web standards movement, championed by organizations like the W3C and advocates like Jeffrey Zeldman, pushed for semantic HTML and proper CSS usage. Developers began to understand that `<div>` elements with classes were more flexible than nested tables, and that separating structure, presentation, and behavior made websites more maintainable and accessible.

## HTML5: A Revolution in Web Standards

When HTML5 emerged in the late 2000s and was standardized in 2014, it represented a quantum leap forward. HTML5 wasn't just an incremental update—it was a reimagining of what the web could be:

### Semantic Elements (and why they mattered)
HTML5 introduced semantic elements that give meaning to content structure:
- `<header>`, `<nav>`, `<article>`, `<section>`, `<aside>`, and `<footer>` replaced generic `<div>` tags
- `<figure>` and `<figcaption>` provide proper ways to markup images with captions
- `<time>`, `<mark>`, and other elements add semantic meaning to inline content

These semantic elements don’t just make code more readable—they improve accessibility for screen readers and help search engines understand content better. For me, they also closed a loop: the early web taught me how to publish; semantic HTML taught me how to publish *with meaning*.

### Multimedia Support
Gone are the days of relying on Flash Player or other plugins:
- `<video>` and `<audio>` elements enable native multimedia playback
- Support for multiple formats ensures cross-browser compatibility
- JavaScript APIs provide fine-grained control over playback

### Form Enhancements
HTML5 revolutionized web forms with new input types and attributes:
- Input types like `email`, `url`, `date`, `number`, `range`, and `color` provide built-in validation
- Attributes like `placeholder`, `required`, `pattern`, and `autocomplete` improve user experience
- The `<datalist>` element enables autocomplete functionality

### Canvas and SVG
HTML5 brought powerful graphics capabilities:
- The `<canvas>` element enables dynamic, scriptable rendering of 2D shapes and bitmap images
- SVG integration allows for scalable vector graphics that are responsive and accessible
- WebGL builds on canvas to bring 3D graphics to the browser

### APIs and Storage
HTML5 introduced a suite of JavaScript APIs that transformed web applications:
- **Local Storage and Session Storage**: Persistent client-side storage without cookies
- **Geolocation API**: Access to device location (with user permission)
- **Drag and Drop API**: Native support for drag-and-drop interactions
- **Web Workers**: Background threads for JavaScript, enabling true multitasking
- **WebSockets**: Real-time, bidirectional communication between client and server
- **History API**: Manipulation of browser history for single-page applications

### Mobile-First Thinking
HTML5 was designed with mobile devices in mind from the start:
- Responsive design principles became standard practice
- Touch events and mobile-specific APIs
- Offline capabilities through Application Cache (later replaced by Service Workers)

## CSS3: From Simple Styles to Complex Designs

While HTML5 was revolutionizing structure and functionality, CSS3 was transforming web design:

### Visual Effects
CSS3 made beautiful designs possible without images:
- **Border-radius**: Rounded corners without multiple background images
- **Box-shadow and text-shadow**: Depth and dimension without Photoshop
- **Gradients**: Linear and radial gradients defined entirely in CSS
- **Opacity and RGBA colors**: Transparency and color with alpha channels
- **Transforms**: 2D and 3D transformations (rotate, scale, skew, translate)
- **Transitions and animations**: Smooth, hardware-accelerated animations

### Layout Revolution
CSS3 introduced powerful layout systems that replaced the table-based layouts of the past:

**Flexbox** (Flexible Box Layout):
- One-dimensional layouts (row or column)
- Automatic space distribution and alignment
- Easy reordering of elements without changing HTML
- Simplified responsive design patterns

**Grid Layout**:
- Two-dimensional layouts with rows and columns
- Explicit control over item placement
- Gap control without margin hacks
- Overlapping and spanning of grid areas

These layout systems mean developers can create complex, responsive layouts with just a few lines of CSS—no more nesting tables twenty levels deep.

### Responsive Design
CSS3 made responsive web design not just possible, but practical:
- **Media queries**: Conditional styles based on device characteristics
- **Flexible units**: `rem`, `em`, `vw`, `vh` for scalable designs
- **Relative sizing**: Percentage-based widths and flexible images
- **Mobile-first approach**: Design for small screens first, then enhance

### Advanced Selectors and Pseudo-elements
CSS3 expanded the selector toolkit dramatically:
- Attribute selectors: `[data-type="article"]`
- Structural pseudo-classes: `:nth-child()`, `:first-of-type`
- State pseudo-classes: `:checked`, `:valid`, `:invalid`
- Pseudo-elements: `::before`, `::after`, `::first-letter`, `::first-line`

## Modern Web Development: The Current Landscape

Today's web development landscape would be unrecognizable to my 1997 self. We now have:

### Progressive Web Apps (PWAs)
Websites that feel like native apps:
- Offline functionality through Service Workers
- Push notifications
- Installation to device home screen
- Access to device hardware

### Component-Based Architecture
Modern frameworks like React, Vue, and Angular enable:
- Reusable UI components
- Virtual DOM for efficient updates
- State management solutions
- Component lifecycle hooks

### CSS Preprocessors and PostCSS
Tools that extend CSS capabilities:
- Variables and mixins (now native with CSS Custom Properties)
- Nesting and modularization
- Automatic vendor prefixing
- Future CSS syntax today

### Build Tools and Package Managers
The development workflow has transformed:
- npm/yarn for dependency management
- Webpack, Vite, and other bundlers for asset optimization
- Babel for JavaScript transpilation
- TypeScript for type safety

### Accessibility and Inclusivity
Modern web development prioritizes:
- WCAG compliance and screen reader compatibility
- Keyboard navigation support
- Color contrast and readability
- Inclusive design patterns

### Performance Optimization
Today's best practices include:
- Code splitting and lazy loading
- Image optimization and WebP/AVIF formats
- Critical CSS and above-the-fold optimization
- Core Web Vitals monitoring

## From Fantasy Football to the Modern Web

That fantasy football website I built in the dorm while working under a pineapple field was more than a hobby project. It was my entry point into a career that would eventually span technology, education, and digital equity work. The problem-solving skills I developed while debugging table layouts and wrestling with browser quirks laid the foundation for more complex challenges later.

Today, I work at the intersection of information, technology, and energy—often thinking about systems, standards, and access. But I don’t forget where it started: a text file, a browser, and the feeling that “if I can figure this out, I can figure out a lot more.”

{% include callout.html type="info" title="A Personal Bridge Between Posts" content="If you’re interested in the learning pattern behind this story, this is the same mindset I describe in ‘The First 5 Things to Teach a Computer’: start simple, practice fundamentals, and let curiosity and iteration do the heavy lifting." %}

## Reflection: The Journey Continues

From that simple fantasy football website on aloha.net to the sophisticated web applications we build today, HTML has truly come a long way. What started as a simple markup language for academic documents has evolved into the foundation of a platform that powers everything from social networks to complex business applications to immersive gaming experiences.

The web in 1997 was static, desktop-only, and limited in what it could do. Today’s web is dynamic, mobile-first, and capable of things I couldn’t have imagined while experimenting in that Air Force dormitory under a pineapple field. We have semantic markup that machines can understand, multimedia capabilities that rival native applications, and styling systems that make beautiful, responsive designs accessible to more developers.

Yet for all the changes, the fundamental beauty of HTML remains: it’s still text files that anyone can write and browsers can render. You don’t need expensive tools or a computer science degree to get started. You need curiosity, patience, and a willingness to iterate—the same things I needed back in 1997.

The web has democratized publishing, enabled global communication, and created opportunities that didn't exist before. As I look at the evolution from HTML 3.2 to HTML5, from inline styles to CSS Grid, from static pages to Progressive Web Apps, I'm filled with excitement for what comes next.

The journey that started under a pineapple field continues, and I can’t wait to see where it leads.

---

*What was your first experience with HTML? Do you remember your first website? I'd love to hear your stories in the comments below.*
