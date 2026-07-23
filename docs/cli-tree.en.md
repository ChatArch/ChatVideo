# ChatVideo CLI Tree

This page lists only command entries that are implemented today. Planned generation, review, and final-delivery commands live in the [design blueprint](cli-design.md) and are not presented here as runnable interfaces.

## Current Command Topology

```text
chatvideo
|-- --help                         # Show top-level help
|-- --version                      # Print the installed package version
`-- design                         # Print provider-neutral video workflow blueprints
    |-- --workflow all             # Default: print every blueprint
    |-- --workflow editing         # Planned: edit and assemble existing clips
    |-- --workflow text-to-video   # Planned: text-to-video jobs
    |-- --workflow image-to-video  # Planned: ordered keyframes to video
    |-- --workflow first-last-frame # Planned: adjacent first/last-frame segments
    |-- --workflow review-to-final # Planned: review-to-final handoff
    |-- --format text              # Default text output
    `-- --format json              # Machine-readable JSON output
```

## Current Capabilities

<div class="grid cards" markdown>

-   **Version And Help**

    `chatvideo --version` and `chatvideo --help` are stable entry points for installation checks and command discovery.

-   **Design Blueprint Output**

    `chatvideo design` prints planned workflow slices so the command shape can be reviewed before provider adapters are implemented.

-   **Workflow Filtering**

    `--workflow` focuses the output on one slice, such as `image-to-video` or `first-last-frame`.

-   **Machine-Readable Output**

    `--format json` supports tests, documentation generation, and future tool integration.

</div>

## Planned Boundaries { #planned-boundaries }

These command names appear in the design blueprint, but they are not runnable subcommands yet:

| Planned command group | Status | Notes |
| --- | --- | --- |
| `chatvideo edit ...` | Planned | Future editing, concatenation, and transition operations for existing clips. |
| `chatvideo generate text ...` | Planned | Future text-to-video provider jobs. |
| `chatvideo generate image ...` | Planned | Future ordered-keyframe image-to-video jobs. |
| `chatvideo generate frames ...` | Planned | Future adjacent first/last-frame segment generation. |
| `chatvideo review ...` | Planned | Future temporary review artifact publishing. |
| `chatvideo final ...` | Planned | Future final artifact verification and delivery. |

## Update Rules

- When a runnable command is added, update this tree before adding deeper docs links.
- Put only implemented commands in the current topology.
- Planned commands must keep explicit status notes so readers do not assume provider execution exists.
