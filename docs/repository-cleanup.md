# 仓库整理记录

## 目标和保留范围

清理不再使用的 AcademicPages / Minimal Mistakes 模板，保留个人主页与 GPS-Gaussian 项目页面的内容、样式、交互和原有访问路径。

- 当前保留范围为 `GPS-Gaussian.html`、整个 `assets/GPS-Gaussian/` 和 `images/`，以及下文列出的主页 CSS、JavaScript、字体及授权文件。
- 第一阶段曾按要求保留整个 `assets/`，并对项目 HTML、`assets/` 和 `images/` 共 79 个文件逐一核对 SHA-256，全部一致。该结果属于第一阶段；后续按新增授权清理了 `assets/css/`、`assets/js/`、`assets/fonts/` 中的旧文件，不再承诺整个 `assets/` 与最初完全相同。
- `GPS-Gaussian.html` 没有 Jekyll front matter，也不依赖旧布局；其运行时本地资源为 `assets/GPS-Gaussian/` 中的 CSS、图片和视频。
- 不修改远程 Font Awesome、YouTube 等外部资源引用。
- 本轮开始前已存在的 `files/paper1.pdf`、`images/hfut.jpeg` 删除没有被恢复或再次修改。

## 结构调整

- 主页源文件从 `_pages/about.md` 移至 `index.md`；保留 `permalink: /`、`/about/` 和 `/about.html` 跳转。
- 后续按维护命名整理：`_data/` → `data/` → `publications/`，`_layouts/` → `layouts/`；论文文件由 `home_publications.yml` 改名为 `piblication_list.yml`。同步设置 Jekyll 的 `data_dir`、`layouts_dir` 和发布排除项；Liquid 仍使用 `site.data`，当前论文列表键为 `site.data.piblication_list`。目录内文件内容保持原样。
- 主页布局 `layouts/home.html`、论文数据 `publications/piblication_list.yml`、所有主页 CSS / JS / 字体保持原样。
- 设计记录移入 `docs/design-qa.md`。文档和检查脚本排除在网站发布内容之外。
- 精简 `_config.yml`、`_config.dev.yml`、`Gemfile`；保留 GitHub Pages 构建、sitemap 和 redirect-from。移除旧博客、评论、社交分享、分类归档等不用的配置。
- 添加 `scripts/check_site.py`，可检查构建结果的两个主页面、跳转、主页锚点及本地资源；可传入 `--baseline` 比较整理前后的输出。
- 重写 README，记录实际目录、维护入口、本地预览及构建检查方法。

## 第一阶段：模板和示例清理

共删除 203 个旧模板或示例文件：

- `_includes/` 和旧版 `_layouts/`（保留 `home.html`）。
- `_sass/` 旧主题和其第三方 Sass 依赖。
- `_data/` 中的旧作者、导航、UI 文案及示例评论（保留论文数据）。
- `_posts/`、`_drafts/`、`_portfolio/`、`_talks/` 中的模板示例。
- `markdown_generator/`、`talkmap/`、`talkmap.py`、`talkmap.ipynb`。
- 旧模板 `CHANGELOG.md`、`CONTRIBUTING.md`、`package.json`。

原模板 LICENSE 和保留资源中的版权信息仍在。第一阶段按当时要求保留了 `assets/` 内的旧文件，并排除旧 Sass 入口 `assets/css/main.scss` 的构建，避免继续依赖被删除的 `_sass/`。这些旧资源不被两个目标页面引用，后续在第二阶段移除。

模板示例的博客、portfolio、talks、talkmap 路径以及旧主题生成的 `assets/css/main.css` 随之退役；它们不在主页或 GPS 页面中被引用。主页和 GPS 页面路径保持不变。

## 第二阶段：旧 CSS、JavaScript 和字体清理

根据新增的清理授权，`assets/css/`、`assets/js/` 和 `assets/fonts/` 只保留现有主页需要的文件：

- `assets/css/home.css`、`assets/css/home-fonts.css`。
- `assets/js/home.js`。
- `assets/fonts/source-sans-3-normal.woff2`、`assets/fonts/source-sans-3-italic.woff2`。
- `assets/fonts/source-serif-4-normal.woff2`、`assets/fonts/source-serif-4-italic.woff2`。
- `assets/fonts/source-sans-3-OFL.txt`、`assets/fonts/source-serif-4-OFL.txt`、`assets/fonts/README.md`。

