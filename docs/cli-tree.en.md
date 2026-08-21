# ChatVideo CLI Tree

This page lists only command entries that are implemented today. ChatVideo uses the shared `chatstyle.add_tree_option()` to generate its tree from the real Click registry. Image-to-video, first/last-frame, review, and final-delivery flows live in the [workflow blueprint](workflow-blueprint.md), not in the CLI.

- `chatvideo --tree` includes parameter signatures for interface review.
- `chatvideo --tree-brief` keeps the same nodes and descriptions while omitting parameter signatures.

The current CLI is root-only and has no business-command parameters, so the full and brief views are identical.

## Full Command Tree

```text
chatvideo
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

## Brief Command Tree

```text
chatvideo
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

## Current Capabilities

<div class="grid cards" markdown>

-   **Help Entry**

    `chatvideo --help` shows the current command surface. There are no video-operation subcommands yet.

-   **Version Entry**

    `chatvideo --version` confirms the installed ChatVideo package version.

-   **Full CLI Tree**

    `chatvideo --tree` generates the registered command tree with parameter signatures.

-   **Brief CLI Tree**

    `chatvideo --tree-brief` generates the same nodes without business-command parameter signatures.

-   **No Design Command**

    Workflow blueprints are documentation, not tool behavior; therefore there is no `chatvideo design` command.

</div>

## Planned Boundaries { #planned-boundaries }

These capabilities are described only in the documentation blueprint; they are not runnable subcommands yet:

| Planned capability | Status | Notes |
| --- | --- | --- |
| `edit` | Planned | Future editing, concatenation, and transition operations for existing clips. |
| `generate text` | Planned | Future text-to-video provider jobs. |
| `generate image` | Planned | Future ordered-keyframe image-to-video jobs. |
| `generate frames` | Planned | Future adjacent first/last-frame segment generation. |
| `review` | Planned | Future temporary review artifact publishing. |
| `final` | Planned | Future final artifact verification and delivery. |

## Update Rules

- Only behavior that performs real video workflow work should enter the CLI.
- Markdown design notes stay in docs; do not wrap them as CLI commands.
- When a runnable command is added, let `chatvideo --tree` / `chatvideo --tree-brief` reflect the registered command surface first, then sync this page, tests, and deeper usage docs.
