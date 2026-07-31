---
layout: post
title: "MATLAB M 文件与函数"
categories: matlab 编程 基础语法
description: "本文将系统介绍 MATLAB 的基本语法，包括环境操作、变量与命令、运算符、输入输出、控制结构，帮助你快速入门 MATLAB 编程基础"
keywords: matlab, 基本语法, 变量, 命令, 运算符, 控制结构, 函数
mermaid: false
sequence: false
flow: false
mathjax: true
mindmap: false
mindmap2: false
---

## 📁 MATLAB M文件

到目前为止，我们已经使用MATLAB环境作为计算器。但是，MATLAB还是一种强大的编程语言，也是一种交互式计算环境。在前面的章节中，您学习了如何从MATLAB命令提示符下输入命令。MATLAB还允许您将一系列命令写入文件并以完整的单元形式执行文件，例如编写函数和调用它。

### 使用edit命令编辑m文件

编辑m文件 `forexp.m`：

```matlab
edit forexp.m
```

如果m文件不存在，matlab会提示用户是否要创建一个新文件。如果用户选择创建，matlab会自动创建一个新文件。如果m文件存在，会打开该文件。
<img src="/images/post/matlab_m.png" width="100%" alt="matlab.png"  style="center"/>  
将下列代码复制到matlab打开的m文件编译窗口中，并保存文件。

```matlab
for i= 1:1:10
    if i == 5
        continue
    end
    disp("i = " + num2str(i))
end
```

回到MATLAB命令提示符下。输入 `forexp` 来调用

```matlab
>> forexp
```

> **运行结果**
>
> i = 2
> i = 3
> i = 4
> i = 6
> i = 7
> i = 8
> i = 9
> i = 10

---

### 函数

#### 函数定义

函数是一起执行任务的一组语句。在MATLAB中，函数是在单独的文件中定义的。文件名和函数名应该相同。

函数语句的语法是：

```matlab
function [out1, out2, ..., outN] = myfun(in1, in2, in3, ..., inN)
```

#### 示例函数

编辑m文件 `a2b3.m`：

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

回到MATLAB命令提示符下。输入 `a2b3` 来调用

```matlab
>> [c, d] = a2b3(2, 3)
```

> **运行结果**
>
> c = 4
> d = 9

#### 函数的参数与返回值

- 函数的参数：函数调用时传递给函数的值。参数可以是标量、向量、矩阵等。

- 函数的返回值：函数执行完毕时返回的值。返回值可以是标量、向量、矩阵。当函数返回多个值时，这些值会被赋值给多个变量。

```matlab
%获取所有的函数返回值：
>> [c, d] = a2b3(2, 3)
```

> **运行结果**
>
> c = 4
> d = 9

```matlab
%只获取第一个返回值，其他返回值会被忽略：
>> c = a2b3(2, 3)
```

> **运行结果**
>
> c = 4

```matlab
%只获取第二个返回值，其他返回值会被忽略：
>> [~, d] = a2b3(2, 3)
```

> **运行结果**
>
> d = 9

#### 匿名函数

匿名函数就像传统编程语言中的内联函数一样，是在单个MATLAB语句中定义的。

```matlab
>> power = @(x, n) x.^n;
>> result1 = power(7, 3)
>> result2 = power(49, 0.5)
>> result3 = power(10, -10)
>> result4 = power(4.5, 1.5)
```

> **运行结果**
>
> result1 = 343
> result2 = 7
> result3 = 1.0000e-10
> result4 = 9.5459

#### 主和子函数

除匿名函数外，所有函数都必须在文件中定义。每个函数文件包含一个必需的主函数（必须首先出现），以及任意数量的可选子函数（位于主函数之后，供主函数调用）。

文件 `a4b5.m`的函数定义如下：

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

> **运行结果**
>
> c = 8
> d = 15

<span style="color: #e74c3c; font-weight: bold;">⚠ 在一个文件中定义多个函数，一定要注意只有主函数（与m文件同名的函数）可以在外部直接调用，其他子函数只能在主函数中调用。</span>
