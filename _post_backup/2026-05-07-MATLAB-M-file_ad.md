---
layout: post
title: "MATLAB M 文件与函数"
categories: matlab 编程 基础语法
description: "本文将详细介绍 MATLAB 中 M 文件的创建与编辑、函数的定义与调用、调试技巧以及编程风格规范，帮助你快速掌握 MATLAB 编程基础"

keywords: matlab, M文件, 函数, 调试, 编程风格, 匿名函数, 子函数
mermaid: false
sequence: false
flow: false
mathjax: true
mindmap: false
mindmap2: false
---

# 📁 MATLAB M文件与函数

> M 文件是 MATLAB 编程的核心载体。MATLAB 不仅是一个交互式计算环境，更是一种强大的编程语言。通过将一系列命令写入 M 文件，我们可以以完整的单元形式执行代码，编写可复用的函数，并构建复杂的应用程序。掌握 M 文件的创建、函数定义与调试技巧，是精通 MATLAB 编程的关键一步。

---

## 📑 目录

> 本文内容导航（可快速了解文章结构）：

1. 📁 **M文件基础** —— M 文件的创建与编辑
   - ✏️ 使用 edit 命令编辑 m 文件
   - 📜 脚本文件与函数文件
   - ▶️ M 文件的执行方式
   - 🗂️ 文件路径与搜索路径
   - 💡 M 文件的注释与帮助
2. 🔧 **函数** —— 函数的定义、参数与返回值
   - 📝 函数定义
   - 🧩 示例函数
   - 🔄 函数的参数与返回值
   - ⚡ 匿名函数
   - 🏗️ 主和子函数
   - 🔢 可变参数 varargin 与 varargout
   - ✅ 参数校验
   - 🎯 函数句柄
   - 🪆 嵌套函数
   - 🔒 私有函数
   - 🔁 递归函数
   - 🎛️ 函数默认参数
3. 🐞 **M文件调试** —— 错误类型、断点调试与错误处理
   - ⚠️ 常见的错误类型
   - 🎯 使用编辑器断点调试
   - ⌨️ 使用命令行调试命令
   - 🛡️ 使用 try-catch 捕获错误
   - 📢 使用 warning 和 error 提示
   - ⏱️ 使用 profiler 性能分析
   - 🧷 使用 assert 断言
   - 🛑 使用 keyboard 暂停调试
4. ✨ **MATLAB编程风格** —— 命名规范、注释与代码布局
   - 🏷️ 命名规范
   - 💬 代码注释
   - 📐 代码布局与缩进
   - 🔇 使用分号控制输出
   - ⚡ 向量化编程
   - 📚 使用帮助文档
   - 🧪 单元测试
   - 🚀 代码性能优化
   - 🔍 使用 checkcode 代码分析
   - 🧬 面向对象编程（OOP）
   - 🔗 版本控制与协作

---

## 📁 M文件基础

到目前为止，我们已经使用 MATLAB 环境作为计算器。但是，MATLAB 还是一种强大的编程语言，也是一种交互式计算环境。在前面的章节中，您学习了如何从 MATLAB 命令提示符下输入命令。MATLAB 还允许您将一系列命令写入文件并以完整的单元形式执行文件，例如编写函数和调用它。

### ✏️ 使用 edit 命令编辑 m 文件

编辑 m 文件 `forexp.m`：

```matlab
edit forexp.m
```

如果 m 文件不存在，MATLAB 会提示用户是否要创建一个新文件。如果用户选择创建，MATLAB 会自动创建一个新文件。如果 m 文件存在，会直接打开该文件。

<img src="/images/post/matlab_m.png" width="100%" alt="matlab.png"  style="center"/>

将下列代码复制到 MATLAB 打开的 m 文件编译窗口中，并保存文件。

```matlab
for i = 1:1:10
    if i == 5
        continue
    end
    disp("i = " + num2str(i))
end
```

回到 MATLAB 命令提示符下，输入 `forexp` 来调用：

```matlab
>> forexp
```

> **💻 运行结果**
>
> ```
> i = 2
> i = 3
> i = 4
> i = 6
> i = 7
> i = 8
> i = 9
> i = 10
> ```

### 📜 脚本文件与函数文件

M 文件分为两种类型：**脚本文件（Script）** 和 **函数文件（Function）**。理解两者的区别是 MATLAB 编程的基础。

|     类型     | 是否有输入输出 |     工作区     |     文件开头      | 典型用途                     |
| :----------: | :------------: | :------------: | :---------------: | :--------------------------- |
| **脚本文件** |   无输入输出   | 共享基础工作区 |    直接写命令     | 执行一系列操作、数据处理流程 |
| **函数文件** |   有输入输出   |   独立工作区   | `function` 关键字 | 封装可复用的计算逻辑         |

```matlab
% 脚本文件 scriptDemo.m —— 直接写命令，无 function 关键字
x = 1:10;
y = x.^2;
plot(x, y)
```

```matlab
% 函数文件 funcDemo.m —— 以 function 关键字开头
function y = funcDemo(x)
    y = x.^2;
end
```

> **💡 提示**：脚本文件共享基础工作区，脚本中创建的变量在脚本运行后仍然存在；而函数文件拥有独立的工作区，函数内部的变量不会污染基础工作区。

