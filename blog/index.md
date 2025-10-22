---
layout: page
title: Blog
permalink: /blog/
---

# Exploring the Intersection of Data, Education & Innovation

{:.lead}
From teaching my first computer "Hello World" in 1983 to collaborating with AI systems today, I've witnessed an incredible evolution in how we learn, teach, and solve problems with technology.

{% include callout.html type="info" title="What You'll Find Here" content="Deep dives into spatial data for community development, smart building technologies, passive optical networks, and the transformative power of knowledge graphs in education. Plus occasional reflections on the journey from BASIC programming to modern AI collaboration." %}

This is where I share discoveries, challenges, and insights from the frontier of **educational technology**, **community development through data**, and **intelligent infrastructure systems**. Whether you're an educator exploring AI integration, a researcher investigating smart buildings, or a community leader interested in spatial data applications, there's something here for you.

## Latest Explorations

*From policy analysis to technical deep-dives, here's what I've been thinking about lately...*

<div class="post-list">
{% for post in site.posts %}
  <article class="post-preview">
    <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
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