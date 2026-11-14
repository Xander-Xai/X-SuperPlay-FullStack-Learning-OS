# V4.2 全栈核心知识关系图｜概念先修、平行选型、跨层协作

> 除核心42节点，另有按需查阅的[17个横向基础能力](CROSS-CUTTING-FOUNDATIONS.md)（环境、算法、调试、协作、UX、国际化、性能、安全、供应链、SLO、成本等），已分别映射回核心节点并可通过[需求路由](DEMAND-ROUTER.md)搜索。它们**不是17个独立强制Gate**。

> **本图不定义学习时间顺序。** 每个节点都能直达[专业定义/类比/原理/最小实验卡](NODE-STUDY-CARDS.md)、[官方阅读](OFFICIAL-RESOURCES.md)、[上游源资料](UPSTREAM-ASSET-INDEX.md)。W1–W24仅作为历史知识坐标；个人状态仍在[PROGRESS](PROGRESS.md)。

## 一、核心技术如何从前台穿过后端

~~~mermaid
flowchart LR
  User["用户和真实需求"] --> Surface["Web/小程序/桌面/移动"]
  Surface --> Web["HTML CSS JS TS"]
  Web --> Vue["Vue F08"] --> Nuxt["Nuxt F09"]
  Web --> React["React F04"] --> Next["Next F05"]
  Web --> Standalone["Vite静态前端 F07"]
  Nuxt & Next & Standalone --> Protocol["HTTP / OpenAPI B01"]
  Protocol --> Fast["Python FastAPI B02"]
  Protocol --> Spring["Java Spring B03 B04"]
  Protocol --> Node["Node Nest B07"]
  Protocol --> Go["Go B08"]
  Fast & Spring & Node & Go --> Data["PG/MySQL D01 D04"]
  Fast & Spring & Node & Go --> Extra["Redis D02 / MQ D03 / 对象/搜索 D05"]
  Protocol -.-> Auth["认证/授权 E03"]
  Fast -.-> Tasks["Worker任务 B06"]
  Surface -.-> Realtime["SSE/WebSocket F11"]
  Protocol -.-> Obs["Trace E04"]
  Data & Extra & Tasks -.-> Obs
  Obs --> Delivery["测试CI E01 / 部署 E02 / 发布P03"]
~~~

> 图中的连接表示**可能协作**，不是同时必须安装或固定部署关系。Nuxt/Next自身也能承担服务端职责；UI可以直接调用现有REST服务而非新建Python/Java/Node全部后端。

## 二、先修和选型不是一个概念

~~~mermaid
flowchart TB
  JS["JS/TS F03"] --> React["React F04"] --> Next["Next F05"]
  JS --> Vue["Vue F08"] --> Nuxt["Nuxt F09"]
  JS --> Node["Node F06"] --> Nest["Nest B07"]
  Java["Java JVM B03"] --> Boot["Spring Boot B04"] --> Security["Spring Data/Security B05"]
  HTTP["Web HTTP F01"] -.-> Boot
  HTTP -.-> Nest
  HTTP -.-> Fast["FastAPI B02"]
  Browser["HTML/CSS F02"] --> React
  Browser --> Vue
~~~

**实线代表最低概念依赖，虚线代表常见配合但可以按场景单独理解。** 技术替代关系（Vue/React、Next/Nuxt、FastAPI/Spring/Nest）不意味着功能完全相同；选择团队正在使用或当前业务合理的一条路径即可。Spring Security**不强制先学PostgreSQL**；Android原生**不强制先学Expo**。

## 三、所有42个节点的索引

