---
layout: post
title: "AI 编程助手完全指南"
categories: ai 数学建模
description: "本文将带你了解三款主流 AI 编程助手：GitHub Copilot、Cursor 和 Cline，帮助你选择最适合的工具"
keywords: vscode copilot, Cline+deepseek ,ai,建模
mermaid: false
sequence: false
flow: false
mathjax: true
mindmap: false
mindmap2: false
---

# 🚀 AI 编程助手完全指南

> 本文将带你了解三款主流 AI 编程助手：GitHub Copilot、Cursor 和 Cline，帮助你选择最适合的工具。

## 🌟 主流 AI 编程助手对比

### 💻 GitHub Copilot

- **核心优势**：
  - ⚡ 基于 OpenAI Codex 模型
  - 🔄 实时代码生成和补全
  - 🌐 多语言支持
  - 🎯 VS Code 完美集成
  - 🗣️ 自然语言转代码

### 🎯 Cursor

- **主要特点**：
  - 🛠️ 独立 AI 驱动编辑器
  - 🔄 强大的代码重构功能
  - 💬 自然语言对话式编程
  - 📊 智能代码分析
  - 📝 文档自动生成

### 🎨 Cline

- **特色功能**：
  - 🤖 支持多种 AI 模型(Claude/GPT/DeepSeek)
  - 🔌 VS Code 侧边栏集成
  - 🇨🇳 中文交互支持
  - ✨ 自定义提示词模板
  - 💰 免费基础功能

## 📚 VS Code + Copilot 详细教程

### 1️⃣ 安装配置

#### VS Code 安装

<!-- 插入链接 -->

