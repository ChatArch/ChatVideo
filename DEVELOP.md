# Development Guide

## CLI Rules

- Keep the public command surface aligned with the real Click registry; `chatvideo --tree` is the source of truth for docs, README snippets, and CLI tests.
- Do not add documentation-only commands such as `design` or placeholder video workflow commands.
- Add provider/profile runtime dependencies only when a real command needs them.

## Verification

```bash
PYTHONPATH=src python -m pytest -q
PYTHONPATH=src python -m chatvideo.cli --tree
python -m build
mkdocs build --strict
```
