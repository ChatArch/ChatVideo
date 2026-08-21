# ChatVideo 文档

ChatVideo 是 ChatArch 的视频工作流 CLI/API 包。当前重点是把真实项目里沉淀出的图片到视频流程整理成可复用的命令设计：给定有序关键图，尤其三张图故事板，通过相邻首尾帧约束生成片段，再 review、拼接并最终交付一个视频。

站点入口：<https://arch.gh.wzhecnu.cn/ChatVideo/>

## 选择入口

<div class="grid cards" markdown>

-   **看当前可用命令**

    从已实现的 `chatvideo` 命令树开始，确认当前只有真实工具入口。

    [查看 CLI 树](cli-tree.md)

-   **理解图片到视频模型**

    三张有序关键图会拆成相邻首尾帧片段，再组装成一个最终视频。

    [查看工作流蓝图](workflow-blueprint.md#chatvideo-generate-image)

-   **规划首尾帧分段**

    适合 provider 支持“首帧 + 尾帧生成一段视频”的场景。

    [查看首尾帧蓝图](workflow-blueprint.md#chatvideo-generate-frames)

-   **区分 review 与 final**

    临时 review 产物和长期最终交付分开记录，避免把内部链接或任务细节写进通用文档。

    [查看交付边界](workflow-blueprint.md#review-to-final)

</div>

## 当前阅读路线

| 想确认什么 | 推荐页面 |
| --- | --- |
| 当前真实命令面 | [CLI 树](cli-tree.md) |
| 三图关键帧如何生成一个视频 | [工作流蓝图](workflow-blueprint.md#chatvideo-generate-frames) |
| 图片到视频输入如何记录顺序 | [工作流蓝图](workflow-blueprint.md#chatvideo-generate-image) |
| 文生视频和剪辑能力如何规划 | [工作流蓝图](workflow-blueprint.md) |
| 哪些能力还只是规划 | [CLI 树：规划边界](cli-tree.md#planned-boundaries) |

## 快速命令

```bash
chatvideo --help
chatvideo --version
chatvideo --tree
chatvideo --tree-brief
```

当前 CLI 只保留真实工具入口。完整和简洁命令树都由共享 ChatStyle runtime 从 Click 注册面生成；工作流规划放在[工作流蓝图](workflow-blueprint.md)里，不作为 `chatvideo` 子命令暴露。
