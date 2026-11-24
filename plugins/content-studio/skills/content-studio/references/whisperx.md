# WhisperX

Research checked: 2026-11-23. Verify installed versions before production.

Use an isolated environment and the project's current installation instructions. Validate PyTorch/CUDA compatibility and memory budget before model downloads. Transcribe real speech, align when the language has a suitable alignment model, and keep segment/word JSON. Diarization has additional model-access requirements; never embed a Hugging Face token. CPU/int8 is a possible fallback when supported by the installed version. Inspect names, Arabic words and timestamps manually. Process final edited audio or remap edits. Convert segment JSON using the bundled captions command.

Starting command (run in the appropriate project/environment):

```sh
whisperx --help
```

Official sources: [WhisperX](https://github.com/m-bain/whisperX) · [Details](https://github.com/m-bain/whisperX#usage-command-line)

