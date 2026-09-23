---
layout: home
permalink: /
title: Shunyuan Zheng
excerpt: Human-centric 3D vision, human reconstruction, and novel view synthesis.
author_profile: false
redirect_from:
  - /about/
  - /about.html
---

<section id="about" aria-labelledby="about-heading">
  <div class="section-head">
    <h2 id="about-heading">Short Bio</h2>
    <button id="theme-toggle" class="theme-btn" type="button" hidden>Theme: Auto</button>
  </div>
  <div class="prose">
    <p>Hi, this is <strong>Shunyuan Zheng</strong>. I am a final-year (2021 – present) Ph.D. student in the Faculty of Computing, Harbin Institute of Technology, advised by <a href="https://homepage.hit.edu.cn/zhangshengping"><strong>Prof. Shengping Zhang</strong></a>. My research focuses on <strong>human-centric 3D vision</strong>, including 3D human reconstruction and novel view synthesis. From 2023 to 2024, I worked as a research intern at the 3D Vision and Computational Photography Group, Tsinghua University, guided by <a href="https://liuyebin.com"><strong>Prof. Yebin Liu</strong></a>. Now I work as a research intern at the Interactive Intelligence Lab, <a href="https://www.antresearch.com">Ant Research</a>, and also work for <a href="https://www.robbyant.com">Robbyant</a>, both under the mentorship of <a href="https://yaourtb.github.io"><strong>Boyao Zhou</strong></a>.</p>
  </div>
</section>

<section id="research" aria-labelledby="publications-heading">
  <h2 id="publications-heading">Publications</h2>
  <div class="publications-root">
    {% assign publication_years = site.data.piblication_list | group_by: 'year' %}
    {% for year in publication_years %}
    <div class="publication-year">
      <h3 class="pub-year-heading">{{ year.name }}</h3>
      <ul class="research-list">
        {% for paper in year.items %}
        <li class="pub-entry">
          <div class="pub-thumb">
            <img src="{{ paper.image | relative_url }}" alt="{{ paper.title | strip_html | escape }} — research preview" loading="lazy" decoding="async"{% if paper.image_width and paper.image_height %} width="{{ paper.image_width }}" height="{{ paper.image_height }}"{% endif %}>
          </div>
          <div class="pub-main">
            <h4 class="pub-title">{{ paper.title }}</h4>
            <p class="pub-authors">{{ paper.authors }}</p>
            <p class="pub-venue">{{ paper.venue }}{% if paper.highlight %} <span class="pub-highlight">(Highlight)</span>{% endif %}</p>
            {% if paper.links.size > 0 %}
            <div class="pub-links" aria-label="Links for {{ paper.title | strip_html | escape }}">
              {% for link in paper.links %}
              <a href="{{ link.url | escape }}" target="_blank" rel="noopener noreferrer">{{ link.label | escape }}</a>
              {% unless forloop.last %}<span class="pub-link-separator" aria-hidden="true">·</span>{% endunless %}
              {% endfor %}
            </div>
            {% endif %}
          </div>
        </li>
        {% endfor %}
      </ul>
    </div>
    {% endfor %}
  </div>
</section>

<section id="background" aria-labelledby="background-heading">
  <h2 id="background-heading">Experiences</h2>
  <ul class="education-list">
    <li class="education-entry">
      <img class="education-logo" src="{{ '/images/logo/robbyant.png' | relative_url }}" alt="Robbyant" width="2328" height="628" decoding="async">
      <div>
        <h3><a href="https://www.robbyant.com">Robbyant</a></h3>
        <p>Sep. 2026 – Present</p>
        <p>Research Intern</p>
      </div>
    </li>
    <li class="education-entry">
      <img class="education-logo" src="{{ '/images/logo/antgroup.png' | relative_url }}" alt="Ant Group" width="954" height="302" decoding="async">
      <div>
        <h3><a href="https://www.antresearch.com">Ant Group</a></h3>
        <p>Aug. 2025 – Present</p>
        <p>Research Intern</p>
      </div>
    </li>
    <li class="education-entry">
      <img class="education-logo" src="{{ '/images/logo/tsinghua.png' | relative_url }}" alt="Tsinghua University" width="1024" height="1024" decoding="async">
      <div>
        <h3><a href="https://www.tsinghua.edu.cn/en">Tsinghua University</a></h3>
        <p>Feb. 2023 – Aug. 2024</p>
        <p>Research Intern</p>
      </div>
    </li>
    <li class="education-entry">
      <img class="education-logo" src="{{ '/images/logo/hit.png' | relative_url }}" alt="Harbin Institute of Technology" width="300" height="300" decoding="async">
      <div>
        <h3><a href="http://en.hit.edu.cn">Harbin Institute of Technology</a></h3>
        <!-- <p><a href="https://encs.hit.edu.cn">Faculty of Computing</a></p> -->
        <p class="degree">Sep. 2021 – Present · Ph.D. Student</p>
        <p>Sep. 2019–Jun. 2021 · Master of Engineering</p>
      </div>
    </li>
    <li class="education-entry">
      <img class="education-logo" src="{{ '/images/logo/hfut.png' | relative_url }}" alt="Hefei University of Technology" width="1261" height="1247" decoding="async">
      <div>
        <h3><a href="https://www.hfut.edu.cn">Hefei University of Technology</a></h3>
        <!-- <p><a href="https://ci.hfut.edu.cn/English/Home.htm">School of Computer Science and Information Engineering</a></p> -->
        <p>Sep. 2015 – Jun. 2019</p>
        <p>Bachelor of Engineering</p>
      </div>
    </li>
  </ul>
</section>

<section id="talk" aria-labelledby="talks-heading">
  <h2 id="talks-heading">Talks</h2>
  <ul class="text-list">
    <li lang="zh-CN">GPS-Gaussian：基于像素级可泛化3D高斯的人体新视点合成（<a href="https://www.shenlanxueyuan.com/open/course/226" target="_blank" rel="noopener noreferrer">深蓝学院</a>）</li>
  </ul>
</section>

<section id="award" aria-labelledby="awards-heading">
  <h2 id="awards-heading">Awards</h2>
  <ul class="text-list">
    <li>National Scholarship, Ministry of Education of China, 2020</li>
  </ul>
</section>
