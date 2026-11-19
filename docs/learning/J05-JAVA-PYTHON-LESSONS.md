# J05｜Java/Spring Boot 微服务与 Python 全栈集成：从零学习路径

> **性质：**面向 J05 面试问题的可选专题课，不是第二份 ROADMAP、强制先修链或独立进度台账。知识位置沿用[42 节点图](KNOWLEDGE-GRAPH.md)，学习状态只记[PROGRESS](PROGRESS.md)，方法遵循[通用学习执行法](LEARNING-BY-EVIDENCE.md)。本路线起始状态为 `NOT_RUN / UNASSESSED`；有课程不等于学会。
>
> **真实性边界：**本课程中的 Gaobao-Advisor 源码、PR、CI 与部署表述，凡未在本次核对具体源码或运行记录的，一律标作“材料所述、待核验”。本仓目前没有可直接复用的 Spring 工程。Java Gateway/Catalog、项目 CI 等可按有证据范围讲述；Transactional Outbox、Redis List 与 Worker 若在相关源码中确认，才可称已有实现；医疗文件 OCR、Java MQ 消费者和生产级多租户系统属于设计练习或待实施，不得冒充现有功能。合成实验、项目 CI 和个人能力是不同证据。

## 怎么用这条路线

- 建议顺序是 **J05-00 → 01…17**，因为学习者当前自述尚未学过这些内容；这是本次面试专项的教学顺序，不是仓库对所有项目的强制路线。
- 每单元执行：**预测 → 原理与小例 → 半引导 → 独立变式 → 正/负例 → 口述**。先 H1 方向、再 H2 定位、再 H3 局部伪代码；练习前不直接给完整答案。
- `L1`：闭卷解释作用、机制、边界，并预测流程。`L2`：本人独立实现变化条件，运行适用正/负例。`L3`：独立故障注入、定位、修复、复测并说明取舍。不是每节都要求 L3。
- 文档中的“验收任务”是学习设计，不是执行记录。未实际运行标 `NOT_RUN`；在[会话卡](GAP-SESSION-TEMPLATE.md)记证据，只在 `PROGRESS.md` 更新状态。相关 Gxx 按题目选择，不要求所有 Gate 顺序通关。
- 代码阅读以你有权限访问的实际项目和确定版本为准。找不到源码时，使用合成练习，不猜文件内容。

## 课程总览

| 阶段 | 单元 | 结果目标 | 对应节点/验收参考 |
|---|---|---|---|
| 0 证据校准 | 00 | 不混淆代码、测试、生产及设计证据 | P02 / E01 |
| 1 服务与集成 | 01–06 | 请求拓扑、Java/Spring、Gateway/限流、跨语言 API、Docker/CI | F01、B01–B04、E01/E02/E05；按范围参考 G09/G10/G13/G15 |
| 2 数据与可靠性 | 07–14 | SQL/MySQL、索引、事务并发、缓存、Outbox、Worker、Python 并发 | B02/B05/B06、D01–D04、E03；按范围参考 G13/G15/G24 |
| 3 综合设计与答辩 | 15–17 | 文件处理设计、故障定位、独立综合答辩 | D05、E01/E02/E04、P02；G24 仅适用于其明确定义的范围 |

> 本路线涉及 MySQL，节点 D01/D04 是仓库 SQL/数据库基础与 MySQL 差异入口，学习时应用 MySQL 官方资料；不要把知识图中 PostgreSQL 的代表资料误当成 MySQL 的全部规范。

## 阶段 0：证据校准

### J05-00｜从项目声明到可辩护证据

**目标 / 前测：**读一句“服务已上线并通过 CI”，先说你需要什么证据才能相信它。

**固定内容：**源代码能证明实现存在；测试报告能证明特定环境、版本和断言通过；部署记录、监控与运行责任证据才能支持“已部署/运行”；架构图或面试答案只是设计/解释。一个 PR 合入也不等于本人独立完成。演示环境通过不能推出生产 SLA。

**大白话：**菜谱写着有一道菜（设计）；厨房里能做出来（代码）；有人按标准试吃过（测试）；餐厅持续对外供应并有人值守（生产）。前一项不能替代后一项。

