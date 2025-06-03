# LightRAG WebUI

LightRAG WebUI 是一个基于 React 的 Web 界面，用于与 LightRAG 系统交互。它提供了一个用户友好的界面，用于查询、管理和探索 LightRAG 的功能。

## 安装

1. **安装 Bun：**

   如果尚未安装 Bun，请按照官方文档进行安装：[https://bun.sh/docs/installation](https://bun.sh/docs/installation)

2. **安装依赖：**

   在 `lightrag_webui` 目录下，运行以下命令以安装项目依赖：

   ```bash
   bun install --frozen-lockfile
   ```

3. **构建项目：**

   运行以下命令以构建项目：

   ```bash
   bun run build --emptyOutDir
   ```

   该命令将打包项目并将构建文件输出到 `lightrag/api/webui` 目录。

## 开发

- **启动开发服务器：**

  如果您想在开发模式下运行 WebUI，请使用以下命令：

  ```bash
  bun run dev
  ```

## 脚本命令

以下是 `package.json` 中定义的一些常用脚本命令：

- `bun install`：安装项目依赖。
- `bun run dev`：启动开发服务器。
- `bun run build`：构建项目。
- `bun run lint`：运行代码检查工具。