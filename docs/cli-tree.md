# ChatVideo CLI 树

这页只列当前已经实现的命令入口。ChatVideo 使用共享的 `chatstyle.add_tree_option()` 从真实 Click 注册面生成命令树；图片到视频、首尾帧、review/final 等内容目前是[工作流蓝图](workflow-blueprint.md)，不是 CLI。

- `chatvideo --tree` 显示参数签名，适合接口审查。
- `chatvideo --tree-brief` 保留相同节点和说明，但省略参数签名。

当前 CLI 是 root-only，没有业务命令参数，因此完整和简洁视图相同。

## 完整命令树

```text
chatvideo
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

## 简洁命令树

```text
chatvideo
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

## 当前能力

<div class="grid cards" markdown>

-   **帮助入口**

    `chatvideo --help` 用来确认当前命令面。现在没有视频操作子命令。

-   **版本入口**

    `chatvideo --version` 用来确认安装的 ChatVideo 包版本。

-   **完整 CLI 树**

    `chatvideo --tree` 从真实 Click 注册面生成带参数签名的命令树。

-   **简洁 CLI 树**

    `chatvideo --tree-brief` 生成相同节点，但省略业务命令参数签名。

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
- 新增可执行命令时，先让 `chatvideo --tree` / `chatvideo --tree-brief` 反映真实注册面，再同步这页、测试和更深的使用文档。