### ▶️ M 文件的执行方式

M 文件有多种执行方式，可以根据需要选择：

|      执行方式      | 说明                                           |
| :----------------: | :--------------------------------------------- |
| **直接输入文件名** | 在命令窗口输入文件名（不带 `.m` 后缀）即可运行 |
|   **`run` 命令**   | 使用 `run('文件名.m')` 运行脚本文件            |
|   **编辑器运行**   | 在编辑器中点击"运行"按钮或按 `F5` 快捷键       |
|  **`eval` 命令**   | 使用 `eval('文件名')` 动态执行                 |

```matlab
>> forexp          % 直接输入文件名运行
>> run('forexp.m') % 使用 run 命令运行
```

### 🗂️ 文件路径与搜索路径

MATLAB 通过**搜索路径（Search Path）** 来查找函数和脚本文件。当你在命令窗口输入一个函数名时，MATLAB 会按照搜索路径的顺序查找该文件。

|   命令    | 功能                                                |
| :-------: | :-------------------------------------------------- |
|  `path`   | 显示当前搜索路径                                    |
| `addpath` | 添加文件夹到搜索路径，例如 `addpath('D:\myfolder')` |
| `rmpath`  | 从搜索路径中移除文件夹                              |
|  `which`  | 显示函数或文件的完整路径，例如 `which forexp`       |
|   `cd`    | 更改当前工作目录                                    |
|   `pwd`   | 显示当前工作目录                                    |

```matlab
>> path                    % 查看搜索路径
>> addpath('D:\myfolder')  % 添加文件夹到搜索路径
>> which forexp            % 查看 forexp 的完整路径
>> pwd                     % 查看当前工作目录
```

> **⚠️ 警告**：<span style="color:red">如果 M 文件不在当前工作目录或搜索路径中，MATLAB 将无法找到该文件并报错。建议将常用的自定义函数文件夹添加到搜索路径中。</span>

### 💡 M 文件的注释与帮助

在函数文件开头使用 `%` 注释，可以生成函数的帮助文档。使用 `help` 命令可以查看这些注释。

```matlab
function y = mySquare(x)
% mySquare 计算输入值的平方
% 输入：
%   x - 数值或数组
% 输出：
%   y - x 的平方
    y = x.^2;
end
```

```matlab
>> help mySquare
```

> **💻 运行结果**
>
> ```
> mySquare 计算输入值的平方
> 输入：
>   x - 数值或数组
> 输出：
>   y - x 的平方
> ```

> **💡 提示**：在函数文件开头紧跟在 `function` 声明之后的注释行，会被 MATLAB 自动识别为帮助文本，可通过 `help` 命令查看。

---

## 🔧 函数

### 📝 函数定义

函数是一起执行任务的一组语句。在 MATLAB 中，函数是在单独的文件中定义的。文件名和函数名应该相同。

函数语句的语法是：

```matlab
function [out1, out2, ..., outN] = myfun(in1, in2, in3, ..., inN)
```

### 🧩 示例函数

编辑 m 文件 `a2b3.m`：

```matlab
edit a2b3.m
```

将下列代码复制到 `a2b3.m` 文件中，并保存文件。

```matlab
function [c, d] = a2b3(a, b)
    c = a * 2;
    d = b * 3;
end
```

回到 MATLAB 命令提示符下，输入 `a2b3` 来调用：

```matlab
>> [c, d] = a2b3(2, 3)
```

> **💻 运行结果**
>
> ```
> c = 4
> d = 9
> ```

### 🔄 函数的参数与返回值

- **函数的参数**：函数调用时传递给函数的值。参数可以是标量、向量、矩阵等。
- **函数的返回值**：函数执行完毕时返回的值。返回值可以是标量、向量、矩阵。当函数返回多个值时，这些值会被赋值给多个变量。

```matlab
% 获取所有的函数返回值：
>> [c, d] = a2b3(2, 3)
```

> **💻 运行结果**
>
> ```
> c = 4
> d = 9
> ```

```matlab
% 只获取第一个返回值，其他返回值会被忽略：
>> c = a2b3(2, 3)
```

> **💻 运行结果**
>
> ```
> c = 4
> ```

```matlab
% 只获取第二个返回值，其他返回值会被忽略：
>> [~, d] = a2b3(2, 3)
```

> **💻 运行结果**
>
> ```
> d = 9
> ```

### ⚡ 匿名函数

匿名函数就像传统编程语言中的内联函数一样，是在单个 MATLAB 语句中定义的。

```matlab
>> power = @(x, n) x.^n;
>> result1 = power(7, 3)
>> result2 = power(49, 0.5)
>> result3 = power(10, -10)
>> result4 = power(4.5, 1.5)
```

> **💻 运行结果**
>
> ```
> result1 = 343
> result2 = 7
> result3 = 1.0000e-10
> result4 = 9.5459
> ```

### 🏗️ 主和子函数

除匿名函数外，所有函数都必须在文件中定义。每个函数文件包含一个必需的主函数（必须首先出现），以及任意数量的可选子函数（位于主函数之后，供主函数调用）。

文件 `a4b5.m` 的函数定义如下：

