# WeChat sidebar icon

- Input: `/Users/zsy/Downloads/wechat.png` (the gray checkerboard was embedded in the image).
- Output: `assets/icons/wechat.png`, with a transparent alpha channel.
- Method: built-in imagegen, background extraction. The original download is unchanged.
- Usage: CSS alpha mask in `.wechat-icon`, inheriting the sidebar text color for both themes.

## Final prompt

Use case: background-extraction. Edit target: the supplied /Users/zsy/Downloads/wechat.png. Produce a clean monochrome UI icon for a personal website sidebar. Preserve the exact black rounded-square WeChat mark, two speech-bubble shapes and four black eyes, with the same proportions and centered framing. Remove ALL baked-in gray/white checkerboard pixels: both outside the rounded square and inside the speech bubbles must become truly transparent alpha, not white or gray. Keep the black foreground opaque, use smooth clean edges. No new details, no text, no shadow, no glow, no checkerboard backdrop. Output a small square PNG with genuine alpha transparency, suitable for use as a CSS alpha mask.
