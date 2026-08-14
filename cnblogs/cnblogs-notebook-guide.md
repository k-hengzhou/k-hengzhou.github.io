# 博客园「笔记本风格」主题使用指南

把 Jekyll 博客（Chirpy 主题）的笔记本风格移植到**博客园**（cnblogs）。

## 📁 文件说明

| 文件                         | 用途                                                                           |
| ---------------------------- | ------------------------------------------------------------------------------ |
| `cnblogs-notebook-theme.css` | 完整主题 CSS，**粘贴到博客园后台即可**                                         |
| `cnblogs-callout.html`       | 让 `> [!TIP]` 等语法生效（可选，**完整 HTML**，粘贴到「页脚HTML代码」）        |
| `cnblogs-sidebar-news.html`  | 侧边栏公告（**纯内容**「关于我」，只含少量内联样式，粘贴到「侧边栏公告」即可） |
| 本文档                       | 使用说明 + 代码块标题栏 HTML 模板                                              |

---

## 🚀 快速开始（3 步）

### 第 1 步：粘贴 CSS

登录博客园 → **管理后台** → **设置** → 找到 **页面定制CSS代码** 文本框 → 粘贴 `cnblogs-notebook-theme.css` 的全部内容 → 保存。

> ⚠️ 注意：粘贴前先确认「禁用模板默认CSS」**不要勾选**（保持默认即可），否则会破坏博客园基础布局。

### 第 2 步：写文章时给代码块加标题栏

博客园 Markdown 编辑器生成的代码块本身**没有** macOS 交通灯标题栏和语言标签，需要你手动在代码块**前一行**加一个 div：

```html
<div class="cn-codebar" data-lang="matlab"></div>
```

实际效果就是：**标题栏 div + 代码块 pre 无缝衔接**，组成一个带交通灯圆点和居中语言标签的深色代码卡片。

在 Markdown 编辑器中的写法示例：

````
<div class="cn-codebar" data-lang="matlab"></div>

​```matlab
x = 1:0.1:10;
plot(x, sin(x));
​```
````

> 💡 如果嫌每篇都手写麻烦，可以把上面的 div 存成一个博客园的「常用HTML片段」或本地代码片段，随时插入。

### 第 3 步：发表

发表后即可看到完整效果。**没加标题栏的旧代码块**也能正常显示为深色卡片 + 左上角红黄绿圆点（只是没有语言标签）。

---

## 🎨 主题效果一览

| 元素                 | 效果                                       |
| -------------------- | ------------------------------------------ |
| 正文容器 `.postBody` | 白色 + 20px 方格笔记本网格                 |
| `# 一级标题`         | 橘红色 `#df5a49` 居中                      |
| `## 二级标题`        | 黑色方框 + 四角十字准星（`📑` 这类也适用） |
| `###` ~ `#####`      | 下方纯蓝色 `#2b6cb0` 横线                  |
| `> 引用`             | 浅青色 `#eaf8f8` 圆角卡片                  |
| `` `行内代码` ``     | 浅紫底 `#f4f0fa` + 紫字 `#8c72cb`          |
| `---` 分割线         | 浅紫色 `#d1badd`                           |
| 表格                 | 深灰边框 + 表头浅灰底 + 斑马纹             |
| 代码块               | atom-one-dark 深色卡片 + 交通灯 + 语言标签 |
| `.custom-toc-box`    | 居中徽章（可选，手动 HTML）                |

---

## 🧩 可选功能

### 0. 侧边栏公告：「关于我」（可选）

把 Jekyll 版的「关于」页面（`_tabs/about.md`）转成博客园侧边栏公告。**纯内容版**：只展示标题、简介、联系信息和二维码，不套用笔记本主题样式，也不依赖主题 CSS。

**如何启用（1 步）**：

1. 登录博客园 → **管理后台** → **设置** → 找到 **侧边栏公告** 文本框 → 把 `cnblogs-sidebar-news.html` 的**全部内容**粘贴进去 → 保存。

> 💡 本文件只含少量内联样式（如二维码尺寸、边框），不使用 `<style>` 标签——博客园「侧边栏公告」的 HTML 校验器不接受内嵌 `<style>`，会报「不是有效的 HTML」。因此本公告**独立生效**，无需任何配套配置。
>
> 💡 二维码图片当前指向 GitHub Pages 上的原图（`https://k-hengzhou.github.io/assets/img/qrcode.jpg`），建议上传到博客园相册后替换为博客园图片直链，避免外链失效。