```matlab
function [c, d] = a4b5(a, b)
    c = a4(a);
    d = b5(b);
end

function c = a4(a)
    c = a * 4;
end

function d = b5(b)
    d = b * 5;
end
```

调用函数：

```matlab
[c, d] = a4b5(2, 3)  % 主函数与m文件同名，可以在外部直接调用
% c = a4(2)          % 错误：子函数不能在外部直接调用
% d = b5(3)          % 错误：子函数不能在外部直接调用
```

> **💻 运行结果**
>
> ```
> c = 8
> d = 15
> ```

> **⚠️ 警告**：<span style="color:red">在一个文件中定义多个函数，一定要注意只有主函数（与 m 文件同名的函数）可以在外部直接调用，其他子函数只能在主函数中调用。</span>

### 🔢 可变参数 varargin 与 varargout

有时函数需要处理**不定数量**的输入或输出参数，此时可以使用 `varargin` 和 `varargout`：

- **`varargin`**：可变数量的输入参数（Variable-length input argument list），以元胞数组的形式保存所有额外传入的参数。
- **`varargout`**：可变数量的输出参数（Variable-length output argument list），同样以元胞数组的形式保存。

```matlab
function result = sumAll(varargin)
% sumAll 计算任意数量输入参数的总和
    result = 0;
    for i = 1:nargin
        result = result + varargin{i};
    end
end
```

调用：

```matlab
>> sumAll(1, 2, 3)
```

> **💻 运行结果**
>
> ```
> ans = 6
> ```

```matlab
>> sumAll(1, 2, 3, 4, 5)
```

> **💻 运行结果**
>
> ```
> ans = 15
> ```

`varargout` 示例：

```matlab
function varargout = minMax(x)
% minMax 返回向量中的最小值和最大值
    varargout{1} = min(x);
    varargout{2} = max(x);
end
```

调用：

```matlab
>> [mn, mx] = minMax([3 1 4 1 5])
```

> **💻 运行结果**
>
> ```
> mn = 1
> mx = 5
> ```

> **💡 提示**：`nargin` 表示函数实际接收的输入参数个数，`nargout` 表示函数实际请求的输出参数个数，二者常与 `varargin`、`varargout` 配合使用。

### ✅ 参数校验

参数校验是指检查输入参数是否符合预期，从而提高代码的健壮性，避免错误结果在不知不觉中产生。常用的方式有以下三种：

**1. 使用 `nargin` 判断参数个数**

```matlab
function y = myFunc(x, a, b)
    if nargin < 3
        error('需要提供至少三个输入参数');
    end
    y = x + a + b;
end
```

**2. 使用 `validateattributes` 校验属性**

```matlab
function y = processData(data)
    validateattributes(data, {'numeric'}, {'vector', 'finite'}, ...
        'processData', 'data', 1);
    y = data * 2;
end
```

**3. 使用 `arguments` 块（R2019b 及以后推荐）**

```matlab
function y = drawLine(x, y, varargin)
    arguments
        x (1, :) double {mustBeFinite}
        y (1, :) double {mustBeFinite}
        varargin
    end
    plot(x, y, varargin{:})
end
```

常用的内置校验函数：

|      校验函数       | 功能                     |
| :-----------------: | :----------------------- |
|   `mustBeNumeric`   | 输入必须为数值           |
|    `mustBeReal`     | 输入必须为实数           |
|  `mustBePositive`   | 输入必须为正数           |
|   `mustBeFinite`    | 输入必须为有限值         |
|   `mustBeMember`    | 输入必须是某个集合的成员 |
| `mustBeNonnegative` | 输入必须为非负数         |

> **💡 提示**：在 `arguments` 块中使用 `mustBe*` 系列函数作为校验条件，当校验失败时 MATLAB 会自动抛出含义清晰的错误信息。

### 🎯 函数句柄

**函数句柄（Function Handle）** 是 MATLAB 的一种数据类型，用于存储指向函数的引用。函数句柄可以像普通变量一样传递、存储和调用，是 MATLAB 函数式编程的核心工具。创建函数句柄使用 `@` 符号。

```matlab
>> f = @sin;           % 创建内置函数 sin 的句柄
>> f(pi/2)
```

> **💻 运行结果**
>
> ```
> ans = 1
> ```

函数句柄的典型应用：

**1. 作为参数传递给其他函数**（例如 `fplot`、`fzero`、`integral`）：

```matlab
>> integral(@(x) x.^2, 0, 1)   % 计算定积分 ∫₀¹ x² dx
```

> **💻 运行结果**
>
> ```
> ans = 0.3333
> ```

**2. 存储在元胞数组中批量调用**：

```matlab
operations = {@(x) x + 1, @(x) x * 2, @(x) x.^2};
r1 = operations{1}(5)  % r1 = 6
r2 = operations{2}(5)  % r2 = 10
r3 = operations{3}(5)  % r3 = 25
```

**3. 查看句柄对应的函数信息**：

```matlab
>> func2str(@sin)
```

> **💻 运行结果**
>
> ```
> ans = 'sin'
> ```

### 🪆 嵌套函数

**嵌套函数（Nested Function）** 是定义在其他函数**内部**、并以 `end` 结尾的函数。嵌套函数最重要的特点是：**可以访问外层函数工作区中的变量**。

