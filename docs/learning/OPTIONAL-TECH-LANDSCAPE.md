# 全栈技术生态外围分支｜知道有哪些，但不强制学习

> **本表是“视野地图”，不是新课程、待办或认定熟练的证据。** 42个核心节点已提供需求驱动学习入口，外围的框架/语言在项目确实遇到时再扩展为正式节点。参考上游[语言与框架地图](https://github.com/Xander-Xai/X-SuperPlay-AI-Learning-OS/blob/main/docs/knowledge/software-engineering/programming-language-stack-map.md)。

## 它们在哪一层？和现有节点是什么关系？

| 方向与技术 | 专业定位 | 大白话 / 与核心栈的关系 | 适用场景及官方/权威资料 |
|---|---|---|---|
| Angular | TypeScript前端应用框架 | 与Vue/React同层的另一套组件/路由/表单体系 | 已有Angular项目、企业标准：[Angular官方](https://angular.dev/overview) |
| Svelte/SvelteKit | UI框架与配套应用框架 | 同层替代Vue+Nuxt/React+Next的一支 | 现有栈、体积/编译模型需求：[Svelte官方](https://svelte.dev/docs/svelte/overview) |
| ASP.NET Core / C# | .NET后端框架与语言 | 跟Java+Spring、Python+FastAPI、Node+Nest平行 | Windows/.NET团队：[Microsoft Learn](https://learn.microsoft.com/en-us/aspnet/core/overview) |
| PHP / Laravel | PHP服务端语言和Web框架 | 传统/现代Web后端另一条成熟路线 | CMS、电商、旧PHP系统：[Laravel官方](https://laravel.com/docs) |
| Ruby / Rails | Ruby生态Web框架 | 用约定管理API/页面/数据库的一体应用 | Rails既有系统：[Rails Guides](https://guides.rubyonrails.org/) |
| GraphQL | API查询语言、Schema与执行模型 | 与REST/OpenAPI风格不同的API接口方案 | 多客户端字段组合、GraphQL既有服务：[GraphQL.org](https://graphql.org/learn/) |
| gRPC / Protobuf | RPC协议/IDL与序列化生态 | 常见服务间通信方案，不代替浏览器所有HTTP请求 | 内部多语言服务、流式RPC：[gRPC官方](https://grpc.io/docs/) |
| tRPC | TypeScript端到端类型化RPC框架 | 同TS项目里把调用类型关联，不能跨语言自动替代OpenAPI | TS全栈单仓：[tRPC官方](https://trpc.io/docs) |
| Serverless/Edge | 函数和边缘运行模式 | 改变后端部署/运行限制，不是另一种编程语言 | 低维护事件处理/边缘延迟：[Cloudflare Workers](https://developers.cloudflare.com/workers/) |
| Spring Cloud / 微服务治理 | Java多服务配置/发现/治理生态 | 先把模块化单体做好，再因组织和扩展需求升级 | 真实多服务：[Spring Cloud官方](https://spring.io/projects/spring-cloud) |
| MongoDB / 文档数据库 | 文档模型与查询/索引数据库 | 不是PostgreSQL的一键替身，事务与Schema取舍不同 | 文档数据/既有系统：[MongoDB官方](https://www.mongodb.com/docs/) |
| 浏览器扩展 | 浏览器权限/脚本/隔离环境 | 仍能复用Web JS/TS，但权限与发布审核另算 | 插件具体需求：[Chrome Extensions](https://developer.chrome.com/docs/extensions) |
| WebRTC | 浏览器实时音视频/数据通道规范与API | 与WebSocket同样实时但连接/媒体模型不同 | 音视频通话：[MDN WebRTC](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API) |
| Kotlin/Swift/Flutter/Dart | 原生和跨平台移动端语言生态 | 共享部分业务协议，但设备生命周期与上架要求不同 | Android/iOS及跨端：[Android](https://developer.android.com/) · [Apple](https://developer.apple.com/) · [Flutter](https://docs.flutter.dev/) |

## 选栈时要判断三件事

1. **有没有现存代码/岗位/真实客户限制？** 已有C#系统就先补.NET，已有Vue系统不需要为了“学全”迁移React。
2. **真正需要的是哪一层能力？** GraphQL/gRPC是API契约路线，Kubernetes/Serverless是部署/运行方案，MongoDB是存储，不能混在“后端框架”一类里。
3. **这个技术解决了什么可复现问题？** 没有明确项目触发时先知道作用、链接和替代项就够了；对技术细节只按需补[42节点卡](NODE-STUDY-CARDS.md)或为新增真实需求建立节点。

**未覆盖的领域**（浏览器扩展安全、复杂实时音视频、游戏引擎、嵌入式、数据湖等）必须按具体任务另列缺口，不能因为地图出现名字就声称完整或已经掌握。
