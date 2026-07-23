# ChatVideo Documentation

ChatVideo is ChatArch's video workflow CLI/API package. The current focus is turning practical image-to-video workflows into reusable command designs: ordered keyframes, especially a three-image storyboard, become adjacent first/last-frame segments that are reviewed, assembled, and delivered as one video.

Site entry: <https://arch.gh.wzhecnu.cn/ChatVideo/>

## Choose An Entry Point

<div class="grid cards" markdown>

-   **See Implemented Commands**

    Start with the implemented `chatvideo` command tree to confirm that the CLI currently keeps only real tool entry points.

    [Open the CLI tree](cli-tree.md)

-   **Understand The Image-To-Video Model**

    Three ordered keyframes become adjacent first/last-frame segments and then one final video.

    [Open the workflow blueprint](workflow-blueprint.md#chatvideo-generate-image)

-   **Plan First/Last-Frame Segments**

    Use this when the provider accepts a first frame plus a last frame to generate one video segment.

    [Open the segment blueprint](workflow-blueprint.md#chatvideo-generate-frames)

-   **Separate Review From Final**

    Temporary review artifacts stay separate from durable final delivery and reusable docs.

    [Open the handoff boundary](workflow-blueprint.md#review-to-final)

</div>

## Reading Map

| Question | Page |
| --- | --- |
| What is actually implemented? | [CLI Tree](cli-tree.md) |
| How do three keyframes become one video? | [Workflow Blueprint](workflow-blueprint.md#chatvideo-generate-frames) |
| How is ordered image input recorded? | [Workflow Blueprint](workflow-blueprint.md#chatvideo-generate-image) |
| How are text-to-video and editing capabilities planned? | [Workflow Blueprint](workflow-blueprint.md) |
| Which capabilities are still planned? | [CLI Tree: Planned Boundaries](cli-tree.md#planned-boundaries) |

## Quick Commands

```bash
chatvideo --help
chatvideo --version
```

The current CLI keeps only real tool entry points. Workflow planning belongs in the [workflow blueprint](workflow-blueprint.md), not in a `chatvideo` subcommand.