```matlab
function result = outerFunc(a, b)
% outerFunc 演示嵌套函数
    x = a + b;
    result = innerFunc(a);               % 调用嵌套函数
    disp(['x 的值为：' num2str(x)])      % x 仍可被访问

    function y = innerFunc(z)
        y = z * x;   % 嵌套函数可以直接使用外层函数的变量 x
    end
end
```

调用：

```matlab
>> outerFunc(3, 4)
```

> **💻 运行结果**
>
> ```
> x 的值为：7
> ans = 21
> ```

> **⚠️ 警告**：<span style="color:red">使用嵌套函数时，文件内**所有**函数（包括外层函数）都必须以 `end` 结尾。这与普通子函数文件的写法不同。</span>

### 🔒 私有函数

**私有函数（Private Function）** 放在名为 `private` 的子文件夹中，只能被其父文件夹中的函数调用，对其他位置的代码不可见。私有函数常用于隐藏内部实现细节，避免命名冲突。

目录结构示例：

```
myfunctions/
    publicFunc.m     % 公共函数
    private/
        helper.m     % 私有函数，只能被 myfunctions 文件夹中的函数调用
```

```matlab
% publicFunc.m —— 公共函数，可被外部调用
function result = publicFunc(x)
    result = helper(x) * 10;   % 调用私有函数
end
```

```matlab
% private/helper.m —— 私有函数，仅在父文件夹内可见
function y = helper(x)
    y = x + 1;
end
```

调用：

```matlab
>> publicFunc(2)   % 正常调用
```

> **💻 运行结果**
>
> ```
> ans = 30
> ```

```matlab
>> helper(2)   % 错误：私有函数只能在父文件夹内调用
```

### 🔁 递归函数

**递归（Recursion）** 是指函数直接或间接地调用自身。递归函数通常包含两个部分：

- **基准情形（Base Case）**：递归的终止条件；
- **递归步骤（Recursive Step）**：函数调用自身、逐步逼近基准情形。

```matlab
function f = myFactorial(n)
% myFactorial 使用递归计算 n 的阶乘
    if n <= 1
        f = 1;                     % 基准情形
    else
        f = n * myFactorial(n-1);  % 递归步骤
    end
end
```

调用：

```matlab
>> myFactorial(5)
```

> **💻 运行结果**
>
> ```
> ans = 120
> ```

> **⚠️ 注意**：递归函数必须确保存在终止条件，否则会陷入无限递归导致栈溢出错误。对于简单的迭代问题，使用循环往往比递归更加高效、不易出错。

### 🎛️ 函数默认参数

MATLAB 本身不提供像其他语言那样直接的默认参数语法，但可以通过以下方式实现：

**1. 使用 `nargin` 判断（最基础）**

```matlab
function greet(name, greeting)
    if nargin < 2
        greeting = '你好';
    end
    if nargin < 1
        name = '世界';
    end
    disp([greeting '，' name '！'])
end
```

**2. 使用 `arguments` 块（R2019b 起，推荐）**

```matlab
function greet(name, greeting)
    arguments
        name (1, 1) string = "世界"
        greeting (1, 1) string = "你好"
    end
    disp(greeting + "，" + name + "！")
end
```

调用：

```matlab
>> greet()                     % 全部使用默认参数
```

> **💻 运行结果**
>
> ```
> 你好，世界！
> ```

```matlab
>> greet("小明")                % 只传第一个参数
```

> **💻 运行结果**
>
> ```
> 你好，小明！
> ```

```matlab
>> greet("小明", "晚上好")      % 传全部参数
```

> **💻 运行结果**
>
> ```
> 晚上好，小明！
> ```

---

## 🐞 M文件调试

调试是程序开发过程中非常重要的一环。当 M 文件运行出错或结果不符合预期时，我们需要借助 MATLAB 提供的调试工具来定位并修复问题。MATLAB 提供了多种调试方式，包括命令行调试命令、编辑器断点调试以及错误信息分析。

### ⚠️ 常见的错误类型

在调试之前，先了解 MATLAB 中常见的错误类型，有助于快速定位问题：

|    错误类型    | 说明                                                                     | 发现时机 |
| :------------: | :----------------------------------------------------------------------- | :------: |
|  **语法错误**  | 代码不符合 MATLAB 语法规则，例如缺少 `end`、括号不匹配、拼写错误等       |  运行前  |
| **运行时错误** | 代码语法正确，但在运行时出现问题，例如数组索引越界、除数为零、变量未定义 |  运行时  |
|  **逻辑错误**  | 代码可以正常运行，但计算结果不符合预期                                   |  运行后  |

> **💡 提示**：逻辑错误最难发现，通常需要借助断点逐步检查。

### 🎯 使用编辑器断点调试

MATLAB 编辑器提供了图形化的断点调试功能，是最直观的调试方式。

#### 设置断点

在编辑器窗口中，点击代码行号左侧的灰色横线区域，即可在该行设置一个红色圆断点。

<img src="/images/post/matalb_debug1.png" width="100%" alt="matlab_debug1.png"  style="center"/>

当程序运行到断点处时会暂停执行，此时可以查看和修改当前工作区的变量值。

