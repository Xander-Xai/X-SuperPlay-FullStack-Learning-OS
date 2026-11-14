# 全栈工程面试与独立答辩：20道问题

> 本文是现有[G01–G24验收目录](ACCEPTANCE.md)的题目检索入口，不新建进度或强制每天刷题。挑当前JD相关的题，从[知识卡](NODE-STUDY-CARDS.md)查专业机制，再用真实项目与[最小实验](labs/README.md)留证据。**当前题目全部UNASSESSED**。

## 20题与可检验依据

| ID/类别 | 核心问题 | 回答应包含的专业机制 | 一项应当亲手验证的负例 | 节点 / 官方资料 |
|---|---|---|---|---|
| Q01 Web | 输入网址后发生什么？ | DNS、TCP/TLS（或QUIC）、HTTP缓存、DOM/CSSOM、渲染；连接可能复用 | DevTools比较首次/重复加载，识别是否重新建连接 | F01/F02 · [官方](https://developer.mozilla.org/en-US/docs/Web/Performance/How_browsers_work) |
| Q02 Web | Cookie、Session、JWT怎么区分？ | Cookie是HTTP携带方式，Session是服务端状态，JWT是签名声明；不是三选一 | 验证HttpOnly/SameSite、过期、撤销、签名伪造与资源权限 | F01/E03 · [官方](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/) |
| Q03 Web | 为何Postman可用而浏览器遇CORS？ | 浏览器同源策略、预检OPTIONS、Allow-Origin/credentials与服务器认证区别 | 在Network重现预检失败，服务端授权仍要单独测试 | F01/E03 · [官方](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS) |
| Q04 Web | HTTP、SSE、WebSocket怎么选择？ | 请求/响应、单向事件流、双向帧的方向、重连、代理和背压差别 | SSE分块/断线与WebSocket重连实验 | F01/F11 · [官方](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events) |
| Q05 前端 | React渲染/提交的过程是什么？ | 状态快照→render计算→commit DOM；key与组件身份决定状态保留 | 改变key复现子组件状态错位并修复 | F04 · [官方](https://react.dev/learn/render-and-commit) |
| Q06 前端 | useEffect为什么重跑，如何避免竞态？ | 与外部系统同步、依赖变化/卸载清理、StrictMode；派生数据常无需Effect | A/B逆序请求故障与清理/序号保护测试 | F03/F04 · [官方](https://react.dev/learn/you-might-not-need-an-effect) |
| Q07 前端 | 浏览器、Query、Redis缓存有何区别？ | HTTP响应缓存、客户端服务器状态缓存、后端数据缓存的责任和失效不同 | 依次注入ETag/Query invalidate/Redis TTL旧数据问题 | F01/F04/D02 · [官方](https://tanstack.com/query/latest/docs/framework/react/guides/important-defaults) |
| Q08 前端 | SSR与CSR各自优势和代价？ | 浏览器计算与服务端HTML、hydration、缓存隐私、SEO、TTFB/运行成本 | Vite与Next对照首包HTML和私有页面缓存负例 | F05/F09 · [官方](https://nextjs.org/docs/app/getting-started/server-and-client-components) |
| Q09 后端 | FastAPI async提高什么，不提高什么？ | 协作式I/O并发不等于CPU并行；阻塞调用拖慢事件循环 | 异步等待、同步阻塞与CPU循环三组并发对比 | B02 · [官方](https://fastapi.tiangolo.com/async/) |
| Q10 后端 | POST怎么保证幂等？ | 幂等键、业务唯一约束、原子状态与重放语义；不保证网络恰好一次 | 并发相同请求/重复重投仅一份记录 | B01/D01/B06 · [官方](https://docs.stripe.com/api/idempotent_requests) |
| Q11 后端 | 隔离级别与丢失更新怎样关联？ | ACID、MVCC、条件更新/锁、隔离级别可见性及冲突 | 两个连接扣减余额，比较行锁和条件更新 | D01 · [官方](https://www.postgresql.org/docs/current/transaction-iso.html) |
| Q12 后端 | Router、Service、Repository为什么拆？ | HTTP边界、业务规则/事务、存储适配分责；简单场景不过度分层 | 换存储实现而不改API契约的测试 | B02/B01 · [官方](https://fastapi.tiangolo.com/tutorial/bigger-applications/) |
| Q13 数据 | 索引有时为何不加速？ | 选择性、执行计划、统计信息、回表/排序与写入维护成本 | EXPLAIN (ANALYZE, BUFFERS)有无索引对照 | D01 · [官方](https://www.postgresql.org/docs/current/using-explain.html) |
| Q14 数据 | 什么是ORM N+1，如何检测？ | 主查询N行后又触发N次关系查询；eager/batched加载及SQL计数 | 10行列表SQL次数前后对照 | D01/B05 · [官方](https://docs.sqlalchemy.org/en/20/orm/queryguide/relationships.html) |
| Q15 数据 | Redis和PG数据不一致怎么办？ | 权威数据源、cache-aside失效/TTL/回填竞态，按一致性目标设计 | DB更新而缓存旧值，记录错误窗口和回源流量 | D01/D02 · [官方](https://redis.io/docs/latest/) |
| Q16 工程 | 镜像、容器、Volume区别？ | 模板层、运行进程实例、容器外持久存储的生命周期 | 删容器重建，验证数据卷是否保留 | E02 · [官方](https://docs.docker.com/get-started/docker-concepts/) |
| Q17 工程 | 本地项目怎样可复现部署？ | 构建、版本、配置密钥、TLS/反代、迁移、健康检查与恢复 | 干净VM验证启动/端口/迁移/备份恢复 | E02/P03 · [官方](https://docs.docker.com/compose/) |
| Q18 工程 | API P95从200ms到3s怎么查？ | 在相同负载口径下看RED指标、Trace、锁/DB/外部依赖 | 注入慢SQL并沿trace定位，复测P95 | E04 · [官方](https://opentelemetry.io/docs/) |
| Q19 工程 | 新版本出错如何安全回滚？ | 配置、数据库Schema前后兼容、回滚与恢复的不同操作 | 模拟新旧代码/迁移兼容与失败演练 | P03/E02 · [官方](https://docs.github.com/en/actions) |
| Q20 设计 | 多用户SaaS的权限、上传和异步怎么设计？ | 资源级授权、对象存储、元数据事务、幂等任务、轮询/SSE及恢复 | A访问B文件、Worker重启、断连/重放/恢复负例 | P02/E03/B06/D01 · [官方](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) |

## 分层评价与怎么使用

- **L1原理**：不看资料解释机制、技术层次、失败会怎样；能说明大白话比喻哪里不成立。
- **L2独立应用**：关AI完成带变化条件的代码/SQL修改，跑正负例，提供commit、命令和测试日志。
- **L3工程掌握**：分析越权、并发、性能、恢复/回滚取舍，基于监控/Trace定位问题；不以本地Demo声称线上经验。

每次从20题中只挑与当前需求/JD密切相关的几题；如果是Java岗位，把FastAPI替换为B03/B04/B05案例进行迁移答辩；如果是Vue岗位，用F08替换F04。第14天可选做5题模拟面试，参见[可选14天冲刺](OPTIONAL-EXECUTION-MODES.md)。

答辩记录写[需求驱动会话卡](GAP-SESSION-TEMPLATE.md)，个人能力证据记[PROGRESS](PROGRESS.md)。**AI给出标准答案不算本人通过**。
