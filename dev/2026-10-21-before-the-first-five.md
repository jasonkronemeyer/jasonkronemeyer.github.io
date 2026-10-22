---
layout: post
title: "Before the First Five: What Anishinaabe Ways of Knowing Can Teach Us About Organizing Information"
date: 2026-10-21
author: Jason F. Kronemeyer
categories:
  - Education
  - Digital Literacy
  - Web Development
  - Information Science
  - Artificial Intelligence
  - Anishinaabe Ways of Knowing
tags:
  - First Five
  - file systems
  - information architecture
  - web development
  - digital literacy
  - HTML
  - CSS
  - JavaScript
  - data
  - AI
  - Anishinaabe
  - Ojibwe
  - relationality
---

I teach Responsive Web Design at the community college level. On paper, it is an introductory course in HTML, CSS, and JavaScript. By the end of the course, students can also use a framework such as Bootstrap to quickly frame up a website.

But over the years, I have realized that one of the biggest barriers to learning web development often appears before we write the first line of HTML. It is the filesystem.

Students increasingly arrive in class without a strong mental model of files, folders, directories, paths, extensions, local storage, remote storage, or how one piece of information refers to another. They know how to open a document. They know how to upload something to an assignment. They know how to find something in "Recent Files." That is not the same thing as understanding where information actually lives.

This has made me think differently about something I have been developing called **The First Five Things to Teach a Computer**. The First Five framework starts with a deceptively simple idea: before we expect computers, data systems, or artificial intelligence to reason effectively about our world, we have to teach them some fundamental things about that world.

But there is another side to that argument. **Before we teach computers how our information relates, we may need to teach people how computers organize information in the first place.** I am increasingly convinced that this is a foundational form of digital literacy.

Living and teaching in the Great Lakes region also makes me wonder whether we can broaden that lesson. Anishinaabe ways of knowing offer a powerful reminder that knowledge is not simply a collection of isolated objects. It is relational, experiential, connected to language, place, community, and the living world (Treuer). The Great Lakes Indian Fish & Wildlife Commission describes Anishinaabe Ways of Knowing as encompassing understandings of landscape ecology, fish and wildlife, medicinal plants, seasonal change, and harvest traditions (Great Lakes Indian Fish & Wildlife Commission). Anton Treuer similarly describes Ojibwe knowledge as observational, experiential, and relational (Treuer). I do not want to collapse those teachings into a computer metaphor. They deserve respect on their own terms. But they can challenge us to notice something computing education sometimes forgets: **information only becomes meaningful when we understand relationships and context.**

## Before Data Comes Organization

We talk a lot today about data literacy. We want students to understand data. We want them to analyze information, use artificial intelligence, build websites, write programs, query databases, create visualizations, and eventually make informed decisions. But there is a more fundamental question: **Where is the information?**

And immediately after that: **What is it called?** Then: **How do I get to it?** And then: **How does it relate to everything around it?**

Those sound like simple questions. In reality, they are some of the fundamental questions of information science. A filesystem is one of the first information systems most of us encounter. It teaches us, whether we realize it or not, about:

**file → name → location → structure → relationship → meaning**

That is why I think filesystem literacy deserves much more attention in introductory computing education.

That emphasis on relationship has a meaningful regional resonance. Anishinaabe communities are not a single, uniform culture, and teachings vary among Tribal Nations, communities, families, and generations. Still, relationality is an important theme in many descriptions of Anishinaabe knowledge (Treuer). Rather than treating knowledge as detached facts, these traditions can situate knowing within relationships among people, language, place, other living beings, experience, and responsibility. That provides an important counterpoint to the way computers tend to make us think about information as discrete files, records, rows, or objects.

## A Website Is an Information System

When I begin teaching HTML, I could start with:

```html
<h1>Hello World</h1>
```

There is nothing wrong with that. But increasingly, I think there is something students need to understand first.

```text
responsive-web-design/
│
├── project-01/
│   ├── index.html
│   ├── about.html
│   │
│   ├── css/
│   │   └── styles.css
│   │
│   ├── js/
│   │   └── main.js
│   │
│   └── images/
│       ├── logo.svg
│       └── campus.jpg
│
├── project-02/
│
└── exercises/
```

Before learning very much HTML at all, a student should be able to look at this and begin to understand what it represents. This is not simply a collection of files. It is an **organized information environment**.

