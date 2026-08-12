from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_publish_workflow_is_tag_only_and_main_guarded():
    workflow = (ROOT / ".github" / "workflows" / "publish.yml").read_text(encoding="utf-8")

    assert "workflow" + "_dispatch:" not in workflow
    assert "id-token: write" in workflow
    assert "pypa/gh-action-pypi-publish@release/v1" in workflow
    assert "git fetch --no-tags origin main:refs/remotes/origin/main" in workflow
    assert "git merge-base --is-ancestor" in workflow
    assert "secrets" + ".PYPI" not in workflow
    assert "TWINE" + "_PASSWORD" not in workflow


def test_preview_workflow_reads_site_url_from_mkdocs():
    workflow = (ROOT / ".github" / "workflows" / "preview.yaml").read_text(encoding="utf-8")

    assert "git fetch origin gh-pages --depth=1 || true" in workflow
    assert "mike deploy dev --push --update-aliases --allow-empty" in workflow
    assert "Path(\"mkdocs.yml\")" in workflow
    assert "CHATARCH_PREVIEW_URL" in workflow
    assert "github" + ".io" not in workflow


def test_mkdocs_material_emoji_renderer_is_configured():
    mkdocs = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")

    assert "site_url: https://arch.gh.wzhecnu.cn/ChatVideo/" in mkdocs
    assert "pymdownx.emoji:" in mkdocs
    assert "material.extensions.emoji.twemoji" in mkdocs
    assert "material.extensions.emoji.to_svg" in mkdocs
