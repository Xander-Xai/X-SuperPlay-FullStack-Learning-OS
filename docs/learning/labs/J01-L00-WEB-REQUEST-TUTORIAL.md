# J01 · L00｜从点击按钮到 Python API：真正的第一节全栈课

> **这是一份能照着操作的完整教材，不是课程大纲。**
> 配套可运行源码：[Python后端](j01-web-request/main.py) · [HTML前端](j01-web-request/index.html) · [依赖](j01-web-request/requirements.txt) · [自动测试](j01-web-request/tests/test_app.py)。
>
> 预计 60～90 分钟（因人而异）；**代码和测试是待本人实际执行的教学基线，不等于本轮 ChatGPT 已替你运行或你本人已通过**。所有学校名称均为合成示例，不代表真实招生数据。
>
> 所属仓库原有节点：[F01 Web/HTTP](../KNOWLEDGE-GRAPH.md)、[F02 HTML/CSS](../KNOWLEDGE-GRAPH.md)、[F03 JavaScript](../KNOWLEDGE-GRAPH.md)、[B01 API合同](../KNOWLEDGE-GRAPH.md)、[B02 FastAPI](../KNOWLEDGE-GRAPH.md)。后续回到 [J01 15节学习路线](../J01-HAIBOTE-FULLSTACK-LESSONS.md)。

## 1. 这一课最后能做成什么？

你可以在浏览器打开自己的网页，在输入框填写「广东」，按下「查询」，页面出现「广东示例大学」。也可以直接访问 API 地址看到 JSON；之后用开发者工具观察真实的 HTTP 请求、响应和状态码。

今天先不用 Vue、Pinia、MySQL、Redis、Java。先把**最小的一条全栈链路**学透：

~~~text
用户输入和点击
    ↓
HTML页面上的表单事件
    ↓
JavaScript调用fetch
    ↓
HTTP GET /api/schools?q=广东
    ↓
FastAPI路由读取q
    ↓
Python筛选合成的内存学校列表
    ↓
返回JSON {"items":[...],"total":1}
    ↓
JavaScript解析JSON并更新网页
~~~

这条链路才是后来 Vue 3 + FastAPI + MySQL 系统的基础，只是大型项目加入了更多职责。

## 2. 六个概念：每个都用大白话 + 准确边界理解

### 2.1 前端、后端是什么？

- **前端**是用户操作的界面：文字、输入框、按钮、列表和交互结果。它运行在用户的浏览器里。
- **后端**是服务器上的应用：接收请求、校验输入、处理规则、读取数据、输出结果。
- **本实验**的前端使用原生 HTML/CSS/JavaScript，后端使用 Python FastAPI。它们不因使用不同语言就不能互相通信，因为双方约定了 HTTP 和 JSON。
- **比喻**：柜台接收顾客要查什么，后台处理业务并把结果交回来。比喻不意味着前端是可靠权限边界；真正的授权仍必须在后端。

### 2.2 HTML、CSS、JavaScript 各自负责什么？

| 技术 | 一句话解释 | 本次代码在哪里 |
|---|---|---|
| HTML | 给网页定义结构、语义：标题、表单、按钮、列表 | [index.html](j01-web-request/index.html) 内的 h1、form、label、input、button、ul |
| CSS | 决定视觉样式和布局 | 同一文件的 style 部分 |
| JavaScript | 监听事件、读取输入、发请求、更新页面 | 同一文件的 script 部分 |
| Vue 3（下节才深入） | 基于 JS 的响应式组件框架，通常不用手工频繁操作 DOM | 本实验故意先不用，避免不明白框架封装了什么 |

HTML 的 label 使用 for 对应 input 的 id，便于点击标签聚焦输入框；form 的 submit 事件既支持按钮也方便键盘操作。

### 2.3 什么是 API？

API 是**明确的调用约定**，不仅是一个 URL。至少包括：

- 请求方法：GET；
- 路径：/api/schools；
- 查询参数：q，字符串，可缺省；
- 成功响应：JSON对象，包含 items 数组和 total 数量；
- 错误约定：例如输入太长时返回 422。

前端不应知道 Python 如何循环或将来如何访问 MySQL；前端只依赖这个约定。**这就是接口契约。**

### 2.4 什么是 HTTP？如何读一个 URL？

~~~text
http://127.0.0.1:8000/api/schools?q=广东
│      │         │    │            └─ q 是查询参数
│      │         │    └─ path 是接口路径
│      │         └─ port 8000
│      └─ 127.0.0.1 是当前机器的回环地址
└─ 使用 HTTP 协议（本地教学，非公网 HTTPS）
~~~

GET 常用于读取数据，POST 常用于创建资源或提交处理；不能简单理解为 GET 一定安全、POST 一定持久写入，具体看服务设计。这里没有登录、生产数据库或任何真实账号。