**效果预览**：

```
📐 关于我
在这里你能发现有意思的数学
─────────────
联系
• 邮箱：w_hengzhou@163.com
• GitHub：@k-hengzhou
• 知乎：@khzz
• 个人网站：k-hengzhou.github.io
• 微信公众号：
   [二维码]
```

### 1. 居中「目录徽章」（可选）

如果你想要像 Jekyll 版那样居中的目录徽章，在 Markdown 里写：

```html
<div class="custom-toc-box">📑 目录</div>
```

CSS 已内置 `.custom-toc-box` 样式（黑色方框 + 上下偏移横线）。

### 2. 博客园自带的「目录」

博客园的 Markdown 编辑器有「插入目录」功能（`[TOC]`），它生成的目录结构与本主题的网格背景兼容，可直接使用。

### 3. `> [!TIP]` 等 GitHub 风格提示框

博客园 Markdown 引擎**默认不会**把 `> [!IMPORTANT]` 渲染成彩色提示框，而是当普通引用。但通过配套的 `cnblogs-callout.html`（带 `<script>` 的完整 HTML）+ 主题 CSS 第 12 节即可支持。

**支持的类型**（GitHub 官方配色）：

| 语法                                          | 效果       |
| --------------------------------------------- | ---------- |
| `> [!NOTE]` / `> [!INFO]`                     | 蓝色信息框 |
| `> [!TIP]`                                    | 绿色提示框 |
| `> [!IMPORTANT]`                              | 紫色重点框 |
| `> [!WARNING]`                                | 黄色警告框 |
| `> [!CAUTION]` / `> [!DANGER]` / `> [!ERROR]` | 红色危险框 |

**如何启用（2 步）**：

1. **CSS**：粘贴主题 CSS 时已包含第 12 节（无需额外操作）；
2. **HTML**：登录博客园 → **管理后台** → **设置** → **页脚HTML代码** → 把 `cnblogs-callout.html` 的**全部内容**（已经带 `<script>` 标签的完整 HTML）粘进去 → 保存。

> ⚠️ **重要**：博客园的「页脚HTML代码」要求内容是**有效的 HTML**，所以必须粘贴 `cnblogs-callout.html` 这个**完整文件**（含 `<script>` 和 `</script>` 标签），不能只复制里面的纯 JS 代码——否则 HTML 校验器会把 JS 里的 `<` 字符当成标签解析，报「在开始标签之后检测到无效字符」错误。

> ⚠️ 若「页脚HTML代码」提示需要 JS 权限，请到后台设置页申请或联系博客园团队开通（admin@cnblogs.com）。

**工作原理**：博客园把 `> [!IMPORTANT]` 渲染成 `<blockquote>` 且保留 `[!IMPORTANT]` 文字。JS 在页面加载后扫描 `#cnblogs_post_body` 中的 `blockquote`，检测到首行 `[!XXX]` 标记（或加粗的 `**IMPORTANT**`）就自动加上 `callout-xxx` 类并清除标记文字，CSS 负责上色。同时兼容博客园**原生渲染**的 `.markdown-alert-*` / `.alert-*` 结构（CSS 第 12.5 节），并带多次延迟重试，兼容异步加载。

**效果预览**（在 Markdown 里写）：

```markdown
> [!IMPORTANT]
> **优秀数学建模论文四要素**
> 假设的合理性，建模的创造性，结果的合理性，表述的清晰程度

> [!TIP]
> 摘要是一篇文章的入口……
```

> 💡 如果某篇博客园的博客/编辑器已经原生渲染了提示框（生成了带 `callout`/`prompt` 类的结构），本主题的引用样式会自动排除，不会冲突。

---

## 🔧 常见问题

### Q1：代码块语言标签没显示？

检查两点：

1. div 的 `data-lang` 属性值是否正确（如 `data-lang="matlab"`）；
2. div 是否紧贴在代码块**前一行**，中间没有空行。

### Q2：代码块顶部圆点重复 / 标题栏和代码块之间有缝隙？

