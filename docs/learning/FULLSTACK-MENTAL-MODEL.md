# 全栈开发脑内全景图｜专业定义 + 大白话 + 技术关系

> 先认清整张地图，再按真正需求学其中一小块。本页是解释层，不是另一个课程进度表。配套：[知识图](KNOWLEDGE-GRAPH.md) · [按需学习](DEMAND-ROUTER.md) · [上游具体资料](UPSTREAM-ASSET-INDEX.md)。

## 一、一次业务请求如何穿过整个技术系统

~~~mermaid
flowchart TD
  User["用户 / 需求"] --> Client["终端：Web / 小程序 / 桌面 / 移动"]
  Client --> UI["HTML / CSS / JS/TS：内容、样式、交互"]
  UI --> Framework["Vue / React / 原生界面"]
  Framework --> Render["SPA / SSR / SSG / Hybrid"]
  Render --> Network["DNS/TLS/HTTP、REST、SSE、WebSocket"]
  Network --> Proxy["CDN / Nginx / API网关"]
  Proxy --> API["API：输入校验 / 身份 / 资源级权限 / 业务规则"]
  API --> Server["后端：Python/FastAPI、Java/Spring、Node/Nest、Go"]
  Server --> SQL["PostgreSQL / MySQL：事务与持久化"]
  Server --> Cache["Redis：缓存 / 数据结构"]
  Server --> Async["Worker / Broker：长任务与跨服务事件"]
  Server --> External["对象存储 / 搜索 / ERP / LLM"]
  Framework -.-> Contract["OpenAPI / Schema：前后端契约"]
  API -.-> Contract
  API -.-> Secure["认证 / 授权 / 审计 / 密钥"]
  Framework -.-> Test["单测 / 集成 / E2E / CI"]
  Server -.-> Test
  Test --> Deploy["Docker / Linux / HTTPS / 回滚"]
  Deploy --> Observe["日志 / Metrics / Trace / 监控"]
~~~

**大白话：** 前端是供用户操作的柜台，API 是接单窗口，Python/Java/Node 的业务逻辑是后厨，关系数据库是持久账本，Redis 是高频数据的速取柜，Worker 是后台任务处理人，MQ 是跨工位传递有状态消息的机制，Nginx 是入口转发，CI 是质检，监控是运行观测。

**边界：** 这是功能责任类比，非技术定义。一个 Next/Nuxt 应用也可能同时承担界面和服务端功能；Redis 不只能做缓存；SSE/MQ 不自动保证任务可靠性；小网站通常不需要把全图所有组件都安装。

## 二、第二张图：谁和谁是同类，谁和谁不是同类

~~~mermaid
flowchart LR
  JS["JS / TypeScript：语言层"] --> Vue["Vue：UI框架"]
  JS --> React["React：UI库"]
  JS --> Node["Node.js：服务端运行时"]
  Vue --> VueVite["Vue + Vite：SPA构建方案"]
  React --> ReactVite["React + Vite：SPA构建方案"]
  Vue --> Nuxt["Nuxt：Vue应用/SSR框架"]
  React --> Next["Next.js：React应用/SSR框架"]
  Node --> Nest["NestJS / Express：Node API"]
  Other["其他服务语言"] --> Python["Python + FastAPI"]
  Other --> Java["Java/JVM + Spring Boot"]
  Other --> Go["Go"]
  Other --> Native["Rust / C++ / CUDA（按需）"]
  VueVite & ReactVite & Nuxt & Next & Nest & Python & Java & Go --> Protocol["HTTP / API边界"]
~~~

| 名称 | 专业定义 | 大白话理解 | 主要关系 |
|---|---|---|---|
| HTML / CSS | 标记语言 / 层叠样式表 | 页面骨架 / 外观 | 浏览器基础 |
| JavaScript | 编程语言，浏览器及其他运行时可执行 | 页面交互和程序逻辑 | Vue/React/Node生态共同基础 |
| TypeScript | JS的类型化扩展和工具链 | 提前核对变量与函数的“合同” | 静态类型不能代替运行时校验 |
| Vue / React | UI框架 / UI库 | 以组件组织界面、更新状态 | 选择现有项目主栈之一实践即可 |
| Vite | 开发服务器和前端构建工具 | 开发热更新、打包工具 | 不是Vue/React的替代品 |
| Nuxt / Next.js | Vue / React生态的应用框架 | 路由、渲染、数据与服务端功能的整合框架 | SSR不是所有页面必需或一定更快 |
| Node.js | JavaScript运行时 | JS在服务端/CLI也能运行 | Node不是TypeScript，更不是新语言 |
| FastAPI / Spring Boot / NestJS | Python / Java / Node生态的Web后端框架 | 三套可选后端开发体系 | 根据已有系统/团队/需求选 |
| SQL / PostgreSQL / Redis | 查询语言 / 关系数据库 / 内存数据平台 | 查询方式 / 账本 / 高速取用 | SQL不是一种数据库产品 |