常见状态码：

| 状态 | 通俗解释 | 本实验能否看到 |
|---|---|---|
| 200 | HTTP请求已正常处理 | 搜索接口正常返回 |
| 404 | 服务上没有这个路径或资源 | 浏览器访问不存在的路径 |
| 422 | FastAPI输入校验拒绝 | q 长于 64 字符 |
| 401 | 需要认证或凭证未通过 | 本实验没有认证，不要声称验证 |
| 403 | 已识别身份但没有对应授权 | 本实验没有授权，不要声称验证 |
| 429 | 请求达到限流条件 | 本实验没有限流，不要声称验证 |
| 503 | 依赖服务不可用等 | 本实验没有高可用部署，不要声称验证 |

### 2.5 什么是 JSON？

JSON 是跨语言传输结构化数据的常用格式。下面是本实验成功响应**示例**：

~~~json
{
  "items": [
    {"id": 1, "name": "广东示例大学", "province": "广东"}
  ],
  "total": 1
}
~~~

- 外层花括号表示对象；items 的方括号表示数组；每个学校又是一个对象；
- data.items[0].name 是 JavaScript 访问第一所学校名称的常见写法；
- Python 字典和 JSON 外观相近，但不是同一个语法标准，布尔值/null等细节有区别；
- 不把整份学校表、密码或内部敏感字段随便送到浏览器。

### 2.6 什么是同步、异步、await？

浏览器发送 HTTP 请求后，服务器需要处理时间。**fetch 返回 Promise**，代表未来才有结果。await 在当前 async 函数中等待 Promise 的兑现结果，而不是让整个浏览器界面停止响应。

~~~js
const response = await fetch("/api/schools?q=广东");
const data = await response.json();
~~~

第一行等待 HTTP 响应，第二行等待响应体读取和 JSON 解析。它们是两个不同的异步步骤。

**重点边界**：fetch 收到 404 或 500 响应一般不会仅因 HTTP 状态错误而自动 reject，所以还必须检查 response.ok；网络断开等错误才会使 fetch reject。

## 3. 认识本节源文件：它们扮演什么角色？

~~~text
docs/learning/labs/
├── J01-L00-WEB-REQUEST-TUTORIAL.md   ← 你正在看的逐行教材
└── j01-web-request/
    ├── main.py                       ← Python FastAPI后端
    ├── index.html                    ← HTML/CSS/JavaScript前端
    ├── requirements.txt              ← 教学依赖
    └── tests/
        └── test_app.py               ← 正例与负例自动测试
~~~

请**先看本页逐行解读，再打开上面的真实文件**。不要求把整个网页手抄一次：核心10～30行要会亲手敲，长文件要能找到关键元素并修改。

## 4. 后端 Python：每一部分到底干什么？

打开 [main.py](j01-web-request/main.py)，依次解释：

**① 导入并创建应用**

~~~python
from pathlib import Path
from fastapi import FastAPI, Query
from fastapi.responses import FileResponse

app = FastAPI(title="J01 L00 学校查询教学实验")
~~~

和你熟悉的 Python import / 实例化一样。app 是 FastAPI 应用实例，不是数据库。Query 用于声明和约束 HTTP 查询参数。

**② 定义合成学校列表**

~~~python
SCHOOLS = [
    {"id": 1, "name": "广东示例大学", "province": "广东"},
    {"id": 2, "name": "广西示例学院", "province": "广西"},
    {"id": 3, "name": "北京示例大学", "province": "北京"},
]
~~~

这只是进程内列表，重启后仍来自源代码。**此时没有 MySQL**；不能说我们完成了数据库查询。

**③ 返回网页**

~~~python
@app.get("/")
def home() -> FileResponse:
    return FileResponse(Path(__file__).with_name("index.html"))
~~~

浏览器访问网站根目录时，返回同文件夹的 HTML。用 Path(__file__) 使得从仓库根目录或实验目录启动时，都能找到这个页面。

**④ 接收查询并筛选**

~~~python
@app.get("/api/schools")
def get_schools(q: str = Query(default="", max_length=64)) -> dict:
    keyword = q.strip().lower()
    matches = [
        school for school in SCHOOLS
        if keyword in school["name"].lower()
    ]
    return {"items": matches, "total": len(matches)}
~~~

逐行理解：

1. @app.get 宣布：GET /api/schools 交给这个函数处理。
2. q 接收浏览器 URL 中的查询参数，默认空，最长64字符；超过长度时框架拒绝输入。
3. strip 删除查询词两端空白，lower 处理大小写；中文不会发生大小写转换。
4. 列表推导式遍历 SCHOOLS，只保留名称包含关键词的对象。
5. 返回 Python 字典；FastAPI 序列化成 JSON，HTTP响应发给浏览器。

