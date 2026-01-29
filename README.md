# 👋 Hi, I'm Jason Kronemeyer

### **Veteran · Digital Transformation Leader · Data Scientist · Digital Equity Advocate**

### Mantra: **LearnIT | BuildIT | TeachIT**

_Building Solutions at the Intersection of Information and Technology._

---

With over 25 years of experience in IT infrastructure, network systems, and educational technology, I am passionate about using technology and data science to create equitable opportunities for all. My journey has spanned service in the U.S. Air Force, leadership in educational innovation, and most recently, earning a Master of Applied Data Science from the University of Michigan.

---

## 🚀 What Drives Me

- **Digital Equity & Broadband Advocacy:** Much of my career has focused on closing the digital divide—ensuring rural schools and communities have the connectivity, skills, and resources to thrive. I am honored to be recognized as a Broadband Champion for my efforts to expand broadband access and digital opportunity.
- **Data Science for Good:** I apply data skills to address real-world problems, as showcased in my [Digital Equity Learning Project](https://github.com/jasonkronemeyer/DigitalEquityLearning.github.io).
- **Lifelong Learning:** My journey is documented through hands-on practice and real-world applications in my [portfolio](https://github.com/jasonkronemeyer/jasonkronemeyer.github.io), where I strive to make my work accessible to all.
- **Ethical Leadership:** I strive to balance innovation with responsibility, ensuring my work is grounded in fairness, transparency, and community impact.

---

## 📘 My GitHub Journey

> **Note on Content Philosophy:** This repository and my website represent a practice of **learning in public**. The content here is experimental and exploratory—documenting my curiosity, research notes, and evolving understanding rather than claiming definitive expertise. I believe in transparency in the learning process and invite feedback, questions, and collaboration. Nothing here is the final word; everything is subject to revision as my knowledge grows.

### Content Status System

To provide transparency about where content sits in my knowledge development process, I use a status system for blog posts:

**Development Stages:**
- 🔍 **Research** - Actively gathering sources and exploring ideas
- 📝 **Draft** - Work in progress, structure and arguments taking shape
- 📋 **Review** - Content complete, making final refinements
- ✨ **Updated** - Previously published content revised with new insights

**Content Types:**
- 📄 **Brief** - Short-form post focused on a single topic or focused idea
- 📚 **Series** - Part of a connected set of posts on related topics
- 🛠️ **Tutorial** - Step-by-step hands-on instructional guide
- 📊 **Analysis** - Deep research and data exploration

Posts without a status label are considered published and stable, representing my current best understanding. See the [full Status Guide](https://www.jasonkronemeyer.com/about/status-guide/) for more details on this system.

From my first repository, [hello-world](https://github.com/jasonkronemeyer/hello-world), I have continuously explored new technologies and methods, building not just technical skills but also a deeper understanding of how technology can be leveraged for social good. My repositories reflect my evolving interests—from early scripting to advanced analytics and digital equity initiatives.

### Discovering Data Science

In my main website and data science portfolio, [jasonkronemeyer.github.io](https://github.com/jasonkronemeyer/jasonkronemeyer.github.io), I share notebooks, experiments, and projects that have shaped my understanding of the field. Here, I explore everything from foundational Python to advanced analytics, always striving to make my work accessible and reusable for others. The public nature of these projects reflects my belief in open learning and community-driven growth.

### Making Technology Work for Everyone

A defining milestone in my journey is the [Digital Equity Learning Project](https://github.com/jasonkronemeyer/DigitalEquityLearning.github.io). Developed as a capstone for the MADS program and a team effort, this repository is dedicated to using data science for social good. Through Jupyter Notebooks, case studies, and equity-focused resources, I investigate ways to understand and address gaps in digital access and skills—empowering learners, educators, and communities striving for digital inclusion.

### Ethics, Reflection, and Impact

Technical expertise must be paired with ethical responsibility and thoughtful reflection. My work is informed by ongoing consideration of bias, fairness, and the broader societal impact of the tools and analyses I create. I believe that every line of code, every model, and every project can shape the world in positive or negative ways. With this awareness, I strive to act conscientiously—balancing innovation with care, and always seeking to ensure that my contributions benefit not just individuals, but society as a whole while doing no harm.

---

## 🏆 Highlights

- Recognized as a **Broadband Champion** by Dr. Pierrette Renée Dagg in the Benton Institute’s series, "Could It Be Me? Should It Be Me? Understanding What Makes Broadband Champions," for advancing broadband access and digital equity.
- **Founder & CEO, Jason Kronemeyer LLC** — Leading strategic technology initiatives for commercial, governmental, educational and nonprofit organizations.
- **Project Director, EUPConnect Collaborative** — Driving connectivity and digital equity in Michigan’s Upper Peninsula.
- **Director of Technology, REMC 22, EUPISD** — Building infrastructure and capacity for 19 rural school districts.
- **Distinguished Partnership Award** — Recognized by Michigan State University for community-engaged service.
- **Military Service** — U.S. Air Force veteran, Signals Intelligence Analyst (TS-SCI clearance).

---

## 📚 Featured Projects

- [Digital Equity Learning Project](https://github.com/jasonkronemeyer/DigitalEquityLearning.github.io): Capstone data science project focused on closing the digital divide.
- [Personal Data Science Portfolio](https://github.com/jasonkronemeyer/jasonkronemeyer.github.io): Notebooks, experiments, and ongoing learning.

---

## 🌱 Values

As I advance in technology and data science, I recognize that technical expertise must be paired with ethical responsibility and thoughtful reflection. My work is informed by ongoing consideration of bias, fairness, and the broader societal impact of the tools and analyses I create. I believe that every line of code, every model, and every project can shape the world in positive or negative ways. With this awareness, I strive to act conscientiously—balancing innovation with care, and always seeking to ensure that my contributions benefit not just individuals, but society as a whole while doing no harm.

---

## 📫 Connect

- [Website & Portfolio](https://www.jasonkronemeyer.com/)
- [LinkedIn](https://www.linkedin.com/in/jasonkronemeyer/)
- [Resume](https://github.com/jasonkronemeyer/jasonkronemeyer.github.io/blob/main/index.html)

---

*Let’s build a more equitable digital future together!*

---

## 🛠️ Build & CI notes

If you use `jekyll-diagrams` (Mermaid) the plugin requires Puppeteer/Chromium to render diagrams during the build. Common issues and solutions:

- "Failed to launch the browser process": install system Chromium (Ubuntu/Debian example):

  sudo apt update && sudo apt install -y chromium-browser ca-certificates fonts-liberation libnss3 libatk1.0-0 libatk-bridge2.0-0 libcups2 libx11-xcb1 libxcomposite1 libxdamage1 libxrandr2 libgbm1 libgtk-3-0 libnspr4 libxss1

- You can set environment variables when building locally:

  export PUPPETEER_EXECUTABLE_PATH=$(which chromium-browser)
  export PUPPETEER_ARGS='--no-sandbox --disable-setuid-sandbox'
  bundle exec jekyll build

- CI: the repository includes a GitHub Actions workflow at `.github/workflows/jekyll-build.yml` which installs Chromium and sets `PUPPETEER_EXECUTABLE_PATH` before building.

If you prefer not to install Chromium, temporarily disable `jekyll-diagrams` in `_config.yml` while editing content.

