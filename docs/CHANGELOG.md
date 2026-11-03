## [2026-10-19 20:30] 修复菊展独立示例空白页面

- **需求/问题描述**：
  > 修复 `character0/261019/liDemo copy.html`。

- **实际实现的功能与改动**：
  - 复用同目录课程页案例，补回热门品种、观赏建议和品种档案。
  - 将正文放入现有菊展样式容器，移除会产生重复标记的幻灯片列表样式。
  - 新增 Python 标准库回归测试；修改前因缺少列表条目失败，修改后 1 项测试通过。
  - `git diff --check` 通过。ego-browser 首次设置未完成，未执行浏览器运行和视觉验证。

- **涉及文件**：
  - `character0/261019/liDemo copy.html`
  - `tests/test_li_demo.py`
  - `memory/agents.md`、`memory/plan.md`、`memory/progress.md`、`memory/verify.md`、`memory/gotchas.md`
  - `docs/CHANGELOG.md`

- **Git 提交**：`7a7c58b fix: restore chrysanthemum list demo content`；已普通推送至 `origin/main`。

---

## [2026-11-03 21:29] 完成墨荷详情页与往返跳转

- **需求/问题描述**：
  > 参照截图完成墨荷详情页，让菊展热门品种“墨荷”进入详情页，并让详情页两处返回链接回到菊展首页。

- **实际实现的功能与改动**：
  - `MH/index.html` 保留为菊展首页，热门品种“墨荷”链接到父目录详情页。
  - 父目录 `index.html` 按截图设置米黄色背景、居中标题和图片，补齐品种档案、品种简介、观赏提示和两处返回链接。
  - 使用指定 Unsplash 图片，提供替代文本与图片宽度适配；未引入依赖或 JavaScript。
  - 新增 3 项专项测试，修改前因缺少链接与详情内容失败，修改后全部 4 项测试通过；`git diff --check` 通过。
  - ego-browser 实际点击首页入口及两处返回链接均成功，图片加载为 600×400，桌面视口无横向溢出。未执行窄屏及截图比对。
  - 沙箱禁止启动本地 HTTP 监听，已通过本地文件路径完成浏览器行为验证。

- **涉及文件**：
  - `assignments/261103/index.html`
  - `assignments/261103/MH/index.html`
  - `tests/test_mohe_navigation.py`
  - `memory/agents.md`、`memory/plan.md`、`memory/progress.md`、`memory/verify.md`
  - `docs/CHANGELOG.md`

- **Git 提交**：待提交。

---
