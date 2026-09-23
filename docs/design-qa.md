# Homepage design QA

final result: passed

## Requested detail refinements (2026-09-23)

Detail reference: https://github.com/sypj-98/sypj-98.github.io/blob/master/assets/css/custom.css.

- Desktop profile now matches the reference's `position: sticky; top: 1.25rem; align-self: start` as a direct grid child. The earlier fixed-position wrapper and both short-window compression rules were removed at the user's request. The portrait has a constant width; there is no independent scroll container or scrollbar.
- Subsequent requested size adjustment: the portrait component was scaled down by 10%, from 200 × 264px to approximately 180 × 237.6px. Padding and corner radii were also reduced to 90%; the photo keeps its 3:4 aspect ratio. This is a constant size change, not viewport-height scaling. The scroll measurements below predate this adjustment.
- Short Bio links match the detail reference: no default underline, a transparent 1px bottom border, and a 150ms color/border transition on hover. Keyboard focus receives the same treatment plus the existing focus outline. Light and dark colors match the reference; reduced motion disables the transition.
- In-app browser verification: at 1280 × 749, the sidebar moved from y=32 at document top to y=20 at scroll y=749 and remained at y=20 at scroll y=1498. The portrait frame stayed 200 × 264px. At 1280 × 600 its width also remained 200px, with visible overflow and no inner scrolling.
- At 390 × 844, the profile returned to normal document flow with no horizontal overflow. Desktop and mobile screenshots were inspected in the task. Light/dark keyboard-focus link styling was also verified in the browser.
- Jekyll rebuilt successfully (8 pages, 88 static files); `git diff --check` passed. Temporary viewport overrides were restored.

These refinements supersede the earlier fixed-sidebar, short-window compression, and biography-link choices recorded below. As with the reference, desktop viewports shorter than the full sidebar can leave its bottom navigation below the viewport while it is sticky. No portrait shrinking or nested scrolling is added; mobile widths retain normal scrolling.

## Target and scope

Style reference: https://wangchenyang.cn/ (captured 2026-09-23).
Implementation: http://127.0.0.1:4173/ built by Jekyll 3.10.0.
The requested change adapts the reference's visual style to Shunyuan Zheng's existing content. The biography, Background, Talks, Awards, Contact, and all 11 publications remain. No news, awards, or biographical claims were imported from the reference.

## Visual evidence

Evidence directory: `/Users/zsy/.codex/visualizations/2026/09/23/01a0cda8-95ab-7900-8a2a-fd0337b30205/homepage-qa/`.

- Source desktop: `reference-desktop.png`; implementation desktop: `homepage-desktop.png`.
- Both desktop captures: 1280 × 900 CSS viewport, 2560 × 1800 pixels (2× density). Both normalized to 1280 × 900 before comparison.
- Source mobile: `reference-mobile.png`; implementation mobile: `homepage-mobile-final.png`.
- Mobile viewport: 390 × 844 CSS pixels. Full-page captures: 780 × 10758 source and 780 × 12300 implementation, both 2× density. Normalized to 390 pixels wide. Different total heights follow from different retained content.
- Full-view comparisons: `desktop-comparison.png` and `mobile-comparison.png`. Source and implementation were opened together in each comparison image.
- Focused comparison: `typography-comparison.png`, equal-scale crops of the opening section.
- Long-page review: full mobile capture plus `mobile-late-publications.png`; late images were captured again after scrolling to trigger lazy loading.
- State: Auto theme under a light system appearance, top of page for layout comparisons. Dark theme and lower-page anchor destinations additionally inspected live.

The in-app browser repeatedly timed out during capture, so visual verification used Chrome through the documented native computer-use API. DevTools responsive mode was restored and DevTools closed afterward.

## Required fidelity surfaces

- Typography: Source Serif 4 headings and Source Sans 3 text match the reference family, hierarchy, weight, and rhythm. Official Adobe WOFF2 files and OFL licenses are hosted locally. The reference's Google Fonts delivery is replaced with local files.
- Layout: 58rem page, 248px sidebar, 2.25rem column inset, thin rules, restrained section spacing, and 140px publication thumbnails match the source layout. Below 860px the profile centers above the content; below 520px publication entries stack.
- Colors: warm gray #f2f2f0 surface, #171717 text, #0f3d6b links, muted dividers, warm accent, and corresponding dark palette checked against the reference.
- Images: existing portrait, institution logos, and research images retained. Portrait uses the reference's 3:4 frame; research previews use contain instead of cover to retain complete diagrams. Animated previews load lazily.
- Copy: all 11 original research titles, author strings, venues, years, equal-contribution notation, two Highlight labels, and 22 nonempty research URLs preserved. Four originally empty links are omitted. Personal details and academic history remain the user's own.

## Findings and iteration history

1. [P2, fixed] A tall sidebar initially introduced an inner scrollbar at short desktop heights. After iterations with normal flow and a compact fixed profile, the final user-requested behavior is the reference's sticky sidebar with an unchanged portrait and no internal scrolling.
2. Inline links initially received persistent underlines. The requested refinement above changes biography links to the reference's hover/focus bottom border; talk and contact links retain persistent underlines.
3. Initial full-page mobile capture contained unloaded images near the bottom because of native lazy loading. Scrolled to the lower content, confirmed images load, and saved `homepage-mobile-final.png`; no missing local asset remained.

No actionable P0/P1/P2 findings remain.

## Functional and build checks

- Actual Jekyll build succeeded with configured feed, sitemap, gist, paginate, and redirect plugins. Existing GPS-Gaussian project page and about redirects still appear in the output.
- Independent content comparison verified all original research data and all nonempty URLs.
- Native browser tested Auto → Light → Dark → Auto, persistence across refresh, Publications anchor, Contact anchor on mobile, and Top navigation.
- Node VM checks exercised theme initialization, cycling, cross-tab changes, clearing preferences, unavailable localStorage, and absent controls.
- Local asset and anchor validation: all referenced files exist, all fragment targets resolve, no empty href or duplicate IDs.
- Console showed zero messages. Chrome's Issues drawer showed one unattributed CSP/eval warning on both the source and local pages; the new homepage contains no eval and the preview sends no CSP header. No broken site behavior was observed.
- `git diff --check` passed.

## Accepted differences and limits

- Background and the additional original sections naturally change vertical positions and mobile page length.
- Short Bio uses the requested reference hover style, while talk/contact links retain underlines. The desktop sidebar follows the reference's sticky positioning without an independent scrollbar or portrait shrinking; mobile content uses normal flow.
- External paper destinations were preserved, not exhaustively revalidated over the network.
- This change is local; no commit, push, or production deployment was performed.
