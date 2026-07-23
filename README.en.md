<div align="center">
    <a href="https://pypi.python.org/pypi/ChatVideo">
        <img src="https://img.shields.io/pypi/v/ChatVideo.svg" alt="PyPI version" />
    </a>
    <a href="https://github.com/ChatArch/ChatVideo/actions/workflows/ci.yml">
        <img src="https://github.com/ChatArch/ChatVideo/actions/workflows/ci.yml/badge.svg" alt="Tests" />
    </a>
</div>

<div align="center">

[English](README.en.md) | [Simplified Chinese](README.md)
</div>

# ChatVideo

ChatArch video tooling package.

## Quick Start

```bash
pip install -e ".[dev]"
chatvideo --help
chatvideo --version
python -m pytest -q
python -m build
python -m pip install -e ".[docs]"
mkdocs build --strict
```

Documentation site: <https://arch.gh.wzhecnu.cn/ChatVideo/>

## Workflow Blueprint In Docs

The package records a provider-neutral image-to-video workflow blueprint as documentation, not as a CLI feature. It avoids embedding concrete project media, internal paths, task ids, share URLs, or credentials in reusable docs. The current focus is not video chat and not only editing existing clips; it is an image-to-video model flow where ordered keyframes, especially a three-image storyboard, are split into adjacent first/last-frame segments and then assembled into one video. See `docs/workflow-blueprint.md` for the full design note.

These workflows are documentation blueprints, not implemented CLI commands:

- `edit`: concat, trim, transitions, and final assembly for existing clips.
- `generate text`: text-to-video submission, polling, download, and safe summaries.
- `generate image`: generate video from ordered keyframes; a typical three-image storyboard becomes adjacent first/last-frame segments.
- `generate frames`: generate one bounded segment, for example image 1 to image 2 and image 2 to image 3.
- `review` / `final`: separate temporary review from durable final delivery.

The current CLI keeps only real tool entry points: `chatvideo --help` and `chatvideo --version`. Add a command only after it performs actual video workflow work.

## CLI Contract

This template depends on `chatstyle>=0.1.0,<0.2.0` and `chatenv>=0.2.0,<0.3.0`. New commands should prefer:

- `CommandSchema` / `CommandField` for inputs.
- `add_interactive_option()` for the shared `-i/-I` switch.
- `resolve_command_inputs()` for missing args, defaults, TTY behavior, and validation.
- Generate `config.py` and a `chatenv.configs` entry point by default so the package is ChatEnv-discoverable; use `--without-chatenv-provider` only when ChatEnv integration is intentionally not needed.

## Layout

- `src/`: package source code
- `tests/code-tests/`: code tests and migrated historical tests
- `tests/cli-tests/`: real CLI tests, doc-first
- `tests/mock-cli-tests/`: mock/fake CLI tests, doc-first

## Development Notes

See `DEVELOP.md` and `AGENTS.md` before expanding the scaffold.
