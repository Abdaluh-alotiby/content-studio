# Manim Community

Research checked: 2026-11-23. Verify installed versions before production.

Install Manim Community in an isolated Python environment following its platform instructions; do not confuse it with ManimGL. Use Scene, geometry, text, transforms and animation composition. Use `assets/manim-scene.py` as a small starting scene. Render at low quality first, then set the delivery resolution and fps. MathTex requires a working LaTeX toolchain; ordinary Text can avoid that dependency when appropriate. Verify mathematical claims separately from animation success.

Starting command (run in the appropriate project/environment):

```sh
python -m manim -ql scene.py ContentScene
```

Official sources: [Manim Community](https://docs.manim.community/en/stable/installation.html) · [Details](https://docs.manim.community/en/stable/tutorials/quickstart.html)

