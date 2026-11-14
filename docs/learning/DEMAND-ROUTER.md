# 按需求学习：FullStack Learning OS 首选入口

> **从需求挑技能，不按 W1→W24 顺序通关。** [ROADMAP](../../ROADMAP.md) 提供完整覆盖地图，[知识关系图](KNOWLEDGE-GRAPH.md) 提供逻辑和最小先修，[权威参考](OFFICIAL-RESOURCES.md) 负责学习原理；学习顺序由真实任务决定。
>
> **不限 ReconLab 或某个下游仓**。工作台/静态站/SaaS/企业系统/小程序/移动App/AI应用/Java岗位都可触发不同学习路径。真正开发需遵循对应仓库授权与工程流程。

**AI辅助路线**：如果只有业务需求，参考[上游BDL](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/prompts/business-demand-learning/v1.0.0/01-business-demand-to-learning-goals.md)；已明确技能目标，参考[上游ANL](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/prompts/ai-native-learning/v1.0.0/01-github-ai-learning-research.md)。完整可复制的导师指令见[AI原生按需学习协议](AI-NATIVE-LEARNING-PROTOCOL.md)。

## 选一个入口：有需求、有时间压力，还是只想构建全局认知？

- **手头有具体业务/Bug**：继续走本页默认需求路由→42节点，直接在现存代码动手。
- **14天内要面试**：使用[14天可选冲刺](OPTIONAL-EXECUTION-MODES.md)与[20道面试题](INTERVIEW-ENGINEERING-DRILLS.md)，根据JD挑题和对应负例，不给已会的能力强制分配重复课程。
- **希望系统性做项目**：使用[8周可选能力簇](OPTIONAL-EXECUTION-MODES.md)与[交付纵向链路](DELIVERY-LIFECYCLE.md)。
- **知道原理名称却不懂细节**：用[30项细节补漏](DETAIL-GAP-INDEX-2026.md)和[节点卡](NODE-STUDY-CARDS.md)查专业定义、类比及官方具体章节。

## 交叉基础补漏：不属于单一框架，却不能遗漏

[17个横向基础卡](CROSS-CUTTING-FOUNDATIONS.md)按42节点归属，例如算法/复杂度归F03/B03/P02，安全威胁建模归E03/P02，国际化/金额时区归F03/D01。**查询这些现实问题时同样能获得官方链接与负例实验**；不会强制安排新的周次或Gate。

## 命令行按需反查（可运行，不只是一张表）

在仓库根目录使用Python 3.12+：

~~~bash
python docs/learning/route_need.py --query "Spring Boot API"
python docs/learning/route_need.py --query "微信小程序"
python docs/learning/route_need.py --query "Vue3后台"
python docs/learning/route_need.py --query "Electron桌面应用"
python docs/learning/route_need.py --query "MCP Server"
python docs/learning/route_need.py --node B04
python docs/learning/route_need.py --node F08 --json
python docs/learning/route_need.py --query "数据结构与复杂度"
python docs/learning/route_need.py --query "国际化时区"
python docs/learning/route_need.py --query "SLO故障响应"
python docs/learning/route_need.py --topic X06 --json
python docs/learning/route_need.py --list-topics
python docs/learning/route_need.py --list
~~~

程序读取[机器可读知识图](knowledge-map.json)，输出**专业定义、机制、大白话、理解边界、最低先修、官方专题章节、上游相关资料类型、实验与失败负例**；`--json` 可交给Coding Agent做定向学习计划，不能由它自动认定个人已会。`--query`现在返回核心节点与相关X专题的候选卡（JSON数组中后者标为 `kind: cross_cutting_topic`）；`--topic X01...X17` 可精确进入横向专题，不建立第二份学习状态。关键词匹配是**初步路由**，不替代理解需求；不匹配时按节点列表人工选择。

## 可运行的按需实验示例

