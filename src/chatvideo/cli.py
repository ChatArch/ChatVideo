"""CLI entrypoint for chatvideo."""

from __future__ import annotations

import click
from chatstyle import add_tree_option

from chatvideo import __version__


@click.group(name="chatvideo", invoke_without_command=True)
@click.version_option(__version__, prog_name="chatvideo")
@add_tree_option(renderer_options={"root_name": "chatvideo"})
def main() -> None:
    """ChatVideo command line interface."""
    # Real tool commands belong here after they operate on video workflows.
    pass


if __name__ == "__main__":
    main()
