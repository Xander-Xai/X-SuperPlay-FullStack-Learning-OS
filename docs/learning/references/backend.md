# 后端专项深挖字典（按需检索，非独立进度表）

> 基础经验可跳过讲解，不能跳过独立故障实验。对照 [唯一主线](../../../ROADMAP.md)。

| 主线阶段 | 专题 | 必做实验 / 失败路径 | 资料 |
|---|---|---|---|
| W3 | FastAPI Router/Service/Repo、异常、Depends | AuthN/AuthZ、资源级 403、统一错误返回 | [FastAPI](https://fastapi.tiangolo.com/tutorial/) |
| W3 | OpenAPI→Orval→TS/CI | 改后端响应字段、重新生成、前端类型与契约测试 | [Orval](https://orval.dev/docs/) |
| W4 | ACID/MVCC/锁/隔离 | 双连接扣款、乐观锁 vs `FOR UPDATE`，死锁对照 | [PostgreSQL](https://www.postgresql.org/docs/current/) |
| W4 | Index/EXPLAIN/ORM | 查询计划、索引维护、N+1、Session 回收 | [SQLAlchemy](https://docs.sqlalchemy.org/) |
| W4 | Redis TTL/缓存失效 | 多请求回源与 single-flight/TTL jitter 对照 | [Redis](https://redis.io/docs/latest/) |
| W5 | Token/Cookie/CSRF/权限 | 不同租户访问、过期会话、刷新竞争 | [OWASP API Security](https://owasp.org/API-Security/) |
| W5/W8 | Request ID、OTel Trace Context | 统一结构化日志与 traceparent 串联，区别关联日志和真实 Span | [OpenTelemetry](https://opentelemetry.io/docs/) |
| W6 | Celery ACK、任务幂等、重试 | 隔离环境杀 Worker、重复入队、状态恢复、去重 | [Celery](https://docs.celeryq.dev/en/stable/userguide/tasks.html) |
| W6 | SSE 服务端回收 | 取消请求后释放 generator/资源；断流对任务运行的影响 | [MDN SSE](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events) |
| W7 | Compose、部署、回滚 | 从新环境启动，备份恢复，模拟 DB 故障 | [Docker](https://docs.docker.com/get-started/) |

**不宣称** `acks_late` 单独保证重投递；任务重试必须以幂等和可观测状态机为基础。