<img src="/images/post/matalb_debug2.png" width="100%" alt="matlab_debug2.png"  style="center"/>

#### 调试工具栏

设置断点后，运行 M 文件，程序会在断点处暂停。此时编辑器上方会出现调试工具栏，常用的按钮包括：

<img src="/images/post/matalb_debug3.png" width="100%" alt="matlab_debug3.png"  style="center"/>

|   按钮   | 说明                                       |
| :------: | :----------------------------------------- |
| **继续** | 继续运行程序，直到下一个断点或程序结束     |
| **步进** | 逐行执行代码，遇到函数调用时会进入函数内部 |
| **步入** | 进入当前行调用的函数内部                   |
| **步出** | 跳出当前函数，返回到调用它的上一层         |
| **停止** | 结束调试会话                               |

#### 查看变量值

程序在断点处暂停时，可以将鼠标悬停在变量名上查看其当前值：

<img src="/images/post/matalb_debug4.png" width="100%" alt="matlab_debug4.png"  style="center"/>

也可以在"工作区"窗口中查看所有变量的值：

<img src="/images/post/matalb_debug5.png" width="100%" alt="matlab_debug5.png"  style="center"/>

还可以在命令行窗口输入变量名来查看其值：

<img src="/images/post/matalb_debug6.png" width="100%" alt="matlab_debug6.png"  style="center"/>

### ⌨️ 使用命令行调试命令

除了编辑器图形化调试，MATLAB 还提供了一组命令行调试命令，适合在脚本或命令行环境中使用。

|   命令    | 功能                                                               |
| :-------: | :----------------------------------------------------------------- |
| `dbstop`  | 设置断点，例如 `dbstop in forexp at 3` 在 `forexp.m` 第3行设置断点 |
| `dbclear` | 清除断点                                                           |
| `dbcont`  | 继续运行程序                                                       |
| `dbstep`  | 单步执行                                                           |
| `dbquit`  | 退出调试模式                                                       |
| `dbstack` | 显示当前调用栈                                                     |

例如，在命令行中设置断点并运行：

```matlab
>> dbstop in forexp at 3
>> forexp
```

程序会在 `forexp.m` 的第3行暂停，此时命令行提示符会变为 `K>>`，表示处于调试模式。可以输入变量名查看其值，使用 `dbstep` 单步执行，使用 `dbcont` 继续运行，使用 `dbquit` 退出调试。

### 🛡️ 使用 try-catch 捕获错误

对于可能出错的代码，可以使用 `try-catch` 结构捕获错误并给出友好提示，避免程序直接崩溃：

```matlab
try
    % 可能出错的代码
    result = 1 / x;
catch ME
    % 出错时执行的代码
    disp("发生错误：" + ME.message)
end
```

其中 `ME` 是错误对象，`ME.message` 保存了错误的具体信息。这样即使发生错误，程序也能继续执行后续代码。

> **💻 运行结果**
>
> ```
> forexp
> 发生错误：函数或变量 'x' 无法识别
> ```

### 📢 使用 warning 和 error 提示

在编写函数时，可以使用 `warning` 和 `error` 主动提示用户：

```matlab
function result = safeDivide(a, b)
    if b == 0
        error("除数不能为零！");
    end
    if abs(b) < 1e-6
        warning("除数接近零，结果可能不准确。");
    end
    result = a / b;
end
```

|   函数    | 说明                             |
| :-------: | :------------------------------- |
|  `error`  | 会抛出错误并终止程序执行         |
| `warning` | 会显示警告信息，但程序会继续执行 |

> **💻 运行结果**
>
> ```
> >> safeDivide(1, 0)
> 错误使用 safeDivide (第 3 行)除数不能为零！
>
> >> safeDivide(1, 0.000000001)
> 警告: 除数接近零，结果可能不准确。
> 位置：forexp (第 6 行)
>
> ans =
>
>                1000000000
> ```

### ⏱️ 使用 profiler 性能分析

当程序运行缓慢时，可以使用 **Profiler（性能分析器）** 找出性能瓶颈，定位耗时最多的代码行和函数。

```matlab
>> profile on          % 开启性能分析
>> myProgram()         % 运行待分析的程序
>> profile viewer      % 打开性能分析报告
>> profile off         % 关闭性能分析
```

`profile viewer` 会打开一个交互式报告窗口，展示每个函数的调用次数、运行总耗时和单次耗时等信息。点击具体的函数行，还能看到每一行代码的耗时分布（Self Time），从而精确定位性能瓶颈。

```matlab
>> profsave(profile('info'), 'profile_results')  % 将报告保存为 HTML 文件
```

> **💡 提示**：性能优化应遵循"先测量、后优化"的原则——先用 Profiler 找到瓶颈，再针对性地优化，而不是凭直觉猜测。

### 🧷 使用 assert 断言

**断言（Assertion）** 用于检查程序中必须成立的条件。如果条件为假，`assert` 会抛出错误并终止执行。断言是调试和防御性编程的重要工具：

```matlab
function result = computeMean(data)
    assert(~isempty(data), 'data 不能为空数组');
    assert(isnumeric(data), 'data 必须是数值数组');
    result = mean(data);
end
```

调用：

```matlab
>> computeMean(1:10)
```