**例子与任务：**把“Java Catalog 已完成”拆成：代码在哪里、接口如何启动、哪些测试/CI 验证、数据是合成还是生产、部署在哪。每项标 `源码 / 测试 / 生产 / 设计 / 待核验`。

**负例与变式：**CI 的单元测试通过，但 Compose 联调没跑，能否说“Java/Python/MySQL 已集成验证”？不能；变式改成 Compose 通过但只有合成数据，准确措辞是什么？

**验收 / 追问：**闭卷分清“已实现、已验证、已上线”；解释一个证据不能证明什么。目标 L1。问：哪些证据能证明个人独立掌握？答案需包含本人完成的陌生变式与真实验证，不是代码存在。

**资料：**[本仓证据学习法](LEARNING-BY-EVIDENCE.md)；[进度状态定义](ACCEPTANCE.md)；[项目边界](REPOSITORY-INDEX.md)。

## 阶段 1：真实服务与 Java/Spring 集成

### J05-01｜一次全栈请求走过哪些服务

**目标 / 前测：**浏览器访问一个院校列表，列出请求到达和返回可能经过哪些层。

**固定内容：**浏览器发 HTTP；Nginx 可终止 TLS/反向代理；Gateway 按路径路由、可执行过滤；FastAPI/Spring Boot 提供业务 API；数据库持久化；响应沿调用链返回。端口是进程监听的网络入口，不是服务职责。SSE 是 HTTP 响应流，WebSocket 是升级后的双向连接，路由配置不同。

**大白话：**Nginx 像大楼门卫按楼层指路，Gateway 像业务总台按请求类别分派，服务才是办事窗口；门卫不替窗口完成业务。

**示例：**假设 `/api/v1/catalog/schools` 指向 Java Catalog，`/api/v1/chat` 指向 FastAPI。请求包含 method、path、headers；响应包含 status、headers、body。这里是教学拓扑，不代表某项目配置已核实。

**动手：**在纸上画 Vue/浏览器→Nginx→Gateway→Java/Python→MySQL/Redis；在每条箭头写协议/数据。用[现成 J01 请求实验](labs/J01-L00-WEB-REQUEST-TUTORIAL.md)复习浏览器→FastAPI，不另造项目。

**负例与变式：**Gateway 不可用会不会由前端自动绕过？不一定，取决于网络拓扑；变式把 SSE 改为 WebSocket，指出必须重新核对哪些代理配置。

**验收 / 追问：**追踪单个 GET 的请求和响应；说出 Gateway 不负责什么。目标 L1。问：Java 和 Python 为什么并存，如何避免为了技术栈重写成熟业务？

