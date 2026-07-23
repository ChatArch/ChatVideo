# ChatVideo Documentation

ChatVideo is ChatArch's video workflow CLI/API package. The current focus is turning practical image-to-video workflows into reusable command designs: ordered keyframes, especially a three-image storyboard, become adjacent first/last-frame segments that are reviewed, assembled, and delivered as one video.

Site entry: <https://arch.gh.wzhecnu.cn/ChatVideo/>

## Choose An Entry Point

<div class="grid cards" markdown>

-   **See Implemented Commands**

    Start with the implemented `chatvideo` command tree to confirm what can run today and what remains planned.

    [Open the CLI tree](cli-tree.md)

-   **Understand The Image-To-Video Model**

    Three ordered keyframes become adjacent first/last-frame segments and then one final video.

    [Open the design blueprint](cli-design.md#chatvideo-generate-image)

-   **Plan First/Last-Frame Segments**

    Use this when the provider accepts a first frame plus a last frame to generate one video segment.

    [Open the segment blueprint](cli-design.md#chatvideo-generate-frames)

-   **Separate Review From Final**

    Temporary review artifacts stay separate from durable final delivery and reusable docs.

    [Open the handoff boundary](cli-design.md#review-to-final)

</div>

## Reading Map

| Question | Page |
| --- | --- |
| What is actually implemented? | [CLI Tree](cli-tree.md) |
| How do three keyframes become one video? | [Design Blueprint](cli-design.md#chatvideo-generate-frames) |
| How is ordered image input recorded? | [Design Blueprint](cli-design.md#chatvideo-generate-image) |
| How are text-to-video and editing commands planned? | [Design Blueprint](cli-design.md) |
| Which commands are still planned? | [CLI Tree: Planned Boundaries](cli-tree.md#planned-boundaries) |

## Quick Commands

```bash
chatvideo --help
chatvideo --version
chatvideo design
chatvideo design --workflow image-to-video --format json
chatvideo design --workflow first-last-frame
```

`chatvideo design` prints the design blueprint. It does not submit provider jobs or publish files.