移除这些目录中的旧模板 Sass 入口、通用 Bootstrap / Academicons / collapse 样式、旧版主页脚本、jQuery、Popper、Bootstrap 脚本、插件，以及 Font Awesome / Academicons 字体。删除的 Bootstrap 文件位于通用 `assets/css/` 和 `assets/js/`；项目实际使用的 `assets/GPS-Gaussian/css/bootstrap-4.4.1.css` 仍保留。

本阶段共删除 36 个文件：5 个 CSS / Sass 文件、19 个旧字体文件、12 个 JavaScript 文件，共 3,701,720 字节。删除前备份位于 `/var/folders/84/jgddn_y177v0_7t4ksphpytm0000gn/T/homepage-legacy-assets-pboxfpol/`。

同步移除 `_config.yml` 中针对 `assets/css/main.scss`、`assets/js/_main.js`、`assets/js/plugins`、`assets/js/vendor` 的过时构建排除项。保留论文数据目录（当时为 `data/`，现为 `publications/`）、`layouts/`、文档和脚本的发布排除设置。

资源删除本身不改写主页内容、布局及保留资源，也不修改 `GPS-Gaussian.html`、`assets/GPS-Gaussian/` 或 `images/`。另外修复了下面记录的 13 处图片路径引用；主页样式、脚本、字体和远程 Font Awesome、YouTube 等外部引用保持原样。

## 已有图片路径问题

第一阶段整理前，主页仍引用已删除的 `/images/hfut.jpeg`，目录中已有 `/images/hfut.png`。当时仅将这一个引用更新为现有 PNG，以恢复合肥工业大学标志；没有改写教育背景或其他页面内容。

第二阶段构建检查时，图片目录已整理为 `images/logo/` 和 `images/paper_thumbnail/`，但 `index.md` 和论文数据文件（现为 `publications/piblication_list.yml`）仍使用旧图片路径，导致图片引用失效。此项修复与旧资源删除分开处理，保留目录中现有图片的内容：

- `index.md` 中的 2 个学校标志引用改为 `/images/logo/hit.png`、`/images/logo/hfut.png`。
- 论文数据文件中的 11 个预览图引用改为 `/images/paper_thumbnail/` 下的原文件名。
- 头像仍位于 `/images/avatar.jpg`；不移动或修改图片，不改变教育背景、论文文字、链接及排列。

第二阶段的主页 HTML 比较仅允许这 13 处路径更新。图片文件以删除旧资源前采集的源文件快照校验，保留现有图片内容。

## 第一阶段验证记录

- 使用同一个 Jekyll 3.10.0 环境分别构建整理前、后的仓库。
- 整理后的主页 HTML 与基线逐字节比较一致，唯一允许的差异为上述 `hfut.jpeg` → `hfut.png` 路径修复。
- GPS 页面 HTML 和所有本地依赖与基线逐字节一致；额外校验整个 assets 和 images 目录的源文件哈希一致。
- 自动检查通过：2 个页面、2 个 about 跳转、主页锚点、32 个本地图片/视频/CSS/字体资源，无缺失。
- Jekyll safe 模式也构建成功，并通过相同的资源与页面基线检查。
- 浏览器实测主页保留 11 篇论文、180px 头像和粘性侧栏，两个学校标志正常加载；GPS 页面两个图片及 7 个内嵌本地视频均加载成功，无视频错误。
- `git diff --check` 通过。

## 第二阶段验证

- Jekyll 3.10.0 构建成功，输出 6 个页面和 39 个静态文件。
- 检查脚本通过：2 个页面、2 个跳转、主页锚点及 32 个本地资源均有效。
- 主页生成 HTML 与删除前构建相比，只有上述 13 处图片路径更新；GPS 页面及两个 about 跳转逐字节一致。
- 保留的主页 CSS、JS、字体和 GPS 专用资源与删除前构建逐字节一致；所有受保护的源文件（包括当前图片）与删除前快照校验一致，仅排除系统 `.DS_Store` 元数据和已单独核对路径变更的两个引用文件。
- `assets/css/`、`assets/fonts/`、`assets/js/` 合计剩余 10 个当前主页文件，36 个旧文件已删除。
- `git diff --check` 通过。

本次整理没有提交、推送或部署。第一阶段开始前的完整源文件备份与删除清单位于本机临时目录 `/var/folders/84/jgddn_y177v0_7t4ksphpytm0000gn/T/homepage-cleanup-backup-2bhru568/`；Git 中的原有已跟踪文件也可恢复。