> **💻 运行结果**
>
> ```
> ans = 5.5000
> ```

```matlab
>> computeMean([])
```

> **💻 运行结果**
>
> ```
> 错误使用 computeMean (第 2 行)
> data 不能为空数组
> ```

|    `assert` 语法    | 说明                               |
| :-----------------: | :--------------------------------- |
|   `assert(cond)`    | 条件 `cond` 为假时抛出默认错误信息 |
| `assert(cond, msg)` | 条件为假时抛出指定错误信息 `msg`   |

> **⚠️ 注意**：<span style="color:red">`assert` 主要用于检查程序内部的逻辑错误（如输入数据不符合预期），而不是用于处理正常业务流程中可预见的异常情况（这种情况应使用 `try-catch`）。</span>

### 🛑 使用 keyboard 暂停调试

在代码中插入 `keyboard` 命令，可以在该处暂停程序，进入**调试模式**。此时命令行提示符变为 `K>>`，可以像在普通命令行一样查看、修改工作区中的变量。输入 `return` 或 `dbcont` 可以恢复程序的执行。

```matlab
% keyboardDemo.m
x = 1:5;
y = x.^2;
keyboard;    % 程序运行到这里会暂停，进入调试模式
z = sum(y);
disp(z)
```

运行脚本：

```matlab
>> keyboardDemo
K>> y           % 在调试模式下查看变量 y
```

> **💻 运行结果**
>
> ```
> y =
>
>      1     4     9    16    25
> ```

```matlab
K>> x = x * 2  % 在调试模式下修改变量 x 的值
K>> dbcont     % 继续运行程序
```

> **💻 运行结果**
>
> ```
> 55
> ```

> **💡 提示**：`keyboard` 常用于在程序崩溃前"截停"程序，以便检查关键时刻的变量状态。但发布代码时务必删除或注释掉 `keyboard`，否则程序会意外暂停。

### 📝 调试技巧总结

|         技巧         | 说明                                                     |
| :------------------: | :------------------------------------------------------- |
|     **分步验证**     | 将复杂问题拆分成小步骤，逐步验证每一步的结果             |
|     **善用断点**     | 在关键计算处设置断点，检查中间变量的值是否符合预期       |
|    **检查工作区**    | 程序暂停时，仔细检查工作区中所有变量的值                 |
| **使用 `disp` 输出** | 在关键位置添加 `disp` 语句输出中间结果，帮助定位逻辑错误 |
|   **阅读错误信息**   | MATLAB 的错误信息通常会指出出错的文件、行号和具体原因    |

---

## ✨ MATLAB编程风格

良好的编程风格不仅能提高代码的可读性，还能减少出错的可能性，方便他人理解和维护你的代码。下面介绍一些 MATLAB 编程中常用的规范和最佳实践。

### 🏷️ 命名规范

#### 变量命名

- 变量名应具有描述性，能够清晰表达其含义。例如，用 `totalCost` 而不是 `tc`，用 `studentScore` 而不是 `s`。
- 变量名通常使用小写字母开头，后续单词首字母大写（驼峰命名法），例如 `maxValue`、`numStudents`。
- 常量通常使用全大写字母，例如 `PI`、`MAX_ITER`。
- 避免使用 MATLAB 内置函数名或关键字作为变量名，例如不要用 `sum`、`mean`、`if` 作为变量名。

```matlab
% 好的命名
totalCost = 100;
maxIterations = 50;

% 不好的命名
tc = 100;
mi = 50;
```

#### 函数命名

- 函数名应与文件名保持一致，且通常使用小写字母开头。
- 函数名应能反映函数的功能，例如 `calculateAverage`、`plotData`。

### 💬 代码注释

注释是代码的重要组成部分，良好的注释能帮助他人（以及未来的自己）理解代码逻辑。

#### 注释规范

- 在关键代码段前添加注释，说明该段代码的功能。
- 使用 `%` 进行单行注释，使用 `%{ ... %}` 进行块注释。
- 函数文件开头应包含注释，说明函数的功能、输入参数和返回值。

```matlab
function [avg] = calculateAverage(data)
% calculateAverage 计算数据的平均值
% 输入：
%   data - 一维数值数组
% 输出：
%   avg  - 数据的平均值
    avg = sum(data) / length(data);
end
```

#### 注释示例

```matlab
% 计算圆的面积
radius = 5;
area = pi * radius^2;  % 面积公式：πr²
```

### 📐 代码布局与缩进

- 使用一致的缩进（通常为4个空格）来体现代码的层级结构。
- 在运算符两侧添加空格，提高可读性，例如 `a + b` 而不是 `a+b`。
- 在逗号后添加空格，例如 `[1, 2, 3]` 而不是 `[1,2,3]`。
- 使用空行分隔逻辑上独立的代码块。

```matlab
for i = 1:10
    if mod(i, 2) == 0
        disp(i)  % 输出偶数
    end
end
```

### 🔇 使用分号控制输出

- 在语句末尾添加分号 `;` 可以抑制命令窗口中的输出，避免大量中间结果刷屏。
- 在调试时，可以暂时去掉分号来查看中间变量的值。

```matlab
x = 1:100;      % 不显示结果
y = x.^2;       % 不显示结果
z = sum(y)      % 显示结果
```

