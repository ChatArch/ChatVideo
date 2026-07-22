# ChatVideo Documentation

ChatVideo is ChatArch's video workflow CLI/API package. The current focus is turning practical image-to-video workflows into reusable command designs: ordered keyframes, especially a three-image storyboard, become adjacent first/last-frame segments that are reviewed, assembled, and delivered as one video.

Site entry: <https://arch.gh.wzhecnu.cn/ChatVideo/>

## Choose A Document

| Scenario | Document |
| --- | --- |
| Understand the current CLI direction | [CLI Design Blueprint](cli-design.md) |
| Plan concat, trim, and transitions for existing clips | [CLI Design Blueprint](cli-design.md#chatvideo-edit) |
| Plan text-to-video submission and download | [CLI Design Blueprint](cli-design.md#chatvideo-generate-text) |
| Plan the image-to-video model input shape | [CLI Design Blueprint](cli-design.md#current-user-model) |
| Plan one video from three keyframe images | [CLI Design Blueprint](cli-design.md#chatvideo-generate-frames) |
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
