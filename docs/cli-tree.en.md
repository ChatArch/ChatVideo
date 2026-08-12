# ChatVideo CLI Tree

This page lists only command entries that are implemented today. ChatVideo does not have real video-operation subcommands yet; image-to-video, first/last-frame, review, and final-delivery flows live in the [workflow blueprint](workflow-blueprint.md), not in the CLI.

## Current Command Topology

```text
chatvideo  # ChatVideo command line interface.
├── --help  # Show CLI help and registered options.
├── --version  # Print the current package version.
└── --tree  # Print the registered CLI tree.
```

## Current Capabilities

<div class="grid cards" markdown>

-   **Help Entry**

    `chatvideo --help` shows the current command surface. There are no video-operation subcommands yet.

-   **Version Entry**

    `chatvideo --version` confirms the installed ChatVideo package version.

-   **CLI Tree Entry**

    `chatvideo --tree` is generated from the real Click registry.

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
- When a runnable command is added, let `chatvideo --tree` reflect the registered command surface first, then sync this page, tests, and deeper usage docs.
