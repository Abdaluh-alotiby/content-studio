# Rough.js

Research checked: 2026-11-23. Verify installed versions before production.

Generate sketch-like Canvas or SVG shapes, paths and fill patterns. Use a fixed seed per shape, generate once, and animate stable geometry through the scene clock. Recreating random rough strokes every frame causes flicker. Use SVG when editable paths are helpful; use Canvas when batch drawing is simpler. Test line weights and hatching after downsampling. It draws graphics; another engine captures and encodes video.

Starting command (run in the appropriate project/environment):

```sh
npm install --save-exact roughjs
```

Official sources: [Rough.js](https://roughjs.com/) · [Details](https://github.com/rough-stuff/rough/wiki)