- 如果两者之间有空行，Markdown 会把它们分成两个块，div 的 `~` 选择器就失效了。**确保 div 和代码块之间没有空行**。

### Q3：我想换网格大小 / 配色？

直接改 CSS 顶部注释标注的色值：

- 网格大小：`background-size: 20px 20px` 改 `30px 30px` 等；
- 网格线色：`#f0f0f5`；
- 交通灯颜色：红 `#ff5f57`、黄 `#febc2e`、绿 `#28c840`。

### Q4：代码块里语法高亮颜色不对？

博客园 Markdown 使用 **highlight.js** 做高亮，token 类名是 `.hljs-keyword`、`.hljs-string` 等，本主题已全部按 atom-one-dark 配色覆盖。如果你发现某类 token 没覆盖到（比如 MATLAB 特有的 `end` 关键字），告诉我，我可以补充对应的 `.hljs-*` 规则。

### Q5：`> [!IMPORTANT]` 没有生效？

先做**三步诊断**，判断是哪一层没生效：

1. **打开文章页面**，按 `F12` 打开开发者工具，在「元素」面板找到该提示框对应的元素：
   - 如果看到的是 `<blockquote class="callout-important">` → **JS 已生效**，问题在 CSS（见第 3 步）；
   - 如果看到的是 `<blockquote>`（无 class，里面文字还是 `[!IMPORTANT]`）→ **JS 没生效**，继续第 2 步；
   - 如果看到的是 `<blockquote class="markdown-alert markdown-alert-important">` 或 `<div class="markdown-alert...">` → 博客园**已原生渲染**，CSS 第 12.5 节已兼容，无需 JS。
2. **JS 没生效**的可能原因：
   - 「页脚HTML代码」保存时没通过校验（必须粘贴带 `<script>` 的完整 HTML 文件内容）；
   - 你的账号没有 JS 权限（博客园会直接丢弃 `<script>`）——后台设置页申请，或联系 admin@cnblogs.com；
   - 页面缓存：清缓存 / 强刷（`Ctrl+F5`）再看。
3. **CSS 没生效**的可能原因：
   - 「页面定制CSS代码」里是否真的保存了最新内容（12.5 节兼容样式在最末尾）；
   - 浏览器缓存：强刷后再看。

**兜底方案（不依赖 JS，100% 生效）**：直接在 Markdown 里写一个带 class 的 HTML 引用块：

```html
<blockquote class="callout-important">
  <p><strong>重要</strong></p>
  <p>这里是重要内容……</p>
</blockquote>
```

这样无论 JS 是否执行，只要 CSS 在就能显示紫色重点框。

---

## 📝 代码块标题栏 HTML 模板速查

```html
<!-- MATLAB -->
<div class="cn-codebar" data-lang="matlab"></div>

<!-- Python -->
<div class="cn-codebar" data-lang="python"></div>

<!-- C++ -->
<div class="cn-codebar" data-lang="cpp"></div>

<!-- Java -->
<div class="cn-codebar" data-lang="java"></div>

<!-- 无语言（纯文本 / 输出） -->
<div class="cn-codebar" data-lang="text"></div>
```

---

## ✅ 对照清单：从 Jekyll 版迁移到博客园版做了什么改动

| Jekyll 版 (custom-notebook.scss)     | 博客园版 (本主题)                                           | 说明                  |
| ------------------------------------ | ----------------------------------------------------------- | --------------------- |
| `article .content`                   | `#cnblogs_post_body`                                        | 博客园文章内容容器 ID |
| `div.language-xxx.highlighter-rouge` | `pre` + `.cn-codebar`                                       | 代码块结构不同        |
| Rouge `.k` / `.s` / `.nf`            | `.hljs-keyword` / `.hljs-string` / `.hljs-title`            | 高亮库不同            |
| `.table-wrapper > table`             | `table`                                                     | 博客园表格直接裸露    |
| `blockquote:not([class^='prompt-'])` | `blockquote:not([class*='callout']):not([class*='prompt'])` | 排除提示框方式不同    |
| `h2` 方框 + 十字准星                 | 同（纯 CSS 直接搬）                                         | 无改动                |
| `.custom-toc-box`                    | 同                                                          | 无改动                |