**预测**：参数 q 为空字符串时，每个学校名都包含空字符串，所以返回所有三所学校；搜索「广东」只返回一所；搜索「不存在」是200响应 + 空数组而非404。

## 5. 前端 HTML/CSS/JavaScript：从页面到发请求

打开 [index.html](j01-web-request/index.html)。

### 5.1 HTML部分：先认识五种标签

~~~html
<h1>学校查询系统</h1>
<form id="searchForm">
  <label for="keyword">学校名称</label>
  <input id="keyword" name="q" placeholder="输入学校名称">
  <button type="submit">查询</button>
</form>
<p id="status" role="status" aria-live="polite"></p>
<ul id="schoolList"></ul>
~~~

- h1：标题；form：一个可提交的表单；
- label：表单字段文字；for=keyword关联 id=keyword 的输入框；
- input：让用户输入；button type=submit：触发表单提交；
- p：反馈查询中的状态；ul：放学校结果；
- id：页面上对应元素的标识；JS 会通过选择器定位它。

**你需要亲手敲**一个 h1 + label/input + button 的最小片段，别背整个文档头部。

### 5.2 CSS部分：选择器与样式

~~~css
body {
  max-width: 640px;
  margin: 40px auto;
  padding: 0 16px;
}
~~~

- body 是被选中的页面主体；大括号里是一组属性；
- max-width 给内容一个最大宽度；margin 左右 auto 让有剩余宽度时水平居中；
- padding 是内部留白，margin 是外部留白；
- 不需背所有CSS属性，本课能修改颜色、宽高、留白即可。

### 5.3 JavaScript部分：读懂核心请求代码

~~~js
const input = document.querySelector("#keyword");
const list = document.querySelector("#schoolList");
~~~

- document 表示当前网页；querySelector 按CSS选择器查找；
- #keyword 选择 id 为 keyword 的元素，返回元素引用；
- const 不允许给该变量绑定重新赋值，但不意味着引用对象完全不可变。

~~~js
async function searchSchools() {
  const keyword = input.value.trim();
  const response = await fetch(
    "/api/schools?q=" + encodeURIComponent(keyword)
  );
  if (!response.ok) {
    throw new Error("HTTP " + response.status);
  }
  const data = await response.json();
}
~~~

- async 允许在函数内使用 await；
- input.value 取用户输入，trim 去首尾空白；
- encodeURIComponent 对查询参数值进行 URL 编码，否则空格、&等字符可能破坏参数含义；
- await fetch 得到响应，response.ok 检查 HTTP 成功范围；
- await response.json 读取响应正文并解析 JSON。注意不是把数据库对象直接拿给浏览器。

~~~js
data.items.forEach((school) => {
  const li = document.createElement("li");
  li.textContent = school.name;
  list.appendChild(li);
});
~~~

- forEach 遍历学校数组；
- createElement 创建 li；textContent 只写文字，不把用户数据当HTML解释；
- appendChild 将结果插入页面。**Vue 会帮你封装不少手动 DOM 更新**，所以学 Vue 前先看懂这几个操作。

完整代码还使用 try/catch 处理异常、状态文字提示与 replaceChildren 清空旧结果。form 提交时调用 event.preventDefault 防止浏览器默认刷新，然后执行查询。**这是本课代码阅读重点，不需要把 HTML 逐字背诵。**

## 6. 真正启动：在你自己的开发环境运行

打开仓库后进入实验目录（此处使用相对仓库根目录的路径）：

~~~bash
cd docs/learning/labs/j01-web-request
python -m venv .venv
~~~

激活虚拟环境：

- **Windows PowerShell**：运行 .venv\Scripts\Activate.ps1；
- **Linux / macOS / WSL**：运行 source .venv/bin/activate。
- 如遇 PowerShell 脚本执行策略限制，可直接使用 .venv\Scripts\python.exe 运行后续命令，无需修改系统安全策略。

安装依赖并启动：

~~~bash
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload --port 8000
~~~

浏览器分别访问：

1. http://127.0.0.1:8000/ —— 前端页面；
2. http://127.0.0.1:8000/api/schools?q=广东 —— 返回 JSON；
3. http://127.0.0.1:8000/docs —— FastAPI 自动生成的交互式接口文档。

**预期**：页面能筛选三所合成学校；关键词「广东」返回1条；空关键词返回3条；无匹配关键词返回0条。**这些是预期，不是本轮替你执行的事实**。

> **排障入口**：若页面无法打开，先检查 uvicorn 是否仍在运行、Python/依赖是否正确、8000端口是否被Gaobao或其他程序占用。若终端显示端口被占用可换为 --port 8010，同时访问8010。前后端由同一个FastAPI提供，教学样例通常不会出现跨端口CORS问题。

## 7. 学浏览器 DevTools：一定要亲眼看到 HTTP

