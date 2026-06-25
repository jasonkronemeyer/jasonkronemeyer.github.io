---
layout: page
title: Tags
permalink: /tags/
---

This page collects the curated tag vocabulary used across the site, with short descriptions to make the taxonomy easier to understand.

<ul>
  {% assign tag_entries = site.data.tags | sort %}
  {% for tag_entry in tag_entries %}
    {% assign tag = tag_entry[0] %}
    {% assign metadata = tag_entry[1] %}
    {% assign tag_posts = site.posts | where_exp: "post", "post.tags contains tag" %}
    <li>
      <strong>{{ metadata.name | default: tag }}</strong>
      {% if metadata.description %} — {{ metadata.description }}{% endif %}
      <small>({{ tag_posts.size }} post{% if tag_posts.size != 1 %}s{% endif %})</small>
    </li>
  {% endfor %}
</ul>