- **JavaScript异步竞态**：`node --test docs/learning/labs/request-race.test.mjs`；先看[最小Lab](labs/README.md)和F03/F08节点。
- **现存FastAPI契约**：[最小Lab命令与官方资料](labs/README.md)（已有合成API测试；不代表权限/生产上线）。
- **Spring资源授权 / PostgreSQL并发**：同一Lab文档有可复现步骤，但当前仍标 `NOT_RUN`，勿将说明变成实验PASS。

## 一、最短的学习循环（每次只解决一个真实 Gap）

1. **需求**：本次要交付什么功能或修复什么故障？写一句用户结果与至少一个失败场景。
2. **反查节点**：在 [知识图](KNOWLEDGE-GRAPH.md) 找目标能力；只补它所列的最小 `requires`，不要求前面所有 W 坐标 PASS。
3. **快速诊断**：给目标做一次最小测试，分成 ALREADY_KNOW / PARTIAL / UNKNOWN；已会的不要重复刷教程。
4. **权威学习**：根据 [官方资料表](OFFICIAL-RESOURCES.md) 定位一两个章节，先回答“它是什么、解决什么问题、与上下游技术怎么连”。
5. **实战应用**：在**当前真实项目**的允许范围内改最小纵切；若下游开发处于冻结/无权限，在学习仓的隔离实验或合成数据中验证。
6. **失败→修复**：注入一个负例，收集原始日志、测试命令、具体版本、提交SHA和失败/修复对照。
7. **独立复测**：关掉 AI，变更一个条件再做一遍；证据记 [PROGRESS](PROGRESS.md) 的需求会话区，Gate 仅记录对应能力。
8. **继续项目**：回归业务功能；下一个 Gap 发生时再进入图谱，不主动发明新技术任务。

**建议一次学习会话 60–180 分钟**（视难度调整）。其中“原理/官方资料 20–30%、亲手写与测试 50–60%、故障复盘 20–30%”只是参考配比，并非硬性考勤。

## 二、先看系统关系图，再选当下需要的一角

先阅读[全栈专业定义与大白话全景图](FULLSTACK-MENTAL-MODEL.md)，再结合[上游资料汇合索引](UPSTREAM-ASSET-INDEX.md)定位 Vue/React、Java/Spring、Node/MCP、数据/部署的具体教程与[42张含官方章节、正负例的节点学习卡](NODE-STUDY-CARDS.md)。**学习方向由当前需求决定，知识结构由依赖图提供；这两个目标并不矛盾。**

## 三、按“要做什么”直接进入知识

| 我现在想实现的功能/产品 | 先定位的技能节点 | 缺什么才补什么 | 不要求先学 |
|---|---|---|---|
| **网页/响应式工具、落地页** | F02、F03、U01、E01 | 有交互再F04；SEO/SSR再F05；部署再E02 | Spring、Redis、Celery |
| **Vue3后台 / 现有Vue项目** | F08、F03、B01、E03 | 接口按项目选B02/B04/B07，SSR需求再F09；上游有Vue3+FastAPI实训 | 不强行迁移React或学Next |
| **Nuxt+Vue全栈/SSR** | F08、F09、F01 | 需要SEO、渲染缓存时深入，配套最小服务器端安全实验 | 先把React或Next也学完 |
| **桌面Electron/Tauri工具** | M03、F03、F02 | 本地文件/IPC/系统权限、安装签名；需求触发后深入Rust/Tauri | 全栈Web 24周先学完 |
| **MCP工具或双向实时服务** | A02或F11、B01 | MCP工具Schema/授权；实时订阅区分SSE/WS、重连和顺序 | 一上来就做多Agent集群 |
| **Go/Rust/C++工程** | B08或B09、E05 | 仅现有项目、岗位或瓶颈证据触发，按语言官方文档最小实现 | 把所有语言列成必修 |
| **React后台/企业管理系统** | P01、F04、B01、E03 | 后端选B02或B04；数据存储D01；CI E01 | Next SSR、Kafka、全套Java与Python并学 |
| **SaaS/Micro-SaaS** | P01、B01、D01、E03、E01、P03 | 根据团队选React/Next与FastAPI/Spring；需要收费才P04；跨服务才D03 | 强制多智能体、无业务理由的微服务 |
| **Java/Spring岗位功能/修Bug** | B03、B04 | 涉及DB补D01/B05，安全补E03，JVM故障补B03并发/JFR | 必须按W1–W11顺序打卡 |
| **Python接口/数据处理/自动化** | B02、B01、E01 | 存储补D01，异步补B06，缓存补D02 | Next/Spring/Vue |
| **AI RAG/Agent/Web应用** | A01、B01、E03、E04 | UI补F04，长任务补B06，数据补D01/D02，消息补D03 | 重新训练大模型、每次重做RAG |
| **Node CLI/现有Dev-Workbench维护** | F03、F06、E01 | 涉及产品路由补P01/P02；页面/性能补F02/F07 | 重写现有CLI为Java |
| **微信小程序** | M01、F03、F01 | 远端API补B01、身份补E03、发布补P03 | Java/React全套必修 |
| **移动App** | M02、P01 | React Native选F03，Flutter补Dart基础；接口补B01，离线/权限按平台官方 | 必须学Next或小程序 |
| **数据库死锁/缓存失效/任务失败** | D01 / D02 / B06 / D03 | 发生在哪层就补哪层，联合E04找证据 | 先造一个完整后台项目 |