Some files contain structure. Some contain presentation. Some contain behavior. Some contain images or other media. The directories provide organization. The names provide clues about meaning. The paths describe relationships. The files have to be able to find one another.

This is also how MDN Web Docs approaches the problem in its introductory material on dealing with files: a website consists of multiple kinds of files that need to be assembled into a sensible structure locally before being placed on a server (Mozilla Developer Network, “Dealing with Files”).

That leads to a simple statement I want my students to understand:

> **A website is not just an HTML document. It is a system of files that have relationships with one another.**

Once students understand that, many things we teach later begin making considerably more sense.

## First: What Is a File?

I think we sometimes assume too much foundational knowledge. Before talking about CSS frameworks or JavaScript libraries, I want students to be comfortable with some basic concepts: file, folder, directory, filename, extension, file type, parent directory, child directory, root, path, local storage, remote storage, copy, move, rename, download, upload, and ZIP archive.

And there is one question I want them to learn to ask constantly:

> **Where is this file actually located?**

That question matters far beyond web design.

## The Filesystem Is a Tree

One of the most important concepts I can teach is that a filesystem is hierarchical.

```text
/
└── students/
    └── jason/
        └── web-design/
            └── project-01/
                ├── index.html
                └── images/
                    └── logo.png
```

We can describe that relationship visually:

```text
web-design
     │
     └── project-01
             │
             ├── index.html
             │
             └── images
                    │
                    └── logo.png
```

Folders contain other folders. Folders contain files. A file exists somewhere within that structure. We can start describing things as having parents and children.

Now we are not just learning to use Windows File Explorer or macOS Finder. We are learning an abstraction. The interface might change. Windows, macOS, Linux, OneDrive, GitHub, a web server, and a cloud environment can all present storage differently. The underlying idea remains remarkably consistent: **information has location and structure.**

## Paths Describe Relationships

Suppose our website looks like this:

```text
my-site/
├── index.html
├── about.html
├── css/
│   └── styles.css
└── images/
    └── logo.png
```

I can ask a student: **Where is `logo.png`?** The human answer might be: it is inside the images folder, which is inside my-site. But we can also describe that relationship to the computer:

```text
images/logo.png
```

Suddenly this starts making sense:

```html
<img src="images/logo.png" alt="Site logo">
```

The same thing happens with CSS:

```html
<link rel="stylesheet" href="css/styles.css">
```

The `src` and `href` attributes are no longer arbitrary pieces of HTML syntax to memorize. We are telling the computer: **Starting from where you are, follow this path until you find the resource I want.** That is a much stronger mental model.

MDN Web Docs explicitly includes file paths alongside file and folder manipulation, naming conventions, website directory structure, and file extensions among the things students should understand when getting started (Mozilla Developer Network, “Dealing with Files”).

Eventually, students can learn to interpret expressions such as:

```text
styles.css
./styles.css
css/styles.css
../index.html
../../images/logo.png
/images/logo.png
https://example.com/images/logo.png
```

These expressions describe different ways of locating information. This is not merely an HTML concept. It is an information-location concept.

## Local and Remote Are Not the Same Place

This becomes even more important when we introduce publishing. A student may have this on a laptop:

```text
Documents/
└── web-design/
    └── restaurant/
        ├── index.html
        ├── css/
        └── images/
```

A web server might contain something conceptually like:

```text
public_html/
├── index.html
├── css/
└── images/
```

These are two different locations. They may contain copies of the same information, but they are not necessarily the same files.

Changing:

```text
Documents/web-design/restaurant/index.html
```

does not automatically mean that:

```text
server/public_html/index.html
```

has changed.

This distinction gives us a foundation for understanding upload, download, synchronization, SFTP, hosting, Git, GitHub, repositories, deployment, and cloud storage. GitHub's documentation describes a repository as containing a project's code, files, and revision history (GitHub). Once a student understands a directory tree, a Git repository becomes far less mysterious. It is an organized project whose files and changes can be tracked.

## Naming Is Part of Information Architecture

Another habit I want students to develop early is intentional naming. Consider this:

```text
my-awesome-site/
about-us.html
student-resources.html
campus-map.jpg
main-navigation.js
```

Now compare it with:

