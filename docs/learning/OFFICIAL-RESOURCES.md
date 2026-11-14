# 全栈官方学习资料｜42核心节点 + 17横向专题

> 横向基础的17个官方/权威原文及负例，统一在[横向基础学习卡](CROSS-CUTTING-FOUNDATIONS.md)与[机器索引](cross-cutting-topics.json)中维护；本文件继续承载42核心节点，不复制第二份URL列表。

> 使用方式：只在当前需求卡上打开1–3个相关章节；不仅收藏网址，还要用[节点学习卡](NODE-STUDY-CARDS.md)的实验检验。页面是否可打开及特定API版本需开始开发时再复核。部分官方教程有平台、版本、硬件/账号限制；**文档存在不等于代码实测**。

## 需求/系统设计

| 节点 | 官方资料直达 | 本次应关注的专业章节 | 上游材料 | 正负例实验 |
|---|---|---|---|---|
| P01 业务需求/验收 | [官方精确小节](https://docs.github.com/en/issues/tracking-your-work-with-issues/learning-about-issues/about-issues) | Issues / User story / Acceptance criteria | [现有参考资料](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/career/market-to-lab-loop.md) | 需求被取消、无权限用户查看、弱网时也要有预期行为。 |
| P02 架构与技术取舍 | [官方精确小节](https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/) | Architecture styles / bounded contexts | [现有参考资料](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/career/ai-product-engineer-roadmap-20261028.md) | 一次跨模块事务失败时归谁回滚？ |
| P03 生产发布/运营 | [官方精确小节](https://docs.github.com/en/actions) | GitHub Actions / deployments | [现有参考资料](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/career/opc-multiplatform-product-engineer-roadmap-20261028.md) | 错误迁移、资源用量异常、回滚后数据版本不兼容。 |
| P04 支付/订阅 | [官方精确小节](https://docs.stripe.com/webhooks) | Stripe webhook signing / idempotency | [现有参考资料](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/labs/freelance-proof-20261025/README.md) | 伪造回调、重复通知、回调乱序/退款。 |

## Web/前端/工具站

| 节点 | 官方资料直达 | 本次应关注的专业章节 | 上游材料 | 正负例实验 |
|---|---|---|---|---|
| F01 Web/HTTP/浏览器 | [官方精确小节](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview) | HTTP overview / CORS / Fetch | [现有Track](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/ai-native-fullstack-track.md) | 断网、超时、跨域预检失败与HTTP 500分别是什么？ |
| F02 HTML/CSS/无障碍 | [官方精确小节](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility) | HTML forms / CSS layout / Accessibility | [现有Track](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/ai-native-fullstack-track.md) | 缩放到200%、Tab导航、无标签输入时会怎样？ |
| F03 JavaScript/TypeScript | [官方精确小节](https://www.typescriptlang.org/docs/handbook/2/narrowing.html) | JavaScript execution model / TypeScript narrowing | [现有参考资料](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/knowledge/software-engineering/programming-language-stack-map.md) | 旧请求最后返回是否覆盖新数据？运行时类型不符怎么办？ |
| F04 React/状态 | [官方精确小节](https://react.dev/learn/state-as-a-snapshot) | State as a snapshot / Effects | [现有Track](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/ai-native-fullstack-track.md) | StrictMode重复effect、切换查询导致旧数据、401后的UI状态。 |
| F05 Next.js/SSR | [官方精确小节](https://nextjs.org/docs/app/getting-started/server-and-client-components) | Server and Client Components | [现有参考资料](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/knowledge/software-engineering/programming-language-stack-map.md) | 服务端读取浏览器API、缓存错配、用户私有页被公开缓存。 |
| F06 Node.js/Streams | [官方精确小节](https://nodejs.org/en/learn/asynchronous-work/event-loop-timers-and-nexttick) | Event loop / Streams | [现有参考资料](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/knowledge/software-engineering/programming-language-stack-map.md) | 同步CPU循环时多个HTTP请求排队，断连后资源能否释放？ |
| F07 构建与前端性能 | [官方精确小节](https://vite.dev/guide/build) | Build for production | [现有参考资料](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/knowledge/software-engineering/programming-language-stack-map.md) | 大依赖引入后bundle暴涨、懒加载资源404时如何回退？ |
| F08 Vue 3/响应式/状态 | [官方精确小节](https://vuejs.org/guide/essentials/watchers.html) | Vue Watchers / Cleanup | [现有Track](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/ai-native-fullstack-track.md) | A请求慢于B，A最后响应但不能覆盖B的视图。 |
| F09 Nuxt/SSR与混合渲染 | [官方精确小节](https://learn.nuxt.com/en/concepts/rendering-modes) | Nuxt rendering modes | [现有参考资料](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/knowledge/software-engineering/programming-language-stack-map.md) | 服务端误用window、登录信息被缓存、hydration不一致。 |
| F10 PWA/Service Worker/浏览器存储 | [官方精确小节](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Offline_and_background_operation) | Offline and background operations | [现有参考资料](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/sources/ai-native-multiplatform-research-20261028.md) | 离线更新陈旧、登录态切换、缓存占用。 |
| F11 SSE/WebSocket/实时连接 | [官方精确小节](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events) | Using server-sent events / WebSockets | [现有LAB](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB02.md) | 流被任意拆块、断线丢事件、慢接收端、代理缓冲。 |
| U01 静态工具站/SEO | [官方精确小节](https://web.dev/learn/seo) | Learn SEO / metadata | [现有参考资料](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/sources/ai-native-multiplatform-research-20261028.md) | 离线加载、恶意输入、robots误禁收录。 |

## 后端/数据

| 节点 | 官方资料直达 | 本次应关注的专业章节 | 上游材料 | 正负例实验 |
|---|---|---|---|---|
| B01 REST/OpenAPI | [官方精确小节](https://spec.openapis.org/oas/latest.html) | OpenAPI specification / Schema | [现有LAB](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB02.md) | 后端删除字段，前端未重新生成仍能编译说明什么？ |
| B02 Python/FastAPI | [官方精确小节](https://fastapi.tiangolo.com/tutorial/dependencies/) | Dependencies / Request body / Testing | [现有LAB](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB02.md) | 跨租户IDOR、非法JSON、依赖服务断线、阻塞调用。 |
| B03 Java/JVM | [官方精确小节](https://dev.java/learn/) | Classes / Generics / Concurrency | [现有LAB](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB14.md) | 两个线程并发修改HashMap/共享计数器会怎样？ |
| B04 Spring Boot/MVC | [官方精确小节](https://docs.spring.io/spring-boot/reference/web/servlet.html) | Servlet web applications / Spring MVC | [现有LAB](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB14.md) | Bean循环依赖、校验失败、没有权限的订单访问。 |
| B05 Spring Data/Security | [官方精确小节](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html) | Authorize HTTP requests / Method Security | [现有LAB](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB14.md) | 仅检查已登录但不检查资源拥有者，是否能跨用户读取？ |
| B06 Celery/后台任务可靠性 | [官方精确小节](https://docs.celeryq.dev/en/stable/userguide/tasks.html) | Celery tasks / acks_late / worker lost | [现有LAB](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB02.md) | 重复提交、Worker崩溃和重放是否造成重复扣费？ |
| B07 Node后端/NestJS/Express | [官方精确小节](https://docs.nestjs.com/controllers) | NestJS Controllers / Providers / Guards | [现有参考资料](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/knowledge/software-engineering/programming-language-stack-map.md) | Pipe校验缺失、服务异常变500、请求上下文丢失。 |
| B08 Go服务与并发 | [官方精确小节](https://go.dev/learn/) | Go official tutorials / context | [现有参考资料](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/knowledge/software-engineering/programming-language-stack-map.md) | context已取消但goroutine仍跑、数据竞争。 |
| B09 Rust/C++/CUDA原生能力 | [官方精确小节](https://doc.rust-lang.org/stable/book/) | The Rust Book / NVIDIA CUDA programming guide | [现有参考资料](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/knowledge/software-engineering/programming-language-stack-map.md) | 内存错误、并发悬挂、无GPU时不得宣称CUDA实测。 |
| D01 PostgreSQL/SQL | [官方精确小节](https://www.postgresql.org/docs/current/transaction-iso.html) | Transaction isolation / EXPLAIN | [现有LAB](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB08.md) | 丢失更新、死锁、超扣和读已提交下的异常。 |
| D02 Redis/缓存 | [官方精确小节](https://redis.io/docs/latest/) | Redis documentation / cache patterns | [现有LAB](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB08.md) | 缓存击穿、读到旧值、重建锁过期时如何避免覆盖？ |
| D03 消息/Outbox | [官方精确小节](https://www.rabbitmq.com/docs/queues) | RabbitMQ queues / Publisher confirms | [现有Track](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/enterprise-ai-application-capstone.md) | 重复消息、消费者掉线、发布成功但ACK丢失。 |
| D04 MySQL差异 | [官方精确小节](https://dev.mysql.com/doc/refman/8.4/en/innodb-transaction-isolation-levels.html) | InnoDB transaction isolation levels | [现有参考资料](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/knowledge/software-engineering/programming-language-stack-map.md) | 幻读/间隙锁、死锁回滚、索引失效。 |
| D05 对象存储/全文搜索/向量数据库 | [官方精确小节](https://www.postgresql.org/docs/current/textsearch.html) | PostgreSQL Full Text Search / S3 / Milvus | [现有LAB](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB03.md) | 删除后仍可检索、未授权用户能读对象、索引更新滞后。 |

## 工程/安全/运营

| 节点 | 官方资料直达 | 本次应关注的专业章节 | 上游材料 | 正负例实验 |
|---|---|---|---|---|
| E01 Git/测试/CI | [官方精确小节](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions) | Workflow syntax / Actions | [现有LAB](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB11.md) | 测试仅覆盖快乐路径、依赖未锁、并行污染。 |
| E02 Docker/Linux/部署 | [官方精确小节](https://docs.docker.com/compose/) | Docker Compose overview | [现有LAB](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB11.md) | 丢环境变量/数据卷、HTTPS证书过期、反代超时。 |
| E03 身份/权限/多租户 | [官方精确小节](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) | Authorization cheat sheet / Broken object-level authorization | [现有LAB](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB09.md) | 横向越权、CSRF、过期会话、泄露私有资源。 |
| E04 Trace/性能/排障 | [官方精确小节](https://www.w3.org/TR/trace-context/) | W3C Trace Context specification | [现有LAB](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB07.md) | span未传播、时钟/采样设置不匹配、错误率被平均值掩盖。 |
| E05 编译/构建/打包/运行时 | [官方精确小节](https://maven.apache.org/guides/getting-started/index.html) | Maven Getting Started / Vite build | [现有参考资料](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/knowledge/software-engineering/programming-language-stack-map.md) | 依赖未锁、目标系统架构不匹配、发布后环境变量缺失。 |

## 跨端/AI

| 节点 | 官方资料直达 | 本次应关注的专业章节 | 上游材料 | 正负例实验 |
|---|---|---|---|---|
| M01 微信小程序 | [官方精确小节](https://developers.weixin.qq.com/miniprogram/dev/framework/) | Mini Program framework | [现有Track](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/ai-native-multiplatform-track.md) | 未配置域名、授权失败、后台切换导致状态丢失。 |
| M02 移动App | [官方精确小节](https://docs.expo.dev/) | Expo documentation / Flutter | [现有参考资料](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/assessments/ai-native-multiplatform-rubric.md) | 手机锁屏/断网、缓存泄漏、Android/iOS行为差异。 |
| M03 Electron/Tauri桌面应用 | [官方精确小节](https://www.electronjs.org/docs/latest/tutorial/process-model) | Electron process model | [现有参考资料](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/career/opc-multiplatform-product-engineer-roadmap-20261028.md) | 渲染进程任意调用文件API、跨目录路径遍历。 |
| M04 uni-app/跨端小程序生态 | [官方精确小节](https://uniapp.dcloud.net.cn/) | uni-app official tutorial | [现有Track](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/ai-native-multiplatform-track.md) | 不支持的组件/插件、登录或支付SDK差异。 |
| M05 Android/iOS原生开发 | [官方精确小节](https://developer.android.com/jetpack/compose) | Android Jetpack Compose / Apple SwiftUI | [现有参考资料](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/career/opc-multiplatform-product-engineer-roadmap-20261028.md) | 权限拒绝、应用被系统回收、离线回放。 |
| A01 AI/RAG/Agent | [官方精确小节](https://docs.langchain.com/oss/python/langgraph/overview) | LangGraph overview / tool calling | [现有Track](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/enterprise-ai-application-capstone.md) | 提示注入、工具重复调用、幻觉引用与成本超标。 |
| A02 MCP工具接口/Agent协议 | [官方精确小节](https://modelcontextprotocol.io/specification/2026-07-28/architecture) | MCP 2026-07-28 architecture | [现有LAB](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB06.md) | 工具声明与实际权限不一致、无害请求被赋予写权限。 |

## 混合节点的权威资料分工

- **B05** Spring Data [数据存取/事务](https://docs.spring.io/spring-data/jpa/reference/) 与 Spring Security [权限判断](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html)各看对应部分，不能将ORM和AuthN/AuthZ视为同一层。
- **B09** Rust [官方书](https://doc.rust-lang.org/stable/book/)、C++ [标准/社区参考](https://en.cppreference.com/w/)、CUDA [NVIDIA编程指南](https://docs.nvidia.com/cuda/cuda-c-programming-guide/)分别学习，不把C++参考站误称C++标准官方原始标准。
- **D05** 对象存储 [Amazon S3官方指南](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)、全文检索 [PostgreSQL](https://www.postgresql.org/docs/current/textsearch.html)、向量检索 [Milvus](https://milvus.io/docs/overview.md)分别学习；权限须回到API/ACL边界。
- **M05** Android [Google Compose](https://developer.android.com/jetpack/compose) 与 iOS [Apple SwiftUI](https://developer.apple.com/tutorials/swiftui)各是独立SDK方向，不要求先学Expo。
- **F11** SSE [MDN Server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events) 与 WebSocket [MDN WebSocket](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)分别确认重连、方向与可靠性。
- **A02** MCP应固定规范版本。本轮阅读[2026-07-28架构](https://modelcontextprotocol.io/specification/2026-07-28/architecture)，不能直接套用旧版有状态会话假设。

## 可核对的来源边界

官方页优先；[上游20+资料汇总](UPSTREAM-ASSET-INDEX.md)是学习导航，不是全都可运行的课程。直达链接的**语义有效性**还要在当前项目选技术时确认其版本、平台与目标章节；CI离线只能做静态结构检查，不能保证第三方站点永远可访问。

