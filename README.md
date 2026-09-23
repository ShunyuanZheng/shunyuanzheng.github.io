# Shunyuan Zheng 的个人主页

## 目录结构

```text
index.md                       主页正文与各板块，访问路径仍为 /
_config.yml                    站点地址、个人资料、构建配置
_config.dev.yml                本地预览地址覆盖配置
publications/piblication_list.yml  论文数据
layouts/home.html              主页 HTML 布局
assets/css/home.css            主页样式
assets/css/home-fonts.css      主页字体声明
assets/js/home.js              自动 / 浅色 / 深色主题切换
assets/fonts/                  Source Sans 3、Source Serif 4 字体与授权说明
images/avatar.jpg              个人头像
images/logo/                   学校、机构标志
images/paper_thumbnail/        论文预览图片
GPS-Gaussian.html              独立项目页面，保持原样
assets/GPS-Gaussian/            项目页面的 CSS、图片、视频，保持原样
docs/                          设计检查与本次清理记录，不发布到网站
scripts/check_site.py          构建产物的资源、锚点及页面一致性检查
Gemfile                        GitHub Pages 构建依赖
LICENSE                        原模板授权
```

## 日常维护

- 简介、教育与实习经历（Experiences）、报告、获奖、联系方式：编辑 `index.md`。
- 论文：编辑 `publications/piblication_list.yml`，年份按从新到旧排列；没有公开链接时使用 `links: []`。
- 姓名、头像文件名、邮箱、Scholar 和 GitHub 链接：编辑 `_config.yml` 中的 `author`。
- 学校、机构标志放入 `images/logo/`，论文预览图放入 `images/paper_thumbnail/`，同步更新正文或论文数据中的路径。论文图片的 `image_width`、`image_height` 填写原图像素尺寸，用于加载前预留正确比例；页面统一显示宽度，高度自适应。
- 主页样式与行为分别在 `assets/css/home.css` 和 `assets/js/home.js`；头像不随窗口高度缩放，桌面侧栏使用粘性定位。

`publications/` 存放论文数据，`layouts/` 存放页面布局。`_config.yml` 通过 `data_dir` 和 `layouts_dir` 指定这两个目录，并排除源文件的直接发布；Liquid 中仍使用 `site.data`，论文列表通过 `site.data.piblication_list` 读取，页面仍使用 `layout: home`。

## 本地预览与检查

安装 Ruby 和 Bundler 后，在仓库根目录执行：

```sh
bundle install
bundle exec jekyll serve --config _config.yml,_config.dev.yml
```

打开 <http://localhost:4000>。修改配置后需要重启预览。

发布前检查：

```sh
bundle exec jekyll build
python3 scripts/check_site.py _site
```

继续使用原有 GitHub Pages 发布方式即可。主页仍位于 `/`，`/about/` 和 `/about.html` 保留跳转；GPS-Gaussian 的原始 `/GPS-Gaussian.html` 路径以及 GitHub Pages 的无扩展名链接保持不变。

## 项目页面与保留资源

`GPS-Gaussian.html` 是不经过 Jekyll 模板处理的静态 HTML，其本地运行依赖位于 `assets/GPS-Gaussian/`。项目 HTML、整个 `assets/GPS-Gaussian/` 和 `images/` 均保留原样；项目使用的 Bootstrap 样式位于其独立目录内。

主页资源目录已清除旧模板文件，目前保留：

- `assets/css/`：`home.css` 和 `home-fonts.css`。
- `assets/js/`：`home.js`。
- `assets/fonts/`：Source Sans 3、Source Serif 4 各自的正常体和斜体 WOFF2 文件、两份 OFL 授权及 `README.md`。

清理范围、验证结果及已发现的图片路径修复见 [清理记录](docs/repository-cleanup.md)，历史视觉检查见 [设计检查](docs/design-qa.md)。

## 授权

仓库最初基于 AcademicPages / Minimal Mistakes。保留原 [MIT License](LICENSE)；本地 Source Sans 3 和 Source Serif 4 的 OFL 授权位于 `assets/fonts/`。其他保留资源中的原有版权信息未改动。
