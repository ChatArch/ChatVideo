# ChatVideo CLI 设计蓝图

本文记录 ChatVideo 第一版 provider-neutral CLI 设计。它来自真实视频工作流实践，但刻意不包含具体项目素材、内部路径、任务 ID、服务链接、账号名、provider 请求 payload 或凭据。

## 设计目标

- 当前核心需求是图片到视频：输入有序关键图，尤其三张图故事板，通过相邻首尾帧约束生成一个视频。
- 覆盖剪辑、文生视频、图生视频、首尾帧生成、review 发布和最终交付。
- 把临时 review 产物和长期最终产物明确分开。
- 每个生成片段都通过本地 manifest 可追踪，但 manifest 不保存密钥。
- 对成本高或不确定的生成任务，支持逐段 review 后再继续。
- provider 细节交给 ChatEnv 风格的环境配置和后续 adapter。

## 当前需求模型

这不是视频聊天产品，也不是只围绕已有视频剪辑的工具。当前要服务的是图片到视频模型：用户给出一组有序图片，让 provider 按图像约束生成视频。

典型的三图故事板可以这样理解：

```text
frame-01.png  ->  frame-02.png  ->  frame-03.png
```

如果 provider 的能力是“给首帧和尾帧生成一段视频”，ChatVideo 的设计应把三张图拆成相邻片段：

```text
segment-01: frame-01.png -> frame-02.png
segment-02: frame-02.png -> frame-03.png
final.mp4:  segment-01 + segment-02
```

因此文档中的 `generate image` / `generate frames` 目前都是设计蓝图：它们描述未来 CLI 应如何接收关键帧、记录顺序、分段 review 和最终拼接；当前 PR 只实现 `chatvideo design` 来输出这个蓝图。

## 命令组草案

### chatvideo edit

负责已有媒体文件上的确定性操作。

```bash
chatvideo edit concat --manifest timeline.json --output draft.mp4
chatvideo edit trim --input clip.mp4 --start 00:00:02 --end 00:00:10
chatvideo edit transition --manifest timeline.json --style cut|xfade
```

预期行为：

- 接收显式 manifest 或文件参数。
- 保留源素材，只写出新的产物。
- 安全时使用 stream copy；必要时再转码。
- 记录时长、编码、音轨、文件大小和产物角色。

### chatvideo generate text

负责 provider-backed 文生视频任务。

```bash
chatvideo generate text --prompt prompt.md --duration 10 --review-dir review/
chatvideo job poll --manifest runs/latest.json --download review/
chatvideo report summarize --manifest runs/latest.json --redact
```

预期行为：

- 优先从 prompt 文件读取，避免把长 prompt 留在 shell history。
- job manifest 只写 provider 名称、安全状态字段和 artifact 元数据。
- 凭据保存在环境配置里，报告只说明凭据是否已配置。

### chatvideo generate image

负责按有序关键图规划图片到视频任务。典型输入不是一张孤立图片，也不是公开素材包，而是用户确认过顺序的关键帧集合。

```bash
chatvideo storyboard order --images frame-01.png frame-02.png frame-03.png --output storyboard.json
chatvideo generate image --keyframes storyboard.json --mode first-last-frame --review-dir review/
chatvideo workflow run --storyboard storyboard.json --one-segment-at-a-time
```

预期行为：

- 生成前记录已确认的图片顺序。
- 三张关键图会进入首尾帧分段生成，而不是作为一个不透明的“多图 prompt”。
- 默认让原始图片留在本地工作区。
- 先产出 review 片段，再进入最终导出。

### chatvideo generate frames

负责把相邻关键帧交给支持首尾帧约束的 provider，生成可 review 的单段视频。

```bash
chatvideo generate frames --first frame-01.png --last frame-02.png --duration 5 --review-dir review/segment-01
chatvideo generate frames --first frame-02.png --last frame-03.png --duration 5 --review-dir review/segment-02
chatvideo edit concat --manifest generated-segments.json --output final.mp4
```

预期行为：

- 把每张关键图都当成私有输入。
- 三张图生成一个视频时，默认拆成两段相邻首尾帧任务。
- 逐段 review，只有通过 review 的片段才能组装成最终视频。

### chatvideo review 和 chatvideo final

负责临时 review 和长期最终产物之间的边界。

```bash
chatvideo review publish --artifact draft.mp4 --target local-share
chatvideo final verify --url-or-path final.mp4
chatvideo final export --artifact final.mp4 --target archive
```

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

## 当前 PR 范围

本 PR 只新增 `chatvideo design` 命令和文档站结构。它不实现 provider adapter，不提交网络生成任务，也不发布文件。后续 PR 可以按这个隐私契约逐步实现各个命令组。
