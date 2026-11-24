# mo.js

Research checked: 2026-11-23. Verify installed versions before production.

Use client-side Shape, ShapeSwirl and Burst for purposeful accents. Run inside a browser, not during server-side rendering. Inspect the installed API for explicit progress control; use `setProgress` where supported. Disable autonomous playback during capture and normalize scene time to 0–1. Test forward and backward sampling. If a feature cannot seek deterministically, isolate and prerender it rather than allowing wall-clock drift. Keep effects subordinate to readable content.

Starting command (run in the appropriate project/environment):

```sh
npm install --save-exact @mojs/core
```

Official sources: [mo.js](https://mojs.github.io/tutorials/getting-started.html) · [Details](https://github.com/mojs/mojs)

