# J05-00/01 完整首课｜证据边界与全栈请求旅程

> **教学设计，不是个人通过记录。** 本教材的拓扑是教学假设；Gaobao-Advisor 的具体版本、路由配置和测试结果须在可访问源码及 CI 中核实。运行本仓已有 J01 实验不会证明外部 Java 服务实际运行。

## 本课结束时

你应该能：

1. 分清“源码存在、测试通过、生产运行、设计方案”四种证据。
2. 从浏览器追踪一个 HTTP 请求：浏览器 → 反向代理/网关 → 后端服务 → 数据库，再沿响应返回。
3. 说明 Gateway、FastAPI/Spring 服务与数据库各自负责什么、不负责什么。
4. 对一条新路由绘出请求和故障边界。

目标是 **L1 理解**。如果尚不能做到，不进入独立面试背诵；按本课变式再练。本课不声明你已经完成任何项目实验。

## 0. 先预测

假设用户打开院校列表，浏览器请求：

```http
GET /api/v1/catalog/schools?province=广东 HTTP/1.1
Host: example.test
Accept: application/json
```

不查答案先写下：

- 哪一层接收浏览器连接？
- 哪一层决定把 `/catalog/` 送给 Java 或 Python？
- 谁验证 province 并查询数据库？
- 返回的 HTTP 状态码、JSON 是谁生成的？
- 若数据库不可用，浏览器会自动改发给另一个服务吗？

## 1. 四种证据，先别混用

- **设计**：架构图、方案、面试回答。能说明“打算怎样做”，不能证明代码存在。
- **源码**：仓库中某个确定版本有实现。能证明代码存在，不能单独证明它可运行。
- **测试/运行**：实际命令在明确环境、数据和断言下得到结果。只证明覆盖范围内的行为。
- **生产运行**：真实部署、权限、监控、回滚和运维记录支持的结论。CI 绿灯不等同于生产上线。

用餐厅作类比：菜单（设计）→厨房做出菜（源码）→试餐并记录结果（测试）→餐厅持续营业且有人负责（生产）。类比不能把低一级证据升级成高一级。

**例子：**“Java Catalog 已通过单测”最多说明某次单测通过；若要说“Java/Python/MySQL 集成已验证”，需要能指出确实启动这些组件的集成测试、版本、数据与断言。说“已上线”还需独立的部署/运行证据。

## 2. 请求的六个零件

1. **Method**：GET 通常读取；POST 通常提交操作。具体语义由 API 契约规定。
2. **Path**：`/api/v1/catalog/schools` 标识资源路径。
3. **Query**：`?province=广东` 提供筛选参数。
4. **Headers**：`Accept` 表明客户端希望接收 JSON；身份相关头不能随意信任或透传。
5. **Status**：200 表示本请求成功；401/403、404、429、503 等应按契约表达不同情况。
6. **Body**：响应 JSON，例如 `{"items":[],"count":0}`。字段和类型必须由接口契约约定。

HTTP 是请求/响应协议。一次 API 请求不会自动跨越所有服务；必须由网络监听、代理路由和服务调用逐段连接。

## 3. 教学拓扑（假设，不是外部项目事实）

```text
浏览器/Vue
   │ HTTPS 请求
   ▼
Nginx（反向代理/入口）
   │ 内部 HTTP
   ▼
Gateway（按路由选择服务，可有过滤器）
   ├── /api/v1/catalog/** → Spring Boot Catalog → MySQL
   └── /api/v1/chat/**    → FastAPI → AI/业务组件
                                      └── 可按需求访问数据库/任务服务
```

每条箭头都是网络调用边界：有目标地址、协议、超时、错误和身份传递问题。这个示意图没有说明实际服务端口、是否同机、认证方案或是否使用 MySQL；这些必须查看具体配置。

**准确类比：**Nginx 像园区入口按楼栋指路；Gateway 像服务总台按业务类型分流；Spring/FastAPI 是负责具体业务的窗口；MySQL 是持久化记录的档案柜。档案柜不替窗口判断业务规则，网关也不应成为唯一的资源权限检查点。

## 4. 一次 GET 的逐步过程

