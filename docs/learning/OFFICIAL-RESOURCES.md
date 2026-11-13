# 全栈权威参考资料库：按问题找原始章节

> **第一优先级：标准/官方原始文档；第二：官方教程和实际测试；第三：经复核的社区文章。** 官方文档是解释技术行为的证据源，但不代表读完后就掌握。资料可能随着版本变化，开始实验时应固定项目版本并核对相应版本文档。
>
> 此资料库与 [知识图](KNOWLEDGE-GRAPH.md) 的节点ID对应，服务于 [按需学习](DEMAND-ROUTER.md)。一项任务通常只需要选1–3个节点的章节，而不是每天去看所有资源。

## 一、Web / 前端 / 浏览器

| ID | 权威资料 | 建议进入的小节/概念 | 对应实战 |
|---|---|---|---|
| F01 | [MDN HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP) · [MDN CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS) | 请求/响应/状态码、缓存、预检与Cookie | Network复现401、CORS、断网、超时 |
| F02 | [MDN Learn](https://developer.mozilla.org/en-US/docs/Learn_web_development) · [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) · [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) · [Accessibility](https://developer.mozilla.org/en-US/docs/Web/Accessibility) | 语义表单、盒模型、Flex/Grid、焦点、响应式 | 390px布局、键盘可操作表单 |
| F03 | [MDN JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) · [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/) | 闭包/事件循环/Promise、泛型、类型收窄、模块 | request<T>、AbortController、竞态 |
| F04 | [React Learn](https://react.dev/learn) · [TanStack Query](https://tanstack.com/query/latest/docs/framework/react/overview) · [React Router](https://reactrouter.com/) | State Snapshot、Render/Commit、Effects、Query/Mutation、路由 | 搜索/分页缓存和请求回滚 |
| F05 | [Next.js App Router](https://nextjs.org/docs/app) | CSR/SSR/SSG、RSC、数据缓存、Client/Server组件 | 同内容SPA与SSR对照实验 |
| F06 | [Node.js Learn](https://nodejs.org/en/learn) · [Stream API](https://nodejs.org/api/stream.html) | Event Loop、Buffer、Stream、backpressure、ESM/CJS | 流式处理大文件和取消 |
| F07 | [Vite Guide](https://vite.dev/guide/) · [web.dev Performance](https://web.dev/learn/performance) · [React Profiler](https://react.dev/reference/react/Profiler) | 构建、分包、SourceMap、LCP/INP/CLS、Profiler | 前端慢页面定位、分包对比 |
| U01 | [web.dev SEO](https://web.dev/learn/seo) · [MDN Learn](https://developer.mozilla.org/en-US/docs/Learn_web_development) | 静态站、可索引内容、用户体验 | 不带后端的浏览器工具 |

## 二、API / Python / Java / 数据

| ID | 权威资料 | 建议进入的小节/概念 | 对应实战 |
|---|---|---|---|
| B01 | [OpenAPI 规范](https://spec.openapis.org/oas/latest.html) · [Orval](https://orval.dev/docs/) | Paths/Schema/Error Response、客户端生成和契约漂移 | 改Schema→生成→TS/集成测试 |
| B02 | [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/) · [Pydantic](https://docs.pydantic.dev/latest/) | Depends/Validation/Response Model、Pytest | 422/401/403、权限与边界校验 |
| B03 | [Dev.java](https://dev.java/learn/) · [Java Virtual Threads](https://docs.oracle.com/en/java/javase/25/core/virtual-threads.html) | 泛型/集合/Stream、并发/JMM、JVM/JFR | JUnit + 线程/GC故障定位 |
| B04 | [Spring Boot](https://docs.spring.io/spring-boot/reference/) · [Spring Framework](https://docs.spring.io/spring-framework/reference/) | IoC/Bean/AOP、Spring MVC、Validation | Bean装配/异常/API测试 |
| B05 | [Spring Data JPA](https://docs.spring.io/spring-data/jpa/reference/) · [Spring Security](https://docs.spring.io/spring-security/reference/) · [Testcontainers](https://java.testcontainers.org/) | 事务代理/自调用、JPA N+1、FilterChain、DB集成测试 | @Transactional和越权负例 |
| B06 | [Celery Tasks](https://docs.celeryq.dev/en/stable/userguide/tasks.html) · [MDN SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events) | ACK、重试、幂等、SSE事件分隔/重连 | Kill Worker和流任意chunk |
| D01 | [PostgreSQL](https://www.postgresql.org/docs/current/) · [SQLAlchemy](https://docs.sqlalchemy.org/en/20/) | 事务隔离、锁、EXPLAIN、索引与迁移 | 双连接并发/索引性能 |
| D02 | [Redis](https://redis.io/docs/latest/) | TTL、失效、数据结构、缓存一致性 | 集中过期的回源压测 |
| D03 | [RabbitMQ](https://www.rabbitmq.com/docs) · [Kafka](https://kafka.apache.org/documentation/) | ACK/offset、重复投递、死信/Outbox | 重复消费无重复副作用；二选一 |
| D04 | [MySQL Reference](https://dev.mysql.com/doc/) · [PostgreSQL](https://www.postgresql.org/docs/current/) | InnoDB与PG锁/隔离、索引、SQL差异 | 同一业务查询引擎对照 |

## 三、生产、安全、应用形态、AI

| ID | 权威资料 | 建议进入的小节/概念 | 对应实战 |
|---|---|---|---|
| E01 | [GitHub Actions](https://docs.github.com/en/actions) · [Playwright](https://playwright.dev/docs/intro) | CI、Unit/Integration/E2E、PR/Review | 红灯阻断发布再修复 |
| E02 | [Docker](https://docs.docker.com/get-started/) · [Nginx](https://nginx.org/en/docs/) | Dockerfile/Compose/Network、TLS/反代 | 冷部署、备份恢复/回滚 |
| E03 | [OWASP API Security](https://owasp.org/API-Security/) · [Spring Security](https://docs.spring.io/spring-security/reference/) | AuthN/AuthZ、OAuth2/OIDC、RBAC/租户安全 | 跨租户读取、过期凭证拒绝 |
| E04 | [OpenTelemetry](https://opentelemetry.io/docs/) · [web.dev](https://web.dev/learn/performance) | TraceContext、Metrics、日志关联、Web Vitals | 链路慢点定位与P95复测 |
| P01 | [GitHub Issues](https://docs.github.com/en/issues) · [Dev-Workbench产品指南](https://github.com/Xander-Xai/X-SuperPlay-Dev-Workbench/blob/main/docs/learning/PRODUCT-GUIDES.md) | User Story、验收条件、负例/边界 | 真实需求AC可测 |
| P02 | [Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/) · [C4 Model](https://c4model.com/) | 组件边界、部署边界、ADR | 模块化单体与服务拆分取舍 |
| P03 | [GitHub Actions/Deployments](https://docs.github.com/en/actions) · [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | 发布审批、UAT、回滚、监控 | 授权环境部署恢复演练 |
| M01 | [微信小程序官方开发文档](https://developers.weixin.qq.com/miniprogram/dev/framework/) | 组件/生命周期、真机、域名与审核 | 真机弱网与平台限制负例 |
| M02 | [Expo](https://docs.expo.dev/) · [Flutter](https://docs.flutter.dev/) | 两种路线择一，设备权限/离线/商店发布 | 模拟器/真机启动与断网 |
| A01 | [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview) · [OpenAI Platform](https://platform.openai.com/docs/overview) | 状态/工具契约、评测/权限、人工介入/降级 | 实际业务工具失败/评测回归 |
| P04 | [Stripe Payments](https://docs.stripe.com/payments) · [Stripe Webhooks](https://docs.stripe.com/webhooks) | 沙箱、签名、幂等回调/对账 | 重复Webhook/虚假金额拒绝 |

**注意**：Stripe是供应商文档示例，不代表国内支付平台的操作规范；微信/Apple/Google审核与具体监管要求需要按目标市场、平台和上线时有效规则另行核对。上游私人知识仓不应复制全文到本公开仓。

## 四、将“看资料”变成“学会”的最小规范

每一知识点都填写 [Gap学习会话卡](GAP-SESSION-TEMPLATE.md)：
```text
需求 → 缺口节点 → 为什么要用这项技术 → 与邻接节点关系
→ 官方某一章节 + 版本/阅读小节 → 自己实现/测试
→ 一项失败注入 → 解释根因/取舍 → 回到项目交付
```

阅读官方文档的目的不是收藏数量，而是能回答：它负责哪一层、与上下层怎样交互、什么时候不该用、怎样用失败测试证明理解。


## V4.1：上游补充的前后端、跨端与其他语言官方直达资源

> 节点编号与[知识图JSON](knowledge-map.json)一一对应。**官方原理**负责定义，**上游资料**负责已有讲解/实验入口，**本次需求**决定要不要实践。原W坐标不新增强制周次。

| ID | 官方资料（准确入口） | 专业核心 / 阅读小节 | 参考的最小实验 |
|---|---|---|---|
| F08 | [官方文档](https://vuejs.org/guide/introduction) · [上游相关讲解](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/knowledge/software-engineering/programming-language-stack-map.md) | Vue的Composition API、ref/reactive/watch/路由与前端状态 | Vue列表请求逆序、watch清理、键盘可用表单 |
| F09 | [官方文档](https://learn.nuxt.com/en/concepts/rendering-modes) · [上游相关讲解](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/knowledge/software-engineering/programming-language-stack-map.md) | Vue生态的全栈路由、SSR/CSR/Hybrid、数据与缓存边界 | 比较Nuxt服务端/浏览器HTML和hydration行为 |
| F10 | [官方文档](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Offline_and_background_operation) · [上游相关讲解](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/career/opc-multiplatform-product-engineer-roadmap-20261028.md) | 离线缓存、浏览器生命周期、资源与业务数据缓存边界 | 断网后受控读缓存，登录切换时不泄露他人数据 |
| F11 | [官方文档](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) · [上游相关讲解](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/enterprise-ai-application-capstone.md) | 区分HTTP轮询、SSE单向事件、WebSocket双向连接和断线策略 | 模拟断开重连、消息乱序和发送速度超过消费速度 |
| B07 | [官方文档](https://docs.nestjs.com/first-steps) · [上游相关讲解](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/knowledge/software-engineering/programming-language-stack-map.md) | Node运行时上的Controller/服务/依赖注入/API架构 | 做Nest/Express最小CRUD并验证400/401/500及进程重启 |
| B08 | [官方文档](https://go.dev/learn/) · [上游相关讲解](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/knowledge/software-engineering/programming-language-stack-map.md) | Go编译/模块/interface/goroutine/context与HTTP服务 | 写最小HTTP服务并复现取消上下文/并发数据竞争 |
| B09 | [官方文档](https://doc.rust-lang.org/stable/book/) · [上游相关讲解](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/knowledge/software-engineering/programming-language-stack-map.md) | 原生模块、内存与并发安全、推理/性能约束下的系统编程 | 独立原生小程序或Rust CLI；仅有目标瓶颈才做CUDA/C++对照 |
| D05 | [官方文档](https://www.postgresql.org/docs/current/textsearch.html) · [上游相关讲解](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/enterprise-ai-application-capstone.md) | 文件、业务数据、全文检索与向量检索的不同存储责任 | 文件元数据与原始对象分离，比较文本与向量召回负例 |
| E05 | [官方文档](https://vite.dev/guide/) · [上游相关讲解](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/knowledge/software-engineering/programming-language-stack-map.md) | JS构建、Python依赖/虚拟环境、JVM JAR、Go/Rust二进制的区别 | 对比npm build、Python安装/启动、Maven打包与实际进程 |
| M03 | [官方文档](https://www.electronjs.org/docs/latest/tutorial/process-model) · [上游相关讲解](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/career/opc-multiplatform-product-engineer-roadmap-20261028.md) | 桌面Web视图、系统API、主/渲染进程或Rust命令与安全边界 | 做本地文件对话框并拒绝未授权的任意文件路径访问 |
| M04 | [官方文档](https://uniapp.dcloud.net.cn/) · [上游相关讲解](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/ai-native-multiplatform-track.md) | 基于Vue的多端页面抽象与目标平台API/审核差异 | 同一受控页面在H5与小程序目标环境运行并对照行为 |
| M05 | [官方文档](https://developer.android.com/jetpack/compose) · [上游相关讲解](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/career/opc-multiplatform-product-engineer-roadmap-20261028.md) | Kotlin/Jetpack Compose或Swift/SwiftUI的设备与原生SDK能力 | Android原生权限负例或有授权设备的iOS构建演示 |
| A02 | [官方文档](https://modelcontextprotocol.io/docs/learn/architecture) · [上游相关讲解](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/enterprise-ai-application-capstone.md) | MCP工具/资源/提示的客户端服务端约定，区分REST和A2A | 最小MCP工具定义+非法参数/拒绝未授权调用 |

特别注意：官网文档内容可能随版本变化；实现前固定相应运行时/框架版本，并在实际使用时复核完整章节。这里的入口已按官方站点和上游文件核验，但**没有在本地安装所有框架或运行全部扩展实验**。
