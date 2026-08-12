# 更新日志

## 2026-08-12

### 新增

- 准备 `0.1.1` patch 版本：新增 `chatvideo --tree`，从真实 Click 注册面生成当前 root-only CLI 树。
- 增加发布/文档 workflow contract 测试，锁定 tag-only OIDC 发布、默认分支 ancestor guard、Preview Docs 从 `mkdocs.yml site_url` 派生 URL。

### 变更

- 继续保持 ChatVideo 当前没有视频业务子命令；工作流规划保留在文档里，不包装成 `design` 或 `generate` CLI。
- MkDocs Material 启用 emoji renderer baseline，并收紧 docs extra 版本窗口。
- 移除未使用的 ChatStyle/ChatEnv 运行时依赖，当前 CLI 仅依赖 Click。

## 2026-07-18

### 新增

- 在 `0.0.1` 占名版本之后，发布第一个真实 ChatVideo 包版本。
- 增加 MkDocs Material 文档站结构，包括中英文首页、工作流蓝图页面、Preview Docs、Deploy Docs 和严格文档构建。
- 记录隐私安全的工作流蓝图，覆盖剪辑、文生视频、图生视频、首尾帧生成、review 发布和最终交付。
- 明确当前图片到视频模型：三张有序关键帧会拆成相邻首尾帧片段，review 通过后再组装成一个视频。

### 变更

- 按 ChatArch MkDocs hub/card 风格对齐文档首页和命令文档，补充第一等 CLI 树页面和正式能力边界。
- 移除只输出文档内容的 `chatvideo design` CLI；在真实视频操作实现前，工作流规划只保留在文档里。

### 修复
