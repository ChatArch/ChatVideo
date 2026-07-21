# ChatVideo Documentation

ChatVideo is ChatArch's video workflow CLI/API package. The current focus is turning practical video workflows into reusable command designs: local editing, text-to-video, image-to-video, first/last-frame segment generation, review publishing, and final delivery.

Site entry: <https://arch.gh.wzhecnu.cn/ChatVideo/>

## Choose A Document

| Scenario | Document |
| --- | --- |
| Understand the current CLI direction | [CLI Design Blueprint](cli-design.md) |
| Plan concat, trim, and transitions for existing clips | [CLI Design Blueprint](cli-design.md#chatvideo-edit) |
| Plan text-to-video submission and download | [CLI Design Blueprint](cli-design.md#chatvideo-generate-text) |
| Plan image-to-video from ordered images | [CLI Design Blueprint](cli-design.md#chatvideo-generate-image) |
| Plan first/last-frame segment generation | [CLI Design Blueprint](cli-design.md#chatvideo-generate-frames) |
| Separate temporary review from final delivery | [CLI Design Blueprint](cli-design.md#chatvideo-review-and-chatvideo-final) |

## Site Structure

The docs stay intentionally small for now:

- **CLI / Workflows**: provider-neutral command blueprints and privacy boundaries.

Future implementation PRs can add usage guides, provider adapters, manifest schemas, and review/final publishing chapters.

## CLI

```bash
chatvideo --help
chatvideo --version
chatvideo design
chatvideo design --workflow image-to-video --format json
```

The current `chatvideo design` command prints the design blueprint only. It does not submit provider jobs or publish files.
