# 全栈42个核心知识点｜专业定义 × 大白话 × 故障实验

> **还须了解通用工程横向基础**：[17专题：命令行/算法/调试、UX/国际化、安全/数据生命周期、SLO/配置](CROSS-CUTTING-FOUNDATIONS.md)。42核心节点与X01–X17横向细分共用一套[需求路由](DEMAND-ROUTER.md)与[学习证据](PROGRESS.md)，不新增强制周数。

> **知识地图不是必修日历。** 学习从[当前真实需求](DEMAND-ROUTER.md)进入，先读[全景图](FULLSTACK-MENTAL-MODEL.md)，只选当前所需的节点。旧W1–W24仍是历史覆盖坐标，不是学习进度；实验是否实际通过，以[PROGRESS](PROGRESS.md)的个人证据为准。

## 关系规则

**最低先修**仅表示理解本技术时需要的概念；**平行替代**如Vue/React、FastAPI/Spring/NestJS，依业务选主栈而非全学；**跨层协作**指浏览器、HTTP、API、DB、异步、鉴权、部署的真实接口关系。

## 需求与产品

### P01 · 业务需求/验收

**专业定义**：把用户问题转换为可验证功能、非功能约束和验收条件的需求工程。

**核心机制**：用户故事→输入/输出→边界/反例→可运行验收，而不是直接指定框架。

**大白话类比**：先写清楚要修哪条路、为什么，才知道买什么工具。

**类比不适用的边界**：需求假设不等于真实用户证据；AI写出的PRD未经用户认可不算真实需求。

**与其他知识的关系**：最低概念先修：无；历史知识坐标 W24；相关验收分类 G12、G24，不强制按序通过。

