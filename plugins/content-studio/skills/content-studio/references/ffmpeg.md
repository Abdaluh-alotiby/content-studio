# FFmpeg

Research checked: 2026-11-23. Verify installed versions before production.

Use explicit stream maps, output dimensions and codecs. Normalize clips before concatenating; stream-copy only compatible streams. For wide MP4 compatibility, use H.264/yuv420p with AAC when audio is needed, even pixel dimensions and faststart. Preserve transparency in a suitable intermediate instead of flattening it by accident. Use ffprobe JSON and full decoding for integrity checks. The bundled verify helper performs these checks without claiming perceptual quality. Inspect filters/encoders available in the actual build.

Starting command (run in the appropriate project/environment):

```sh
ffmpeg -version
```

Official sources: [FFmpeg](https://ffmpeg.org/ffmpeg.html) · [Details](https://ffmpeg.org/ffprobe.html)

