# Remotion

Research checked: 2026-11-23. Verify installed versions before production.

Build React compositions with declared width, height, fps and frame duration. Derive state from `useCurrentFrame`, not wall-clock hooks. Use `assets/remotion-scene.tsx` as a component inside the official scaffold and register its composition. Render using `npx remotion render <entry> <composition-id> out.mp4`; supply props via a JSON file on Windows. Preload assets and fonts and check package-version consistency. Review current licensing for the intended deployment; do not assume all commercial use is unrestricted.

Starting command (run in the appropriate project/environment):

```sh
npx create-video@latest --yes --blank react-scene
```

Official sources: [Remotion](https://www.remotion.dev/docs/) · [Details](https://www.remotion.dev/docs/cli/render)

