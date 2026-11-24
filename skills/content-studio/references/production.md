# Production rules

## Story and design

Use one message per scene. Introduce the question or result early and make movement serve the explanation. Hold text long enough to read. Use supplied product screenshots; never label invented screens authentic. Choose a purposeful palette, clear type hierarchy and consistent margins. Adapt layout to each aspect ratio. Record target-platform safe areas instead of assuming universal overlays.

## Reproducible time

Plan in integer frames; convert to seconds only at API boundaries. A scene in `[start,end)` contains `end-start` frames. Drive visuals from absolute time rather than accumulated delta time, timers or render order. Seed randomness and test backward seeks. Preload fonts, media and models. Disable interaction-dependent export state. Save dependencies, lockfiles, versions and exact render commands.

## Arabic and mixed language

Use UTF-8 and fonts with confirmed Arabic shaping. Set direction/language per container; isolate code and English with LTR spans or `bdi`. Never reverse Arabic strings. Inspect joining, punctuation, numbers, diacritics and wrapping in exported frames. Animate words or text blocks when character animation breaks shaping. Keep captions in semantic order and let the renderer handle bidi. Disclose unreviewed narration pronunciation.

## Audio and editing

Decide whether sound is wanted. Use supplied narration or an authorized voice-generation tool; these 12 libraries do not provide a general TTS service. Preserve originals. Complete cuts before alignment, or maintain a source-to-output time map. Keep breaths and review word boundaries. Mix speech above music, avoid clipping, and measure loudness against the requested destination. Never reuse original timestamps after cuts without remapping.

## Delivery

Keep `brief.md`, `storyboard.md`, `plan.json`, `sources.md`, `assets/credits.json`, `src/`, `out/` and `qa/`. Record exact reproduction commands. Supply actual media separately from source. Include relevant social copy and thumbnail direction without exaggeration. Record limitations instead of claiming unavailable inspections.

