# ChatVideo Workflow Blueprint

This document records ChatVideo's image-to-video workflow planning. It is documentation, not a current CLI feature; capability names describe future tool boundaries and do not mean matching `chatvideo` subcommands exist today.

## Design Goals

- Prioritize the current image-to-video need: ordered keyframe images, especially a three-image storyboard, produce one video through adjacent first/last-frame segments.
- Separate existing-video editing, text-to-video, image-to-video, first/last-frame generation, review publishing, and final delivery.
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

This page is a design note for future tool behavior. The current executable CLI only exposes `chatvideo --help`, `chatvideo --version`, and `chatvideo --tree`.

## Planned Capabilities

<div class="grid cards" markdown>

-   **Existing-Video Editing**

    Concatenate, trim, transition, and assemble already-local media files while preserving source assets.

-   **Text-To-Video**

    Submit provider-backed text-to-video jobs. Prompts should come from files when possible, not shell history.

-   **Image-To-Video**

    Work from ordered keyframes. The typical input is not one isolated picture and not a public sample bundle; it is a user-reviewed ordered keyframe set.

-   **First/Last-Frame Segments**

    Use providers that accept a first frame plus a last frame for one generated segment. One video from three images becomes two adjacent segment jobs.

-   **Review And Final**

    Review artifacts are temporary operational details; final artifacts are confirmed deliverables copied to durable locations.

</div>

## Image-To-Video { #chatvideo-generate-image }

Image-to-video capability should record image order before any provider task. A three-keyframe story enters first/last-frame segment planning instead of one opaque multi-image prompt.

Expected behavior:

- Captures the reviewed image order before generation.
- Keeps raw images local by default.
- Produces review clips before final export.
- Does not copy source images to public storage just to satisfy provider inputs.

## First/Last-Frame Segments { #chatvideo-generate-frames }

First/last-frame capability owns the adjacent-keyframe jobs sent to a provider that supports bounded video generation.

Expected behavior:

- Treats every keyframe image as a private input.
- For one video from three images, defaults to two adjacent first/last-frame jobs.
- Reviews each segment and assembles only approved segments into the final video.

## Review And Final { #review-to-final }

The review/final boundary should be explicit: review links can be temporary, while final artifacts must be durable user-approved outputs.

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

    The current CLI exposes only help, version, and generated tree entry points.

-   **Planned**

    Editing, generation, review, and final-delivery video operations are documentation blueprints only.

-   **Safe Defaults**

    Raw images and provider credentials stay in the local environment by default; reusable docs record only generic workflows and metadata.

</div>