1. 浏览器解析 URL，建立连接，并发送 HTTP 请求。
2. Nginx 接受连接，按配置决定转发目标；代理配置错误可能造成 404、502 或连接失败。
3. Gateway 检查路由规则。只有实际配置匹配时，才向 Catalog 服务发请求。
4. Spring Controller 读取参数并校验输入；业务/Repository 逻辑构造带参数的 SQL。
5. MySQL 返回行或错误。服务把数据映射成契约规定的响应。
6. 响应逐层返回，浏览器按状态码与 JSON 更新页面。

**注意：**如果 `/api/v1/catalog/**` 实际指向 Java，那不是 HTTP 自带的规则，而是路由配置决定的。Python 和 Java 都可实现 API，但两边需约定字段、分页、错误、权限和兼容性。

## 5. 最小可运行基线：复用已有 J01 实验

本仓已有合成实验 [J01 L00 教程](J01-L00-WEB-REQUEST-TUTORIAL.md) 和 [代码目录](j01-web-request/)。它演示浏览器→FastAPI→JSON，不包含 Java Gateway、MySQL、真实身份验证或生产部署。

按 [实验目录操作说明](README.md#实验零-j01-l00-浏览器fastapijson-的第一条链路教学基线not_run) 在本地运行后，观察：

- 页面请求 `/api/schools?q=广东` 的 URL 与 query。
- 浏览器 Network 中的 method、status、response body。
- 将无效查询条件提交后，实测响应与预期是否一致。

不要仅凭本教材宣称上述命令已在你的电脑执行；若未运行，记录 `NOT_RUN`。执行实验不会证明 Java 部分实现。

## 6. 半引导练习：画出 Catalog 查询

用下面框架填空，不必添加代码：

```text
浏览器 --(____)--> Nginx --(____)--> Gateway
Gateway --(路由规则 ____ )--> Java Catalog
Java Catalog --(查询 ____ )--> MySQL
MySQL --(结果 ____ )--> Java Catalog --(HTTP ____ + JSON ____ )--> 浏览器
```

然后为每一跳写一个可能失败的原因，以及谁最容易观察到该失败（浏览器、代理日志、Gateway 指标、应用日志或 DB 错误）。

**H1**：先标出每条箭头承载的是协议还是业务数据。\\
**H2**：找出接收 HTTP 的入口、执行路由规则的组件、执行 SQL 的组件。\\
**H3**：将异常放在具体调用边界上：连接失败、路由无匹配、参数校验失败、SQL 失败。

## 7. 负例与陌生变式

### 负例 A：把 Gateway 当权限系统

Gateway 透传 `X-User-Id: 123`，Java 服务不验证该身份头，客户端自己伪造 123。**预测：**是否构成可信身份？不可信；服务必须使用可信认证上下文并执行资源授权，不能单靠客户端可控头。

### 负例 B：服务失败就“自动切另一语言”

Java Catalog 不可用时，前端是否能无条件向 Python 发同一路由？不能假设。需要有等价 API、路由策略、鉴权及数据一致性约定；否则切换可能返回错误语义或绕开权限。

### 变式

现在聊天接口由 HTTP SSE 改成 WebSocket：在图上标出需要重新检查的代理能力、连接时限、鉴权位置、断线恢复方式。不能只把 URL 改名就当协议转换完成。

## 8. 本课独立验收

关掉本页，口述 60–90 秒：

- 一次学校列表请求经过哪些层？
- 哪一层负责路由？哪一层负责业务？哪一层持久化？
- Java 与 Python 并存的合理理由是什么？共享数据库有什么边界？
- 哪些结论目前只是教学假设？要把它说成项目事实，需要检查什么证据？

**L1 通过条件：**四问均能解释且未把假设说成事实。没有进行口述或记录则仍是 `NOT_RUN`。本课不要求 L2 编码，也不证明整道 J05 已掌握。

记录到 [GAP 会话卡](../GAP-SESSION-TEMPLATE.md)，个人进度只更新 [PROGRESS](../PROGRESS.md)。本课会话中的口述/讲解属于 `EXPLAINED`；只有明确进行无提示考试并有相应证据，才可标记独立表现。

## 官方资料

- [MDN: HTTP overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview)：请求、响应和协议基础。
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)：API 契约的结构化表达。
- [Spring Boot Web/Servlet](https://docs.spring.io/spring-boot/reference/web/servlet.html)：Spring Web 请求处理入口。
- [FastAPI First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)：FastAPI 路由和响应示例。
- [Nginx Beginner's Guide](https://nginx.org/en/docs/beginners_guide.html)：Nginx 配置与代理基础。
