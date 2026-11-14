# 2026细节补漏索引｜不创建新节点或重复教程

> 依据新增“2026全栈学习路线”审查已存在的[42节点专业卡](NODE-STUDY-CARDS.md)和[ROADMAP](../../ROADMAP.md)。下面只强调原资料中**散落或表达不够显式的高频细节**，每行指向既有节点、权威小节和最小故障实验。**不会因清单多就要求全部学完**。

## 高频细节、所属层与可以动手的负例

| 层 | 现有节点 | 补充知识点 | 专业重点（避免误解） | 需求触发后的最小实操 | 权威资料 |
|---|---|---|---|---|---|
| Web与浏览器 | F01 | DNS/TCP/TLS、HTTP/2/3、连接复用 | 一条请求的DNS/TLS不一定每次重走；区分浏览器连接复用与缓存 | DevTools看首次和二次访问瀑布 | [官方/权威](https://developer.mozilla.org/en-US/docs/Web/Performance/How_browsers_work) |
| Web与浏览器 | F01 | Cookie/Session/JWT/刷新与撤销 | Cookie载体≠Session状态≠JWT声明；JWT签名≠加密，资源权限仍由服务端查 | 会话失效和Token重放负例 | [官方/权威](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/) |
| Web与浏览器 | F01 | SameSite、CSRF、CORS、Preflight | CORS限制浏览器跨源读取，与授权不是一回事；SameSite不是无条件CSRF免疫 | 模拟预检、跨域带凭证失败及CSRF校验 | [官方/权威](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS) |
| Web与浏览器 | F01 | localStorage/sessionStorage/IndexedDB/Cookie | 客户端储存生命周期、容量、同源和脚本访问差异；敏感会话勿随意长期存localStorage | 切换账号确认私有缓存不会跨用户泄露 | [官方/权威](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API) |
| Web与浏览器 | F01 | Cache-Control/ETag/CDN | 强缓存/协商缓存和CDN边缘缓存要区分，用户私有响应应谨慎缓存 | 改变ETag与Cache-Control观察304和缓存命中 | [官方/权威](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching) |
| 前端基础 | F02 | 语义HTML/表单/键盘/响应式 | 按钮、label、focus、盒模型、Flex/Grid、断点和语义影响操作体验和无障碍 | 手机窄屏与键盘Tab独立完成表单 | [官方/权威](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/HTML_forms) |
| 前端基础 | F03 | JS原型链/this/闭包/事件委托 | 对象原型委托、this绑定与词法闭包属于不同机制 | 事件监听器this和箭头函数的行为对照 | [官方/权威](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Inheritance_and_the_prototype_chain) |
| 前端基础 | F03 | Event Loop/任务/微任务/Promise | 异步回调排序由事件循环和任务/微任务规则影响，不等同于网络完成顺序 | 用queueMicrotask/Promise/setTimeout记录顺序 | [官方/权威](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Event_loop) |
| 前端基础 | F03 | TS Utility Types、泛型、类型收窄 | Partial/Pick/Omit/Record等只在静态类型层工作，后端JSON需要运行时Schema验证 | 故意改变响应类型，使TS检查失败并用运行时验证补充 | [官方/权威](https://www.typescriptlang.org/docs/handbook/utility-types.html) |
| 前端工程 | F04 | Render/Commit、key、状态快照 | 父子组件身份、稳定key和状态快照决定状态保留，不能靠背Hooks名字 | 错误索引key造成编辑状态错位后修复 | [官方/权威](https://react.dev/learn/preserving-and-resetting-state) |
| 前端工程 | F04 | Effect清理、StrictMode及无效Effect | Effect连接外部系统而不是替代事件处理或派生计算；使用Query管理服务器状态 | 快速切换条件时旧响应不可覆盖新状态 | [官方/权威](https://react.dev/learn/you-might-not-need-an-effect) |
| 前端工程 | F04 | React Router/TanStack Query/Zustand | 路由URL、服务端缓存与轻量客户端共享状态是三种不同问题；Zustand不是所有项目必需 | 查询分页/删除后失效缓存；局部状态无需全局库 | [官方/权威](https://tanstack.com/query/latest/docs/framework/react/overview) |
| 前端工程 | F05 | CSR/SSR/SSG/ISR、Next App Router | 渲染时机/缓存再验证/服务端和客户端组件边界，不能把SSR当性能万灵药 | 比较原始HTML，模拟私有缓存和hydration失败 | [官方/权威](https://nextjs.org/docs/app/getting-started/server-and-client-components) |
| 前端工程 | F07 | npm/pnpm、Vite、lint、构建与环境变量 | 依赖锁定、构建产物和客户端环境变量暴露边界，不能把密钥放前端bundle | 检查构建产物中是否泄漏模拟secret | [官方/权威](https://vite.dev/guide/env-and-mode) |
| API工程 | B01 | REST语义、分页/过滤/幂等、OpenAPI | GET幂等但不保证可安全重复POST；响应状态和契约需要语义一致 | 改后端字段→重新生成客户端→类型与集成检查 | [官方/权威](https://spec.openapis.org/oas/latest.html) |
| API工程 | B02 | FastAPI Depends/Router-Service-Repository | 依赖对象生命周期、路由和服务职责、数据库Session边界，不机械多拆层 | 替换Repository不改对外契约，坏输入返回准确状态 | [官方/权威](https://fastapi.tiangolo.com/tutorial/bigger-applications/) |
| API工程 | B02 | FastAPI认证、JWT与密码哈希 | 密码安全存储、Claims验证与资源级授权不是同一层 | 伪造/过期token、用户B访问用户A资源 | [官方/权威](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/) |
| API工程 | B02 | async/await、线程/进程、阻塞与超时 | 协作式I/O非CPU并行，CPU或同步IO阻塞事件循环 | 故意注入time.sleep/CPU循环并测并发延迟 | [官方/权威](https://fastapi.tiangolo.com/async/) |
| API工程 | D05 | 上传/下载、对象存储/配额/病毒与越权 | 前端MIME检查不可替代服务端大小、内容、对象归属与下载授权 | 跨租户下载对象、超大文件上传/类型伪造 | [官方/权威](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html) |
| 数据 | D01 | JOIN/CTE/窗口函数、索引/EXPLAIN | 复杂SQL与执行计划/选择性互相联系，索引不是越多越好 | 构造查询并用EXPLAIN ANALYZE前后对照 | [官方/权威](https://www.postgresql.org/docs/current/using-explain.html) |
| 数据 | D01 | ORM N+1、Lazy loading、Session生命周期 | 一个列表主查询可能触发N次关联SQL，且Session关闭后惰性访问失败 | 记录SQL次数并批量加载优化 | [官方/权威](https://docs.sqlalchemy.org/en/20/orm/queryguide/relationships.html) |
| 数据 | D01 | 迁移、外键/唯一/事务、并发写入 | 数据正确性来自DB约束与事务边界，不依赖前端禁止重复点击 | 双连接并发扣减、唯一键冲突与rollback | [官方/权威](https://www.postgresql.org/docs/current/transaction-iso.html) |
| 数据 | D02 | Redis数据结构、缓存击穿/雪崩 | TTL、热点Key、缓存失效/重建和DB回源是性能与一致性取舍 | 模拟统一过期和随机TTL、记录回源并发 | [官方/权威](https://redis.io/docs/latest/) |
| 工程安全 | E02 | Linux进程/端口/systemd/SSH/日志 | 系统服务生命周期、网络暴露、用户/组权限和容器边界需分清 | 故障注入进程退出、systemd重启及端口检查 | [官方/权威](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html) |
| 工程安全 | E02 | Docker/Compose/Volume、Nginx/TLS | 镜像/容器/卷、反代、TLS终止及密钥管理均影响可复现交付 | 删容器恢复数据、测试反代超时与不公开DB端口 | [官方/权威](https://docs.docker.com/compose/) |
| 工程安全 | E01 | Pytest/Vitest/Playwright的测试层次 | 单元测试关注局部规则、集成验证数据库/API、E2E验证真实操作与隔离 | 在授权测试环境创建A/B用户，E2E拒绝越权，失败阻断CI | [官方/权威](https://playwright.dev/docs/writing-tests) |
| 工程安全 | E03 | XSS/CSRF/SQL注入/SSRF/IDOR | Web和API安全分别涉及用户输入、Cookie、服务端网络访问与资源授权 | 权限绕过/SSRF白名单/SQL参数化负例，禁止接触生产 | [官方/权威](https://owasp.org/API-Security/editions/2023/en/0x00-header/) |
| 工程安全 | E04 | Logs/Metrics/Trace与P50/P95/P99 | 分位数受负载/样本影响，Request ID日志关联不是W3C traceparent | 慢SQL注入、错误率/吞吐与P95优化前后对照 | [官方/权威](https://opentelemetry.io/docs/) |
| 工程安全 | P03 | 发布、迁移、备份、恢复、回滚 | 镜像回滚和数据库Schema回滚并不等价，恢复必须真实演练 | 新旧代码Schema兼容/恢复时间与数据损失界限测试 | [官方/权威](https://docs.github.com/en/actions) |
| Java专项 | B03/B04/B05 | Java/JVM/Maven→Spring IoC/MVC/Security/Data | 按JD选择Java服务路线；既有FastAPI业务可做同一API Java对照 | Spring Controller+MockMvc、事务/授权负例，非自动必修 | [官方/权威](https://spring.io/guides/gs/rest-service/) |

## 遇到真实需求时怎样选一行，而不是机械学习30行

- **浏览器登录过期**：先F01/E03的Cookie/Session/JWT，读对应官方安全章节，做过期+撤销负例；不必先学全部CSS。
- **React列表旧数据覆盖**：先F03/F04的事件循环和Effect/Query状态；直接跑[请求竞态测试](labs/README.md)再回当前项目。
- **Spring岗位**：先B03/B04最低Java语法与Spring MVC，事务/安全问题出现时B05/D01；不要求先把Next部署一遍。
- **用户要上线静态工具**：F02/F03/U01/E01/E02只做相关发布、安全和监测门禁；不强制Redis、Celery或RAG。
- **PDF任务未更新进度**：先B06/F11区分Worker业务状态与SSE连接；再查D01的任务持久状态，按[交付案例](DELIVERY-LIFECYCLE.md)做隔离实验。

**资料状态**：这里列的是学习资源、实验设计；不存在“逐个读过、做过或已通过”结论。个人完成证据仅登记[PROGRESS](PROGRESS.md)。外部文档上线/变更应在使用时复核版本。