## 四、三个实例：学习顺序确实可以不一样

**场景A：接到 Spring Boot API 岗位任务**

```text
真实JD/API需求 → 最小Java语法 B03 → Spring MVC B04 → 功能测试 E01
               → 事务/授权出现问题 → D01 + B05 + E03
               → JVM性能有问题才继续 B03(JFR/并发)
```

这里可以先做旧坐标 W12，再回旧坐标 W09/W11 的深层内容。只要目标实验和必要先修确实跑通，**不需要按周排序**。

**场景B：做一个静态海外工具站**

```text
用户需求 P01 → HTML/CSS F02 → JS/TS F03 → SEO工具 U01
             → Git CI E01 → 静态部署 E02 → 运行回执 P03
```

如果无账号、无存储、无后台任务，就没必要学完 D01/D03/B04 才能上线。

**场景C：修现有多智能体客服工具失败**

```text
线上问题/Trace → E04 → B01(工具契约) → B02(服务)
              → B06(任务状态) or D03(消息) → E03(权限)
              → 回归E01
```

此时优先修真实故障，前端React/Next可能完全与该问题无关。

## 五、项目不是“指定练习题”，而是可选的实战载体

- **用户自己的当前项目**：首选，前提是获授权并且不会触碰真实客户敏感数据。学习内容由当前项目的需求和故障定义。
- **Dev-Workbench**：已有Node/测试/CI代码，可作为现有软件维护、调试、工程化的真实案例，遵循其11阶段和PR流程。
- **Utility-Sites**：应按它**当时真实产品状态**判断能否开发；ReconCheck当前冻结，不能把学习任务包装为正式上线授权。
- **ReconLab**：[合成业务示例](../../ai-fullstack-workbench/README.md)，用于缺少安全可用真实工程场景时练习，不是所有知识的唯一主项目。
- **独立最小Lab**：针对Spring事务、React并发、Docker恢复等难以在现有项目安全故障注入的知识点；代码与测试仍要实际跑通。
- **未来新增任何项目**：在 [需求覆盖矩阵](REQUIREMENTS-COVERAGE.md) 中按产品类型反查节点，无需重写24周计划。

## 六、每次“学什么”都能留下具体记录

复制 [需求驱动学习会话模板](GAP-SESSION-TEMPLATE.md) 到 Issue 或 `docs/learning/sessions/`。**唯一实际学习状态**仍在 [PROGRESS.md](PROGRESS.md) 中；Issue是任务和证据链接，不是第二本进度账。没有实测的知识点写 NOT_RUN/UNASSESSED，不强制一次把全部G01–G24做完。

**判断是否该继续学习某一模块**：如果能说清原理、独立实现并在负例中定位根因，就回到当前产品开发；如果只会复制AI生成代码而无法修改，就针对这个 Gap 做深入练习。
