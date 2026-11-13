# V3.0 工具版本选择与升级约束

> 版本基线建议，非已安装。应在**对应实验开始时核对官方兼容矩阵并固定当前实际使用的具体版本**，避免把 2026 年 11 月的最新版本误当长期有效默认值。

## 2026-11-14 核验来源与合理默认

| 生态 | 可选择的基线 | 核对事项 |
|---|---|---|
| Java / JDK | **Eclipse Temurin 21 LTS**（兼容优先）或 **25 LTS**（现代特性） | 用 `java -version` 固定发行商/补丁版本；虚拟线程在 JDK 21+ 可用，项目尽量保持 LTS |
| Spring Boot | 最新**稳定且兼容 JDK 的支持版本**；官方 2026-11 页面显示 4.1.2 最低 Java 17，兼容到 Java 27 | 依赖、数据库驱动、插件生态可能有额外要求，需核实并固定；不可无验证地在 3.x→4.x 跨大版本 |
| Node | **24.x 或 26.x LTS**，按 Vite/Next 工具链兼容性选定；2026-11 当前 Node 26 为 Active LTS | 禁止用 Node 27 Alpha 做唯一主工作流；记录 `node -v`/pnpm/lockfile |
| Python | 在 FastAPI/SQLAlchemy/Celery 兼容范围内选受支持的正式版本并固定 | 保存 `python --version` 和 lockfile/constraints；不要不同服务默认为相同运行时 |
| 数据/中间件 | PostgreSQL、Redis、RabbitMQ（或 Kafka）选一个项目兼容的稳定版本 | Docker Image 用可复现的具体版本/摘要，不用无约束 `latest` |
| Web | React/Vite/Orval/Next 使用相互兼容的稳定版本 | 保存 `package.json`/lockfile、Typecheck/ESLint/E2E 结果 |

## 关键许可证提醒

Oracle 的公开路线说明 **Oracle JDK 21 在 2026 年 10 月后补丁版本的许可发生变化**。这不等于“所有 Java 21 都收费”；选用 Temurin 等符合使用要求的 OpenJDK 发行版并核对其许可条款，避免把 Oracle JDK 的具体商业许可证与 OpenJDK 混同。

## 版本固定检查

```bash
java -version
javac -version
mvn -v
node -v
pnpm --version
python --version
docker version
docker compose version
```

- 这些是**准备运行的命令样本**，并非本仓已经运行。实际输出只能在相关实验的记录里填。
- 必要时使用 `.nvmrc`、`packageManager`、Maven Wrapper/`gradlew`、容器固定标签，以及迁移日志。
- 故障排查前先保存运行版本；不要一边升级依赖一边对比性能，再声称只变了一个因素。

## 官方依据

- [Oracle Java SE Support Roadmap](https://www.oracle.com/java/technologies/java-se-support-roadmap.html)（Java 21、25 LTS）
- [Oracle JDK 21 License FAQ](https://www.oracle.com/java/technologies/javase/jdk-faqs.html)
- [Spring Boot System Requirements](https://docs.spring.io/spring-boot/system-requirements.html)
- [Node.js Release Schedule](https://nodejs.org/en/about/previous-releases)
- [Eclipse Temurin](https://adoptium.net/)
