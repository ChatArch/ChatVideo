import click
from click.testing import CliRunner
from chatstyle import add_tree_option

from chatvideo import __version__
from chatvideo.cli import main


def test_help_mentions_full_and_brief_tree_options():
    result = CliRunner().invoke(main, ["--help"])

    assert result.exit_code == 0
    assert "--tree" in result.output
    assert "--tree-brief" in result.output


def test_version_option_reports_package_version():
    result = CliRunner().invoke(main, ["--version"])

    assert result.exit_code == 0
    assert f"chatvideo, version {__version__}" in result.output


def test_tree_reports_registered_root_only_surface():
    result = CliRunner().invoke(main, ["--tree"])

    assert result.exit_code == 0
    assert result.output == (
        "chatvideo\n"
        "├── --help  # Show this message and exit.\n"
        "├── --version  # Show the version and exit.\n"
        "├── --tree  # Print the registered CLI tree and exit.\n"
        "└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.\n"
    )
    assert result.output.splitlines().count("chatvideo") == 1


def test_tree_brief_reports_the_same_root_only_nodes():
    full = CliRunner().invoke(main, ["--tree"])
    brief = CliRunner().invoke(main, ["--tree-brief"])

    assert brief.exit_code == 0
    assert brief.output == full.output
    assert brief.output.splitlines().count("chatvideo") == 1


def test_tree_brief_omits_registered_command_signatures():
    @click.group(name="sample")
    @add_tree_option(renderer_options={"root_name": "sample"})
    def sample() -> None:
        """Sample commands."""

    @sample.command()
    @click.argument("source")
    def inspect(source: str) -> None:
        """Inspect a video input; read-only text output."""

    full = CliRunner().invoke(sample, ["--tree"])
    brief = CliRunner().invoke(sample, ["--tree-brief"])

    assert full.exit_code == brief.exit_code == 0
    assert "inspect <SOURCE>" in full.output
    assert "inspect  # Inspect a video input; read-only text output." in brief.output
    assert "<SOURCE>" not in brief.output


def test_help_does_not_expose_documentation_blueprints_as_tools():
    result = CliRunner().invoke(main, ["--help"])

    assert result.exit_code == 0
    assert "design" not in result.output
    assert "generate" not in result.output
    assert "--tree" in result.output
    assert "--tree-brief" in result.output


def test_design_is_not_a_cli_command():
    result = CliRunner().invoke(main, ["design"])

    assert result.exit_code != 0
    assert "No such command" in result.output