[官方下载链接](https://code.visualstudio.com/download)，下载与系统对应的版本

1. 同意协议
   同意安装协议，并点击下一步

<img src="/images/post/vscode1.png" width="100%" alt="xieyi"  style="center"/>

2. 选择安装路径
   选择 VS Code 的安装路径，建议使用默认路径，点击下一步

<img src="/images/post/vscode2.png" width="100%" alt="lujing"  style="center"/>

3. 直接点击下一步

<img src="/images/post/vscode3.png" width="100%" alt="anzhuangzhong"  style="center"/>

4. 直接点击下一步

<img src="/images/post/vscode4.png" width="100%" alt="wancheng"  style="center"/>

5. 点击安装，等待安装完整

<img src="/images/post/vscode5.png" width="100%" alt="wancheng"  style="center"/>

#### VS Code 汉化

1. 打开 vscode 插件面板
2. 在输入框输入"中文"
3. 选择简体中文插件
4. 点击安装

<img src="/images/post/hanhua.png" width="100%" alt="vscode7"  style="center"/>

5. 安装完成后，选择右下角的 "change language and restart"

<img src="/images/post/hanhua2.png" width="100%" alt="vscode7"  style="center"/>

#### Copilot 配置

1. **获取 Copilot 许可**

   - 访问 [GitHub Student Developer Pack](https://education.github.com/pack)
   - 使用学校邮箱注册 GitHub 账号
   - 完成学生身份验证
   - 获取免费的 Copilot 访问权限

2. **安装 VS Code Copilot 插件**

   - 打开 VS Code 扩展面板 (Ctrl+Shift+X)
   - 搜索 "GitHub Copilot"
   - 点击"安装"按钮

3. **GitHub 账号授权**

   - 再 vscode 欢迎界面点击”配置 copilot“

    <img src="/images/post/copilot1.png" width="100%" alt="vscode7"  style="center"/>

   - 点击登录

     <img src="/images/post/copilot2.png" width="100%" alt="vscode7"  style="center"/>

   - 按要求进行授权
   - 授权完成后打开 vscode,点击顶部工具栏的兔头图标。打开 copilot 对话框

    <img src="/images/post/copilot.png" width="100%" alt="vscode7"  style="center"/>

    <img src="/images/post/copilot3.png" width="100%" alt="vscode7"  style="center"/>

4. **配置快捷键（可选）**

   - 打开快捷键设置 (Ctrl+K Ctrl+S)
   - 搜索 "copilot"
   - 可自定义以下快捷键：
     - 接受建议: Tab
     - 显示下一建议: Alt+]
     - 显示上一建议: Alt+ [
     - 触发行内建议: Alt+\

5. **验证工作状态**
   - 新建一个代码文件
   - 输入一些代码或注释
   - 观察是否出现实时代码建议
   - 确认 Tab 键可以接受建议

### 2️⃣ Copilot 使用指南

#### 💡 功能亮点

- 🚀 实时代码补全
- 🔄 自然语言转代码
- ⚡ 智能代码生成
- 🌐 多语言支持

#### 🎮 交互模式

1. **Ask 模式**

   - 💭 简单问题咨询
   - ⚡ 快速代码建议
   - 📝 简洁直接回答

2. **Agent 模式**
   - 🔍 复杂任务处理
   - 📂 工作区文件分析
   - 🔄 多步骤问题解决

### 3️⃣ 实战案例：MATLAB 心形曲线

1. 咒语

```
使用xx 语言帮我生成一个xxx 功能的程序，并满足下列要求
要求1：
要求2：
要求3：
```

2. 实战输入

```
使用matlab语言帮我生成一个绘制心型曲线的程序，并满足下列要求
1. 图形位于正中间
2. 添加标题"心型曲线"
3. x轴每一个小格为0.5
4. 自动帮我新建matlab 文件 heart.m
```

1. 将上述对话输入的 copilot 对话框并选择 agent 模式，等待 copilot
2. copilot 运行结果：

```matlab
% 清空工作区和命令窗口
clear all;
clc;

% 生成参数方程的参数 t
t = linspace(0, 2*pi, 1000);

% 心形曲线的参数方程
x = 16 * (sin(t)).^3;
y = 13 * cos(t) - 5 * cos(2*t) - 2 * cos(3*t) - cos(4*t);

% 创建图形窗口并设置位置
figure('Position', [300 200 600 500]);  % 设置窗口位置和大小

% 绘制曲线
plot(x, y, 'r-', 'LineWidth', 2);

% 设置图形属性
title('心型曲线', 'FontSize', 14);  % 添加标题
grid on;  % 显示网格
axis equal;  % 等比例显示
axis([-20 20 -20 15]);  % 设置坐标轴范围

% 设置坐标轴刻度间隔
xticks(-20:0.5:20);  % x轴每0.5一个刻度
yticks(-20:0.5:15);  % y轴每0.5一个刻度

% 添加坐标轴标签
xlabel('X轴');
ylabel('Y轴');
```

5. 打开 matlab ，找到生成的文件并拉入到 matlab 中，输出结果

<img src="/images/post/heart1.png" width="100%" alt="vscode7"  style="center"/>

## cline + deepseek

### 安装步骤

1. 在 vscode 插件界面，搜索 cline 并安装
2. 打开网页 [deepseek_api_key](https://platform.deepseek.com/api_keys),注册并申请 api_key
3. 在 cline 的设置界面输入 api_key

<img src="/images/post/cline8.png" width="100%" alt="vscode7"  style="center"/>

<img src="/images/post/cline1.png" width="100%" alt="vscode7"  style="center"/>

安装配置推荐查看这篇文章[cline + deepseek
](https://zhuanlan.zhihu.com/p/17795804526)

### cline 中文配置

将下面语句复制到，cline 设置的 custon instructions 中

```
Always respond in 中文
```

<img src="/images/post/cline1.png" width="100%" alt="vscode7"  style="center"/>

### Cline 的 Act 模式与 Plan 模式

Cline 提供两种核心交互模式，满足不同场景需求：

#### Act 模式（执行模式）

- **核心功能**：直接执行代码操作
- **适用场景**：

  - 文件创建/修改
  - 代码重构
  - 系统命令执行
  - 自动化任务

- **特点**：
  - 每步操作需用户确认
  - 支持文件读写/命令执行等底层操作
  - 适合明确的技术任务

#### Plan 模式（规划模式）

- **核心功能**：方案设计与信息收集
- **适用场景**：

  - 需求不明确的任务
  - 技术方案设计
  - 架构讨论
  - 学习研究

- **特点**：
  - 纯对话交互，不执行实际操作
  - 可生成技术图表和方案文档
  - 适合探索性任务

#### 模式选择建议

| 场景类型     | 推荐模式  | 原因说明               |
| ------------ | --------- | ---------------------- |
| 明确编码任务 | Act 模式  | 直接执行，效率高       |
| 需求模糊任务 | Plan 模式 | 先厘清需求再执行       |
| 系统级操作   | Act 模式  | 需要底层工具支持       |
| 技术方案讨论 | Plan 模式 | 适合头脑风暴和方案设计 |

### deepseek api key 收费

deepseek 使用相对便宜，具体一个 task 收费在 0.01 美元左右

<img src="/images/post/deepseek.png" width="100%" alt="vscode7"  style="center"/>

具体来说：DeepSeek 采用积分制收费模式：

1. **新用户福利**：

   - 注册即可获得 100 积分免费试用
   - 积分可用于体验所有 API 功能

2. **购买方案**：

   - 入门套餐：¥69/1000 积分
   - 进阶套餐：¥329/6000 积分
   - 专业套餐：¥669/15000 积分
   - 企业套餐：可定制

3. **积分使用说明**：

   - 按照实际使用量扣除积分
   - 基础对话消耗 1-2 积分/次
   - 代码生成任务消耗 2-5 积分/次
   - 复杂分析任务消耗 5-10 积分/次
   - 积分永久有效

4. **支付方式**：

   - 支持支付宝
   - 支持微信支付
   - 支持银联卡支付

5. **优惠政策**：
   - 学生认证可享受 8 折优惠
   - 批量购买有额外折扣
   - 定期推出促销活动
   - 推荐新用户可获得额外积分奖励

### 实战

1. 点击 vscode 的侧边栏，打开 cline 对话框

<img src="/images/post/cline6.png" width="100%" alt="vscode7"  style="center"/>

2. 将下列语句复制到对话框，

```
使用matlab语言帮我生成一个绘制心型曲线的程序，并满足下列要求
1. 图形位于正中间
2. 添加标题"心型曲线"
3. x轴每一个小格为0.5
4. 自动帮我新建matlab 文件 heart.m
```

3. 选择"act" 模式并点击发送。
4. 根据输出提示操作
5. 输出结果

<img src="/images/post/heart2.png" width="100%" alt="vscode7"  style="center"/>

### cline 总结

1. cline 不能使用 tab 补全功能，针对文件修改整体体验不如 copilot
2. cline 的 act 模式比 copilot 的 agent 模式强大
3. cline 费用便宜，适合预算有限的开发者
4. 使用 deepseek 对中文语境支持较高
5. deepseek 文本更新没有跟上最新进展，使用近几年的建模方法可能无法使用

### 使用建议

1. **适合使用 Copilot 的场景**

   - 需要频繁代码补全
   - 追求实时编码体验
   - 主要使用英语编程
   - 预算充足的团队或个人

2. **适合使用 Cline 的场景**
   - 需要中文交互
   - 预算有限的个人开发者
   - 需要灵活切换不同 AI 模型
   - 偏好对话式编程辅助

## Cursor

1. corsor 是最好的编程助手没有之一
2. cursor 也是最贵的编程助手

### cursor 收费

Cursor 采用订阅制收费模式，价格相对较高：

1. **订阅方案**：

   - 个人版：$20/月
   - 团队版：$40/用户/月
   - 企业定制版

2. **计费特点**：

   - 订阅包含所有功能
   - 无限制的 AI 对话次数
   - 无限制的代码生成
   - 实时代码分析和建议
   - 高级代码重构功能

3. **主要功能**：
   - GPT-4 驱动的代码智能
   - 自然语言代码生成
   - 代码解释和优化建议
   - 自动代码重构
   - 智能错误诊断
   - 实时代码审查

### 学生优惠

[学生优惠申请](https://blog.csdn.net/2503_90234341/article/details/147795169)

1. **资格要求**：

   - 需要有效的学生邮箱
   - 必须是全日制在校学生
   - 需要提供学生证明文件

2. **优惠力度**：

   - 个人版订阅半价优惠
   - 可获得完整功能访问权限
   - 优惠期限为一年
   - 到期后可续期（如仍是学生身份）

3. **申请步骤**：

   - 访问官网学生计划页面
   - 使用学校邮箱注册
   - 上传学生证明材料
   - 等待审核（1-2 工作日）

4. **注意事项**：
   - 优惠仅适用于个人使用
   - 不得用于商业用途
   - 每年需要重新验证身份
   - 违反使用条款将取消资格

## 🚀 最佳实践与建议

### 💡 工具选择指南

1. **Copilot 最适合**：

   - 🔄 持续编程开发
   - 🌐 英文环境工作
   - 💰 预算充足团队

2. **Cline 最适合**：

   - 🇨🇳 中文交互为主
   - 💰 预算控制场景
   - 🔄 需要灵活切换模型

3. **Cursor 最适合**：
   - 🏢 专业开发团队
   - 👥 大型项目协作
   - ⚡ 追求极致体验
