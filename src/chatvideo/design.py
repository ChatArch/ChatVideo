"""Provider-neutral CLI design blueprints for ChatVideo."""

from __future__ import annotations

from dataclasses import asdict, dataclass
import json


@dataclass(frozen=True)
class CommandBlueprint:
    """A proposed user-facing command and what it should own."""

    command: str
    purpose: str


@dataclass(frozen=True)
class WorkflowBlueprint:
    """A privacy-safe workflow slice for future ChatVideo CLI work."""

    key: str
    title: str
    purpose: str
    commands: tuple[CommandBlueprint, ...]
    privacy: tuple[str, ...]


PRIVACY_BASELINE = (
    "Keep provider credentials in environment profiles; never write secrets to manifests.",
    "Keep raw inputs local by default; publish only explicit review or final artifacts.",
    "Write shareable reports with generic metadata and redact task ids, URLs, and paths when requested.",
)

BLUEPRINTS = (
    WorkflowBlueprint(
        key="editing",
        title="Editing and Assembly",
        purpose="Turn existing clips into review cuts and final deliverables.",
        commands=(
            CommandBlueprint(
                "chatvideo edit concat --manifest timeline.json --output draft.mp4",
                "Concatenate clips from a timeline manifest with optional stream copy.",
            ),
            CommandBlueprint(
                "chatvideo edit trim --input clip.mp4 --start 00:00:02 --end 00:00:10",
                "Create exact review slices without changing source assets.",
            ),
            CommandBlueprint(
                "chatvideo edit transition --manifest timeline.json --style cut|xfade",
                "Apply explicit transitions while preserving an auditable timeline.",
            ),
        ),
        privacy=PRIVACY_BASELINE,
    ),
    WorkflowBlueprint(
        key="text-to-video",
        title="Text to Video",
        purpose="Submit provider-backed text prompts and track review outputs.",
        commands=(
            CommandBlueprint(
                "chatvideo generate text --prompt prompt.md --duration 10 --review-dir review/",
                "Generate a draft clip from a text prompt file.",
            ),
            CommandBlueprint(
                "chatvideo job poll --manifest runs/latest.json --download review/",
                "Poll provider jobs and download review artifacts into the project workspace.",
            ),
            CommandBlueprint(
                "chatvideo report summarize --manifest runs/latest.json --redact",
                "Create a safe, shareable generation summary.",
            ),
        ),
        privacy=PRIVACY_BASELINE
        + (
            "Prompt files stay in the workspace unless the user explicitly shares a review package.",
        ),
    ),
    WorkflowBlueprint(
        key="image-to-video",
        title="Image to Video",
        purpose="Generate video from ordered keyframe images, especially a three-image story that is split into first/last-frame segments.",
        commands=(
            CommandBlueprint(
                "chatvideo storyboard order --images frame-01.png frame-02.png frame-03.png --output storyboard.json",
                "Record the reviewed three-keyframe order before generation.",
            ),
            CommandBlueprint(
                "chatvideo generate image --keyframes storyboard.json --mode first-last-frame --review-dir review/",
                "Use an image-to-video provider through adjacent first/last-frame segment jobs.",
            ),
            CommandBlueprint(
                "chatvideo workflow run --storyboard storyboard.json --one-segment-at-a-time",
                "Generate longer videos as reviewable segments instead of one opaque run.",
            ),
        ),
        privacy=PRIVACY_BASELINE
        + (
            "Do not copy source images to public storage just to satisfy provider inputs.",
            "Treat the three keyframe images as private source inputs until the user approves a review or final artifact.",
        ),
    ),
    WorkflowBlueprint(
        key="first-last-frame",
        title="First and Last Frame",
        purpose="Turn adjacent keyframe pairs into bounded image-to-video segments.",
        commands=(
            CommandBlueprint(
                "chatvideo generate frames --first frame-01.png --last frame-02.png --duration 5 --review-dir review/segment-01",
                "Create the first bounded segment from the first and middle keyframes.",
            ),
            CommandBlueprint(
                "chatvideo generate frames --first frame-02.png --last frame-03.png --duration 5 --review-dir review/segment-02",
                "Create the second bounded segment from the middle and final keyframes.",
            ),
            CommandBlueprint(
                "chatvideo edit concat --manifest generated-segments.json --output final.mp4",
                "Assemble approved first/last-frame segments into one final video.",
            ),
        ),
        privacy=PRIVACY_BASELINE
        + (
            "Endpoint/keyframe images are treated as private inputs; only approved clips become shareable.",
            "A three-image input becomes adjacent segment jobs instead of a public three-image prompt bundle.",
        ),
    ),
    WorkflowBlueprint(
        key="review-to-final",
        title="Review to Final",
        purpose="Keep temporary review sharing separate from durable final export.",
        commands=(
            CommandBlueprint(
                "chatvideo review publish --artifact draft.mp4 --target local-share",
                "Publish temporary review artifacts with short metadata.",
            ),
            CommandBlueprint(
                "chatvideo final export --artifact final.mp4 --target archive",
                "Copy only approved deliverables to durable storage.",
            ),
            CommandBlueprint(
                "chatvideo final verify --url-or-path final.mp4",
                "Verify duration, streams, size, and reachability before handoff.",
            ),
        ),
        privacy=PRIVACY_BASELINE
        + (
            "Review links are operational details and should not be stored in reusable templates.",
        ),
    ),
)


def workflow_keys() -> tuple[str, ...]:
    """Return valid workflow keys for CLI choices."""

    return tuple(blueprint.key for blueprint in BLUEPRINTS)


def select_blueprints(workflow: str = "all") -> tuple[WorkflowBlueprint, ...]:
    """Select all blueprints or a single workflow by key."""

    if workflow == "all":
        return BLUEPRINTS
    return tuple(blueprint for blueprint in BLUEPRINTS if blueprint.key == workflow)


def render_text(blueprints: tuple[WorkflowBlueprint, ...]) -> str:
    """Render blueprints as deterministic CLI-friendly text."""

    lines = ["ChatVideo CLI design", ""]
    for blueprint in blueprints:
        lines.append(f"[{blueprint.key}] {blueprint.title}")
        lines.append(f"Purpose: {blueprint.purpose}")
        lines.append("Commands:")
        for command in blueprint.commands:
            lines.append(f"  - {command.command}")
            lines.append(f"    {command.purpose}")
        lines.append("Privacy:")
        for rule in blueprint.privacy:
            lines.append(f"  - {rule}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_json(blueprints: tuple[WorkflowBlueprint, ...]) -> str:
    """Render blueprints as stable JSON for doc-first CLI tests."""

    payload = [asdict(blueprint) for blueprint in blueprints]
    return json.dumps(payload, indent=2, sort_keys=True) + "\n"
