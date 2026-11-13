# 前端专项深挖字典（按需检索，非独立进度表）

> 仅为 [唯一主线](../../../ROADMAP.md) 的问题索引，不复制另一套 8 周学习安排。

| 主线阶段 | 查阅专题 | 自己应做的最小实验 | 资料 |
|---|---|---|---|
| W1 | HTTP/CORS/HTTPS/Cookie/缓存、DevTools | 用 Network 解释预检和 Cookie；对比 401/403/5xx | [MDN](https://developer.mozilla.org/en-US/docs/Learn_web_development) |
| W1 | Promise/Event Loop/AbortController | 发起两次请求逆序返回；验证取消和超时 | [MDN JS](https://developer.mozilla.org/en-US/docs/Web/JavaScript) |
| W1 | TS 泛型/联合/类型收窄 | 定义 `Result<T>` 和 API 错误辨别联合 | [TS Handbook](https://www.typescriptlang.org/docs/handbook/) |
| W2 | React Render/Commit、State 快照/闭包 | 快速输入、批量 state 更新，解释捕获的旧值 | [React Learn](https://react.dev/learn) |
| W2 | useEffect、StrictMode、清理 | 控制 Effect 是否触发，取消旧请求 | [Synchronizing with Effects](https://react.dev/learn/synchronizing-with-effects) |
| W2/W5 | Query 缓存、Mutation、Query Key | 改动数据后的精确 invalidation 与竞态验证 | [TanStack Query](https://tanstack.com/query/latest/docs/framework/react/overview) |
| W5 | 登录态、Cookie、CSRF | 401→退出，403→拒绝，重复刷新不风暴 | [OWASP](https://cheatsheetseries.owasp.org/) |
| W6 | SSE 事件边界、重连、分块与取消 | 任意分块输入、断开、Last-Event-ID 策略 | [MDN SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events) |
| W7 | Playwright 与可访问性 | 登录→编辑→刷新→权限失败 E2E | [Playwright](https://playwright.dev/docs/intro) |

**选用规则**：遇到某 Gap → 查一节官方文档 → 本人写最小失败/修复实验 → 回到工作台 → 在 [进度台账](../PROGRESS.md) 记录证据。避免“看完全部文档才动手”。
