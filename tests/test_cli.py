from click.testing import CliRunner

from chatvideo import __version__
from chatvideo.cli import main


def test_version_option_reports_package_version():
    result = CliRunner().invoke(main, ["--version"])

    assert result.exit_code == 0
    assert f"chatvideo, version {__version__}" in result.output


def test_help_does_not_expose_documentation_blueprints_as_tools():
    result = CliRunner().invoke(main, ["--help"])

    assert result.exit_code == 0
    assert "design" not in result.output
    assert "generate" not in result.output


def test_design_is_not_a_cli_command():
    result = CliRunner().invoke(main, ["design"])

    assert result.exit_code != 0
    assert "No such command" in result.output