### ⚡ 向量化编程

MATLAB 擅长矩阵运算，应尽量使用向量化操作代替循环，以提高代码运行效率。

```matlab
% 不好的做法：使用循环
y = zeros(1, 100);
for i = 1:100
    y(i) = i^2;
end

% 好的做法：向量化
x = 1:100;
y = x.^2;
```

### 📚 使用帮助文档

- 使用 `help` 命令查看函数的使用说明，例如 `help sum`。
- 使用 `doc` 命令打开函数的详细文档，例如 `doc plot`。
- 使用 `lookfor` 命令根据关键词搜索相关函数，例如 `lookfor average`。

```matlab
>> help sum
>> doc plot
>> lookfor average
```

### 🧪 单元测试

**单元测试（Unit Test）** 用于验证函数在给定输入下是否产生正确的输出，是保证代码质量的重要手段。MATLAB 使用 **`matlab.unittest`** 框架进行单元测试。

#### 编写测试类

```matlab
% testMySquare.m —— 单元测试文件
classdef testMySquare < matlab.unittest.TestCase

    methods (Test)
        function testPositiveNumber(testCase)
            % 验证正数平方
            testCase.verifyEqual(mySquare(3), 9);
        end

        function testZero(testCase)
            % 验证 0 的平方
            testCase.verifyEqual(mySquare(0), 0);
        end

        function testVector(testCase)
            % 验证向量逐元素平方
            testCase.verifyEqual(mySquare([1 2 3]), [1 4 9]);
        end
    end
end
```

#### 运行测试

```matlab
>> results = runtests('testMySquare')
```

> **💻 运行结果**
>
> ```
> Running testMySquare
> ...
> Done testMySquare
> __________
> ```
>
> `results` 对象包含测试是否通过、失败数量等信息，可以查看 `results` 的摘要。

常用的验证方法：

|        方法         | 验证内容                     |
| :-----------------: | :--------------------------- |
|    `verifyEqual`    | 实际值等于期望值             |
|    `verifyTrue`     | 条件为真                     |
|    `verifyFalse`    | 条件为假                     |
| `verifyGreaterThan` | 实际值大于某个阈值           |
|    `verifyEmpty`    | 实际值为空                   |
|    `verifyError`    | 验证某段代码是否抛出指定错误 |

> **💡 提示**：养成"边写函数、边写测试"的习惯，在修改代码后重新运行测试，可以及时发现回归问题。

### 🚀 代码性能优化

当程序运行效率成为瓶颈时，可以从以下几个层面进行优化：

|      优化手段      | 说明                                                       |
| :----------------: | :--------------------------------------------------------- |
|   **预分配内存**   | 使用 `zeros` 或 `NaN` 预先分配数组大小，避免循环中动态扩容 |
|     **向量化**     | 使用矩阵运算代替循环，充分利用 MATLAB 的矩阵计算优势       |
|    **逻辑索引**    | 使用 `data(data > 5)` 代替 `find` + 循环                   |
|  **减少重复计算**  | 将循环内不变的计算提取到循环外                             |
| **使用 `tic/toc`** | 测量代码运行时间，评估优化效果                             |
|  **避免 `eval`**   | `eval` 会降低运行速度且难以调试，应尽量使用函数句柄代替    |

**预分配内存示例：**

```matlab
% 不好的做法：循环中动态扩容
for i = 1:10000
    y(i) = i^2;
end

% 好的做法：预分配内存
y = zeros(1, 10000);
for i = 1:10000
    y(i) = i^2;
end
```

**逻辑索引示例：**

```matlab
data = randn(1, 1e6);

% 方式一：使用 find + 循环（较慢）
idx = find(data > 0);
positive1 = data(idx);

% 方式二：逻辑索引（更快、更简洁）
positive2 = data(data > 0);
```

**使用 `tic/toc` 测量时间：**

```matlab
tic;
result = sum(1:1e6);
toc
```

> **💻 运行结果**
>
> ```
> 经过的时间是 0.001234 秒。
> ```

> **⚠️ 注意**：<span style="color:red">性能优化应遵循"先测量、后优化"原则，先用 Profiler 定位真正的瓶颈，避免过度优化浪费开发时间。</span>

### 🔍 使用 checkcode 代码分析

**`checkcode`**（编辑器中也称为 **Code Analyzer**）可以静态分析 M 文件，找出潜在的问题、隐患与风格问题，是提升代码质量的有力工具。

```matlab
>> checkcode('forexp.m')
```

对于含有潜在问题的代码，`checkcode` 会输出警告信息。例如对于以下文件 `demoCheck.m`：

```matlab
x = 1:10;
y = x.^2;
plot(x, y);
for i = 1:10
    z(i) = x(i) + 1;   % 未预分配数组 z
end
```

运行分析：

```matlab
>> checkcode('demoCheck.m')
```

> **💻 运行结果**
>
> ```
> L 7 (C 5-8): 变量 'z' 在每次循环迭代时都会更改大小，请考虑预先分配以提高速度。
> ```

在 MATLAB 编辑器中，代码行右侧或底部会出现**橙色波浪线**提示，将鼠标悬停即可查看分析结果。常见分析项包括：

