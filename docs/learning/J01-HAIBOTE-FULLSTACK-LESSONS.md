# J01｜海博特全栈面试：15 节学习路径与独立验收

> **性质：一个针对 J01 的可选专题导航，不是第二份 ROADMAP、知识图、学员进度或强制先修。** 仍以 [42 节点知识图](KNOWLEDGE-GRAPH.md) 为技术坐标，以 [PROGRESS](PROGRESS.md) 为唯一学习证据台账。教程写好 ≠ 本人已学会，当前均为 NOT_RUN / UNASSESSED。
>
> **立即开始**：[L00 完整逐行教程与可运行实验](labs/J01-L00-WEB-REQUEST-TUTORIAL.md)，包含概念解释、代码、运行、独立变式和验收。后续 L01–L14 对应原有 [42 节点学习卡](NODE-STUDY-CARDS.md)、[权威资料](OFFICIAL-RESOURCES.md)，不虚构已经写成 15 本完整教材。

## 0. 学编程到底是学概念，还是敲代码？

**两者都要，但方式不同。**

| 面对什么 | 正确学习动作 | 不算学会的行为 |
|---|---|---|
| 概念（HTTP、响应式、事务） | 能说清是什么、解决什么、输入输出、什么情况不适用 | 背一个术语定义 |
| 10～30 行最小示例 | 自己敲并运行，不看答案预测结果，再改一个条件 | 跟着复制一次 |
| 50～200 行组件 | 看清事件→状态→API 主线，主动修改一个功能 | 原样手抄整个文件 |
| 几百行后端模块 | 追踪关键函数、权限、数据流、错误处理和测试 | 记住每一行语法 |
| 已有项目/AI Coding | 先提出验收条件，再读代码、实现/审查、跑正负例、解释失败 | AI 生成/CI 绿就声称本人掌握 |

**每节统一六步**：①大白话概念（约10分钟）→②10～30行关键代码逐行拆解（10分钟）→③关答案亲手实现（20分钟）→④独立变式（15分钟）→⑤负例与排错（10分钟）→⑥三道面试追问（10分钟）。时间只是参考，可跳过已通过独立测评的内容，也可对困难节点追加时间。

**本仓能力标准不是聊天中口头提及的“五级”**，统一使用 [AI-CODING-POLICY](AI-CODING-POLICY.md)：

- **仓库 L1 理解**：关文档能解释原理、输入输出、限制和失败路径。
- **仓库 L2 独立应用**：本人关 AI 独立完成变化条件的编码与正负例测试。
- **仓库 L3 工程掌握**：能故障注入、诊断、修复、复测并解释可靠性/安全等取舍。
- **五项检查是观察动作而非新等级**：概念讲清、代码看懂、自己写、能改新需求、能测试排错。
- 学习目标：前端、FastAPI、SQL 优先争取 L2；Java/Redis/Gateway 先达到 L1、实际修改并测试后争取 L2；关键排障再争取 L3。没有本人实验不填 PASS。

## 1. 从零到 J01：15 节具体学什么、做什么？

