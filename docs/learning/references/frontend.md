# 前端专项深挖字典 V3.0（按需查阅，不是第二条进度表）

> **REFERENCE / NOT_RUN / NEED_FIRST**。本字典仅作深挖资料，优先从[需求路由](../DEMAND-ROUTER.md)与[知识依赖图](../KNOWLEDGE-GRAPH.md)定位问题。W序号是旧课程坐标，不要求按顺序学习。原W1–W24只作为[ROADMAP](../../../ROADMAP.md)覆盖坐标；当需求触发界面/SSR/性能才从相应节点入手，学习证据记[PROGRESS](../PROGRESS.md)，无需按周学习或对每个项目强加SSR。

## 一、HTML / CSS / Web 平台：不能被组件库替代

| 主题 | 应掌握的知识 | 对应周 | 自己做的实验 |
|---|---|---|---|
| HTML5 | 语义、表单/label、原生校验、DOM、事件传播、ARIA 的适用边界 | W1/W14 | 重新实现无障碍的上传/筛选表单，键盘可操作 |
| CSS 核心 | 盒模型、层叠/特异性、继承、BFC、定位/层叠上下文、Flex/Grid | W14 | 修复定位和覆盖 bug，解释具体规则 |
| 响应式 UI | 断点、Container Queries、min/max、布局自适应、暗黑模式、Design Tokens | W14 | 390/1280 宽度的后台页无布局溢出 |
| 浏览器 | DOM/CSSOM、渲染流水线、Layout/Paint/Composite、浏览器缓存、Performance Timeline | W1/W14 | DevTools 分析布局/长任务和慢资源 |
| 可访问性 | 键盘焦点、对比度、语义角色、错误提示、屏幕阅读器基础 | W14 | 对话框/表单键盘测试，检查焦点管理 |
| Web 安全 | 同源/CORS/Cookie/CSRF/XSS/CSP、浏览器存储的 Token 风险 | W5/W21 | 401/403 与受控 XSS/CSRF 负例 |

参考：[MDN Core Curriculum](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core)、[CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)、[Accessibility](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility)。

## 二、JavaScript / TypeScript 与工程化

| 主题 | 深度 | 对应周/实验 |
|---|---|---|
| JS 运行机制 | 作用域、闭包、this/原型链、微/宏任务、Promise、async/await、Generator、GC/内存泄漏 | W1/W15：请求竞态、取消、闭包旧值 |
| TypeScript | interface/type、泛型、条件类型、映射类型、unknown/never、类型守卫、strict、类型推导 | W1/W15：类型安全 Result<T> 和组件 API；Typecheck 负例 |
| ES Modules | ESM/CJS、依赖解析、动态 import、package exports、模块副作用 | W15：对比浏览器与 Node 加载 |
| Toolchain | pnpm workspace、Vite/Bundler、ESLint、Source Maps、tree-shaking、code splitting | W15：打包分析及懒加载前后对比 |
| 浏览器网络 API | Fetch/AbortController、WebSocket/SSE、ReadableStream、缓存/Service Worker 认知 | W1/W6/W18：分块/重连/背压/取消 |

参考：[TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/)、[Vite](https://vite.dev/guide/)、[MDN JS](https://developer.mozilla.org/en-US/docs/Web/JavaScript)。

## 三、React 实战到生产前端

| 主题 | 必须理解 | 验收 |
|---|---|---|
| React 基础/原理 | State Snapshot、Render/Commit、Identity/key、Effect Cleanup/Strict Mode | W2/W16：竞态与状态残留负例 |
| 状态管理 | local UI state vs Query server state vs Context/useReducer；Zustand/Redux 何时需要 | W16：合理分层与 Mutation 回滚 |
| 表单/表格 | React Hook Form + Zod、TanStack Table、分页、虚拟列表、复杂表单校验 | W16：错误回滚/表单可访问性 |
| 组件架构 | Feature Slices、Composition、Custom Hooks、Error Boundaries、Suspense/Portal | W16：独立复用、错误隔离 |
| 性能 | React Profiler、memo/useMemo/useCallback 的取舍、列表虚拟化 | W16/W23：可复现优化对照 |
| 测试 | Vitest、React Testing Library、Playwright、Mock 的边界 | W16/W23：单测/组件/E2E/错误态 |

参考：[React Learn](https://react.dev/learn)、[TanStack Query](https://tanstack.com/query/latest/docs/framework/react/overview)、[Playwright](https://playwright.dev/docs/intro)。

## 四、Next.js/SSR、Node.js 与架构比较

- W17 **必做比较实验**：SPA/CSR、SSR/SSG/ISR、Hydration、RSC、Next App Router、Server/Client 边界、Server Actions/Route Handlers 与缓存/SEO。做一页相同的公开合成内容，测/解释两种方案，不强行迁移工作台主前端。
- W18 **必做最小 Node.js 实验**：Event Loop/libuv、Buffer/Stream、背压/取消、ESM/CJS、最小 Express/Fastify BFF。NestJS 基础认知足够；完整 Nest 业务属于选修。
- W23 Web 性能：LCP/INP/CLS、资源瀑布图、JS Bundle、渲染阻塞、缓存/CDN、错误监控；提交固定环境下的前后比较。
- Vue3（Composition API、ref/reactive/watch）、Nuxt、GraphQL/gRPC、复杂 Service Worker 离线能力按 JD/业务选修，不另建独立学习路线。

资料：[Next.js App Router](https://nextjs.org/docs/app)、[Node.js Learn](https://nodejs.org/en/learn)、[MDN Web Performance](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Performance)。

## 五、最常见的五种错误

1. 会 Tailwind/shadcn 不等于懂 HTML/CSS/可访问性。
2. 会 Hooks 不等于理解 React 重新渲染、请求竞态和服务端缓存。
3. 用 useMemo 到处包裹不等于性能优化；必须用 Profiler/真实指标对比。
4. “Next SSR 更高级”不意味着纯后台 SPA 一定需要 SSR；必须解释成本与缓存边界。
5. AI 生成页面/CI 绿灯不等于学员能独立查出 Hydration、分块流、权限、缓存和性能故障。

[能力验收 G17–G20](../ACCEPTANCE.md) · [主项目蓝图](../../project/PROJECT-BLUEPRINT.md)。