| ID | 主题 | 最低概念先修 | 专业作用 | 官方专题章节 | 上游材料类型 | 独立实验 |
|---|---|---|---|---|---|---|
| P01 | 业务需求/验收 | 无 | 解决什么问题、什么算成功 | [阅读](https://docs.github.com/en/issues/tracking-your-work-with-issues/learning-about-issues/about-issues) | 学习方法 | [查看本节点卡](NODE-STUDY-CARDS.md) |
| P02 | 架构与技术取舍 | P01 | 模块边界、数据归属、技术选型 | [阅读](https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/) | 概念综述 | [查看本节点卡](NODE-STUDY-CARDS.md) |
| F01 | Web/HTTP/浏览器 | 无 | 请求、Cookie、状态码、CORS、TLS | [阅读](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview) | 课程参考 | [查看本节点卡](NODE-STUDY-CARDS.md) |
| F02 | HTML/CSS/无障碍 | 无 | 布局、语义表单、响应式与键盘操作 | [阅读](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility) | 课程参考 | [查看本节点卡](NODE-STUDY-CARDS.md) |
| F03 | JavaScript/TypeScript | 无 | 事件循环、异步取消、泛型、模块 | [阅读](https://www.typescriptlang.org/docs/handbook/2/narrowing.html) | 概念综述 | [查看本节点卡](NODE-STUDY-CARDS.md) |
| F04 | React/状态 | F02、F03 | 组件、路由、服务端数据与交互 | [阅读](https://react.dev/learn/state-as-a-snapshot) | 课程参考 | [查看本节点卡](NODE-STUDY-CARDS.md) |
| F05 | Next.js/SSR | F04 | 按SEO、缓存、服务端边界选择渲染 | [阅读](https://nextjs.org/docs/app/getting-started/server-and-client-components) | 概念综述 | [查看本节点卡](NODE-STUDY-CARDS.md) |
| F06 | Node.js/Streams | F03 | 服务端JS、BFF和流背压 | [阅读](https://nodejs.org/en/learn/asynchronous-work/event-loop-timers-and-nexttick) | 概念综述 | [查看本节点卡](NODE-STUDY-CARDS.md) |
| F07 | 构建与前端性能 | F03 | ESM、Vite、分包、Profiler | [阅读](https://vite.dev/guide/build) | 概念综述 | [查看本节点卡](NODE-STUDY-CARDS.md) |
| B01 | REST/OpenAPI | F01 | 定义前后端契约、类型与错误 | [阅读](https://spec.openapis.org/oas/latest.html) | 专题LAB | [查看本节点卡](NODE-STUDY-CARDS.md) |
| B02 | Python/FastAPI | F01 | 请求校验、业务逻辑、分层与测试 | [阅读](https://fastapi.tiangolo.com/tutorial/dependencies/) | 专题LAB | [查看本节点卡](NODE-STUDY-CARDS.md) |
| B03 | Java/JVM | 无 | 集合/泛型、JMM、线程、GC/JFR | [阅读](https://dev.java/learn/) | 专题LAB | [查看本节点卡](NODE-STUDY-CARDS.md) |
| B04 | Spring Boot/MVC | B03、F01 | Bean/IoC、Web服务、异常映射 | [阅读](https://docs.spring.io/spring-boot/reference/web/servlet.html) | 专题LAB | [查看本节点卡](NODE-STUDY-CARDS.md) |
| B05 | Spring Data/Security | B04 | 数据库事务、ORM、服务端权限 | [阅读](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html) | 专题LAB | [查看本节点卡](NODE-STUDY-CARDS.md) |
| B06 | Celery/后台任务可靠性 | B02 | 任务确认/重试/幂等与业务状态，而不是SSE解析 | [阅读](https://docs.celeryq.dev/en/stable/userguide/tasks.html) | 专题LAB | [查看本节点卡](NODE-STUDY-CARDS.md) |
| D01 | PostgreSQL/SQL | 无 | 持久化、MVCC、事务、索引 | [阅读](https://www.postgresql.org/docs/current/transaction-iso.html) | 专题LAB | [查看本节点卡](NODE-STUDY-CARDS.md) |
| D02 | Redis/缓存 | 无 | TTL、缓存击穿、失效与一致性 | [阅读](https://redis.io/docs/latest/) | 专题LAB | [查看本节点卡](NODE-STUDY-CARDS.md) |
| D03 | 消息/Outbox | D01 | 跨服务事件的可靠交付和幂等 | [阅读](https://www.rabbitmq.com/docs/queues) | 课程参考 | [查看本节点卡](NODE-STUDY-CARDS.md) |
| D04 | MySQL差异 | 无 | 比较InnoDB与PG事务和索引 | [阅读](https://dev.mysql.com/doc/refman/8.4/en/innodb-transaction-isolation-levels.html) | 概念综述 | [查看本节点卡](NODE-STUDY-CARDS.md) |
| E01 | Git/测试/CI | 无 | 回归、审查、自动验证 | [阅读](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions) | 专题LAB | [查看本节点卡](NODE-STUDY-CARDS.md) |
| E02 | Docker/Linux/部署 | 无 | 运行环境、HTTPS、备份与回滚 | [阅读](https://docs.docker.com/compose/) | 专题LAB | [查看本节点卡](NODE-STUDY-CARDS.md) |
| E03 | 身份/权限/多租户 | F01 | Cookie、OAuth/OIDC、资源级授权 | [阅读](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) | 专题LAB | [查看本节点卡](NODE-STUDY-CARDS.md) |
| E04 | Trace/性能/排障 | 无 | 日志、OpenTelemetry、P95、JFR | [阅读](https://www.w3.org/TR/trace-context/) | 专题LAB | [查看本节点卡](NODE-STUDY-CARDS.md) |
| P03 | 生产发布/运营 | P01、E01 | UAT、监控、成本、恢复责任 | [阅读](https://docs.github.com/en/actions) | 概念综述 | [查看本节点卡](NODE-STUDY-CARDS.md) |
| U01 | 静态工具站/SEO | F02、F03 | 纯浏览器工具与静态发布 | [阅读](https://web.dev/learn/seo) | 概念综述 | [查看本节点卡](NODE-STUDY-CARDS.md) |
| M01 | 微信小程序 | F03 | 平台生命周期、真机与审核 | [阅读](https://developers.weixin.qq.com/miniprogram/dev/framework/) | 课程参考 | [查看本节点卡](NODE-STUDY-CARDS.md) |
| M02 | 移动App | 无 | 设备权限、离线、签名与应用商店 | [阅读](https://docs.expo.dev/) | 概念综述 | [查看本节点卡](NODE-STUDY-CARDS.md) |
| A01 | AI/RAG/Agent | B01 | 模型/工具契约、评测和安全降级 | [阅读](https://docs.langchain.com/oss/python/langgraph/overview) | 课程参考 | [查看本节点卡](NODE-STUDY-CARDS.md) |
| P04 | 支付/订阅 | B01、E03 | 沙箱回调、验签、幂等与对账 | [阅读](https://docs.stripe.com/webhooks) | 概念综述 | [查看本节点卡](NODE-STUDY-CARDS.md) |
| F08 | Vue 3/响应式/状态 | F02、F03 | Vue的Composition API、ref/reactive/watch/路由与前端状态 | [阅读](https://vuejs.org/guide/essentials/watchers.html) | 课程参考 | [查看本节点卡](NODE-STUDY-CARDS.md) |
| F09 | Nuxt/SSR与混合渲染 | F08、F01 | Vue生态的全栈路由、SSR/CSR/Hybrid、数据与缓存边界 | [阅读](https://learn.nuxt.com/en/concepts/rendering-modes) | 概念综述 | [查看本节点卡](NODE-STUDY-CARDS.md) |
| F10 | PWA/Service Worker/浏览器存储 | F01、F03 | 离线缓存、浏览器生命周期、资源与业务数据缓存边界 | [阅读](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Offline_and_background_operation) | 概念综述 | [查看本节点卡](NODE-STUDY-CARDS.md) |
| F11 | SSE/WebSocket/实时连接 | F01 | 单向事件流与双向实时协议、断线重连和背压 | [阅读](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events) | 专题LAB | [查看本节点卡](NODE-STUDY-CARDS.md) |
| B07 | Node后端/NestJS/Express | F06、F01 | Node运行时上的Controller/服务/依赖注入/API架构 | [阅读](https://docs.nestjs.com/controllers) | 概念综述 | [查看本节点卡](NODE-STUDY-CARDS.md) |
| B08 | Go服务与并发 | F01 | Go编译/模块/interface/goroutine/context与HTTP服务 | [阅读](https://go.dev/learn/) | 概念综述 | [查看本节点卡](NODE-STUDY-CARDS.md) |
| B09 | Rust/C++/CUDA原生能力 | 无 | 原生模块、内存与并发安全、推理/性能约束下的系统编程 | [阅读](https://doc.rust-lang.org/stable/book/) | 概念综述 | [查看本节点卡](NODE-STUDY-CARDS.md) |
| D05 | 对象存储/全文搜索/向量数据库 | 无 | 文件、业务数据、全文检索与向量检索的不同存储责任 | [阅读](https://www.postgresql.org/docs/current/textsearch.html) | 专题LAB | [查看本节点卡](NODE-STUDY-CARDS.md) |
| E05 | 编译/构建/打包/运行时 | 无 | JS构建、Python依赖/虚拟环境、JVM JAR、Go/Rust二进制的区别 | [阅读](https://maven.apache.org/guides/getting-started/index.html) | 概念综述 | [查看本节点卡](NODE-STUDY-CARDS.md) |
| M03 | Electron/Tauri桌面应用 | F02、F03 | 桌面Web视图、系统API、主/渲染进程或Rust命令与安全边界 | [阅读](https://www.electronjs.org/docs/latest/tutorial/process-model) | 概念综述 | [查看本节点卡](NODE-STUDY-CARDS.md) |
| M04 | uni-app/跨端小程序生态 | F08 | 基于Vue的多端页面抽象与目标平台API/审核差异 | [阅读](https://uniapp.dcloud.net.cn/) | 课程参考 | [查看本节点卡](NODE-STUDY-CARDS.md) |
| M05 | Android/iOS原生开发 | 无 | Kotlin/Jetpack Compose或Swift/SwiftUI的设备与原生SDK能力 | [阅读](https://developer.android.com/jetpack/compose) | 概念综述 | [查看本节点卡](NODE-STUDY-CARDS.md) |
| A02 | MCP工具接口/Agent协议 | 无 | MCP工具/资源/提示的客户端服务端约定，区分REST和A2A | [阅读](https://modelcontextprotocol.io/specification/2026-07-28/architecture) | 专题LAB | [查看本节点卡](NODE-STUDY-CARDS.md) |

## 四、使用规则：一个真实需求就是一次学习入口

1. 不知道该学什么：先描述业务，使用[需求路由器](DEMAND-ROUTER.md)找到目标节点。
2. 先扫[全栈脑内图](FULLSTACK-MENTAL-MODEL.md)，知道它在哪一层、与上下层有什么关系。
3. 只按本图 `requires` 查缺补漏；相邻、替代和未来可能用到的技术仅形成**认知**，不强制开题。
4. 打开[节点卡](NODE-STUDY-CARDS.md)，读专业定义与类比的边界、官方精确章节、现成的上游LAB。
5. 真实编码→失败注入→独立复测，结束后回到产品开发；不以记住框架名字代替工程能力。

**注意复合节点的拆分意识**：B06（后台任务）与F11（实时流）是两条不同轴；B09（Rust/C++/CUDA）、D05（对象/全文/向量）、B05（Data/Security）只是**相关领域的索引桶**，真正写代码时需选择其中实际用到的子技术，不能拿一个教程覆盖全部。