**官方阅读**：[准确专题入口](https://docs.github.com/en/issues/tracking-your-work-with-issues/learning-about-issues/about-issues) — 先看 **Issues / User story / Acceptance criteria**。[基础文档](https://docs.github.com/en/issues)。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/career/market-to-lab-loop.md) · [资料2](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/prompts/business-demand-learning/v1.0.0/01-business-demand-to-learning-goals.md)。来源性质：学习方法论（非技术实训）。

**最小亲手实验**：写一个已有工单列表的3条AC和2条异常场景，并以测试或手工UAT执行。

**故障/反例**：需求被取消、无权限用户查看、弱网时也要有预期行为。

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

### P02 · 架构与技术取舍

**专业定义**：按业务能力和变化频率划分模块、边界、数据所有权与技术选型的系统设计。

**核心机制**：需求/质量属性→模块边界→API/数据流→ADR→验证假设。

**大白话类比**：给厨房分工，不是每种设备都买一遍。

**类比不适用的边界**：架构图不等于部署事实，微服务也不是默认更先进。

**与其他知识的关系**：最低概念先修：P01（业务需求/验收）；历史知识坐标 W24；相关验收分类 G12、G24，不强制按序通过。

**官方阅读**：[准确专题入口](https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/) — 先看 **Architecture styles / bounded contexts**。[基础文档](https://learn.microsoft.com/en-us/azure/architecture/)。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/career/ai-product-engineer-roadmap-20261028.md)。来源性质：概念综述（非可运行教程）。

**最小亲手实验**：给同一工单需求画模块化单体和双服务图并用变更成本对比。

**故障/反例**：一次跨模块事务失败时归谁回滚？

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

### P03 · 生产发布/运营

**专业定义**：生产发布包括用户验收、变更审批、健康监控、回滚、成本与灾备责任。

**核心机制**：需求验收→风险评估→staging→发布→监控→恢复/撤销。

**大白话类比**：不是把饭菜送出厨房就完事，还要知道能否服务顾客和出现投诉如何处理。

**类比不适用的边界**：学习仓CI绿不等于生产发布授权或客户验收。

**与其他知识的关系**：最低概念先修：P01（业务需求/验收）、E01（Git/测试/CI）；历史知识坐标 W22、W24；相关验收分类 G11、G23、G24，不强制按序通过。

**官方阅读**：[准确专题入口](https://docs.github.com/en/actions) — 先看 **GitHub Actions / deployments**。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/career/opc-multiplatform-product-engineer-roadmap-20261028.md)。来源性质：概念综述（非可运行教程）。

**最小亲手实验**：在隔离环境执行部署、打回滚版本、恢复数据库并记录RTO。

**故障/反例**：错误迁移、资源用量异常、回滚后数据版本不兼容。

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

### P04 · 支付/订阅

**专业定义**：支付/订阅是资金状态与异步回调的持久业务流程，须验签和幂等对账。

**核心机制**：建单→平台支付→签名Webhook→幂等状态更新→退款/对账。

**大白话类比**：账本确认到账才能发货，不能凭页面说支付成功。

**类比不适用的边界**：Stripe只是供应商示例，国内平台需按实际支付服务商规则实现。

**与其他知识的关系**：最低概念先修：B01（REST/OpenAPI）、E03（身份/权限/多租户）；历史知识坐标 W24；相关验收分类 G21、G22、G24，不强制按序通过。

**官方阅读**：[准确专题入口](https://docs.stripe.com/webhooks) — 先看 **Stripe webhook signing / idempotency**。[基础文档](https://docs.stripe.com/payments)。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/labs/freelance-proof-20261025/README.md)。来源性质：概念综述（非可运行教程）。

**最小亲手实验**：沙箱重复Webhook与恶意金额测试，验证不重复开通。

**故障/反例**：伪造回调、重复通知、回调乱序/退款。

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

## Web、前端和浏览器

### F01 · Web/HTTP/浏览器

**专业定义**：浏览器与服务端通过HTTP等协议交换表示，并受同源、缓存、Cookie等Web平台约束。

**核心机制**：URL→DNS/TLS→请求/响应→状态码与缓存→CORS/凭证/重试。

**大白话类比**：外卖订单从地址、保密运输到收件回执的一套规矩。

**类比不适用的边界**：CORS是浏览器策略而非服务端鉴权；请求ID不是Trace。

**与其他知识的关系**：最低概念先修：无；历史知识坐标 W01、W05；相关验收分类 G01、G08，不强制按序通过。

**官方阅读**：[准确专题入口](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview) — 先看 **HTTP overview / CORS / Fetch**。[基础文档](https://developer.mozilla.org/en-US/docs/Web/HTTP)。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/ai-native-fullstack-track.md)。来源性质：课程/场景说明（非实测）。

**最小亲手实验**：DevTools观察GET/POST、401、缓存和跨域预检，并手写取消请求。

**故障/反例**：断网、超时、跨域预检失败与HTTP 500分别是什么？

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

### F02 · HTML/CSS/无障碍

**专业定义**：HTML语义结构、CSS盒模型/布局与可访问性共同决定Web页面的结构、显示和可操作性。

**核心机制**：DOM语义→CSS流式布局/Flex/Grid→响应式→键盘焦点与语义。

**大白话类比**：骨架、装修和让所有人都能找到门把手的设计。

**类比不适用的边界**：只看桌面截图不能证明移动端、键盘和读屏可用。

**与其他知识的关系**：最低概念先修：无；历史知识坐标 W02、W14；相关验收分类 G01、G17，不强制按序通过。

**官方阅读**：[准确专题入口](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility) — 先看 **HTML forms / CSS layout / Accessibility**。[基础文档](https://developer.mozilla.org/en-US/docs/Learn_web_development)。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/ai-native-fullstack-track.md)。来源性质：课程/场景说明（非实测）。

**最小亲手实验**：做可用键盘导航的登录表单和响应式表格，使用浏览器a11y检查。

**故障/反例**：缩放到200%、Tab导航、无标签输入时会怎样？

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

### F03 · JavaScript/TypeScript

**专业定义**：JS执行模型和TS静态类型系统共同支撑浏览器与Node程序编写。

**核心机制**：词法作用域/闭包→Event Loop/Promise→TS类型收窄/泛型→构建期检查。

**大白话类比**：JS安排每件事什么时候做，TS在开工前帮你核对参数清单。

**类比不适用的边界**：TS类型检查不验证未知HTTP JSON，也不保证异步执行顺序。

**与其他知识的关系**：最低概念先修：无；历史知识坐标 W01、W15；相关验收分类 G01、G18，不强制按序通过。

**官方阅读**：[准确专题入口](https://www.typescriptlang.org/docs/handbook/2/narrowing.html) — 先看 **JavaScript execution model / TypeScript narrowing**。[基础文档](https://www.typescriptlang.org/docs/handbook/)。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/knowledge/software-engineering/programming-language-stack-map.md)。来源性质：概念综述（非可运行教程）。

**最小亲手实验**：手写带AbortController和错误归一化的请求函数；模拟A/B逆序返回。

**故障/反例**：旧请求最后返回是否覆盖新数据？运行时类型不符怎么办？

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

### F04 · React/状态

**专业定义**：React声明式组件树依托状态快照、渲染/提交过程与Hooks管理UI。

**核心机制**：state snapshot→render/commit→effect cleanup→Query缓存/Mutation状态。

**大白话类比**：组件是可复用的柜台部件，状态决定现在应该显示什么。

**类比不适用的边界**：useEffect不是所有网络请求的最佳容器；缓存失效需要显式治理。

**与其他知识的关系**：最低概念先修：F02（HTML/CSS/无障碍）、F03（JavaScript/TypeScript）；历史知识坐标 W02、W16；相关验收分类 G01、G19，不强制按序通过。

**官方阅读**：[准确专题入口](https://react.dev/learn/state-as-a-snapshot) — 先看 **State as a snapshot / Effects**。[基础文档](https://react.dev/learn)。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/ai-native-fullstack-track.md)。来源性质：课程/场景说明（非实测）。

**最小亲手实验**：实现React项目搜索、分页、删除，写竞态与缓存失效测试。

**故障/反例**：StrictMode重复effect、切换查询导致旧数据、401后的UI状态。

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

### F05 · Next.js/SSR

**专业定义**：Next.js基于React提供路由、服务器/客户端组件和服务端功能等应用级约定。

**核心机制**：React组件→Server/Client边界→数据获取/缓存→SSR或预渲染。

**大白话类比**：React负责家具，Next帮你安排房子布局及哪些工作在仓库完成。

**类比不适用的边界**：Server Components不是天然安全授权层；SSR不必然更快且增加运维约束。

**与其他知识的关系**：最低概念先修：F04（React/状态）；历史知识坐标 W17；相关验收分类 G20，不强制按序通过。

**官方阅读**：[准确专题入口](https://nextjs.org/docs/app/getting-started/server-and-client-components) — 先看 **Server and Client Components**。[基础文档](https://nextjs.org/docs/app)。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/knowledge/software-engineering/programming-language-stack-map.md)。来源性质：概念综述（非可运行教程）。

**最小亲手实验**：对比同一列表的Vite SPA和Next服务渲染，记录首包HTML与缓存行为。

**故障/反例**：服务端读取浏览器API、缓存错配、用户私有页被公开缓存。

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

### F06 · Node.js/Streams

**专业定义**：Node.js是运行JS程序的服务器运行时，具有事件循环、Streams和系统API。

**核心机制**：JS执行→libuv/事件循环→流背压→网络/文件IO与错误处理。

**大白话类比**：让同一种语言从网页柜台走进服务器后厨。

**类比不适用的边界**：Node不等于Nest；CPU密集型同步阻塞会影响事件循环。

**与其他知识的关系**：最低概念先修：F03（JavaScript/TypeScript）；历史知识坐标 W18；相关验收分类 G20，不强制按序通过。

**官方阅读**：[准确专题入口](https://nodejs.org/en/learn/asynchronous-work/event-loop-timers-and-nexttick) — 先看 **Event loop / Streams**。[基础文档](https://nodejs.org/en/learn)。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/knowledge/software-engineering/programming-language-stack-map.md)。来源性质：概念综述（非可运行教程）。

**最小亲手实验**：编写Node流式读取文件/API并使用背压处理；注入慢消费者。

**故障/反例**：同步CPU循环时多个HTTP请求排队，断连后资源能否释放？

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

### F07 · 构建与前端性能

**专业定义**：前端构建通过模块依赖处理、优化和产物输出实现可部署资源。

**核心机制**：ESM/import→Vite构建→代码拆分/静态资源→测量页面性能。

**大白话类比**：将开发零件打包成可交付安装箱，不等于箱子能在每台机器上跑。

**类比不适用的边界**：一次构建成功不能证明真实Web Vitals、可访问性与安全。

**与其他知识的关系**：最低概念先修：F03（JavaScript/TypeScript）；历史知识坐标 W15、W16、W23；相关验收分类 G18、G19、G23，不强制按序通过。

**官方阅读**：[准确专题入口](https://vite.dev/guide/build) — 先看 **Build for production**。[基础文档](https://vite.dev/guide/)。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/knowledge/software-engineering/programming-language-stack-map.md)。来源性质：概念综述（非可运行教程）。

**最小亲手实验**：将页面按路由拆包，测构建体积/首屏加载并解释tradeoff。

**故障/反例**：大依赖引入后bundle暴涨、懒加载资源404时如何回退？

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

### F08 · Vue 3/响应式/状态

**专业定义**：Vue3响应式系统通过ref/reactive、computed和watch驱动组件更新。

**核心机制**：响应式依赖→组件更新→watch副作用清理与异步取消。

**大白话类比**：柜台屏幕跟着库存自动变，旧订单回执应作废。

**类比不适用的边界**：watch/onWatcherCleanup受Vue版本与同步注册规则限制；旧响应仍需防污染。

**与其他知识的关系**：最低概念先修：F02（HTML/CSS/无障碍）、F03（JavaScript/TypeScript）；历史知识坐标 W02、W16；相关验收分类 G01、G19，不强制按序通过。

**官方阅读**：[准确专题入口](https://vuejs.org/guide/essentials/watchers.html) — 先看 **Vue Watchers / Cleanup**。[基础文档](https://vuejs.org/guide/introduction)。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/ai-native-fullstack-track.md) · [资料2](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/knowledge/software-engineering/programming-language-stack-map.md)。来源性质：课程/场景说明（非实测）。

**最小亲手实验**：Vue搜索页watch发请求，模拟逆序返回并加入取消/序列保护。

**故障/反例**：A请求慢于B，A最后响应但不能覆盖B的视图。

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

### F09 · Nuxt/SSR与混合渲染

**专业定义**：Nuxt在Vue生态整合文件路由、服务端渲染和按路由配置的混合缓存。

**核心机制**：universal/client渲染→hydration→routeRules→缓存/SEO安全。

**大白话类比**：既可以先在后厨做好页面，也可以让顾客自己拼装页面。

**类比不适用的边界**：服务端有私有会话时不得把个性化HTML共享缓存。

**与其他知识的关系**：最低概念先修：F08（Vue 3/响应式/状态）、F01（Web/HTTP/浏览器）；历史知识坐标 W17；相关验收分类 G20，不强制按序通过。

**官方阅读**：[准确专题入口](https://learn.nuxt.com/en/concepts/rendering-modes) — 先看 **Nuxt rendering modes**。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/knowledge/software-engineering/programming-language-stack-map.md)。来源性质：概念综述（非可运行教程）。

**最小亲手实验**：同一页面做SSR/CSR切换，比较响应HTML和缓存行为。

**故障/反例**：服务端误用window、登录信息被缓存、hydration不一致。

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

### F10 · PWA/Service Worker/浏览器存储

**专业定义**：PWA使用Service Worker等浏览器能力实现可安装与受控离线体验。

**核心机制**：Service Worker生命周期→Cache Storage→更新和清除策略。

**大白话类比**：浏览器内有值班的离线服务员，但会被系统暂停。

**类比不适用的边界**：Service Worker并非长驻后台，也不适合缓存敏感用户响应。

**与其他知识的关系**：最低概念先修：F01（Web/HTTP/浏览器）、F03（JavaScript/TypeScript）；历史知识坐标 W14、W17；相关验收分类 G17、G20，不强制按序通过。

**官方阅读**：[准确专题入口](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Offline_and_background_operation) — 先看 **Offline and background operations**。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/sources/ai-native-multiplatform-research-20261028.md)。来源性质：概念综述（非可运行教程）。

**最小亲手实验**：离线读取公开资源、切换账号并验证旧用户缓存不可见。

**故障/反例**：离线更新陈旧、登录态切换、缓存占用。

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

### F11 · SSE/WebSocket/实时连接

**专业定义**：SSE是单向服务器到浏览器事件流，WebSocket支持建立连接后的双向帧通信。

**核心机制**：HTTP text/event-stream / WebSocket升级→断线/重连/顺序/背压。

**大白话类比**：SSE像单向广播电台，WebSocket像双向对讲机。

**类比不适用的边界**：二者都不是持久任务队列；EventSource不能随意设置自定义请求头。

**与其他知识的关系**：最低概念先修：F01（Web/HTTP/浏览器）；历史知识坐标 W06、W18；相关验收分类 G07、G20，不强制按序通过。

**官方阅读**：[准确专题入口](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events) — 先看 **Using server-sent events / WebSockets**。[基础文档](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB02.md)。来源性质：已有专题LAB（仍需本人实际运行）。

**最小亲手实验**：对SSE任意分块解析并重连；对WS验证双向和断线状态。

**故障/反例**：流被任意拆块、断线丢事件、慢接收端、代理缓冲。

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

### U01 · 静态工具站/SEO

**专业定义**：静态站只需构建发布HTML/CSS/JS资源，SEO涉及可索引HTML和语义。

**核心机制**：需求→页面与元信息→静态构建→CDN/HTTPS→搜索与性能检查。

**大白话类比**：无需后厨也能运营只在浏览器计算的小工具店。

**类比不适用的边界**：静态站仍需关注XSS/依赖安全；无需账号时不必引入DB。

**与其他知识的关系**：最低概念先修：F02（HTML/CSS/无障碍）、F03（JavaScript/TypeScript）；历史知识坐标 W14、W17；相关验收分类 G17、G20，不强制按序通过。

**官方阅读**：[准确专题入口](https://web.dev/learn/seo) — 先看 **Learn SEO / metadata**。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/sources/ai-native-multiplatform-research-20261028.md)。来源性质：概念综述（非可运行教程）。

**最小亲手实验**：实现一个本地文本转换工具并静态发布，验证无服务端通信。

**故障/反例**：离线加载、恶意输入、robots误禁收录。

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

## 后端与数据

### B01 · REST/OpenAPI

**专业定义**：REST描述资源交互风格，OpenAPI用机器可读Schema描述HTTP接口契约。

**核心机制**：请求/响应Schema→版本化OpenAPI→客户端生成→契约/集成测试。

**大白话类比**：前后端使用同一份菜单：菜名、规格、错误码必须一致。

**类比不适用的边界**：生成类型不保证服务端真实语义；变更字段要重新导出生成检查。

**与其他知识的关系**：最低概念先修：F01（Web/HTTP/浏览器）；历史知识坐标 W03；相关验收分类 G02、G03，不强制按序通过。

**官方阅读**：[准确专题入口](https://spec.openapis.org/oas/latest.html) — 先看 **OpenAPI specification / Schema**。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB02.md)。来源性质：已有专题LAB（仍需本人实际运行）。

**最小亲手实验**：FastAPI导出OpenAPI并用Orval生成TS；改字段验证编译/集成失败。

**故障/反例**：后端删除字段，前端未重新生成仍能编译说明什么？

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

### B02 · Python/FastAPI

**专业定义**：FastAPI基于ASGI、Python类型提示、Pydantic及依赖系统提供Web API。

**核心机制**：请求路由→依赖注入/验证→业务service→数据库/外部调用→响应。

**大白话类比**：后厨里的Python接单流水线，检验订单和权限后才办事。

**类比不适用的边界**：async函数里同步阻塞会损害并发；路由成功不代表鉴权正确。

**与其他知识的关系**：最低概念先修：F01（Web/HTTP/浏览器）；历史知识坐标 W03、W05；相关验收分类 G02、G03，不强制按序通过。

**官方阅读**：[准确专题入口](https://fastapi.tiangolo.com/tutorial/dependencies/) — 先看 **Dependencies / Request body / Testing**。[基础文档](https://fastapi.tiangolo.com/tutorial/)。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB02.md)。来源性质：已有专题LAB（仍需本人实际运行）。

**最小亲手实验**：实现资源级权限API+pytest正负例，模拟外部服务超时。

**故障/反例**：跨租户IDOR、非法JSON、依赖服务断线、阻塞调用。

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

### B03 · Java/JVM

**专业定义**：Java是JVM生态常用的静态类型语言，涉及类/接口、集合、泛型、内存和并发。

**核心机制**：源码→javac字节码→JVM类加载/JIT/GC；线程和内存模型。

**大白话类比**：同一道业务流程可用Java在另一套后厨运转，JVM负责运行环境。

**类比不适用的边界**：只会Spring注解不等于理解Java线程安全与异常传播。

**与其他知识的关系**：最低概念先修：无；历史知识坐标 W09、W10、W11；相关验收分类 G13、G14，不强制按序通过。

**官方阅读**：[准确专题入口](https://dev.java/learn/) — 先看 **Classes / Generics / Concurrency**。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB14.md)。来源性质：已有专题LAB（仍需本人实际运行）。

**最小亲手实验**：Java独立实现幂等键映射、单元测试，复现共享可变状态竞态。

**故障/反例**：两个线程并发修改HashMap/共享计数器会怎样？

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

### B04 · Spring Boot/MVC

**专业定义**：Spring Boot整合Spring容器、配置与Web MVC/Servlet等进行Java应用开发。

**核心机制**：Bean/DI→MVC DispatcherServlet→Controller→Service→错误/测试。

**大白话类比**：容器帮你把业务部件装配好，HTTP请求沿着流水线走。

**类比不适用的边界**：Spring Boot不是Java语言本身；DTO验证不能代替权限。

**与其他知识的关系**：最低概念先修：B03（Java/JVM）、F01（Web/HTTP/浏览器）；历史知识坐标 W12；相关验收分类 G15，不强制按序通过。

**官方阅读**：[准确专题入口](https://docs.spring.io/spring-boot/reference/web/servlet.html) — 先看 **Servlet web applications / Spring MVC**。[基础文档](https://docs.spring.io/spring-boot/reference/)。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB14.md)。来源性质：已有专题LAB（仍需本人实际运行）。

**最小亲手实验**：Spring Boot做GET/POST资源API并用MockMvc测试，覆盖400/403/500等约定错误路径。

**故障/反例**：Bean循环依赖、校验失败、没有权限的订单访问。

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

### B05 · Spring Data/Security

**专业定义**：Spring Data、事务代理与Spring Security是不同职责的生态模块。

**核心机制**：Repository/事务代理→SQL一致性；FilterChain/方法级授权→拒绝无权访问。

**大白话类比**：账本保管员与门禁保安合作，但不是同一个角色。

**类比不适用的边界**：Spring Security不依赖PostgreSQL；事务边界和鉴权机制应独立验证。

**与其他知识的关系**：最低概念先修：B04（Spring Boot/MVC）；历史知识坐标 W13；相关验收分类 G16，不强制按序通过。

**官方阅读**：[准确专题入口](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html) — 先看 **Authorize HTTP requests / Method Security**。[基础文档](https://docs.spring.io/spring-security/reference/)。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB14.md)。来源性质：已有专题LAB（仍需本人实际运行）。

**最小亲手实验**：独立实现用户A/B资源级访问限制，事务失败回滚测试。

**故障/反例**：仅检查已登录但不检查资源拥有者，是否能跨用户读取？

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

### B06 · Celery/后台任务可靠性

**专业定义**：Celery任务队列用于把耗时工作分派给Worker，业务状态和幂等需额外设计。

**核心机制**：Broker→任务确认/重试→业务数据库状态机→幂等副作用与恢复。

**大白话类比**：前台先开受理单，后厨排队处理，窗口关了订单仍可查询。

**类比不适用的边界**：acks_late也不保证杀子进程后一定重投；不要把Celery内部状态当业务状态。

**与其他知识的关系**：最低概念先修：B02（Python/FastAPI）；历史知识坐标 W06；相关验收分类 G06、G07，不强制按序通过。

**官方阅读**：[准确专题入口](https://docs.celeryq.dev/en/stable/userguide/tasks.html) — 先看 **Celery tasks / acks_late / worker lost**。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB02.md)。来源性质：已有专题LAB（仍需本人实际运行）。

**最小亲手实验**：Worker处理耗时任务，杀Worker并重启，核对业务幂等与状态一致。

**故障/反例**：重复提交、Worker崩溃和重放是否造成重复扣费？

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

### B07 · Node后端/NestJS/Express

**专业定义**：Node生态后端框架NestJS/Express负责HTTP路由、依赖组织和服务端业务。

**核心机制**：Node事件循环→Controller/Provider→Validation/Guard→DB/外部API。

**大白话类比**：同一个JS语言在服务器也能处理真正的业务订单。

**类比不适用的边界**：NestJS是框架、Node是运行时；同步阻塞和权限边界仍需考虑。

**与其他知识的关系**：最低概念先修：F06（Node.js/Streams）、F01（Web/HTTP/浏览器）；历史知识坐标 W18；相关验收分类 G20、G24，不强制按序通过。

**官方阅读**：[准确专题入口](https://docs.nestjs.com/controllers) — 先看 **NestJS Controllers / Providers / Guards**。[基础文档](https://docs.nestjs.com/first-steps)。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/knowledge/software-engineering/programming-language-stack-map.md)。来源性质：概念综述（非可运行教程）。

**最小亲手实验**：建Nest最小CRUD+HTTP状态正负例，用测试核查越权。

**故障/反例**：Pipe校验缺失、服务异常变500、请求上下文丢失。

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

### B08 · Go服务与并发

**专业定义**：Go通过模块、接口、goroutine和context组织编译型网络/并发服务。

**核心机制**：go mod→HTTP handler→goroutine/channel/context cancellation→测试。

**大白话类比**：用轻量服务员同时接很多单，但仍要安排取消和共享状态。

**类比不适用的边界**：goroutine并发不等于无数据竞态；按需使用不用全面转Go。

**与其他知识的关系**：最低概念先修：F01（Web/HTTP/浏览器）；历史知识坐标 W24；相关验收分类 G24，不强制按序通过。

**官方阅读**：[准确专题入口](https://go.dev/learn/) — 先看 **Go official tutorials / context**。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/knowledge/software-engineering/programming-language-stack-map.md)。来源性质：概念综述（非可运行教程）。

**最小亲手实验**：写带超时/取消的Go HTTP handler，通过-race发现共享变量竞态。

**故障/反例**：context已取消但goroutine仍跑、数据竞争。

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

### B09 · Rust/C++/CUDA原生能力

**专业定义**：Rust/C++/CUDA分别服务于安全系统程序、原生性能代码及GPU计算，适用场景不同。

**核心机制**：Rust所有权/借用或C++生命周期/RAII；CUDA host/device执行模型。

**大白话类比**：把性能瓶颈从普通后厨移到更精密的机器，不是每道菜都要用。

**类比不适用的边界**：一份Rust官方书不能代表C++和CUDA三门都覆盖；不能因可能性能优化就提前学习。

**与其他知识的关系**：最低概念先修：无；历史知识坐标 W24；相关验收分类 G24，不强制按序通过。

**官方阅读**：[准确专题入口](https://doc.rust-lang.org/stable/book/) — 先看 **The Rust Book / NVIDIA CUDA programming guide**。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/knowledge/software-engineering/programming-language-stack-map.md)。来源性质：概念综述（非可运行教程）。

**最小亲手实验**：选择一个真实的原生瓶颈：Rust CLI或C++解析或CUDA kernel做受控基准。

**故障/反例**：内存错误、并发悬挂、无GPU时不得宣称CUDA实测。

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

### D01 · PostgreSQL/SQL

**专业定义**：SQL关系数据库通过约束、事务、MVCC、索引等维护持久数据和并发正确性。

**核心机制**：Schema→约束→隔离/行锁→执行计划→备份恢复。

**大白话类比**：正式账本有规则和并发记账机制，不能靠缓存当账本。

**类比不适用的边界**：READ COMMITTED不能自动避免所有业务竞态；索引也有写入成本。

**与其他知识的关系**：最低概念先修：无；历史知识坐标 W04；相关验收分类 G04，不强制按序通过。

**官方阅读**：[准确专题入口](https://www.postgresql.org/docs/current/transaction-iso.html) — 先看 **Transaction isolation / EXPLAIN**。[基础文档](https://www.postgresql.org/docs/current/)。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB08.md)。来源性质：已有专题LAB（仍需本人实际运行）。

**最小亲手实验**：两个连接同时扣余额，比较无锁/条件更新/行锁并记录执行计划。

**故障/反例**：丢失更新、死锁、超扣和读已提交下的异常。

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

### D02 · Redis/缓存

**专业定义**：Redis是支持多种数据结构的内存数据平台，常用于缓存、限流和短期协调。

**核心机制**：key/value与TTL→缓存模式→失效/回源→并发更新。

**大白话类比**：热数据速取柜，提升取用速度但不默认代替正式账本。

**类比不适用的边界**：缓存不是数据库事务的替身；分布式锁要考虑故障和有效期。

**与其他知识的关系**：最低概念先修：无；历史知识坐标 W04、W20；相关验收分类 G05、G21，不强制按序通过。

**官方阅读**：[准确专题入口](https://redis.io/docs/latest/) — 先看 **Redis documentation / cache patterns**。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB08.md)。来源性质：已有专题LAB（仍需本人实际运行）。

**最小亲手实验**：模拟热点TTL同时失效，统计数据库回源并发并实现请求合并。

**故障/反例**：缓存击穿、读到旧值、重建锁过期时如何避免覆盖？

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

### D03 · 消息/Outbox

**专业定义**：消息系统通过队列/主题传递异步事件，Outbox处理业务事务与发布之间的一致性缺口。

**核心机制**：业务事务写入Outbox→发布→消费者去重/重试/死信。

**大白话类比**：订单签收同时留下派送指令，防止业务成功但通知没发出。

**类比不适用的边界**：MQ默认不保证业务恰好执行一次；Kafka/RabbitMQ角色与语义不同。

**与其他知识的关系**：最低概念先修：D01（PostgreSQL/SQL）；历史知识坐标 W19、W20；相关验收分类 G21，不强制按序通过。

**官方阅读**：[准确专题入口](https://www.rabbitmq.com/docs/queues) — 先看 **RabbitMQ queues / Publisher confirms**。[基础文档](https://www.rabbitmq.com/docs)。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/enterprise-ai-application-capstone.md)。来源性质：课程/场景说明（非实测）。

**最小亲手实验**：在DB提交后人为阻断发布，使用Outbox+幂等消费者恢复。

**故障/反例**：重复消息、消费者掉线、发布成功但ACK丢失。

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

### D04 · MySQL差异

**专业定义**：MySQL/InnoDB是关系数据库引擎，其隔离/索引/锁行为须按版本与PostgreSQL比较。

**核心机制**：InnoDB MVCC、索引、间隙锁及事务隔离；比较实现差异。

**大白话类比**：同样是账本，不同品牌对并发冲突有不同操作规程。

**类比不适用的边界**：不能把PostgreSQL的可重复读行为直接迁移成MySQL规则。

**与其他知识的关系**：最低概念先修：无；历史知识坐标 W20；相关验收分类 G21，不强制按序通过。

**官方阅读**：[准确专题入口](https://dev.mysql.com/doc/refman/8.4/en/innodb-transaction-isolation-levels.html) — 先看 **InnoDB transaction isolation levels**。[基础文档](https://dev.mysql.com/doc/)。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/knowledge/software-engineering/programming-language-stack-map.md)。来源性质：概念综述（非可运行教程）。

**最小亲手实验**：同一并发更新测试分别跑MySQL和PG并比较结果。

**故障/反例**：幻读/间隙锁、死锁回滚、索引失效。

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

### D05 · 对象存储/全文搜索/向量数据库

**专业定义**：对象存储、全文检索和向量数据库分别承担二进制对象、词项索引和相似度检索。

**核心机制**：对象键/元数据→全文倒排索引→向量近邻检索→授权过滤。

**大白话类比**：仓库存文件、目录按词找、相似照片按特征找，是三种不同功能。

**类比不适用的边界**：PostgreSQL全文搜索文档不能替代S3/Milvus的官方定义；检索不是鉴权。

**与其他知识的关系**：最低概念先修：无；历史知识坐标 W20、W24；相关验收分类 G21、G24，不强制按序通过。

**官方阅读**：[准确专题入口](https://www.postgresql.org/docs/current/textsearch.html) — 先看 **PostgreSQL Full Text Search / S3 / Milvus**。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB03.md) · [资料2](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB04.md)。来源性质：已有专题LAB（仍需本人实际运行）。

**最小亲手实验**：上传合成文件、维护元数据和ACL；比较词项/向量查询误召回。

**故障/反例**：删除后仍可检索、未授权用户能读对象、索引更新滞后。

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

## 工程与运维

### E01 · Git/测试/CI

**专业定义**：Git、测试金字塔和CI将可重复验证与代码审查嵌入变更流程。

**核心机制**：分支/PR→lint/type→unit/integration/e2e→构建→失败阻断。

**大白话类比**：每次改装配线，先让自动质检抽查正常和坏件。

**类比不适用的边界**：CI绿不能证明没漏测试，更不能等同个人闭卷掌握。

**与其他知识的关系**：最低概念先修：无；历史知识坐标 W07；相关验收分类 G10，不强制按序通过。

**官方阅读**：[准确专题入口](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions) — 先看 **Workflow syntax / Actions**。[基础文档](https://docs.github.com/en/actions)。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB11.md) · [资料2](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/assessments/ai-native-fullstack-rubric.md) · [资料3](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/sources/ai-native-fullstack-research-20261028.md)。来源性质：已有专题LAB（仍需本人实际运行）。

**最小亲手实验**：故意破坏接口字段/权限测试，看CI红灯并恢复。

**故障/反例**：测试仅覆盖快乐路径、依赖未锁、并行污染。

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

### E02 · Docker/Linux/部署

**专业定义**：Linux/容器/反代/HTTPS组合实现服务进程隔离、网络入口与可重复部署。

**核心机制**：镜像/容器→Compose网络/卷→Nginx/TLS→发布和恢复。

**大白话类比**：包装、运输、站点入口和灾备机制，不等于业务自动上线。

**类比不适用的边界**：容器重启≠数据恢复；单机Compose≠HA/Kubernetes。

**与其他知识的关系**：最低概念先修：无；历史知识坐标 W07、W22；相关验收分类 G09、G11、G23，不强制按序通过。

**官方阅读**：[准确专题入口](https://docs.docker.com/compose/) — 先看 **Docker Compose overview**。[基础文档](https://docs.docker.com/get-started/)。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB11.md)。来源性质：已有专题LAB（仍需本人实际运行）。

**最小亲手实验**：全新环境启动API+DB+前端，执行备份/恢复、回滚演练。

**故障/反例**：丢环境变量/数据卷、HTTPS证书过期、反代超时。

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

### E03 · 身份/权限/多租户

**专业定义**：认证确认身份，授权确认某身份能否操作特定资源，审计记录决策。

**核心机制**：Cookie/Session/OIDC→服务器授权检查→租户/资源级限制→审计。

**大白话类比**：认识来访者不是让他有所有钥匙，具体房间还要查权限。

**类比不适用的边界**：前端隐藏按钮不构成授权；SameSite不替代完整CSRF威胁分析。

**与其他知识的关系**：最低概念先修：F01（Web/HTTP/浏览器）；历史知识坐标 W05、W21；相关验收分类 G02、G16、G22，不强制按序通过。

**官方阅读**：[准确专题入口](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) — 先看 **Authorization cheat sheet / Broken object-level authorization**。[基础文档](https://owasp.org/API-Security/)。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB09.md)。来源性质：已有专题LAB（仍需本人实际运行）。

**最小亲手实验**：设计A/B用户同一API资源，验证401/403或隐匿404策略及Cookie安全。

**故障/反例**：横向越权、CSRF、过期会话、泄露私有资源。

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

### E04 · Trace/性能/排障

**专业定义**：可观测性通过日志、指标、分布式追踪关联服务行为与性能瓶颈。

**核心机制**：日志RequestID→Span/traceparent→Metrics P95→定位慢路径。

**大白话类比**：物流查询单记录经过各站所耗时间，而不只说包裹慢。

**类比不适用的边界**：X-Request-ID用于日志关联，不自动等于跨进程Trace；测试条件影响P95。

**与其他知识的关系**：最低概念先修：无；历史知识坐标 W08、W23；相关验收分类 G08、G23，不强制按序通过。

**官方阅读**：[准确专题入口](https://www.w3.org/TR/trace-context/) — 先看 **W3C Trace Context specification**。[基础文档](https://opentelemetry.io/docs/)。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB07.md)。来源性质：已有专题LAB（仍需本人实际运行）。

**最小亲手实验**：注入DB慢查询，沿HTTP→API→DB查看trace与耗时，前后比较。

**故障/反例**：span未传播、时钟/采样设置不匹配、错误率被平均值掩盖。

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

### E05 · 编译/构建/打包/运行时

**专业定义**：构建系统将源码、依赖与编译转换为可分发产物，运行环境和发布独立。

**核心机制**：Vite/tsc→浏览器bundle；Maven/Gradle→JAR；Python环境→启动；Go/Rust→binary。

**大白话类比**：食材、包装成品、运输容器、上架运行是不同环节。

**类比不适用的边界**：Python打包不等于原生可执行程序；Docker镜像不自动管理数据库。

**与其他知识的关系**：最低概念先修：无；历史知识坐标 W07、W15、W22；相关验收分类 G10、G18、G23，不强制按序通过。

**官方阅读**：[准确专题入口](https://maven.apache.org/guides/getting-started/index.html) — 先看 **Maven Getting Started / Vite build**。[基础文档](https://vite.dev/guide/)。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/knowledge/software-engineering/programming-language-stack-map.md)。来源性质：概念综述（非可运行教程）。

**最小亲手实验**：比较JS npm build、Java mvn package、Python安装/启动的产物差异。

**故障/反例**：依赖未锁、目标系统架构不匹配、发布后环境变量缺失。

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

## 移动、桌面与AI

### M01 · 微信小程序

**专业定义**：微信小程序是微信容器内运行的组件/生命周期/平台API程序。

**核心机制**：页面生命周期→平台请求/登录→合法域名→真机审核。

**大白话类比**：在微信商场里开店，要遵守商场门禁和运行规则。

**类比不适用的边界**：浏览器H5通过不代表小程序合法域名/真机/审核通过。

**与其他知识的关系**：最低概念先修：F03（JavaScript/TypeScript）；历史知识坐标 W24；相关验收分类 G10、G24，不强制按序通过。

**官方阅读**：[准确专题入口](https://developers.weixin.qq.com/miniprogram/dev/framework/) — 先看 **Mini Program framework**。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/ai-native-multiplatform-track.md)。来源性质：课程/场景说明（非实测）。

**最小亲手实验**：做简单页面调用Mock API，模拟弱网并核查真机/基础库行为。

**故障/反例**：未配置域名、授权失败、后台切换导致状态丢失。

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

### M02 · 移动App

**专业定义**：移动跨平台框架通过共享UI/逻辑调用Android/iOS能力，设备权限与分发各自独立。

**核心机制**：RN/Expo或Flutter二选一→设备生命周期/存储→构建/签名。

**大白话类比**：一份图纸尽量盖两家不同规范的店，仍要分别验收。

**类比不适用的边界**：跨平台不等于原生能力完全相同；Expo不是Swift/Kotlin先修。

**与其他知识的关系**：最低概念先修：无；历史知识坐标 W24；相关验收分类 G10、G24，不强制按序通过。

**官方阅读**：[准确专题入口](https://docs.expo.dev/) — 先看 **Expo documentation / Flutter**。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/assessments/ai-native-multiplatform-rubric.md)。来源性质：概念综述（非可运行教程）。

**最小亲手实验**：用RN/Expo或Flutter完成离线表单，拒绝权限再恢复。

**故障/反例**：手机锁屏/断网、缓存泄漏、Android/iOS行为差异。

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

### M03 · Electron/Tauri桌面应用

**专业定义**：Electron/Tauri通过Web界面加桌面宿主访问本机能力，需严格限制IPC和系统权限。

**核心机制**：UI渲染进程→主进程/命令桥接→OS文件权限→签名更新。

**大白话类比**：网页柜台进入本地电脑后能摸到文件和设备，必须加隔离门。

**类比不适用的边界**：默认开启危险Node集成/宽松IPC会扩大攻击面；Tauri不是纯前端框架。

**与其他知识的关系**：最低概念先修：F02（HTML/CSS/无障碍）、F03（JavaScript/TypeScript）；历史知识坐标 W24；相关验收分类 G22、G24，不强制按序通过。

**官方阅读**：[准确专题入口](https://www.electronjs.org/docs/latest/tutorial/process-model) — 先看 **Electron process model**。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/career/opc-multiplatform-product-engineer-roadmap-20261028.md)。来源性质：概念综述（非可运行教程）。

**最小亲手实验**：仅允许用户选定目录文件读取，测试恶意路径被拒绝。

**故障/反例**：渲染进程任意调用文件API、跨目录路径遍历。

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

### M04 · uni-app/跨端小程序生态

**专业定义**：uni-app在Vue风格开发体验上面向多端编译/运行，但各平台API和构建限制不同。

**核心机制**：Vue页面→跨端组件编译→微信/其他端API→真机检查。

**大白话类比**：一份柜台装修图分发不同商场，每家仍有单独验收。

**类比不适用的边界**：一份代码不能保证平台交互、性能和审核完全一致。

**与其他知识的关系**：最低概念先修：F08（Vue 3/响应式/状态）；历史知识坐标 W24；相关验收分类 G24，不强制按序通过。

**官方阅读**：[准确专题入口](https://uniapp.dcloud.net.cn/) — 先看 **uni-app official tutorial**。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/ai-native-multiplatform-track.md)。来源性质：课程/场景说明（非实测）。

**最小亲手实验**：同页H5/微信端运行对照，记录系统API差异。

**故障/反例**：不支持的组件/插件、登录或支付SDK差异。

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

### M05 · Android/iOS原生开发

**专业定义**：Android Kotlin/Compose与iOS Swift/SwiftUI是两套原生UI/平台SDK体系。

**核心机制**：设备权限→UI生命周期→本地存储→构建/签名/商店。

**大白话类比**：分别掌握安卓和苹果原厂工具，不能用一个跨端教程代替。

**类比不适用的边界**：原生开发不以先学Expo为必要条件；iOS构建通常需符合Xcode/macOS约束。

**与其他知识的关系**：最低概念先修：无；历史知识坐标 W24；相关验收分类 G24，不强制按序通过。

**官方阅读**：[准确专题入口](https://developer.android.com/jetpack/compose) — 先看 **Android Jetpack Compose / Apple SwiftUI**。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/career/opc-multiplatform-product-engineer-roadmap-20261028.md)。来源性质：概念综述（非可运行教程）。

**最小亲手实验**：选择一个真实平台，做权限拒绝与离线恢复，记录设备/构建条件。

**故障/反例**：权限拒绝、应用被系统回收、离线回放。

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

### A01 · AI/RAG/Agent

**专业定义**：RAG/Agent将模型/检索/工具与业务API组合，通过评测和权限限制不确定性。

**核心机制**：检索或模型推理→证据/工具Schema→策略审批→业务写入/评测。

**大白话类比**：模型像会提出建议的助手，但不能直接拿全部仓库钥匙。

**类比不适用的边界**：LLM生成文本不是可信数据库写入命令；模型准确率不能代替权限。

**与其他知识的关系**：最低概念先修：B01（REST/OpenAPI）；历史知识坐标 W24；相关验收分类 G24，不强制按序通过。

**官方阅读**：[准确专题入口](https://docs.langchain.com/oss/python/langgraph/overview) — 先看 **LangGraph overview / tool calling**。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/enterprise-ai-application-capstone.md)。来源性质：课程/场景说明（非实测）。

**最小亲手实验**：合成文档问答与受限工具调用，记录无证据拒答/越权拒写。

**故障/反例**：提示注入、工具重复调用、幻觉引用与成本超标。

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

### A02 · MCP工具接口/Agent协议

**专业定义**：MCP规范AI宿主/客户端/服务器之间的工具和上下文交换，基于JSON-RPC。

**核心机制**：Host→Client→Server工具/资源声明→受限调用和授权/协议版本协商。

**大白话类比**：给AI助理统一的工具插座，同时限定每个插座有权做什么。

**类比不适用的边界**：MCP不是通用REST替代也不是Agent与Agent通信的全部标准；依规范版本区分有状态/无状态语义。

**与其他知识的关系**：最低概念先修：无；历史知识坐标 W24；相关验收分类 G24，不强制按序通过。

**官方阅读**：[准确专题入口](https://modelcontextprotocol.io/specification/2026-07-28/architecture) — 先看 **MCP 2026-07-28 architecture**。[基础文档](https://modelcontextprotocol.io/docs/learn/architecture)。

**上游相关资料**：[资料1](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB06.md)。来源性质：已有专题LAB（仍需本人实际运行）。

**最小亲手实验**：最小MCP工具返回合成数据，非法参数与无权限调用必须失败。

**故障/反例**：工具声明与实际权限不一致、无害请求被赋予写权限。

**完成标准**：本人解释原因，保存真实测试命令、失败和修复前后日志、commit；关AI做一次条件变化的复验。未执行始终标 `NOT_RUN`。

## 同组技术不等于同一技术

- B05的Spring Data与Spring Security互有关联却职责不同，**Spring Security不以PostgreSQL为硬先修**。
- B06是Celery后台任务可靠性；F11是SSE/WebSocket实时通信。连接断了≠任务就应终止。
- B09收纳Rust/C++/CUDA原生方向的**存在感与选型认知**，不能拿一本Rust书当成全部；分别查[Rust官方](https://doc.rust-lang.org/stable/book/)、[C++参考](https://en.cppreference.com/w/)、[CUDA官方](https://docs.nvidia.com/cuda/cuda-c-programming-guide/)。
- D05是对象存储、全文检索、向量相似搜索三种职责：[S3文档](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)、[PostgreSQL全文搜索](https://www.postgresql.org/docs/current/textsearch.html)、[Milvus](https://milvus.io/docs/overview.md)。检索不是鉴权。
- M05 Android/Kotlin和iOS/Swift可直接进入原生平台，不要求先学Expo/React Native：[Android官方](https://developer.android.com/jetpack/compose) / [Apple官方](https://developer.apple.com/tutorials/swiftui)。
- E05多语言构建与发布不是一回事；Webpack/Vite、Maven、Python工具链、Go/Rust的产物不同。

**资料取舍**：先看官方1–3小节；如果上游只有概念总图，就明确它不是专项实训，回到真实代码或最小受控实验补验证。