|      常见问题       | 说明                                       |
| :-----------------: | :----------------------------------------- |
|   **变量预分配**    | 循环中数组动态增长，建议预分配内存         |
| **未使用变量/函数** | 定义但从未使用的变量或函数                 |
|    **可疑代码**     | 无法访问的代码、被覆盖的变量等             |
|  **代码风格问题**   | 建议使用分号抑制输出、增加括号明确优先级等 |

> **💡 提示**：养成定期运行 `checkcode` 的习惯，把编辑器的橙色波浪线当作"代码体检报告"，尽早发现问题。

### 🧬 面向对象编程（OOP）

MATLAB 不仅支持面向过程编程，还支持完整的**面向对象编程（Object-Oriented Programming，OOP）**。通过定义**类（Class）**，可以将数据（属性）和操作（方法）封装在一起，提升代码的复用性与可维护性。

#### 类的定义

在文件 `Student.m` 中定义一个学生类：

```matlab
classdef Student
    properties
        Name        % 姓名
        Score       % 成绩
    end

    methods
        % 构造函数
        function obj = Student(name, score)
            obj.Name = name;
            obj.Score = score;
        end

        % 普通方法
        function grade = getGrade(obj)
            if obj.Score >= 90
                grade = '优秀';
            elseif obj.Score >= 80
                grade = '良好';
            else
                grade = '及格';
            end
        end
    end
end
```

#### 类的使用

```matlab
>> s = Student('小明', 95);
>> s.Name
```

> **💻 运行结果**
>
> ```
> ans = '小明'
> ```

```matlab
>> s.getGrade()
```

> **💻 运行结果**
>
> ```
> ans = '优秀'
> ```

#### 类的继承

子类可以使用 `@` 继承父类，实现代码复用：

```matlab
classdef GraduateStudent < Student
    properties
        Advisor     % 导师
    end

    methods
        function obj = GraduateStudent(name, score, advisor)
            obj = obj@Student(name, score);
            obj.Advisor = advisor;
        end
    end
end
```

|       概念       | 关键字/语法            | 说明                     |
| :--------------: | :--------------------- | :----------------------- |
|    **类定义**    | `classdef`             | 定义一个新的类           |
|     **属性**     | `properties ... end`   | 类的数据                 |
|     **方法**     | `methods ... end`      | 类的操作                 |
|   **构造函数**   | `function obj = 类名`  | 创建对象的特殊方法       |
|     **继承**     | `classdef 子类 < 父类` | 子类复用父类的属性和方法 |
| **属性访问控制** | `(Access = private)`   | 限制属性的访问范围       |

> **💡 提示**：对于简单的计算任务，使用函数和脚本即可；当项目规模较大、涉及复杂数据结构时，OOP 能显著提升代码的组织性和可扩展性。

### 🔗 版本控制与协作

**版本控制（Version Control）** 是团队协作开发的基石。MATLAB 提供了与 **Git**、**Subversion（SVN）** 等版本控制系统的集成，帮助开发者跟踪代码变更、协同开发并避免冲突。

#### 常用 Git 命令

```bash
git init                    # 初始化仓库
git add .                   # 暂存所有更改
git commit -m "提交说明"     # 提交更改
git pull                    # 拉取远程更新
git push                    # 推送本地提交到远程
git status                  # 查看当前状态
git log                     # 查看提交历史
```

#### 在 MATLAB 中使用 Git

在 MATLAB 编辑器的"主页"选项卡中，点击"**Simulink**"旁的下拉菜单或右键文件，可以查看文件的 **Git 差异（Diff）**、提交（Commit）历史等信息。MATLAB 还提供了命令行接口：

```matlab
>> !git status        % 在 MATLAB 中执行系统命令
>> !git diff          % 查看当前更改
```

#### 协作开发的最佳实践

|        实践        | 说明                                                |
| :----------------: | :-------------------------------------------------- |
|    **分支管理**    | 使用独立分支开发新功能，通过合并（Merge）整合代码   |
|  **清晰提交信息**  | 每次提交附带简洁明了的说明，便于回溯历史            |
|    **及时同步**    | 定期 `pull` 拉取队友更新，减少冲突                  |
|  **忽略生成文件**  | 使用 `.gitignore` 忽略 `.asv`、`.m~` 等自动生成文件 |
|    **代码评审**    | 重大改动通过合并请求（Pull Request）进行团队评审    |
| **良好注释与文档** | 配合本文前述的命名规范与注释规范，让协作更加顺畅    |

> **⚠️ 注意**：<span style="color:red">MATLAB 的自动保存文件 `.asv`、备份文件 `~` 以及 `slprj` 等生成目录不应纳入版本控制，建议在 `.gitignore` 中加以排除。</span>

### 📝 编程风格总结

|     规范     | 说明                                   |
| :----------: | :------------------------------------- |
| **命名清晰** | 使用有意义的变量名和函数名             |
| **注释充分** | 在关键位置添加注释，说明代码意图       |
| **布局规范** | 保持一致的缩进和空格，提高可读性       |
| **控制输出** | 使用分号抑制不必要的输出               |
|  **向量化**  | 尽量使用矩阵运算代替循环               |
| **善用帮助** | 熟练使用 `help`、`doc`、`lookfor` 命令 |

---
