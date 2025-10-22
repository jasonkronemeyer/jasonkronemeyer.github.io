---
layout: page
title: Blog
permalink: /blog/
---

# Blog Posts

Welcome to my blog where I share insights on data science, education technology, and emerging innovations.

## Recent Posts

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

## Categories

<div class="categories">
{% assign categories = site.categories | sort %}
{% for category in categories %}
  <span class="category-tag">
    <a href="#{{ category[0] | slugify }}">{{ category[0] }}</a> ({{ category[1].size }})
  </span>
{% endfor %}
</div>