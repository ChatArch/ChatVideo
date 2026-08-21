# ChatVideo

[英文版](README.en.md) | [简体中文](README.md)

ChatArch 视频工作流工具包。

## 快速开始

```bash
pip install -e ".[dev]"
chatvideo --help
chatvideo --version
chatvideo --tree
chatvideo --tree-brief
python -m pytest -q
python -m build
python -m twine check dist/*
python -m pip install -e ".[docs]"
mkdocs build --strict
```

文档站：<https://arch.gh.wzhecnu.cn/ChatVideo/>

## 文档中的工作流蓝图

当前包先用文档沉淀 provider-neutral 的图片到视频工作流蓝图，避免把具体项目素材、内部路径、任务 ID、分享链接或密钥写进可复用说明。当前重点不是视频聊天，也不是只做已有视频剪辑，而是面向图生视频模型：给定有序关键图，尤其三张图的故事板，通过相邻首尾帧约束生成片段，再合成为一个视频。完整说明见 `docs/workflow-blueprint.md`。

这些工作流现在是文档蓝图，不是已实现 CLI 命令：

- `edit`：已有视频的拼接、裁剪、转场和终版组装。
- `generate text`：文生视频任务提交、轮询、下载和安全摘要。
- `generate image`：按有序关键图生成视频，典型三图故事板会拆成相邻首尾帧片段。
- `generate frames`：首尾帧约束的单段生成，例如第 1 张到第 2 张、第 2 张到第 3 张。
- `review` / `final`：临时 review 与最终交付分离。

当前 CLI 只保留真实工具入口：`chatvideo --help`、`chatvideo --version`、`chatvideo --tree` 和 `chatvideo --tree-brief`。完整和简洁树都由真实 Click 注册面生成；等某个视频操作真的实现后，再把它加入 CLI。

## CLI 规范

ChatVideo 使用 `chatstyle>=0.2.0,<0.3.0` 的共享 `add_tree_option()` 生成 `--tree` / `--tree-brief`，不维护包内 tree renderer。新增可执行命令时，应先更新真实 Click 注册面，再同步 README、MkDocs CLI 树和测试。当前没有 env/profile/config 行为，因此不引入 ChatEnv；需要 provider/profile 配置时再使用 typed provider registration 和 ChatEnv 管理的 storage 路径。

## 目录结构

- `src/`：包源码
- `tests/code-tests/`：代码测试和历史测试迁移
- `tests/cli-tests/`：真实 CLI 测试，doc-first
- `tests/mock-cli-tests/`：mock/fake CLI 测试，doc-first

## 开发说明

扩展脚手架前，先阅读 `DEVELOP.md` 和 `AGENTS.md`。
