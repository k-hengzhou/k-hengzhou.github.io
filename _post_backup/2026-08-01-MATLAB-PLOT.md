---
layout: post
title: "MATLAB 向量和矩阵一：向量"
categories: matlab 编程 基础语法
description: "本文将详细介绍 MATLAB 中向量的创建、引用与运算，包括行向量与列向量、向量生成方式、向量运算、常用函数、逻辑运算、向量化编程与内存性能优化，帮助你快速掌握 MATLAB 向量编程基础"
keywords: matlab, 向量, 行向量, 列向量, 向量运算, 向量化编程, 逻辑运算, 内存性能
mermaid: false
sequence: false
flow: false
mathjax: true
mindmap: false
mindmap2: false
---

---

## 绘图功能

### 基本绘图

要绘制函数的图形，需要执行以下步骤：

1. 通过指定变量x的值范围来定义x
2. 定义函数 y = f(x)
3. 调用 plot(x, y) 命令

```matlab
clear; clc;
x = 0:5:100;
y = x;
plot(x, y)
```

> **运行结果**
>
> \>> clear; clc;
> \>> x = 3;
> \>> if x == 3
> disp("x is 3")
> end
> x is 3

```matlab
x = -100:1:100;
y = x.^2;
plot(x, y)
```

> **运行结果**
>
> \>> x = -100:1:100;
> \>> y = x.^2;
> \>> plot(x, y)
> % 显示一条抛物线

### 添加标题、标签、网格线和缩放

```matlab
x = 0:0.01:10;
y = sin(x);
plot(x, y), xlabel('x'), ylabel('Sin(x)'), title('Sin(x) Graph'),
grid on        % 允许您将网格线放在图形上
axis equal     % 命令生成一个正方形图
```

> **运行结果**
>
> \>> x = 0:0.01:10;
> \>> y = sin(x);
> \>> plot(x, y), xlabel('x'), ylabel('Sin(x)'), title('Sin(x) Graph'),
> \>> grid on
> \>> axis equal
> % 显示带网格的正弦曲线图

### 在同一图形上绘制多个函数

```matlab
x = 0:0.01:10;
y = sin(x);
g = cos(x);
plot(x, y, x, g), legend('Sin(x)', 'Cos(x)')
```

> **运行结果**
>
> \>> x = 0:0.01:10;
> \>> y = sin(x);
> \>> plot(x, y), xlabel('x'), ylabel('Sin(x)'), title('Sin(x) Graph'),
> \>> grid on
> \>> axis equal
> % 显示带网格的正弦曲线图

### 设置颜色

MATLAB提供了八种基本的颜色选项来绘制图形：

| 代码 | 颜色   |
| ---- | ------ |
| w    | 白色   |
| k    | 黑色   |
| b    | 蓝色   |
| r    | 红色   |
| c    | 青色   |
| g    | 绿色   |
| m    | 洋红色 |
| y    | 黄色   |

```matlab
x = -10:0.01:10;
y = 3*x.^4 + 2*x.^3 + 7*x.^2 + 2*x + 9;
g = 5*x.^3 + 9*x + 2;
plot(x, y, 'r', x, g, 'g')
```

> **运行结果**
>
> \>> x = -10:0.01:10;
> \>> y = 3*x.^4 + 2*x.^3 + 7*x.^2 + 2*x + 9;
> \>> g = 5*x.^3 + 9*x + 2;
> \>> plot(x, y, 'r', x, g, 'g')
> % 显示红色和绿色两条曲线

### 设定轴比例

```matlab
x = 0:0.01:10;
y = exp(-x).* sin(2*x + 3);
plot(x, y), axis([0 10 -1 1])
```

> **运行结果**
>
> \>> x = 0:0.01:10;
> \>> y = sin(x);
> \>> plot(x, y), xlabel('x'), ylabel('Sin(x)'), title('Sin(x) Graph'),
> \>> grid on
> \>> axis equal
> % 显示带网格的正弦曲线图

### 生成子图

```matlab
x = 0:0.01:5;
y = exp(-1.5*x).*sin(10*x);
subplot(1, 2, 1)
plot(x, y), xlabel('x'), ylabel('exp(–1.5x)*sin(10x)'), axis([0 5 -1 1])

y = exp(-2*x).*sin(10*x);
subplot(1, 2, 2)
plot(x, y), xlabel('x'), ylabel('exp(–2x)*sin(10x)'), axis([0 5 -1 1])
```

> **运行结果**
>
> \>> x = 0:0.01:5;
> \>> y = exp(-1.5*x).*sin(10*x);
> \>> subplot(1, 2, 1)
> \>> plot(x, y), xlabel('x'), ylabel('exp(–1.5x)*sin(10x)'), axis([0 5 -1 1])
>
> \>> y = exp(-2*x).*sin(10*x);
> \>> subplot(1, 2, 2)
> \>> plot(x, y), xlabel('x'), ylabel('exp(–2x)*sin(10x)'), axis([0 5 -1 1])
> % 显示两个子图

### 绘制条形图

```matlab
clear; clc; close all;
x = 1:10;
y = [75, 58, 90, 87, 50, 85, 92, 75, 60, 95];
bar(x, y), xlabel('Student'), ylabel('Score'), title('First Sem:')
```

> **运行结果**
>
> \>> clear; clc; close all;
> \>> x = 1:10;
> \>> y = [75, 58, 90, 87, 50, 85, 92, 75, 60, 95];
> \>> bar(x, y), xlabel('Student'), ylabel('Score'), title('First Sem:')
> % 显示条形图

### 三维图

三维图显示了由函数定义的两个变量 g = f(x, y) 的曲面。

```matlab
[x, y] = meshgrid(-2:.2:2);
z = x .* exp(-x.^2 - y.^2);
surf(x, y, z)
```

> **运行结果**
>
> \>> [x, y] = meshgrid(-2:.2:2);
> \>> z = x .\* exp(-x.^2 - y.^2);
> \>> surf(x, y, z)
> % 显示三维曲面图

---