**资料：**[HTTP 概览](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview)、[OpenAPI](https://spec.openapis.org/oas/latest.html)、[Spring MVC](https://docs.spring.io/spring-boot/reference/web/servlet.html)。

### J05-02｜Java 基础：类、对象、方法、集合与异常

**目标 / 前测：**给出学校对象，解释“类型”和“某条学校记录”有什么不同。

**固定内容：**类描述对象的字段/行为；对象是运行时实例；方法接收参数并返回值；构造方法初始化对象；接口描述可替换行为契约；异常表达无法按正常路径完成的情况。Java 编译成 JVM 可运行的字节码；JDK 含编译和开发工具，JVM 负责运行字节码。

**小例：**`record School(long id, String name) {}`（现代 Java record；普通 class 亦可）。`List<School>` 是一组 School；泛型约束集合元素类型。不要把 `null` 与“空集合”当成同一概念。

**半引导：**为合成 School 写 `matchesName(School school, String query)`，先规定大小写与空字符串行为，再实现。检查 `null` 是否允许并一致处理。

**负例与变式：**空 query 若被当成包含任意名称，是否符合需求？变式增加 province 筛选。目标 L1→L2（需真实编译/测试）。

**验收 / 追问：**解释 class/object/interface/exception 的边界；指出一个非法输入如何处理。问：`Optional` 能否用来替代所有字段的 null？不能，需按 API 语义选择。

**资料：**[Dev.java Learn](https://dev.java/learn/)、[JDK 工具概览](https://docs.oracle.com/en/java/javase/21/docs/specs/man/javac.html)、[Maven 入门](https://maven.apache.org/guides/getting-started/index.html)。具体版本按仓库版本策略确认。

#### Java 集合、泛型、Map、Optional 与 JUnit（J05-02 后半）

**目标 / 前测：**一组 School 中按省份找记录，用什么结构保存有序列表，按 ID 查找？

**固定内容：**`List<T>` 表示有序元素序列；`Map<K,V>` 以键查值；泛型在编译期约束类型；`Optional<T>` 表示可能没有值的返回语义，不是所有字段的通用包装；单元测试检查一个可隔离的逻辑规则。

**示例任务：**对 `List<School>` 过滤名称和省份；定义空列表、无匹配、重复 ID 的预期。先口算输出，再写方法和 JUnit 正反例。

**变式：**列表可能有重复学校 ID，决定保留首个、拒绝重复或返回多值，并用测试固定规则。**负例：**不匹配时返回 `null` 导致调用处 NPE。

**验收 / 追问：**闭卷解释 List/Map 差异；能说明测试断言验证的条件及未覆盖的行为。目标 L1/L2。

**资料：**[Java Collections](https://dev.java/learn/api/collections-framework/)、[JUnit 5 User Guide](https://junit.org/junit5/docs/current/user-guide/)。

### J05-03｜Spring Boot 与分层：IoC、Bean、Controller 到 Repository

**目标 / 前测：**Controller 为什么不应该在每次请求里自己 `new` 数据库连接？

**固定内容：**IoC 将对象创建/依赖组装交给容器；Bean 是由 Spring 容器管理的对象；依赖注入把合作对象提供给类；配置外置环境差异。Spring Boot 提供自动配置和应用启动机制，不会自动让代码正确或安全。

**调用链：**启动→组件扫描/配置→容器创建 Bean→注入依赖→服务器监听→收到请求。构造器注入通常使依赖清晰且便于测试。

**练习：**阅读一个最小 `@RestController` 及构造器注入，不新增真实项目配置；画对象依赖图。设计一个不存在路径的测试，预期 404（具体错误响应形状取决于配置）。

**负例/变式：**循环依赖或漏注册 Bean 导致启动失败；变式替换 Repository 实现，说明为什么依赖接口有帮助。

**验收 / 追问：**说明 Bean 生命周期只需到“容器创建并提供依赖”的层次；目标 L1。问：Spring Boot 自动配置是否等于生产配置已安全？否。

**资料：**[Spring Boot Web/Servlet](https://docs.spring.io/spring-boot/reference/web/servlet.html)、[Externalized Configuration](https://docs.spring.io/spring-boot/reference/features/external-config.html)。

#### Controller、Service、Repository 与参数化 SQL（J05-03 实作）

**目标 / 前测：**一个 HTTP 查询参数怎样变成数据库查询结果？

**固定内容：**Controller 负责 HTTP 输入输出；Service 放业务规则/编排；Repository 封装持久化访问。小应用不一定必须有三层空壳，分层应让变化和测试更清晰。参数化 SQL 把数据作为参数，不拼接用户输入为 SQL 语法。

**例子：**`SELECT id,name FROM schools WHERE province = :province`。参数安全不意味着查询一定快，也不能代替授权和租户条件。

**练习：**对合成表添加 province 查询；列出输入、SQL 参数、返回 DTO。正例为存在省份，负例为未知省份/非法分页。变式增加查询限制，使用白名单允许排序列，不能直接拼接任意 order 参数。

**验收 / 追问：**口述 Controller→Service→Repository→DB→返回链路；解释参数化 SQL 防什么、不防什么。目标 L1，实际修改并测试后 L2。

**资料：**[Spring JDBC](https://docs.spring.io/spring-framework/reference/data-access/jdbc/core.html)、[OWASP SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)。

### J05-04｜Spring Cloud Gateway 与 Redis 共享限流

**目标 / 前测：**反向代理与业务 API 各自做什么？

**固定内容：**Gateway 根据路由谓词选目标服务，Filter 可在转发前后处理请求/响应；路由配置必须考虑超时、错误映射、头部和敏感信息。Spring Cloud Gateway 常用 Reactor/WebFlux 响应式模型；`Mono<T>` 代表 0/1 个异步结果，不等于开新线程，也不应在事件循环中随意阻塞。

**练习：**根据假设路由表标出 Catalog、chat、SSE、WebSocket 目标；对于下游 404、超时、连接失败分别写预期响应策略。负例：转发不可信的身份头，造成信任边界错误。

**变式：**下游 Java 暂时不可达，Gateway 返回何种状态/错误体？说明需以服务合同为准，不能杜撰固定行为。

**验收 / 追问：**解释 Gateway 不是数据权限的唯一防线；目标 L1。问：为何响应式链路里的阻塞调用会拖累并发？

**资料：**[Spring Cloud Gateway Reference](https://docs.spring.io/spring-cloud-gateway/reference/)、[Reactor Core Reference](https://projectreactor.io/docs/core/release/reference/)。

#### Redis Lua 限流与失败关闭（J05-04 实作）

**目标 / 前测：**两个 Gateway 实例各自做本地限流，是否构成共享的全局限流？

**固定内容：**共享 Redis 状态可让多个实例按同一租户/来源协调限流。Lua 脚本在 Redis 单命令执行上下文中原子执行一段检查和更新；令牌桶按时间补充令牌，请求消耗令牌；超限一般返回 429。Redis 不可用时 fail-closed 拒绝请求（例如 503）会牺牲可用性换取保护，fail-open 则相反，必须由威胁和业务要求决定。

**练习：**画两个实例共享 token key 的时序；给出额度已满、剩余 1 个令牌、Redis 超时三种预测。用伪代码先判断，再根据获授权项目的实际实现核验。

**负例/变式：**仅先 GET 再 SET 会有并发竞态；Key 未包含租户可能互相影响。变式为不同租户独立额度。

**验收 / 追问：**区分令牌桶与缓存；说明 429 与 503 的意义需依合同。目标 L1；实现/测试后 L2。

**资料：**[Redis programmability](https://redis.io/docs/latest/develop/programmability/)、[HTTP 429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429)、[HTTP 503](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/503)。

### J05-05｜Java/Python 跨服务接口与实时协议

**目标 / 前测：**同一“学校列表”接口怎样保证两个服务返回语义一致？

**固定内容：**API 契约定义 path/method/query、JSON 字段、分页、错误、认证、超时。HTTP 401 通常是未认证，403 通常是已识别但无权限；具体 API 合同需明确。SSE 单向服务端事件，适合服务端持续推送；WebSocket 双向消息。代理、超时、断线重试都要按协议处理。

**练习：**写一份字段/状态码分页契约，对比两实现的正例、空结果、非法 cursor、未授权结果。请求头透传只允许明确白名单，不能盲目转发 hop-by-hop 或不可信身份头。

**负例/变式：**Java 返回 `next_cursor` 字符串，Python 返回数字，客户端类型不一致；变式增加一个字段，讨论向后兼容。

**验收 / 追问：**画调用链并解释哪个服务负责鉴权；目标 L1/L2。问：客户端超时后可否无条件重放 POST？只有幂等契约支持时才可。

**资料：**[OpenAPI](https://spec.openapis.org/oas/latest.html)、[SSE 使用](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events)、[WebSocket API](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)。

### J05-06｜Docker Compose 与 CI/CD 验证

**目标 / 前测：**容器启动成功是否证明应用功能正确？

**固定内容：**镜像是应用及运行环境的打包产物；容器是其运行实例；Compose 编排本地多容器网络；环境变量提供环境配置但不应泄密；healthcheck 是服务健康信号，不能替代端到端功能测试。CI 按工作流执行构建/测试，结论仅覆盖命令、版本、数据和断言。

**练习：**读 Compose 片段，标出服务、端口、依赖、健康检查和持久卷；阅读一份 Maven/JUnit、pytest 或 Compose CI 日志，归纳它能/不能证明什么。负例：只看容器 `running` 就声称接口可用。变式：依赖 MySQL 健康但应用仍连接失败，排查 DNS、凭据、数据库名和日志。

**验收 / 追问：**能复述一个测试命令的输入和退出结果；未实际运行时标 `NOT_RUN`。目标 L1。

**资料：**[Docker Compose](https://docs.docker.com/compose/)、[GitHub Actions workflow syntax](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions)、[Maven verify 生命周期](https://maven.apache.org/guides/introduction/introduction-to-the-lifecycle.html)。

## 阶段 2：数据库、缓存和可靠性

### J05-07｜MySQL 与 SQL 入门

**目标 / 前测：**一个订单写入后，如何查找并验证它确实持久化？

**固定内容：**表由行和列组成；主键标识行；约束由数据库保护数据规则；SELECT/INSERT/UPDATE/DELETE 操作数据。事务把一组数据库操作作为一个提交/回滚单元。InnoDB 提供事务能力；自动提交、隔离级别和锁行为按实际配置及 MySQL 版本核对。

**例子：**`START TRANSACTION; INSERT ...; SELECT ...; COMMIT;`。在合成库里插入一行，再用 `ROLLBACK` 练习撤销；不得连接生产库。

**负例/变式：**对不存在主键更新影响 0 行；增加 NOT NULL/唯一约束，预测重复值结果。目标 L1/L2。

**验收 / 追问：**解释 commit 与 rollback；说明“事务成功”只覆盖该事务所在数据库，不自动覆盖 Redis/MQ。资料：[MySQL 8.4 InnoDB Transactions](https://dev.mysql.com/doc/refman/8.4/en/innodb-transaction-model.html)、[SQL Tutorial](https://dev.mysql.com/doc/refman/8.4/en/tutorial.html)。

### J05-08｜复合索引、分页与慢查询

**目标 / 前测：**租户审核列表按状态筛选并按更新时间倒序，怎样减少扫描？

**固定内容：**B-Tree 索引保存排序键以减少候选扫描；复合索引按列序组织，左侧前缀影响可用性；查询可能回表读取未在索引中的列。优化必须以真实执行计划和数据分布验证，不能只背口诀。

**示例任务：**针对 `WHERE tenant_id=? AND status=? ORDER BY updated_at DESC, id DESC LIMIT 20`，提出候选 `(tenant_id,status,updated_at,id)`。解释 id 作为稳定排序的 tie-breaker。使用 `EXPLAIN`/适用版本的 `EXPLAIN ANALYZE` 对比，不预设一定消除 filesort。

**负例/变式：**只按 `status` 查询通常无法直接利用复合索引左侧完整前缀；变式去掉 tenant 条件，重新分析计划。目标 L1/L2。

**验收 / 追问：**解释 key、rows、Extra 和实际耗时分别代表什么；区分估算与实测。资料：[MySQL 8.4 Optimization and Indexes](https://dev.mysql.com/doc/refman/8.4/en/optimization-indexes.html)、[EXPLAIN](https://dev.mysql.com/doc/refman/8.4/en/explain.html)。

### J05-09｜事务、并发更新与乐观锁

**目标 / 前测：**两个审核员同时审批一条待审核记录，怎样避免后一个静默覆盖前一个？

**固定内容：**数据库并发下“先 SELECT、再 UPDATE”存在检查后竞争；唯一约束让数据库最终裁决唯一性；乐观锁用版本号/状态条件更新，更新 1 行表示条件成立，0 行表示冲突或对象不匹配，需按安全策略区分错误。悲观锁通过锁定保护竞争区域但带来等待和死锁风险。

**示例：**`UPDATE documents SET status='APPROVED', version=version+1 WHERE id=? AND tenant_id=? AND version=? AND status='PENDING';`。此 SQL 为合成示例，尚未运行。

**练习：**推演两个事务携带同一版本同时更新；必须只有一个影响 1 行。变式要求同一幂等键相同请求返回原结果、相同键不同请求体拒绝。负例是只在应用层查“是否待审核”。

**验收 / 追问：**说明 409 可表示版本冲突的合同选择，不能笼统认为所有 0 行更新都是 409；目标 L1，实测后 L2。

**资料：**[InnoDB Transaction Model](https://dev.mysql.com/doc/refman/8.4/en/innodb-transaction-model.html)、[HTTP 409](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/409)、[OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)。

### J05-10｜Redis Cache-Aside 与租户隔离

**目标 / 前测：**查询数据时 Redis miss 应做什么？数据库更新后缓存怎样避免长期旧值？

**固定内容：**Cache-Aside 通常先读缓存，miss 查数据库并回填 TTL；写入时先提交数据库，再失效相关缓存。TTL 限制陈旧窗口；随机抖动可分散同时过期。缓存 Key 必须涵盖租户和影响结果的查询/权限维度。高变化列表可能不适合缓存。

**例子：**key `doc:{tenant_id}:{document_id}`；缓存 miss 后查询必须同时按 tenant_id 和 id 限定。写后删除缓存仍可能遭遇并发旧值回填；版本化 key/版本检查是备选而非魔法保证。

**负例/变式：**遗漏 tenant_id 导致跨租户数据泄露；并发旧请求在失效后回填旧值。验收目标 L1/L2。

**资料：**[Redis EXPIRE](https://redis.io/docs/latest/commands/expire/)、[OWASP Multi-Tenant Security](https://cheatsheetseries.owasp.org/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.html)。

### J05-11｜Transactional Outbox：数据库和消息双写

**目标 / 前测：**数据库提交成功，但消息发送失败，业务会发生什么？

**固定内容：**DB 与 Redis/MQ 是独立系统，普通本地事务不能原子提交两边。先写 DB 再发消息可丢事件；先发消息再写 DB 会让消费者看见未提交状态。Outbox 把业务记录与待发事件在同一个 DB 事务内提交；后台发布器扫描待发记录并投递。投递可重复，消费者必须幂等。Outbox 提供可靠重试基础，不等于 exactly-once。

**教学表：**`outbox_events(event_id UNIQUE, aggregate_id, event_type, payload, status, attempts, next_attempt_at)`；真实生产还需保留/归档、并发领取/锁或租约、顺序策略、监控与毒消息处置。

**练习：**画 DB commit 前崩溃、commit 后 publish 前崩溃、broker 接收但 ACK 丢失三个窗口。对每个窗口预测 DB/outbox/消息状态；设计唯一 event_id。变式把 Redis List 换 RabbitMQ：讲清抽象概念可迁移，具体 ack/可见性语义需重学。

**负例：**把“数据库与消息最终一致”说成“原子提交”或“只投递一次”。目标 L1；完成实验后 L2。

**资料：**[Transactional Outbox pattern (AWS Prescriptive Guidance)](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html)、[RabbitMQ Acknowledgements](https://www.rabbitmq.com/docs/confirms)。

### J05-12｜发布器、重试、退避与死信

**目标 / 前测：**发布失败时立刻无限重试有什么后果？

**固定内容：**发布器读取到期事件，安全领取后发送，收到确认再标记已发布；确认窗口有歧义时允许重复。退避可减少下游压力；重试要有上限/告警，永久错误进入人工处理或死信。多个发布器需原子领取、租约/锁及过期恢复；事件顺序只在业务需要时维护。

**练习：**用纸面模拟失败两次后成功；列 `attempts` 和 `next_attempt_at` 变化。设计“临时网络错误”和“无效事件载荷”不同策略。

**负例/变式：**发布成功但更新 Outbox 前进程崩溃→事件再发；变式连续失败到上限后怎样可观测、可重放？目标 L1。

**资料：**[AWS Outbox pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html)、[RabbitMQ Publisher Confirms](https://www.rabbitmq.com/docs/confirms)。任何数据库锁/领取 SQL 要按数据库版本验证，当前为设计练习。

### J05-13｜Worker 状态机、幂等与 Fencing Token

**目标 / 前测：**Worker 领取任务后崩溃，任务怎样再处理？

**固定内容：**任务状态可含 PENDING/RUNNING/SUCCEEDED/FAILED；租约允许超时回收；attempts 可限制重试；幂等键/唯一约束抑制重复业务效果。Fencing token 是单调递增的所有权代数，写结果时要求 token 仍为最新，避免暂停后恢复的旧 Worker 覆盖新 Worker。它必须由存储端条件更新强制，不能只在进程内比较。

**练习：**画 Worker A 获 token 4 后暂停、Worker B 获 token 5 并成功、A 恢复的时序；写出 A 更新条件必须失败。区分消息 ACK、任务状态、外部副作用。

**负例/变式：**邮件已发送但 Worker 在记录成功前崩溃，数据库去重不能撤销邮件；需要外部幂等键或补偿。变式任务不可重试时设终态。目标 L1/L2；故障实验为 L3 证据候选。

**资料：**[Celery Tasks: retries and idempotency](https://docs.celeryq.dev/en/stable/userguide/tasks.html)、[RabbitMQ Consumer Acknowledgements](https://www.rabbitmq.com/docs/confirms)。Redis List、BRPOP、BLMOVE、Streams 的具体语义必须按实现/版本核实，不能统称 MQ。

### J05-14｜FastAPI asyncio、线程池、进程池与任务队列

**目标 / 前测：**在 `async def` 路由中运行 CPU 重计算，会自动并行吗？

**固定内容：**asyncio 用协程在等待 I/O 时切换；事件循环本身不会自动让 CPU 密集代码并行。阻塞 I/O 可由线程池隔离；CPU 密集 Python 工作通常考虑进程池/独立 Worker；Celery/持久化任务队列适合长任务、跨进程状态、重试和故障恢复。请求超时/取消不必然撤销已经开始的外部副作用。

**练习：**比较 `time.sleep` 与 `await asyncio.sleep` 的并发语义（纸面预测后在隔离本地环境运行）；把耗时 OCR 分为请求快速返回任务 ID、后台处理、状态查询。负例：在 async handler 直接跑阻塞函数，拖住同一事件循环。

**变式：**工作负载从 I/O 等待改为 CPU 解析，重新选执行机制并解释成本/序列化/部署取舍。目标 L1；独立实验后 L2。

**资料：**[Python asyncio Tasks](https://docs.python.org/3/library/asyncio-task.html)、[asyncio event loop](https://docs.python.org/3/library/asyncio-eventloop.html)、[Celery tasks](https://docs.celeryq.dev/en/stable/userguide/tasks.html)。

## 阶段 3：设计、排障和面试综合

### J05-15｜文件异步处理设计（明确为新设计）

> 本单元教学方案不是“已有医疗 OCR 功能”的证据；没有真实数据、生产凭据或真实用户文件参与。

**流程：**客户端上传→身份/租户授权→对象存储写文件→MySQL 同事务写文件元数据、任务及 Outbox→发布器投递→Worker 领取并处理→写结果/审计/状态→客户端轮询或 SSE 查询。文件本体与结构化元数据适合不同存储职责。

**练习：**设计 Multipart 限制、文件大小/类型验证、对象 key 不可猜测、租户校验、重复上传幂等键、对象存储失败补偿、任务状态和清理策略。画出数据库提交成功但消息失败、对象已写而 DB 回滚、Worker 重复处理三条故障路径。

**负例：**只靠文件名授权；用客户端给出的 tenant_id 决定访问权；把文件内容放进日志；假设数据库回滚会自动删除对象存储文件。

**验收：**能指出每个资源的所有者和一致性边界，提出补偿/重试/人工处理方案；目标 L1 设计能力。L2 必须在合成环境实现并测试，不因画图升级。

**资料：**[OWASP File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)、[S3 presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html)、[OWASP Multi-Tenant](https://cheatsheetseries.owasp.org/cheatsheets/Multi_Tenant_Security_Cheat_Sheet.html)。

### J05-16｜故障定位、可观测性与交付边界

**目标 / 前测：**用户报告“任务一直处理中”，第一步查什么？

**固定内容：**Request/Correlation ID 串联服务日志；结构化日志记录状态变化但不记录凭据/敏感文件；Metrics 用计数器/直方图观察错误率、延迟、队列积压；Trace 观察跨服务调用。慢查询要结合执行计划和实际测量；降级/回滚应有责任边界。CI、合成演示和生产运行分别说明。

**练习：**给定虚构日志序列（任务创建、outbox 待发、发布重试、worker 无心跳），形成“现象→证据→假设→区分实验→修复→复测→遗留风险”。不伪造本地真实日志。

**负例/变式：**日志有请求 ID但记录了 Authorization token；变式把故障改为 DB 连接池耗尽，说明下一步需查哪些指标。

**验收 / 追问：**解释至少一个故障的可证实根因；对生产部署的声明给出部署、监控、回滚和授权证据。目标 L1，独立故障修复后可申请 L3。

**资料：**[W3C Trace Context](https://www.w3.org/TR/trace-context/)、[OpenTelemetry概念](https://opentelemetry.io/docs/concepts/)、[OWASP Logging](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)。

### J05-17｜J05 主问与追问综合答辩

**目标：**把技术链路、真实证据、设计能力和边界组织成可信答案，而不是背稿。

**三分钟结构：**①项目需求及个人职责；②已核实的服务拓扑；③选一个 Java 请求讲 Controller→数据访问→测试；④讲一个真实可靠性实现（若查证存在）；⑤给一项失败/故障证据；⑥说明尚未实现的文件处理/MQ/生产部分是设计，不是经历。每个“做过”附可展示代码/测试/运行范围。

**独立练习：**不看答案，画拓扑并回答：为何多语言共存？DB 提交后消息失败？重复消费？索引如何验证？Redis 是限流还是缓存？async CPU 工作放哪里？最大的架构不足是什么？

**变式：**去掉 Redis，改成 RabbitMQ；或把只读 Catalog 改为审核写入。指出哪些接口、事务、权限、幂等和测试必须重做，不能把旧结论直接迁移。

**验收：**闭卷答辩后由学习者/面试教练用[会话卡](GAP-SESSION-TEMPLATE.md)记录遗漏，目标 L1；真正代码任务独立实现并测试后才可主张 L2；真实故障排障/取舍证据支持 L3。课程写成不等于通过。

## 关键概念速记（非替代理解）

- **服务边界：**谁负责业务规则、数据访问和错误契约。
- **事务 Outbox：**业务数据与待发布事件同一数据库事务；网络投递异步且可能重复。
- **幂等：**相同操作重复到达，业务结果仍满足预期；靠约束/条件更新/幂等记录等实现。
- **Fencing：**新所有者获得更大令牌，旧持有者的迟到写入由存储端拒绝。
- **可验证交付：**说清环境、版本、命令、结果、覆盖范围和未覆盖边界。

## 可复制的授课指令

```text
你是我的 J05 初学者导师。先读 docs/learning/J05-JAVA-PYTHON-LESSONS.md 和当次单元链接的知识卡/官方章节。
我从零开始，不要假设我理解 HTTP、Java、事务或 MQ 缩写。严格按该单元固定的概念、例子和验收教，不扩展成新路线。
每次只教一个单元：先给目标和一个预测题；用专业定义+不误导的大白话+上下游关系+适用边界解释；逐步讲最短示例；然后给半引导练习。我提交尝试后再审查，先 H1/H2/H3 提示，不抢先贴完整答案。
练习后给具体陌生变式、适用正例和负例、三道口述追问。没有执行的写 NOT_RUN；不把仓库材料、AI生成代码、CI结果写成我独立掌握。学习状态只记 PROGRESS.md，会话证据用 GAP-SESSION-TEMPLATE.md。
未经授权不改外部项目、不访问真实用户数据或生产系统。结束时说明本单元未掌握的具体 Gap 及下一步。
```

## 维护规则

- 技术版本和官方链接变动时核对节点卡及官方来源；不要将代码示例未执行描述为通过。
- 本专题不是 Gaobao 项目源码清单；读取外部源码后须注明路径/commit/访问日期和实际观察，未读取则标“待核验”。
- 本专题推荐先后服务于本题零基础学习，不改变 42 节点依赖图、G01–G24 定义、全局学习路线或 PROGRESS 唯一台账。
