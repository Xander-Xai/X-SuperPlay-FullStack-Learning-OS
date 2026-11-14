# ADR-0002：V3.0 扩展 Java/Spring、前端深度和学习周期

> **历史V3全量覆盖决策**：本页的“Java/Next必修、WorkBench单项目”**不适用于现行需求驱动学习与所有下游项目**。现行优先级见[ADR-0004](ADR-0004-fullstack-foundations-and-authority.md)和[ADR-0003](ADR-0003-demand-driven-learning.md)。

- 日期：2026-11-14
- 状态：**PARTIALLY_SUPERSEDED_BY_ADR-0003**（历史V3全量能力覆盖有效；单一项目和24周固定执行顺序已失效）。请以[ADR-0003](ADR-0003-demand-driven-learning.md)为当前学习治理决策。
- 关系：继承 [ADR-0001](ADR-0001-stack-and-boundaries.md) 的 Phase A 决策，但**将其中“Java/Spring Boot 深度后置 P2”这一句明确更新为 W9–W13 必修**，不是撤销 Vite/FastAPI 主链路。

## 决策

1. **一个 ROADMAP 覆盖 24 周**：W1–W8 基线 144h，W9–W16 语言框架强化 144h，W17–W24 多栈架构/交付 144h；总 432h 为参考时间，不能自动毕业。
2. Java 作为多语言全栈的**必修目标能力**：Java Core/Collections/Streams、并发/JMM/JVM/GC/JFR、Spring IoC/AOP/MVC/Boot、Spring Security、Spring Data/事务、Testcontainers。
3. 前端从 React UI 扩到**Web 平台基础 + 现代工程**：HTML/CSS/a11y、TS/JS 执行与工具链、React 状态/性能/测试、SSR/Next 核心比较；Next.js **对比实验必修**，替换主 SPA 架构仍按需求决定。
4. 同一个 Workbench 保留 `apps/web` + `apps/api` 的主流量；Java 只拥有新增的一块独立审计/通知业务边界，**不重复实现同一 CRUD，也不互相无授权直接更新表**。
5. Node.js runtime/BFF 学会执行模型/流/背压，NestJS、Vue3、GraphQL/gRPC 深度与 K8s 真机集群是按需求选修，不为了“技术栈齐全”强制全做。
6. G01–G12 保留作为基线，新增 G13–G24 深入验收。文档、代码生成、实验、个人独立通过和产品交付保持独立状态。

## 取舍与复审

- 24 周不是保证“架构师”的期限，真实岗位 MUST 优先可以 Gap Jump，但所有被声明已掌握的知识仍需测评。
- 多语言会增加 CI/部署/鉴权/数据边界成本，因此把 Java 作为晚于基础纵切的显式边界服务，可作为独立实验按需启动。
- 具体 JDK LTS 与 Spring Boot 小版本在创建 Java 项目前按官方兼容矩阵固定，不在 Roadmap 写死未经核实的安装版本。
- 本 ADR **不等于**已创建 Java 代码、修改下游 Utility-Sites 或发布任何服务。
