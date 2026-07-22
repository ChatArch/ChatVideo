import json

from click.testing import CliRunner

from chatvideo import __version__
from chatvideo.cli import main


DISALLOWED_SHAREABLE_SNIPPETS = (
    "http://",
    "https://",
    "Authorization",
    "api_key",
    "/home/",
    "/Users/",
)


def test_version_option_reports_package_version():
    result = CliRunner().invoke(main, ["--version"])

    assert result.exit_code == 0
    assert f"chatvideo, version {__version__}" in result.output


def test_design_outputs_provider_neutral_workflows():
    result = CliRunner().invoke(main, ["design"])

    assert result.exit_code == 0
    assert "ChatVideo CLI design" in result.output
    assert "text-to-video" in result.output
    assert "image-to-video" in result.output
    assert "first-last-frame" in result.output
    assert "three-image story" in result.output
    assert "review-to-final" in result.output
    assert "never write secrets" in result.output
    assert all(snippet not in result.output for snippet in DISALLOWED_SHAREABLE_SNIPPETS)


def test_design_can_filter_workflow_as_json():
    result = CliRunner().invoke(
        main,
        ["design", "--workflow", "image-to-video", "--format", "json"],
    )

    assert result.exit_code == 0
    payload = json.loads(result.output)
    assert [workflow["key"] for workflow in payload] == ["image-to-video"]
    assert payload[0]["commands"][0]["command"].startswith("chatvideo storyboard order")
    assert "frame-01.png" in payload[0]["commands"][0]["command"]
    assert "first-last-frame" in payload[0]["commands"][1]["command"]
    assert any("source images" in rule for rule in payload[0]["privacy"])
    assert any("three keyframe images" in rule for rule in payload[0]["privacy"])