```text
My Awesome Site/
About Us.HTML
Student Resources FINAL final2.html
Campus Map (1).JPG
MainNavigationNEW!!!!.js
```

Both might technically contain the information we need. But they are not equally maintainable. The second example is the beginning of technical debt.

MDN Web Docs recommends establishing predictable naming habits for web projects, including lowercase filenames, avoiding spaces, and using hyphens between words. It also makes students aware that web-server environments can be case-sensitive (Mozilla Developer Network, “Dealing with Files”).

For beginning web students, I would reduce this to five rules:

### Five Rules for Naming Web Files

1. **Use lowercase.**
2. **Don't use spaces.**
3. **Use hyphens between words.**
4. **Use meaningful names.**
5. **Be consistent.**

So I would rather see:

```text
blue-sky.jpg
```

than:

```text
IMG_5837.JPG
```

when the purpose of the image is known and the descriptive name improves maintainability.

This is more than housekeeping. **Naming something is an act of information architecture.** When we give something a meaningful name, we are adding information about the information. In other words, we are beginning to create metadata.

## Relationship Comes Before Abstraction

One of the risks of teaching computing is that we can make abstraction seem like the final goal. We turn something in the world into a filename, then a record, then a field, then perhaps a node in a graph. Abstraction is tremendously useful, but every abstraction leaves something behind.

Anishinaabe Ways of Knowing give me another way to talk with students about that problem. Great Lakes Indian Fish & Wildlife Commission describes Indigenous knowledge in the Great Lakes region as a philosophy and worldview reflecting Indigenous language and lifeways, grounded in knowledge accumulated through relationships with landscape, plants, animals, seasons, and harvest traditions (Great Lakes Indian Fish & Wildlife Commission). Anton Treuer describes Ojibwe knowledge systems as observational, experiential, and relational, and emphasizes that knowledge is embedded in life rather than separated from it (Treuer).

That suggests a useful question to place next to **Where is the file?**

> **What relationships are lost when I reduce something to a file?**

A photograph called `wild-rice.jpg`, for example, has a filename and a location in a filesystem. The filename may tell a human something about the image. Metadata might tell us when and where the photograph was taken. But none of those things, by themselves, necessarily tell us what manoomin means to a community, who has knowledge about it, what relationships surround its harvest, or what responsibilities accompany that knowledge. A computer can store the file long before it understands the context.

This becomes increasingly important as students eventually encounter databases and artificial intelligence. The technical ability to store information is not the same as understanding that information. **Representation is not the same thing as relationship.**

## Language Does More Than Label Things

This also changes how I think about naming. In computing, naming often appears to be purely functional. We ask whether the name is valid, unique, predictable, and easy for software to process. Those are important concerns. But language carries much more than identifiers.

Sault Ste. Marie Tribe of Chippewa Indians describes its Anishinaabemowin work as part of preserving Anishinaabe Bimaadiziwin, or Anishinaabe ways of life, and explicitly connects language teaching with protecting lifeways inherited from ancestors. That is an important reminder that words can carry relationships, histories, ways of seeing, and cultural knowledge that a literal database label may not capture.

So when I teach students to replace `IMG_5837.JPG` with `blue-sky.jpg`, I can still teach the practical lesson about useful filenames. But I can also introduce a deeper question: **Who gets to name the thing, and what knowledge is carried or lost in that name?**

That question becomes essential when we move from websites into data science, artificial intelligence, GIS, or knowledge graphs.

## Find It, Name It, Organize It, Relate It

This is where I see a direct connection to my First Five framework. Before we can ask a computer to do sophisticated things with information, we have to establish some basic concepts.

What is this thing? What do we call it? Where is it? What contains it? What does it contain? How is it related to another thing? How do I refer to it?

Those questions sound simple when we are talking about `logo.png`. They become much more consequential when we start talking about datasets, databases, knowledge graphs, artificial intelligence, or large organizational knowledge repositories.

The conceptual progression is surprisingly consistent:

```text
Thing
  ↓
Name
  ↓
Location
  ↓
Structure
  ↓
Relationship
  ↓
Meaning
```

That is why I increasingly see basic filesystem literacy as preparation for much more than web development.

## Physical, Logical, and Semantic Organization

There are actually several different kinds of organization occurring at the same time.

### Physical Organization

Where something resides:

