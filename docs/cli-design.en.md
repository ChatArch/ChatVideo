# ChatVideo CLI Design Blueprint

This document records the first provider-neutral CLI shape for ChatVideo. It is based on practical video workflows, but it intentionally avoids private project media, internal paths, task ids, service URLs, account names, provider request payloads, and credentials.

## Design Goals

- Prioritize the current image-to-video need: ordered keyframe images, especially a three-image storyboard, produce one video through adjacent first/last-frame segments.
- Cover editing, text-to-video, image-to-video, first/last-frame generation, review publishing, and final export.
- Keep review artifacts separate from durable final deliverables.
- Make every generated clip traceable through local manifests without storing secrets.
- Support one-segment-at-a-time review for expensive or uncertain generation jobs.
- Leave provider details behind ChatEnv-style environment profiles and future adapters.

## Current User Model

This is not a video-chat product, and it is not only an editing wrapper for existing clips. The current target is an image-to-video model flow: the user provides ordered images, and the provider generates video under those image constraints.

A typical three-image storyboard looks like this:

```text
frame-01.png  ->  frame-02.png  ->  frame-03.png
```

If the provider accepts first and last frames for one generated segment, ChatVideo should split the three images into adjacent segment jobs:

```text
segment-01: frame-01.png -> frame-02.png
segment-02: frame-02.png -> frame-03.png
final.mp4:  segment-01 + segment-02
```

Therefore, the `generate image` and `generate frames` commands documented here are design blueprints. They describe how a future CLI should accept keyframes, record order, review segments, and assemble the final video. The current executable interface is `chatvideo design`, which prints and filters these blueprints.

## Proposed Command Groups

### chatvideo edit

Owns deterministic media operations on existing clips.

```bash
chatvideo edit concat --manifest timeline.json --output draft.mp4
chatvideo edit trim --input clip.mp4 --start 00:00:02 --end 00:00:10
chatvideo edit transition --manifest timeline.json --style cut|xfade
```

Expected behavior:

- Accepts explicit manifests or file arguments.
- Preserves source media and writes new artifacts.
- Uses stream copy when safe, then falls back to re-encoding only when necessary.
- Records duration, codec, audio presence, size, and artifact role.

### chatvideo generate text

Owns provider-backed text-to-video jobs.

```bash
chatvideo generate text --prompt prompt.md --duration 10 --review-dir review/
chatvideo job poll --manifest runs/latest.json --download review/
chatvideo report summarize --manifest runs/latest.json --redact
```

Expected behavior:

- Reads prompts from files instead of shell history when possible.
- Writes job manifests with provider names, safe status fields, and artifact metadata only.
- Keeps secrets in environment profiles and reports only whether credentials are configured.

### chatvideo generate image

Owns image-to-video planning from ordered keyframes. The typical input is not one isolated picture and not a public sample bundle; it is a user-reviewed ordered keyframe set.

```bash
chatvideo storyboard order --images frame-01.png frame-02.png frame-03.png --output storyboard.json
chatvideo generate image --keyframes storyboard.json --mode first-last-frame --review-dir review/
chatvideo workflow run --storyboard storyboard.json --one-segment-at-a-time
```

Expected behavior:

- Captures the reviewed image order before generation.
- Sends a three-keyframe story into first/last-frame segment planning instead of one opaque multi-image prompt.
- Keeps raw images local by default.
- Produces review clips before final export.

### chatvideo generate frames

Owns the adjacent-keyframe jobs sent to a provider that supports first/last-frame constrained video generation.

```bash
chatvideo generate frames --first frame-01.png --last frame-02.png --duration 5 --review-dir review/segment-01
chatvideo generate frames --first frame-02.png --last frame-03.png --duration 5 --review-dir review/segment-02
chatvideo edit concat --manifest generated-segments.json --output final.mp4
```

Expected behavior:

- Treats every keyframe image as a private input.
- For one video from three images, defaults to two adjacent first/last-frame jobs.
- Reviews each segment and assembles only approved segments into the final video.

### chatvideo review and chatvideo final { #review-to-final }

Own the handoff boundary between temporary review and durable output.

```bash
chatvideo review publish --artifact draft.mp4 --target local-share
chatvideo final verify --url-or-path final.mp4
chatvideo final export --artifact final.mp4 --target archive
```

Expected behavior:

- Review links are temporary operational details.
- Final export copies only approved deliverables to durable storage.
- Verification checks duration, streams, size, and reachability when a URL is provided.

## Privacy Baseline

- Keep provider credentials in environment profiles; never write secrets to manifests.
- Keep raw inputs local by default; publish only explicit review or final artifacts.
- Redact task ids, URLs, paths, and provider-specific request payloads from shareable reports when requested.
- Avoid embedding user-specific source descriptions in reusable templates.
- Prefer generic metadata such as duration, resolution, codec, audio presence, and artifact role.

## Current Capability And Planned Boundaries

<div class="grid cards" markdown>

-   **Implemented**

    `chatvideo design` can print all workflow blueprints or one selected blueprint in text or JSON format.

-   **Planned**

    The `edit`, `generate`, `review`, and `final` command groups describe target interfaces and safety boundaries; they are not provider execution entry points yet.

-   **Safe Defaults**

    Raw images and provider credentials stay in the local environment by default; reusable docs record only generic workflows and metadata.

</div>