| 节次 | 对应现有节点 | 这节要理解的具体知识 | 自己必须做的操作与验收 |
|---|---|---|---|
| **L00 全栈请求链路** | F01/B01/P02 | 浏览器、前端、后端、API、URL、GET、JSON、200/404/422 分别是什么 | 跟 [L00 完整教程](labs/J01-L00-WEB-REQUEST-TUTORIAL.md) 运行 Python + HTML；独立增加省份筛选，看浏览器 Network |
| **L01 HTML/CSS** | F02 | HTML 标签/属性、label/input/button/list、id/class、盒模型、Flexbox、键盘可访问性 | 写一个有标题、搜索框、按钮、列表的页面；改窄屏布局，Tab 可操作 |
| **L02 JavaScript** | F03 | const/let、函数、数组对象、filter/map/forEach、DOM、click事件、try/catch | 不看答案做列表关键词筛选；添加重置按钮，故意制造错误再排查 |
| **L03 HTTP/REST/JSON** | F01/B01 | URL组成、query/path/body、GET/POST、头部、状态码、同源/CORS、fetch | 用浏览器Network和curl观察正常/错误响应，说明为何返回 JSON |
| **L04 TypeScript** | F03 | interface/type、联合类型、可选字段、null、Promise泛型、静态类型边界 | 为学校列表定义类型，让错误字段触发 typecheck 并修复 |
| **L05 Vue 3核心** | F08/F02 | SFC、template、script setup、ref/reactive、computed、v-model、v-if/v-for、@click | 自己写一个搜索组件；不看答案新增清空功能并验证 |
| **L06 Vue组件/Pinia/Router** | F08/F07 | props/emits、路由切换、组件本地与跨组件共享状态、Pinia Setup Store | 追踪 Gaobao 的 filters→loadSchools；做快捷985筛选并验收分页 |
| **L07 API/SSE/异常** | F03/F08/B01/F11 | async/await、AbortController、loading/empty/error、401/403、SSE vs WebSocket | 查 adminApi 请求封装；模拟断网和空数据；区分普通 GET 和聊天 SSE |
| **L08 FastAPI** | B02/B01/E03 | 路由装饰器、Query/Pydantic、Depends 鉴权、Route/Service/Repository 分工 | 找到学校查询路由并追至 Repository；写非法参数422测试 |
| **L09 MySQL/SQL/ORM** | D01/D04/B02 | SELECT/WHERE/排序/分页、索引、EXPLAIN、事务、乐观锁、SQLAlchemy | 解释分页SQL，验证无效排序，独立更改查询条件 |
| **L10 权限/Redis/异步** | E03/D02/B06/D03 | 认证≠授权，RBAC、幂等键、任务状态、Outbox、Redis限流与429/503 | 查看 admin 角色依赖与质检任务；跑权限、重复请求负例 |
| **L11 Java/Spring/Gateway** | B03/B04/B05/D02 | Java类/注解、Controller/Repository、依赖注入、Gateway路由、Lua原子限流/fail-closed | 阅读 Catalog Controller、Gateway filter 与 JUnit；区分选配服务与生产环境 |
| **L12 Docker/Compose/Nginx** | E02 | 镜像/容器/卷、端口、服务网络、反向代理、健康检查、环境变量与日志 | 在合成环境启动默认服务；按文档可选验证 Java overlay |
| **L13 测试/CI** | E01 | pytest、Vitest、JUnit、红绿测试、契约/CI、测试环境与生产的区别 | 故意破坏一个断言→看到失败→修复→保留真实日志 |
| **L14 综合全链路与面试** | P02/B01/E01/E03 | 90秒经历、3分钟架构、5分钟代码穿透、失败与能力边界 | 展示真实文件/PR/测试；回答5道故障追问，指出尚未验证的地方 |

这 15 节是**为了这个岗位选出的教学顺序**，不是普遍强制先修链。已能独立用 Python 可跳过通用编程概念；当前只有 Vue 需求就不必先学深度 Java；临近面试可先练 L00、L05～L09、L11～L14，再补自己的短板。

## 2. 实战主线：Gaobao-Advisor 管理后台

这个项目**不是本学习仓新建立的业务代码**，而是本次外部参考和可选授权练习载体。

