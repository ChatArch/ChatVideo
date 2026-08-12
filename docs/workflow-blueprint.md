# ChatVideo 工作流蓝图

本文记录 ChatVideo 的图片到视频工作流规划。它是文档，不是当前 CLI 功能；这里的能力名用于说明未来工具边界，不表示现在已经有对应的 `chatvideo` 子命令。

## 设计目标

- 当前核心需求是图片到视频：输入有序关键图，尤其三张图故事板，通过相邻首尾帧约束生成一个视频。
- 区分已有视频剪辑、文生视频、图生视频、首尾帧生成、review 发布和最终交付。
- 把临时 review 产物和长期最终产物明确分开。
- 每个生成片段都应通过本地 manifest 可追踪，但 manifest 不保存密钥。
- 对成本高或不确定的生成任务，支持逐段 review 后再继续。
- provider 细节交给 ChatEnv 风格的环境配置和后续 adapter。

## 当前需求模型

这不是视频聊天产品，也不是只围绕已有视频剪辑的工具。当前要服务的是图片到视频模型：用户给出一组有序图片，让 provider 按图像约束生成视频。

典型的三图故事板可以这样理解：

```text
frame-01.png  ->  frame-02.png  ->  frame-03.png
```

如果 provider 的能力是“给首帧和尾帧生成一段视频”，ChatVideo 的规划应把三张图拆成相邻片段：

```text
segment-01: frame-01.png -> frame-02.png
segment-02: frame-02.png -> frame-03.png
final.mp4:  segment-01 + segment-02
```

这些内容是未来工具能力的设计说明。当前可执行 CLI 只有 `chatvideo --help`、`chatvideo --version` 和 `chatvideo --tree`。

## 规划能力

<div class="grid cards" markdown>

-   **已有视频剪辑**

    面向本地已有媒体文件的拼接、裁剪、转场和终版组装。它应该保留源素材，只写出新的产物。

-   **文生视频**

    面向 provider-backed 文生视频任务。prompt 优先来自文件，避免把长 prompt 留在 shell history。

-   **图生视频**

    面向有序关键图。典型输入不是一张孤立图片，也不是公开素材包，而是用户确认过顺序的关键帧集合。

-   **首尾帧片段**

    面向支持首帧 + 尾帧约束的 provider。三张图生成一个视频时，默认拆成两段相邻首尾帧任务。

-   **review 与 final**

    review 是临时操作细节；final 只复制已确认的最终产物到长期位置。

</div>

## 图生视频 { #chatvideo-generate-image }

图生视频能力应先记录图片顺序，再进入 provider 任务。三张关键图会进入首尾帧分段生成，而不是作为一个不透明的“多图 prompt”。

预期行为：

- 生成前记录已确认的图片顺序。
- 默认让原始图片留在本地工作区。
- 先产出 review 片段，再进入最终导出。
- 不为了满足 provider 输入而把原始图复制到公开存储。

## 首尾帧分段 { #chatvideo-generate-frames }

首尾帧能力负责把相邻关键帧交给 provider，生成可 review 的单段视频。

预期行为：

- 把每张关键图都当成私有输入。
- 三张图生成一个视频时，默认拆成两段相邻首尾帧任务。
- 逐段 review，只有通过 review 的片段才能组装成最终视频。

## review 和 final { #review-to-final }

review 与 final 的边界要清楚：review 链接可以是临时的，final 产物必须是用户确认后的长期交付物。

预期行为：

- review 链接是临时操作细节。
- final export 只复制已确认的最终产物。
- verify 检查时长、音视频流、大小；传入 URL 时也检查可访问性。

## 隐私基线

- provider 凭据只放在环境配置里，manifest 不写密钥。
- 原始输入默认留在本地，只发布明确的 review 或 final artifact。
- 需要分享报告时，按需隐去任务 ID、URL、路径和 provider 请求 payload。
- 可复用模板不嵌入用户特定的素材描述。
- 优先记录通用元数据：时长、分辨率、编码、音轨和产物角色。

## 当前能力与规划边界

<div class="grid cards" markdown>

-   **已实现**

    当前 CLI 只有帮助和版本入口。

-   **规划中**

    剪辑、生成、review、final 等视频操作能力还只是文档蓝图。

-   **安全默认值**

    原始图片和 provider 凭据默认留在本地环境；可复用文档只记录通用流程和元数据。

</div>
