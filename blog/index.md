---
layout: page
title: The Signal
permalink: /blog/
---

# Exploring the Intersection of Data, Education & Innovation

{:.lead}
From teaching my first computer "Hello World" in 1983 to collaborating with AI systems today, I've witnessed an incredible evolution in how we learn, teach, and solve problems with technology.

<p style="font-size: 0.9rem; color: #666; font-style: italic; margin-bottom: 1.5rem;">
Posts are marked by development stage—learn more about the <a href="{{ '/about/status-guide/' | relative_url }}">status system</a> behind this transparent approach to knowledge sharing.
</p>

{% include callout.html type="info" title="What You'll Find Here" content="Deep dives into spatial data for community development, smart building technologies, passive optical networks, and the transformative power of knowledge graphs in education. Plus occasional reflections on the journey from BASIC programming to modern AI collaboration." %}

This is where I share discoveries, challenges, and insights from the frontier of **educational technology**, **community development through data**, and **intelligent infrastructure systems**. Whether you're an educator exploring AI integration, a researcher investigating smart buildings, or a community leader interested in spatial data applications, there's something here for you.

<div class="site-disclaimer">
  <p>🔬 <em>Learning in Public</em> — This site is my digital laboratory—a space for curiosity, experimentation, and evolving ideas. The content here reflects my ongoing experimentation and learning process, and may be revised as my understanding deepens over time.</p>
</div>

## Latest Explorations

*From policy analysis to technical deep-dives, here's what I've been thinking about lately...*

<div class="post-list">
{% for post in site.posts %}
  <article class="post-preview">
    <h3>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      {% if post.status == "research" %}<span style="background-color: #ff9800; color: #fff; padding: 2px 8px; border-radius: 3px; font-size: 0.75em; margin-left: 8px;">🔍 RESEARCH</span>{% endif %}
      {% if post.status == "draft" %}<span style="background-color: #ffc107; color: #000; padding: 2px 8px; border-radius: 3px; font-size: 0.75em; margin-left: 8px;">📝 DRAFT</span>{% endif %}
      {% if post.status == "review" %}<span style="background-color: #2196f3; color: #fff; padding: 2px 8px; border-radius: 3px; font-size: 0.75em; margin-left: 8px;">📋 REVIEW</span>{% endif %}
      {% if post.status == "updated" %}<span style="background-color: #4caf50; color: #fff; padding: 2px 8px; border-radius: 3px; font-size: 0.75em; margin-left: 8px;">✨ UPDATED</span>{% endif %}
      {% if post.status == "brief" %}<span style="background-color: #9c27b0; color: #fff; padding: 2px 8px; border-radius: 3px; font-size: 0.75em; margin-left: 8px;">📄 BRIEF</span>{% endif %}
      {% if post.status == "series" %}<span style="background-color: #3f51b5; color: #fff; padding: 2px 8px; border-radius: 3px; font-size: 0.75em; margin-left: 8px;">📚 SERIES</span>{% endif %}
      {% if post.status == "tutorial" %}<span style="background-color: #009688; color: #fff; padding: 2px 8px; border-radius: 3px; font-size: 0.75em; margin-left: 8px;">🛠️ TUTORIAL</span>{% endif %}
      {% if post.status == "analysis" %}<span style="background-color: #0277bd; color: #fff; padding: 2px 8px; border-radius: 3px; font-size: 0.75em; margin-left: 8px;">📊 ANALYSIS</span>{% endif %}
    </h3>
    <p class="post-meta">
      <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time>
      {% if post.author %} • by {{ post.author }}{% endif %}
      {% if post.categories.size > 0 %} • {% for category in post.categories %}{{ category }}{% unless forloop.last %}, {% endunless %}{% endfor %}{% endif %}
    </p>
    {% if post.excerpt %}
      <p class="post-excerpt">{{ post.excerpt | strip_html | truncatewords: 30 }}</p>
    {% endif %}
  </article>
{% endfor %}
</div>

## Explore by Topic

*Find posts organized by the themes that drive my work and research:*

<div class="categories">
{% assign categories = site.categories | sort %}
{% for category in categories %}
  <span class="category-tag">
    <a href="#{{ category[0] | slugify }}">{{ category[0] }}</a> ({{ category[1].size }})
  </span>
{% endfor %}
</div>