打开网页，按 F12 → Network（网络）→ Fetch/XHR。输入「广东」并点击查询，找到 /api/schools?q=... 请求。

按下面几项观察并自己写下来：

| 你要检查的地方 | 预期能看到什么 | 这说明什么 |
|---|---|---|
| Request URL | /api/schools?q=... | 请求路径和查询参数 |
| Method | GET | 在读取数据 |
| Status | 200 | 该请求在HTTP层成功 |
| Response | items 数组 + total | 后端按契约返回JSON |
| Timing | 有实际耗时 | 发送与等待响应不是同步取本地变量 |

可以再试一个不存在的地址 /api/not-found，观察 404；试传 65 个英文 a 作为 q，观察 422；浏览器网络断开或服务停止时前端会出现失败提示。

**不要强行期待本实验有401/403**：没有账号鉴权功能。这些状态要到 L08/L10 再学。

## 8. 代码到底要手敲多少？本课三个实操关卡

### 关卡 A（自己敲 5～15 行，入门）

不看上面的 HTML 片段，在 index.html 中**自己找到**标题与按钮，把「学校查询系统」改成「高考志愿查询系统」，按钮改成「搜索学校」。刷新确认改变，能说清这是HTML修改，不是Python逻辑。

### 关卡 B（自己改 Python 数据结构，基本）

在 main.py 的 SCHOOLS 数组里自行添加第四所**明显标注为示例**的学校。不要复制粘贴整个已有字典后不理解就改字。运行请求验证无关键词返回4条、新学校可按名称检索。若误少写逗号或引号，观察 Python 错误并修复。

### 关卡 C（关教程独立做新需求，关键验收）

把接口从只有关键词搜索，扩展为同时支持省份参数：

- GET /api/schools?province=广东 只返回广东学校；
- GET /api/schools?q=示例&province=广西 返回两个条件都满足的结果；
- 无匹配返回 200、items空数组与total=0；
- 不改变原有 q 接口兼容性；
- 进阶：给 HTML 增加省份选择框，把选择值发送给后端。

**此关不附完整答案**，学习者先改并运行；卡住时让导师先提示“函数参数怎么加”“filter条件如何组合”“前端如何编码第二个参数”，再请求完整解析。

## 9. 自动化测试：会运行，还要懂断言

在同一个实验目录执行：

~~~bash
python -m pytest -q
~~~

[测试源码](j01-web-request/tests/test_app.py) 针对以下行为给出训练用断言：

- 首页能够返回HTML；
- 空查询得到3条；
- 名称关键词筛选正确；
- 去除前后空白；
- 无匹配是成功响应 + 空数组；
- 超长参数被拒绝（422）。

**注意**：上述测试与初始3条演示数据绑定，完成关卡 B 添加第四条后，应更新相关预期断言，不能为了绿灯删除必要测试。完成 C 时，应自己增加省份/组合筛选的正负例测试。

**故意制造一个红灯**：将某个期望数量改成明显错误的数字，运行测试确认失败；再恢复正确期望，重跑观察变化。这是最小「失败→修复→复测」闭环，但要区分课程体验与真实生产故障处置。

## 10. 最后进行三道面试验收

1. **概念题**：HTML、CSS、JavaScript、FastAPI 分别负责什么？为什么不能说 Vue 3 不需要 HTML/CSS？
2. **读代码题**：逐句解释 fetch、await、response.ok、response.json；为什么获取404时仍需检查 ok？
3. **故障题**：Network看到200和正确 JSON，但网页列表不显示，如何从状态、DOM/选择器与Console定位？若服务器未启动又有什么不同？

### 通过标准（使用本仓 L1/L2/L3，而不是第二套等级）

- **L1**：不用照背术语，能解释请求链路和代码输入/输出；会用Network证明浏览器确实请求了后端。
- **L2**：亲手完成关卡 C（有变化条件）、新增正负例、真实测试通过并解释为什么通过。
- **L3**：再注入网络错误/无效输入，能自己定位修复、复测且说明为什么不通过“前端隐藏按钮”代替授权。

按照 [学习会话卡](../GAP-SESSION-TEMPLATE.md) 记录代码位置、commit、命令、真实日志、失败/修复、AI参与范围；结果写回唯一 [PROGRESS](../PROGRESS.md)。本页当前只证明**资料和代码被提供**，不证明任一学员已通过。

## 11. 继续深入的最少官方资料

- [MDN：HTML基础](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website/Creating_the_content)
- [MDN：CSS基础](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website/Styling_the_content)
- [MDN：HTTP概览](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview)
- [MDN：Fetch API使用](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)
- [FastAPI：First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/) 与 [Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/)

**停止条件**：亲手完成新需求并留证据，就进入 [J01 路线 L01/L02/L05 等实际缺口](../J01-HAIBOTE-FULLSTACK-LESSONS.md)；不要为了刷进度继续重复这一节。