| 组件 | 真实代码 | 重点追问 |
|---|---|---|
| Vue 页面 | [AdminDataPanel.vue](https://github.com/Xander-Xai/Gaobao-Advisor/blob/master/frontend/src/components/admin/AdminDataPanel.vue) | 搜索/分页/空状态/错误如何触发 |
| Pinia | [stores/admin.ts](https://github.com/Xander-Xai/Gaobao-Advisor/blob/master/frontend/src/stores/admin.ts) | filters、schoolsLoading、loadSchools |
| TypeScript 请求 | [api/admin.ts](https://github.com/Xander-Xai/Gaobao-Advisor/blob/master/frontend/src/api/admin.ts) | 查询参数、Bearer、超时与错误信封 |
| TypeScript 类型 | [types/admin.ts](https://github.com/Xander-Xai/Gaobao-Advisor/blob/master/frontend/src/types/admin.ts) | SchoolQuery 和 Page 泛型 |
| FastAPI | [server/admin/routes.py](https://github.com/Xander-Xai/Gaobao-Advisor/blob/master/server/admin/routes.py) | 服务器权限、参数验证、返回模型 |
| Repository | [server/admin/repository.py](https://github.com/Xander-Xai/Gaobao-Advisor/blob/master/server/admin/repository.py) | SQLAlchemy过滤、排序白名单、分页 |
| API 测试 | [test_admin_schools.py](https://github.com/Xander-Xai/Gaobao-Advisor/blob/master/tests/test_admin_schools.py) | 合成数据、无效排序/页码 |
| Java 目录 API | [SchoolCatalogController.java](https://github.com/Xander-Xai/Gaobao-Advisor/blob/master/java-services/catalog/src/main/java/com/xsuperplay/gaobao/catalog/SchoolCatalogController.java) | 独立只读路由与 JDBC 查询 |
| Java 限流 | [Gateway filter](https://github.com/Xander-Xai/Gaobao-Advisor/blob/master/java-services/gateway/src/main/java/com/xsuperplay/gaobao/gateway/FailClosedCatalogRateLimiterGatewayFilterFactory.java) | Redis Lua、429、503、故障拒绝 |
| 启动验证 | [Java可选部署手册](https://github.com/Xander-Xai/Gaobao-Advisor/blob/master/docs/java-microservices.md) | 默认 Python/SQLite 与可选 Java/MySQL/Redis 的区别 |

历史证据：[PR #32](https://github.com/Xander-Xai/Gaobao-Advisor/pull/32) 管理后台和 [PR #89](https://github.com/Xander-Xai/Gaobao-Advisor/pull/89) Java 服务已合入该项目。**该项目仍明确标注公网生产 NO-GO**；历史 CI、模拟招生数据和单宿主机短时测试不能证明生产SLA或你本人已独立掌握。

**第一项迁移练习（设计态、尚未修改项目）**：在 AdminDataPanel 增加“快捷筛选985院校”，复用已有 Pinia filters.level 和 loadSchools(1)，观察 Network、空/错误/加载状态与分页归一，并补对应前端测试。改动应在自己的独立实验分支完成。

## 3. 一节课如何判断真正学会？

每节的讲授和验收都使用相同模板：

1. 用自己的话解释技术作用、上下游关系和限制。
2. 解释 10～30 行关键示例，并预测输出。
3. 关闭完整答案，**亲手写**一个最小功能（语法可查官方文档）。
4. 对原题施加**新约束**：比如筛选从名称变成名称+省份。
5. 运行正例和至少一个负例，定位修复，再独立复述。
6. 用 [GAP 会话卡](GAP-SESSION-TEMPLATE.md) 记录环境、实际代码、命令、输出、失败/修复和 AI 参与范围；**仅在 [PROGRESS](PROGRESS.md) 记状态**。

### AI 导师授课提示词

~~~text
你是我的 J01 全栈技术导师。先读 docs/learning/J01-HAIBOTE-FULLSTACK-LESSONS.md，
以及当次单元对应的旧知识节点、学习卡和官方资料。
如果教 L00，必须以 labs/J01-L00-WEB-REQUEST-TUTORIAL.md 为完整教材。
一次只讲一个知识点：用大白话解释→给10～30行示例逐行讲→让我预测输出→
给我亲手写的任务→我提交后检查→出一个变式与负例→三道面试题。
不能只给课表或网址，也不要抢先把我正在考核的代码完整写好。
我不会时先分层提示，最后才给参考答案。未经真实执行不能写 PASS。
学习记录遵循 AI-CODING-POLICY.md 的 L1/L2/L3 与 PROGRESS.md 唯一台账。
不自动修改 Gaobao 项目、生产服务或外部用户数据。
~~~

## 4. 继续学习的准确入口

- [L00 完整教程：HTML/CSS/JavaScript/FastAPI/HTTP/JSON](labs/J01-L00-WEB-REQUEST-TUTORIAL.md)
- [前端专业参考](references/frontend.md) · [后端专业参考](references/backend.md)
- [所有知识节点学习卡](NODE-STUDY-CARDS.md) · [官方细分链接](OFFICIAL-RESOURCES.md)
- [面试工程题20问](INTERVIEW-ENGINEERING-DRILLS.md) · [可选14天/8周节奏](OPTIONAL-EXECUTION-MODES.md)

**本次内容状态：** J01导航已编写，L00有逐行教程和代码，L01–L14已有现存节点的资料/精确练习地图，但**没有在本次假装生成另外14份完整逐行教材**；实际授课应按需补足，学员验收仍全部 NOT_RUN。
