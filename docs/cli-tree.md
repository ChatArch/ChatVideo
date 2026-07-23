# ChatVideo CLI 树

这页只列当前已经实现的命令入口。规划中的生成、review、final 等命令放在[设计蓝图](cli-design.md)，不在这里伪装成可执行接口。

## 当前命令拓扑

```text
chatvideo
|-- --help                         # 查看顶层帮助
|-- --version                      # 输出当前包版本
`-- design                         # 输出 provider-neutral 的视频工作流蓝图
    |-- --workflow all             # 默认输出全部蓝图
    |-- --workflow editing         # 规划：已有视频剪辑与组装
    |-- --workflow text-to-video   # 规划：文生视频任务
    |-- --workflow image-to-video  # 规划：有序关键图生成视频
    |-- --workflow first-last-frame # 规划：相邻首尾帧分段生成
    |-- --workflow review-to-final # 规划：review 到最终交付边界
    |-- --format text              # 默认文本输出
    `-- --format json              # 机器可读 JSON 输出
```

## 当前能力

<div class="grid cards" markdown>

-   **版本与帮助**

    `chatvideo --version` 和 `chatvideo --help` 是稳定入口，用来确认安装结果和查看当前命令面。

-   **设计蓝图输出**

    `chatvideo design` 输出规划中的工作流切片，方便先 review 命令形状，再实现 provider adapter。

-   **工作流过滤**

    `--workflow` 可以聚焦到一个切片，例如 `image-to-video` 或 `first-last-frame`。

-   **机器可读输出**

    `--format json` 适合测试、文档生成和后续工具消费。

</div>

## 规划边界 { #planned-boundaries }

以下命令名出现在设计蓝图中，但当前还不是可执行子命令：

| 规划命令组 | 当前状态 | 说明 |
| --- | --- | --- |
| `chatvideo edit ...` | 规划中 | 未来负责已有视频的剪辑、拼接和转场。 |
| `chatvideo generate text ...` | 规划中 | 未来负责文生视频 provider 任务。 |
| `chatvideo generate image ...` | 规划中 | 未来负责有序关键图到视频的任务入口。 |
| `chatvideo generate frames ...` | 规划中 | 未来负责相邻首尾帧片段生成。 |
| `chatvideo review ...` | 规划中 | 未来负责临时 review 产物发布。 |
| `chatvideo final ...` | 规划中 | 未来负责最终产物验证和交付。 |

## 更新规则

- 新增可执行命令时，先更新这页的树，再补测试和设计页链接。
- 只把真实可执行命令放进“当前命令拓扑”。
- 规划命令必须带状态说明，不能让读者误以为已经能调用 provider。
