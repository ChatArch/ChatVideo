# ChatVideo CLI 设计蓝图

本文记录 ChatVideo 第一版 provider-neutral CLI 设计。它来自真实视频工作流实践，但刻意不包含具体项目素材、内部路径、任务 ID、服务链接、账号名、provider 请求 payload 或凭据。

## 设计目标

- 覆盖剪辑、文生视频、图生视频、首尾帧生成、review 发布和最终交付。
- 把临时 review 产物和长期最终产物明确分开。
- 每个生成片段都通过本地 manifest 可追踪，但 manifest 不保存密钥。
- 对成本高或不确定的生成任务，支持逐段 review 后再继续。
- provider 细节交给 ChatEnv 风格的环境配置和后续 adapter。

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

负责一个或多个有序参考图的图生视频任务。

```bash
chatvideo storyboard order --images inputs/ --output storyboard.json
chatvideo generate image --images inputs/ --duration 10 --review-dir review/
chatvideo workflow run --storyboard storyboard.json --one-segment-at-a-time
```

预期行为：

- 生成前记录已确认的图片顺序。
- 默认让原始图片留在本地工作区。
- 先产出 review 片段，再进入最终导出。

### chatvideo generate frames

负责首尾帧约束的单段生成。

```bash
chatvideo generate frames --first start.png --last end.png --duration 10
chatvideo workflow split --frames ordered/ --duration-per-segment 10
chatvideo edit concat --manifest generated-segments.json --output final.mp4
```

预期行为：

- 把首帧/尾帧当成私有输入。
- 多帧故事拆成相邻的首尾帧 segment job。
- 只把通过 review 的片段组装成最终视频。

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