```text
images/campus/library.jpg
```

### Logical Organization

Why we grouped resources together:

```text
images/
css/
js/
pages/
```

### Semantic Organization

What the information means:

```text
student-services.html
financial-aid.html
academics.html
```

Those distinctions become increasingly important as students move deeper into computing. Eventually physical organization might be abstracted away by a database, content management system, object store, API, or cloud platform. But the underlying problems do not disappear. We still have to answer questions about identity, location, classification, relationships, and meaning.

## The Broken Website Challenge

I think one of the best ways to teach these concepts is not to give students a perfectly structured website. Give them a mess.

```text
broken-site/
├── Index.HTML
├── About Us.html
├── CSS/
│   └── STYLE.css
├── Images/
│   ├── Logo FINAL.png
│   └── picture 1.JPG
└── javascript/
    └── Script.js
```

Then deliberately give them HTML containing references that do not match the structure:

```html
<link rel="stylesheet" href="css/style.css">

<img src="images/logo.png" alt="Logo">

<a href="about-us.html">About</a>

<script src="js/script.js"></script>
```

Then give them a simple assignment:

> **Don't redesign the website. Fix the information system.**

The students have to inspect the directory, determine what is wrong, rename files, reorganize directories, repair the paths, identify unnecessary duplicates, verify every link and resource, and document the final structure.

Now we are teaching more than file management. We are teaching troubleshooting. We are teaching systems thinking. We are teaching students that **structure has consequences**.

## Ask the Computer: Where Am I?

I would even introduce a tiny amount of command-line work. Not enough to turn an introductory web design course into a Linux administration course. Just enough to expose the underlying model.

```bash
pwd
ls
cd
mkdir
```

Of these, `pwd` may be the most conceptually important. It asks a remarkably useful question:

> **Where am I right now?**

Once a student can answer that question, relative paths become much easier to understand. If I know where I am, and I know where the information is, I can describe how to get from one to the other. That idea extends far beyond the command line.

## Organization Also Carries Responsibility

There is another lesson I would borrow carefully from Anishinaabe teachings: organizing knowledge is not value-neutral. Once we collect, name, classify, copy, publish, or share information, we have taken an action that can affect other people and relationships.

The **Seven Sacred Teachings** provide one useful ethical vocabulary for thinking about those responsibilities. At Bay Mills Community College, where I teach, the teachings are presented as Courage (*Aakide'ewin*), Honesty (*Gwe'ekwaadiziwin*), Humility (*Dibaadendiziwin*), Love (*Gaazhwenimowin*), Respect (*Minaadendimowin*), Truth (*Debwewin*), and Wisdom (*Nibwaakaawin*). BMCC has made these teachings part of the physical and educational environment of the college through its Seven Sacred Teachings mural in the Michael C. Parish Administration Building. The mural incorporates recordings of BMCC faculty pronouncing the Anishinaabemowin words and BMCC students explaining what the teachings mean to them (Bay Mills Community College, “Culture”). I would still be careful not to present a single published description as the only interpretation across all Anishinaabe communities.

I would not turn those teachings into seven rules for naming computer files. That would trivialize them. But I do think they raise an important educational question: **What responsibilities come with the information we organize?**

If a student creates a folder, copies a photograph, publishes a story, builds a dataset, or trains an AI system, technical correctness is only part of the work. We also have to think about provenance, permission, representation, context, and stewardship.

That is a much richer definition of information literacy.

## File Organization Is Really Information Organization

This is ultimately why I think this belongs alongside the First Five. It would be easy to dismiss file-management skills as remedial computer literacy. I think that would be a mistake.

The student who learns that `images/logo.png` describes a relationship between locations is beginning to learn how computers represent relationships. The student who learns the difference between `logo.png` and `images/logo.png` is learning about context. The student who understands why `../images/logo.png` works is learning about relative location.

The student who renames `Logo FINAL Final2 USETHISONE.png` to `college-logo.png` is learning about metadata, semantics, maintainability, and technical debt. And the student who understands why the version on a laptop might be different from the version on a web server is beginning to understand synchronization, replication, version control, and distributed information systems.

Those are not insignificant ideas. They are foundational computing concepts hiding inside everyday tasks.

## This Is Where Data Literacy Really Begins