## 三、第三张图：用户点击“提交”到底发生了什么

~~~mermaid
sequenceDiagram
  autonumber
  participant User as 用户
  participant UI as Vue/React
  participant Edge as HTTP/反代
  participant API as FastAPI/Spring/Nest
  participant DB as PostgreSQL
  participant Worker as Worker（可选）
  User->>UI: 填写表单并提交
  UI->>UI: 即时校验与加载状态
  UI->>Edge: POST JSON + 凭证
  Edge->>API: 请求转发
  API->>API: 服务端输入验证、认证、资源授权
  API->>DB: 事务读写
  DB-->>API: 提交或回滚
  opt 需要长时间处理
    API->>Worker: 业务任务入队
    Worker->>DB: 更新权威状态
  end
  API-->>UI: HTTP响应、状态码和契约字段
  UI-->>User: 展示业务结果或错误
  opt 需要实时进度
    UI->>API: 订阅SSE或WebSocket
    API-->>UI: 进度事件
  end
~~~

从这里理解真正的分工：浏览器管理事件、呈现和请求竞态；API契约规范HTTP状态与数据结构；后端掌管服务器权威校验/权限/业务规则；数据库保障事务一致性；后台任务保障耗时操作可追踪；CI/部署/观测使功能能够验证和持续维护。**前端表单校验不是权限保障；HTTP 200不代表数据库不会出现并发问题。**

## 四、知识之间三类关系

- **最低先修**：Vue/React至少需要JS和HTML概念；Spring MVC至少需要Java对象概念与HTTP请求。但“先修”不是要先把前面所有课程全部学完。
- **平行替代**：React ↔ Vue、Next ↔ Nuxt、FastAPI ↔ Spring/Nest、Electron ↔ Tauri。它们并不完全等价，但通常按团队与场景选一种主实现。
- **跨层协作**：Vue页面 → OpenAPI → Spring业务 → SQL；也可以React → FastAPI → Redis/Worker。跨层技术关系永远重要，具体框架可变。

## 五、专业原理加类比怎么使用

每个知识点要能回答：**它是什么？它解决什么问题？它运行在哪？它依赖什么？谁是替代方案？何时不该用？怎样用失败实验证明自己懂了？**

例子：在 Vue 列表中输入搜索词A、再输入B，B先响应，A后响应导致旧数据覆盖。
- **专业定义**：异步请求竞态，完成顺序并不保证与业务最新输入一致。
- **大白话**：两份外卖订单先后下单，先到的可能是后下单的；不能因为旧单最后送到就把新单替换掉。
- **关联知识**：JS Promise/闭包、Vue响应式/watch、HTTP取消、客户端服务端状态同步。
- **最小实验**：模拟逆序网络返回，使用请求序列标识或AbortController修正，测试旧响应不覆盖新状态。
- **权威资料**：[MDN Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)、[Vue Watchers](https://vuejs.org/guide/essentials/watchers.html)；解决此问题无需先学完24周。

## 六、按需求走最短路径

| 真实场景 | 先学什么 | 什么时候才扩展 |
|---|---|---|
| 纯前端网站/浏览器工具 | HTML/CSS/JS、部署、测试 | 账号/存储出现才学后端 |
| 已有 Vue 企业后台 | Vue、API、HTTP、权限、数据库 | SEO/SSR需要时才学Nuxt |
| Java API维护 | Java最低语法、Spring MVC、测试 | 涉及事务/安全才补Spring Data/Security |
| AI问答助手 | FastAPI或Node API、工具契约、评测、权限 | 任务耗时才加Worker，跨系统才加MQ |
| Electron桌面工具 | JS/TS、主进程/渲染进程、安全IPC | 原生体积/系统能力限制才评估Tauri |
| 小程序/移动应用 | 对应平台运行时、合法网络请求、真机/模拟器 | 按真实平台和设备能力增补 |

## 七、核心权威来源与限制

- [上游编程语言技术栈地图](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/knowledge/software-engineering/programming-language-stack-map.md)
- [MDN 客户端与服务端](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps/Client-Server_overview)
- [Vue官方](https://vuejs.org/guide/introduction) / [Nuxt渲染模式](https://learn.nuxt.com/en/concepts/rendering-modes)
- [React官方](https://react.dev/learn) / [Next的Server/Client组件](https://nextjs.org/docs/app/getting-started/server-and-client-components)
- [Spring MVC](https://docs.spring.io/spring-boot/reference/web/servlet.html)
- [MDN SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events) / [WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)
- [Electron进程模型](https://www.electronjs.org/docs/latest/tutorial/process-model)

**停止规则**：当本次真实需求已通过独立实现、负例测试和复测，立即回到产品开发；其他模块保持知识地图索引即可，不需要刷完。
