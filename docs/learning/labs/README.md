# 需求驱动最小实验：先复现故障，再补刚好够用的原理

> **真实可运行的实验与课程设计严格分开。** 这个目录包含一个不依赖浏览器/框架的Node测试，用于证明JavaScript请求竞态的核心机制。它**不等于**Vue/React组件级验收，也不等于本人关闭AI完成训练。

## 实验一：前端列表搜索返回顺序错误（F03 → F08/F04）

**实际需求**：用户输入搜索词A后立即输入B；B更快返回，界面却最后显示A。先用纯JS把竞态变成可靠单测，再回原Vue/React项目修复。

**本地执行**：仓库根目录，安装Node.js 24（或支持内置node:test的现代版本），执行：

```bash
node --test docs/learning/labs/request-race.test.mjs
```

**应当观察**：3个自动测试通过——第一条显式证明*有Bug的原始行为*，后两条证明**请求序号守卫**避免旧成功/旧错误覆盖新的结果。第一条通过不是产品通过，它只是成功复现Bug。

**先修按需**：只要F03的Promise/闭包和F08的Vue watch（或F04的React状态），不必先学后端。阅读[Vue官方watch清理](https://vuejs.org/guide/essentials/watchers.html)；Vue3.5+的`onWatcherCleanup`要求同步注册。React需求则从[状态快照](https://react.dev/learn/state-as-a-snapshot)和现有Query实现开始。**练习新条件**：再给AB中间加入C和取消操作，关AI改代码后复测。

**边界**：Node单测验证异步顺序逻辑；浏览器真实Fetch取消、TanStack Query缓存、Vue watch生命周期仍需在相应真实项目用组件或E2E验证。

## 实验二：后端输入契约变化（B01 → B02/F03）

已有**合成且训练专用**的FastAPI测试代码：
[API入口](../../../ai-fullstack-workbench/apps/api/app/main.py)、[测试](../../../ai-fullstack-workbench/apps/api/tests/test_api.py)。

```bash
cd ai-fullstack-workbench/apps/api
python -m venv .venv
# 激活虚拟环境后执行（Windows PowerShell: .venv\Scripts\Activate.ps1）
python -m pip install -r requirements.txt
python -m pytest tests/test_api.py -q
```

**学习观察**：合法演示数据返回200；非法Decimal浮点、额外字段、重复账单在现有测试中返回422。随后**独立改变一项Pydantic字段限制**并用负例验证；进一步导出`/openapi.json`核对schema变化。原合成API**没有登录/授权/生产数据库**，不能拿这个实验声称真实权限安全或上线。

官方：[FastAPI请求体](https://fastapi.tiangolo.com/tutorial/body/) · [OpenAPI规范](https://spec.openapis.org/oas/latest.html)。

## 实验三：Java Spring接口越权（B03 → B04/B05，设计态）

当前仓库**没有可复用的Spring工程，也没有完成此实验的CI**。若遇到Java岗位/实际Spring业务，参考[Spring Boot Servlet/MVC](https://docs.spring.io/spring-boot/reference/web/servlet.html)、[Spring Security资源授权](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html)及[上游LAB14](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/tracks/project-driven/lab-guides/LAB14.md)。

定义最小资源`GET /tasks/{id}`：用户A请求自己的资源成功，用户B请求A资源必须由服务器拒绝（403或有意选择的404），而不是只在页面隐藏按钮；401/403语义按服务所用认证方案验证。关闭AI新增一个资源拥有者变更场景。**本仓状态：NOT_RUN**，不宣称已经完成Java开发。

## 实验四：数据库并发扣减（D01，设计态）

**真实需求**：余额为100，同时扣80，不能产生负数。需要在独立的本地PostgreSQL测试库中准备示例表：

```sql
CREATE TABLE lab_balance (
  id integer PRIMARY KEY,
  balance integer NOT NULL CHECK (balance >= 0)
);
INSERT INTO lab_balance(id, balance) VALUES (1, 100);

-- 在两个独立数据库会话中并发执行：
BEGIN;
UPDATE lab_balance
SET balance = balance - 80
WHERE id = 1 AND balance >= 80
RETURNING balance;
COMMIT;
```

**预期**：两个会话按适当交错提交后，仅一个UPDATE成功修改行，另一个因条件不满足而返回0行；余额为20。再尝试故意写入负余额，观察CHECK约束，解释条件更新与MVCC/锁等待的联系。

**注意**：这里是操作说明，**未连接真实数据库执行**。严禁在生产库运行故障注入。官方阅读：[PostgreSQL事务隔离](https://www.postgresql.org/docs/current/transaction-iso.html)。

## 如何用这些实验

输入当前业务功能→运行[需求路由器](../route_need.py)（命令：`python docs/learning/route_need.py --query "..."`）→看[42节点学习卡](../NODE-STUDY-CARDS.md)→只做相关实验→把真实结果写入[需求会话模板](../GAP-SESSION-TEMPLATE.md)，不必连续安排24周课程。
