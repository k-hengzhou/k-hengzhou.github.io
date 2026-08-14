---
# the default layout is 'page'
icon: fas fa-info-circle
order: 4
---

> 在这里你能发现有意思的数学

## 联系

欢迎通过以下方式联系我：

<ul class="contact-list">
  <li>
    邮箱：<a href="mailto:{{ site.social.email }}" target="_blank">{{ site.social.email }}</a>
  </li>
  <li>
    GitHub：<a href="https://github.com/{{ site.github.username }}" target="_blank">@{{ site.github.username }}</a>
  </li>
{% for website in site.data.social %}
  <li>
    {{ website.sitename }}：<a href="{{ website.url }}" target="_blank">@{{ website.name }}</a>
  </li>
{% endfor %}
  <li>
    微信公众号：<br />
    <img style="height:192px;width:192px;border:1px solid lightgrey;" src="{{ site.url }}/assets/img/qrcode.jpg" alt="微信公众号二维码" />
  </li>
  
</ul>
