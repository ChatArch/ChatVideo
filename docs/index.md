# ChatVideo 文档

ChatVideo 是 ChatArch 的视频工作流 CLI/API 包。当前重点是把真实项目里沉淀出的通用流程整理成可复用的命令设计：本地剪辑、文生视频、图生视频、首尾帧分段生成、review 发布和最终交付。

站点入口：<https://arch.gh.wzhecnu.cn/ChatVideo/>

## 按场景选择文档

| 场景 | 文档 |
| --- | --- |
| 了解当前 CLI 总体设计 | [CLI 设计蓝图](cli-design.md) |
| 规划已有视频的拼接、裁剪和转场 | [CLI 设计蓝图](cli-design.md#chatvideo-edit) |
| 规划文生视频任务提交和下载 | [CLI 设计蓝图](cli-design.md#chatvideo-generate-text) |
| 规划多图图生视频和顺序确认 | [CLI 设计蓝图](cli-design.md#chatvideo-generate-image) |
| 规划首尾帧约束的分段生成 | [CLI 设计蓝图](cli-design.md#chatvideo-generate-frames) |
| 区分临时 review 和最终交付 | [CLI 设计蓝图](cli-design.md) |

## 文档栏目组织

当前文档先保持轻量：

- **CLI / 工作流**：记录 provider-neutral 的命令蓝图和隐私边界。

后续实现真实命令时，再按 ChatArch 包文档惯例拆出使用指南、provider adapter、manifest schema、review/final 发布等章节。

## CLI

```bash
chatvideo --help
chatvideo --version
chatvideo design
chatvideo design --workflow image-to-video --format json
```

当前 `chatvideo design` 只输出设计蓝图，不提交外部生成任务，也不发布文件。
