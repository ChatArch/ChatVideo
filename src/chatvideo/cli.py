"""CLI entrypoint for chatvideo."""

import click

from chatvideo import __version__


@click.group()
@click.version_option(__version__, prog_name="chatvideo")
def main() -> None:
    """ChatVideo command line interface."""
    # Real tool commands belong here after they operate on video workflows.


if __name__ == "__main__":
    main()