We often want to start the conversation about data literacy with spreadsheets, databases, statistics, dashboards, or artificial intelligence. I think we may need to start earlier.

Before someone can meaningfully manage data, they need to understand that information has structure. They need to understand that things have names. They need to understand that things have locations. They need to understand that location establishes context. They need to understand that things can contain other things. They need to understand that one thing can point to another thing. And they need to understand that organizational decisions made today can either reduce or create complexity tomorrow.

That is remarkably close to what we eventually ask people to understand about databases, data lakes, ontologies, knowledge graphs, and artificial intelligence. The scale changes. The fundamental questions do not.

## Before We Teach the Computer, We Have to Teach the Human

The First Five Things to Teach a Computer is ultimately about giving machines enough structure and context to work meaningfully with our world. But perhaps there is a prerequisite.

Before we teach the computer, we need to make sure the human understands the structure too. For my Responsive Web Design students, I increasingly think that means starting not with HTML, CSS, JavaScript, or Bootstrap. It means starting with information.

**What is it?** **What is it called?** **Where is it?** **How is it organized?** **How is it related to everything else?**

Only then do we start telling the computer what to do with it. And perhaps that is one of the most fundamental forms of digital literacy we can teach.

For me, bringing an Anishinaabe perspective into this discussion does not mean claiming that a filesystem is Indigenous knowledge, or translating cultural teachings into computer-science terminology. It means allowing a different knowledge tradition to challenge one of computing's easiest assumptions: that if we can identify, store, classify, and retrieve something, we therefore understand it.

We do not.

Understanding requires context. It requires relationships. It requires knowing where knowledge came from and what responsibilities travel with it. In that sense, the lesson I want students to carry forward is larger than file management. **Before data becomes information, and before information becomes knowledge, we have to understand what is connected to what, and why those connections matter.**

## A Simple Introductory Learning Sequence

For educators who want to incorporate this into an introductory computing or web-development course, I would use a short "Module 0" before beginning HTML.

| Day | Topic | Core Question |
|---|---|---|
| 1 | Files and folders | What is it, and where is it? |
| 2 | Trees and paths | How is information organized and located? |
| 3 | Web project organization | How should related information be grouped? |
| 4 | Local and remote systems | Which copy of the information am I working with? |
| 5 | Broken Website Challenge | Can I diagnose and repair a disorganized information system? |

Then start HTML. At that point, `href` and `src` are not just syntax. They have meaning.

### Works Cited

Bay Mills Community College. “Culture.” *Bay Mills Community College*, https://bmcc.edu/community/culture/index.html. Accessed 21 Oct. 2026.

GitHub. “Repositories Documentation.” *GitHub Docs*, https://docs.github.com/en/repositories. Accessed 21 Oct. 2026.

Great Lakes Indian Fish & Wildlife Commission. “Indigenous Knowledge.” *Great Lakes Indian Fish & Wildlife Commission*, https://glifwc.org/language-culture/indigenous-knowledge. Accessed 21 Oct. 2026.

Mozilla Developer Network. “Dealing with Files.” *MDN Web Docs*, https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Environment_setup/Dealing_with_files. Accessed 21 Oct. 2026.

Mozilla Developer Network. “Resolving Relative References to a URL.” *MDN Web Docs*, https://developer.mozilla.org/en-US/docs/Web/API/URL_API/Resolving_relative_references. Accessed 21 Oct. 2026.

Sault Ste. Marie Tribe of Chippewa Indians. “Anishinaabemowin.” *Sault Ste. Marie Tribe of Chippewa Indians*, 21 Feb. 2024, https://www.saulttribe.com/membership-services/culture/language-department/. Accessed 21 Oct. 2026.

Sault Ste. Marie Tribe of Chippewa Indians. “Language & Culture.” *Sault Ste. Marie Tribe of Chippewa Indians*, 24 May 2024, https://www.saulttribe.com/membership-services/culture. Accessed 21 Oct. 2026.


Treuer, Anton. “Indigenous Ways of Knowing: Ojibwe Knowledge, Science, and the Value of Different Worldviews.” *Anton Treuer*, 8 Apr. 2026, https://antontreuer.com/insights/2026/4/8/indigenous-ways-of-knowing-ojibwe-knowledge-science-and-the-value-of-different-worldviews. Accessed 21 Oct. 2026.
