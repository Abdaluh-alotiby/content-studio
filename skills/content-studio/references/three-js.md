# Three.js

Research checked: 2026-11-23. Verify installed versions before production.

Create a scene, camera, lights, materials and renderer. Set export dimensions and camera aspect explicitly. Derive transforms from absolute seconds and render exactly after updating them. Load assets before capture and keep the renderer package/addons versions aligned. Test WebGL availability in the actual export environment; GPU access is not guaranteed. Dispose geometries, textures and materials. The starter `assets/three-scene.mjs` exposes a deterministic render function to embed in a browser scene.

Starting command (run in the appropriate project/environment):

```sh
npm install --save-exact three
```

Official sources: [Three.js](https://github.com/mrdoob/three.js) · [Details](https://threejs.org/manual/)

