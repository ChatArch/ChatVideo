# ChatVideo CLI 树

这页只列当前已经实现的命令入口。ChatVideo 还没有真正的视频操作子命令；图片到视频、首尾帧、review/final 等内容目前是[工作流蓝图](workflow-blueprint.md)，不是 CLI。

## 当前命令拓扑

```text
chatvideo
|-- --help     # 查看顶层帮助
`-- --version  # 输出当前包版本
```

## 当前能力

<div class="grid cards" markdown>

-   **帮助入口**

    `chatvideo --help` 用来确认当前命令面。现在没有视频操作子命令。

-   **版本入口**

    `chatvideo --version` 用来确认安装的 ChatVideo 包版本。

-   **无设计命令**

    工作流蓝图是文档内容，不是工具行为；因此没有 `chatvideo design`。

</div>

## 规划边界 { #planned-boundaries }

以下能力只在文档蓝图中描述，当前还不是可执行子命令：

| 规划能力 | 当前状态 | 说明 |
| --- | --- | --- |
| `edit` | 规划中 | 未来负责已有视频的剪辑、拼接和转场。 |
| `generate text` | 规划中 | 未来负责文生视频 provider 任务。 |
| `generate image` | 规划中 | 未来负责有序关键图到视频的任务入口。 |
| `generate frames` | 规划中 | 未来负责相邻首尾帧片段生成。 |
| `review` | 规划中 | 未来负责临时 review 产物发布。 |
| `final` | 规划中 | 未来负责最终产物验证和交付。 |

## 更新规则

- 只有真正执行视频工作流的功能，才应该进入 CLI。
- Markdown 设计说明留在 docs，不包装成 CLI 命令。
- 新增可执行命令时，先更新这页的树，再补测试和更深的使用文档。
