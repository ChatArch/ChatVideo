# ChatVideo CLI Design Blueprint

This document records the first provider-neutral CLI shape for ChatVideo. It is based on practical video workflows, but it intentionally avoids private project media, internal paths, task ids, service URLs, account names, provider request payloads, and credentials.

## Design Goals

- Cover editing, text-to-video, image-to-video, first/last-frame generation, review publishing, and final export.
- Keep review artifacts separate from durable final deliverables.
- Make every generated clip traceable through local manifests without storing secrets.
- Support one-segment-at-a-time review for expensive or uncertain generation jobs.
- Leave provider details behind ChatEnv-style environment profiles and future adapters.

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

Owns image-to-video jobs with one or more ordered reference images.

```bash
chatvideo storyboard order --images inputs/ --output storyboard.json
chatvideo generate image --images inputs/ --duration 10 --review-dir review/
chatvideo workflow run --storyboard storyboard.json --one-segment-at-a-time
```

Expected behavior:

- Captures the reviewed image order before generation.
- Keeps raw images local by default.
- Produces review clips before final export.

### chatvideo generate frames

Owns first/last-frame generation for a single bounded segment.

```bash
chatvideo generate frames --first start.png --last end.png --duration 10
chatvideo workflow split --frames ordered/ --duration-per-segment 10
chatvideo edit concat --manifest generated-segments.json --output final.mp4
```

Expected behavior:

- Treats endpoint frames as private inputs.
- Splits multi-frame stories into adjacent first/last-frame jobs.
- Assembles only approved segments into a final cut.

### chatvideo review and chatvideo final

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

## Current PR Scope

This PR adds the `chatvideo design` command and documentation site structure only. It does not implement provider adapters, submit network jobs, or publish files. Future PRs can implement each command group behind the documented privacy contract.
