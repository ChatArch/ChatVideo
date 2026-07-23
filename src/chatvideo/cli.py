"""CLI entrypoint for chatvideo."""

import click

from chatvideo import __version__
from chatvideo.design import render_json, render_text, select_blueprints, workflow_keys


@click.group()
@click.version_option(__version__, prog_name="chatvideo")
def main() -> None:
    """ChatVideo command line interface."""
    # Add package-specific commands here. Prefer ChatStyle helpers for
    # interactive input when a command needs recoverable user input.


@main.command()
@click.option(
    "--workflow",
    type=click.Choice(("all",) + workflow_keys()),
    default="all",
    show_default=True,
    help="Limit the design output to one workflow slice.",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(("text", "json")),
    default="text",
    show_default=True,
    help="Output format for the CLI blueprint.",
)
def design(workflow: str, output_format: str) -> None:
    """Print the provider-neutral ChatVideo CLI design."""

    blueprints = select_blueprints(workflow)
    output = render_json(blueprints) if output_format == "json" else render_text(blueprints)
    click.echo(output, nl=False)


if __name__ == "__main__":
    main()
