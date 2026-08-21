# Development Guide

## CLI Rules

- Keep the public command surface aligned with the real Click registry; `chatvideo --tree` and `chatvideo --tree-brief` are the source of truth for docs, README snippets, and CLI tests.
- Use the shared ChatStyle `add_tree_option()` runtime; do not add a package-local tree renderer.
- Keep the root command explicitly named `chatvideo`.
- Do not add documentation-only commands such as `design` or placeholder video workflow commands.
- Add ChatEnv typed provider/profile behavior only when a real command needs it, and then use ChatEnv-managed storage paths.

## Verification

```bash
PYTHONPATH=src python -m pytest -q
PYTHONPATH=src python -m chatvideo.cli --version
PYTHONPATH=src python -m chatvideo.cli --tree
PYTHONPATH=src python -m chatvideo.cli --tree-brief
python -m build
python -m twine check dist/*
mkdocs build --strict
```
