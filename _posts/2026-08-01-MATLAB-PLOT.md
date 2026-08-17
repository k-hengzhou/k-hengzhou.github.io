---
layout: post
title: "MATLAB 绘图基础"
categories: matlab
tags: [MATLAB, 绘图]
description: "面向 MATLAB 学习者与科研绘图用户的数据可视化教程：从 plot 基本绘图、样式定制与标注，到条形图、散点图、饼图、直方图、误差棒图、箱线图等常用数据图，再到 subplot/tiledlayout 子图布局与图形保存导出，助你系统掌握 MATLAB 绘图"
keywords: matlab, 绘图
mermaid: false
---

# 📈 MATLAB 绘图基础

> 绘图是 MATLAB 最强大的功能之一，掌握 `plot`、`bar`、`scatter` 等绘图命令，是 MATLAB 数据可视化与工程分析中不可或缺的一步。

---

## 🖌️ 二维曲线绘图

`plot` 命令是 MATLAB 最基础、最常用的二维绘图命令，本节介绍从绘制第一条曲线到多曲线叠加的完整过程。

### 📝 基本绘图

要绘制函数的图形，需要执行以下步骤：

1. 📝 通过指定变量 `x` 的值范围来定义 `x`
2. 🔧 定义函数 `y = f(x)`
3. 📈 调用 `plot(x, y)` 命令

```matlab
clear; clc;
x = 0:5:100;
y = x;
plot(x, y)
```

**运行结果**

<img src="/images/post/matlab_plot/plot1.png" width="100%" alt="matlab.png"   style="center" style="width: auto; height: auto;">

再看一个绘制抛物线（二次函数曲线）的例子：

```matlab
x = -100:1:100;
y = x.^2;
plot(x, y)
```

**运行结果**

<img src="/images/post/matlab_plot/plot2.png" width="100%" alt="matlab.png"   style="center" style="width: auto; height: auto;">

> **💡 提示**：当函数表达式中含有乘方、乘法、除法等运算时，必须使用点运算符（如 `x.^2`、`.*`、`./`）进行元素级运算，才能得到与向量 `x` 同维度的结果。

### 🏷️ 添加标题、标签、网格线和缩放

使用 `xlabel`、`ylabel`、`title` 可以为图形添加轴标签和标题；`grid on` 在图形上显示网格线；`grid minor` 显示更细的网格线；`axis equal` 生成正方形坐标轴（即横纵坐标的刻度间距相同）。

```matlab
x = 0:0.01:10;
y = sin(x);
plot(x, y), xlabel('x'), ylabel('Sin(x)'), title('Sin(x) Graph'),
grid on        % 允许您将网格线放在图形上
grid minor     % 显示更细的网格线
axis equal     % 命令生成一个正方形图
```

**运行结果**

<img src="/images/post/matlab_plot/plot3.png" width="100%" alt="matlab.png"   style="center" style="width: auto; height: auto;">

> **💡 提示**：`xlabel`、`ylabel`、`title` 等命令既可以使用逗号与 `plot` 写在同一行（如上例），也可以分行书写，二者效果完全相同。若不再需要网格，可使用 `grid off` 关闭。

### 📊 在同一图形上绘制多个函数

`plot` 命令支持一次绘制多条曲线，只需将多组 `(x, y)` 数据依次传入即可。使用 `legend` 命令为各条曲线添加图例。

```matlab
x = 0:0.01:10;
y = sin(x);
g = cos(x);
plot(x, y, x, g), legend('Sin(x)', 'Cos(x)')
```

**运行结果**

<img src="/images/post/matlab_plot/plot4.png" width="100%" alt="matlab.png"   style="center" style="width: auto; height: auto;">

### 🔀 hold on 与 hold off

`plot` 命令每次调用都会**清空**当前图形窗口并重新绘图。若想在同一个图形上**分步**叠加多条曲线，需要使用 `hold on` 保持当前图形，绘制完成后用 `hold off` 结束保持。

```matlab
x = 0:0.01:2*pi;
y1 = sin(x);
y2 = cos(x);
y3 = sin(x) + cos(x);

plot(x, y1)         % 绘制第一条曲线
hold on             % 保持当前图形，后续曲线叠加在同一图上
plot(x, y2)         % 叠加第二条曲线
plot(x, y3)         % 叠加第三条曲线
hold off            % 结束保持
legend('sin(x)', 'cos(x)', 'sin+cos')
```

**运行结果**

<img src="/images/post/matlab_plot/plot5.png" width="100%" alt="matlab.png"   style="center" style="width: auto; height: auto;">

> **💡 提示**：`hold on` 与一次传入多组数据（如 `plot(x, y1, x, y2)`）效果相同，但 `hold on` 更适合需要分步计算、动态添加曲线或叠加不同坐标系图形的场景。

### 🪟 figure 多窗口绘图

`figure` 命令用于创建新的图形窗口。当有多个数据需要对比时，可以分别在多个窗口中绘图；使用 `figure(n)` 可以在已编号的窗口间切换。

```matlab
x = 0:0.01:10;
y = sin(x);
figure                    % 创建图形窗口 1
plot(x, y), title('Sin(x)')

g = cos(x);
figure                    % 创建图形窗口 2
plot(x, g), title('Cos(x)')

figure(1)                 % 切换回窗口 1
```

**运行结果**

<img src="/images/post/matlab_plot/plot6.png" width="100%" alt="matlab.png"   style="center" style="width: auto; height: auto;">

> **💡 提示**：`close all` 可以一次性关闭所有图形窗口，`close(1)` 只关闭编号为 1 的窗口。

### 🪟 clf 与 close 图形窗口控制

`clf` 命令用于**清空**当前图形窗口中的所有内容（包括坐标轴、曲线、标注等），但窗口本身保持打开；`close` 命令则用于**关闭**图形窗口。两者常配合 `figure` 使用，用于管理多个图形窗口。

> **💡 提示**：三者的区别——`clf` **清空不关闭**窗口，`close` **关闭**当前窗口，`close all` **关闭所有**窗口。

### 📈 双 y 轴绘图

当两条曲线的**量纲差异较大**时（如一条取值范围在 0~1，另一条在 0~1000），如果画在同一个坐标轴上，较小量纲的曲线会被压扁。此时可以使用 **`yyaxis`** 命令在图形左右两侧分别显示两个 y 轴。

```matlab
x = 0:0.01:10;
y1 = sin(x);              % 第一条曲线，取值范围约 [-1, 1]
y2 = 100*exp(-x);         % 第二条曲线，取值范围约 [0, 100]

yyaxis left               % 激活左侧 y 轴
plot(x, y1), ylabel('sin(x)')

yyaxis right              % 激活右侧 y 轴
plot(x, y2), ylabel('100*exp(-x)')
```

**运行结果**

<img src="/images/post/matlab_plot/plot_yy.png" width="100%" alt="matlab.png"   style="center" style="width: auto; height: auto;">

> **💡 提示**：`yyaxis left` 与 `yyaxis right` 分别激活左右两个 y 轴；使用 `yyaxis left` 切换回左侧后，可以继续添加左侧曲线。双 y 轴非常适合温度与压力、销量与增长率等不同量纲数据的对比展示。

---

## 🎨 图形样式与标注

绘制完基本曲线后，可以通过颜色、线型、标记、字体等参数美化图形，并通过坐标轴控制和文字标注让图形信息更清晰。

### 🎨 设置颜色、线型与标记

MATLAB 提供了八种基本的颜色选项来绘制图形：

| 代码 |  颜色  |
| :--: | :----: |
|  w   |  白色  |
|  k   |  黑色  |
|  b   |  蓝色  |
|  r   |  红色  |
|  c   |  青色  |
|  g   |  绿色  |
|  m   | 洋红色 |
|  y   |  黄色  |

在 `plot` 命令中，可以在每组数据后添加颜色字符来指定该曲线的颜色。

```matlab
x = -10:0.01:10;
y = 3*x.^4 + 2*x.^3 + 7*x.^2 + 2*x + 9;
g = 5*x.^3 + 9*x + 2;
plot(x, y, 'r', x, g, 'g')
```

**运行结果**

<img src="/images/post/matlab_plot/plot7.png" width="100%" alt="matlab.png"   style="center" style="width: auto; height: auto;">

除了颜色，`plot` 还支持通过**线型（LineStyle）**和**标记（Marker）**来定制曲线样式：

| 线型 |     说明     | 标记 |    说明    |
| :--: | :----------: | :--: | :--------: |
| `-`  | 实线（默认） | `o`  |    圆圈    |
| `--` |     虚线     | `*`  |    星号    |
| `:`  |     点线     | `+`  |    加号    |
| `-.` |    点划线    | `s`  |    方形    |
|      |              | `d`  |    菱形    |
|      |              | `^`  | 上三角标记 |

```matlab
x = 0:0.1:2*pi;
y1 = sin(x);
y2 = cos(x);
plot(x, y1, 'r--o', x, y2, 'b:^')   % 红色虚线+圆圈，蓝色点线+上三角
```

**运行结果**

<img src="/images/post/matlab_plot/plot8.png" width="100%" alt="matlab.png"   style="center" style="width: auto; height: auto;">

> **💡 提示**：颜色、线型和标记可以任意组合成一行字符串，如 `'r--o'` 表示**红色虚线加圆形标记**；`'b:'` 表示**蓝色点线**。不指定颜色时，MATLAB 会自动为每条曲线分配不同颜色。

### 🎨 自定义颜色（RGB）

除了 8 种基本颜色字符，MATLAB 还支持使用 **RGB 三元组** `[r g b]` 自定义任意颜色，其中 `r`、`g`、`b` 分别代表红、绿、蓝三通道的强度，取值范围均为 `0 ~ 1`。

| 颜色 |  RGB 三元组   |
| :--: | :-----------: |
| 橙色 |  `[1 0.5 0]`  |
| 紫色 | `[0.5 0 0.5]` |
| 棕色 | `[0.4 0.2 0]` |
| 天蓝 |  `[0 0.6 1]`  |
| 粉色 | `[1 0.7 0.8]` |

```matlab
x = 0:0.01:2*pi;
y = sin(x);
plot(x, y, 'Color', [1 0.5 0], 'LineWidth', 2)   % 橙色曲线
```

**运行结果**

<img src="/images/post/matlab_plot/plot_color.png" width="100%" alt="matlab.png"   style="center" style="width: auto; height: auto;">

> **💡 提示**：RGB 三元组必须配合名称-值对 `'Color'` 使用（如 `'Color', [r g b]`），不能像颜色字符那样直接写在样式字符串中。常用颜色的 RGB 值可以通过 `colors` 命令查看。

### 📏 设置线宽、标记大小与字体

`plot` 命令还支持通过 **名称-值对（Name-Value Pair）** 参数对图形细节进行美化，例如线宽 `'LineWidth'`、标记大小 `'MarkerSize'`、标记样式 `'Marker'` 等；`xlabel`、`title` 等命令同样支持 `'FontSize'` 参数。

|      参数      |      说明      | 示例              |
| :------------: | :------------: | :---------------- |
| `'LineWidth'`  |   线宽（磅）   | `'LineWidth', 2`  |
| `'MarkerSize'` | 标记大小（磅） | `'MarkerSize', 8` |
|   `'Marker'`   |    标记样式    | `'Marker', 'o'`   |
|  `'FontSize'`  | 字体大小（磅） | `'FontSize', 14`  |

```matlab
x = 0:0.1:2*pi;
y = sin(x);
plot(x, y, 'LineWidth', 2, 'MarkerSize', 8, 'Marker', 'o')
xlabel('x', 'FontSize', 14)
title('正弦曲线', 'FontSize', 16)
```

**运行结果**

<img src="/images/post/matlab_plot/plot9.png" width="100%" alt="matlab.png"   style="center" style="width: auto; height: auto;">

> **💡 提示**：`'LineWidth'` 的默认值为 `0.5`，取值范围一般取 `0.5 ~ 3` 即可获得清晰美观的显示效果。

### 📐 设定轴比例

使用 `axis` 命令可以控制坐标轴的显示范围：

- `axis equal` —— 生成正方形坐标轴，使横纵刻度间距相同；
- `axis([xmin xmax ymin ymax])` —— 指定坐标轴的最小值与最大值。

```matlab
x = 0:0.01:10;
y = exp(-x).* sin(2*x + 3);
plot(x, y), axis([0 10 -1 1])
```

**运行结果**

<img src="/images/post/matlab_plot/plot10.png" width="100%" alt="matlab.png"   style="center" style="width: auto; height: auto;">

> **💡 提示**：除了 `axis equal` 和 `axis([...])`，还常用 `axis tight` 让坐标轴范围贴合数据范围、`axis on/off` 显示/隐藏坐标轴。

### 📐 坐标轴刻度自定义

从 MATLAB R2016b 开始，推荐使用 **`xticks`、`yticks`、`xticklabels`、`yticklabels`** 等命令来设置坐标轴刻度，比传统的 `set(gca, ...)` 写法更简洁直观。

|         命令         |        说明         | 示例                            |
| :------------------: | :-----------------: | :------------------------------ |
|   `xticks([...])`    |  设置 x 轴刻度位置  | `xticks(0:2:10)`                |
|   `yticks([...])`    |  设置 y 轴刻度位置  | `yticks(-1:0.5:1)`              |
| `xticklabels({...})` | 自定义 x 轴刻度标签 | `xticklabels({'a','b','c'})`    |
| `yticklabels({...})` | 自定义 y 轴刻度标签 | `yticklabels({'低','中','高'})` |

```matlab
x = 0:0.01:2*pi;
y = sin(x);
plot(x, y)

xticks(0:pi/2:2*pi)                             % 设置 x 轴刻度位置
xticklabels({'0', 'π/2', 'π', '3π/2', '2π'})   % 自定义 x 轴刻度标签
grid on
```

**运行结果**

<img src="/images/post/matlab_plot/plot13.png" width="100%" alt="matlab.png"   style="center" style="width: auto; height: auto;">

> **💡 提示**：`xticks` 与 `yticks` 设置刻度**位置**，`xticklabels` 与 `yticklabels` 设置刻度上的**文字标签**，两者通常配合使用。这也比 `set(gca, 'XTick', ...)` 的写法更加直观易读。

### 📝 text 文字标注

`text(x, y, '字符串')` 命令可以在图形指定坐标位置 `(x, y)` 处添加文字标注，常用于标记曲线的关键点（最大值、最小值、交点等）。

```matlab
x = 0:0.01:2*pi;
y = sin(x);
plot(x, y)
text(pi/2, 1, '最大值点 (π/2, 1)', 'FontSize', 12)   % 在最大值点处添加标注
```

**运行结果**

<img src="/images/post/matlab_plot/plot11.png" width="100%" alt="matlab.png"   style="center" style="width: auto; height: auto;">

> **💡 提示**：`annotation` 命令可以创建**相对于整个图形窗口**的箭头、文本框等注释对象，配合 `text` 使用可以制作出效果更好的标注。

### 🔑 legend 进阶用法

`legend` 命令除了基础用法，还可以通过名称-值对参数控制图例的**位置**与**样式**。

|     参数     |     说明     | 示例                      |
| :----------: | :----------: | :------------------------ |
| `'Location'` | 图例显示位置 | `'Location', 'northwest'` |
| `'FontSize'` |   字体大小   | `'FontSize', 12`          |
|   `'Box'`    | 是否显示边框 | `'Box', 'off'`            |

```matlab
x = 0:0.01:2*pi;
plot(x, sin(x), x, cos(x))
legend({'sin(x)', 'cos(x)'}, 'Location', 'northwest', 'FontSize', 12)
```

**运行结果**

<img src="/images/post/matlab_plot/plot12.png" width="100%" alt="matlab.png"   style="center" style="width: auto; height: auto;">

> **💡 提示**：`'Location'` 常用取值还有 `'north'`（顶部居中）、`'southeast'`（右下角）、`'best'`（自动选择最佳位置）等。

---

## 📊 常用数据图

除了 `plot` 曲线图，MATLAB 还提供了条形图、散点图、茎叶图、饼图等多种常用图形，适用于不同类型的数据展示。

### 📊 绘制条形图

`bar` 命令用于绘制条形图（柱状图），常用于展示离散数据的对比。

```matlab
clear; clc; close all;
x = 1:10;
y = [75, 58, 90, 87, 50, 85, 92, 75, 60, 95];
bar(x, y), xlabel('Student'), ylabel('Score'), title('First Sem:')
```

**运行结果**

<img src="/images/post/matlab_plot/bar1.png" width="100%" alt="matlab.png"   style="center" style="width: auto; height: auto;">

> **💡 提示**：`close all` 用于关闭所有已打开的图形窗口，避免多个图窗口叠加影响观察。`barh` 可以绘制**水平条形图**。

### 🔵 scatter 散点图

`scatter` 命令用于绘制散点图，适用于展示大量数据点的分布规律，是数据统计分析中的常用图形。

```matlab
x = randn(1, 100);          % 生成 100 个标准正态分布随机数
y = randn(1, 100);
scatter(x, y, 'filled')
```

**运行结果**

<img src="/images/post/matlab_plot/scatter1.png" width="100%" alt="matlab.png"   style="center" style="width: auto; height: auto;">

> **💡 提示**：`scatter(x, y, sz, c)` 可以通过 `sz` 控制点的大小、`c` 控制点的颜色，从而在散点图中编码第三维信息。

### 🌱 stem 茎叶图

`stem` 命令绘制茎叶图，以垂直短线连接基线与数据点，非常适合展示**离散信号**或**采样序列**。

```matlab
n = 0:10;
y = exp(-0.2*n) .* sin(2*n);
stem(n, y), xlabel('n'), ylabel('y'), title('Stem Plot')
```

**运行结果**

<img src="/images/post/matlab_plot/stem1.png" width="100%" alt="matlab.png"   style="center" style="width: auto; height: auto;">

> **💡 提示**：`stem` 与 `plot` 的用法类似，也支持颜色、线型、标记等样式设置。

### 🍕 饼图

`pie` 命令用于绘制饼图，适合展示各部分占总体的比例。

```matlab
pie([30, 40, 20, 10])       % 饼图（按占比绘图）
```

**运行结果**

<img src="/images/post/matlab_plot/pie1.png" width="100%" alt="matlab.png"   style="center" style="width: auto; height: auto;">

> **💡 提示**：`pie([30, 40, 20, 10])` 的输入无需归一化，MATLAB 会自动按总和计算各扇区占比。

### 📊 直方图

`histogram` 命令用于绘制直方图，将数据的取值范围划分为若干区间，统计每个区间内的数据个数，是最常用的**数据分布分析**工具。

```matlab
data = randn(1, 1000);          % 生成 1000 个标准正态分布随机数
histogram(data, 30)             % 将数据分成 30 个区间
xlabel('数值'), ylabel('频数'), title('正态分布直方图')
```

**运行结果**

<img src="/images/post/matlab_plot/histogram.png" width="100%" alt="matlab.png"   style="center" style="width: auto; height: auto;">

> **💡 提示**：`histogram(data, 30)` 的第二个参数指定**区间个数**；也可以传入向量指定区间边界，如 `histogram(data, -4:0.5:4)`。默认情况下直方图显示的是**频数**，添加 `'Normalization', 'probability'` 可以改为显示概率。

### 📏 误差棒图

`errorbar` 命令在数据点上绘制**误差棒**（Error Bar），用来展示数据的均值与误差范围，是科研论文中非常常见的图形。

```matlab
x = 1:5;
y = [2.1, 3.4, 4.6, 5.2, 6.8];      % 数据的均值
e = [0.3, 0.5, 0.4, 0.6, 0.5];      % 误差范围
errorbar(x, y, e), xlabel('x'), ylabel('y'), title('Error Bar Plot')
```

**运行结果**

<img src="/images/post/matlab_plot/errorbar.png" width="100%" alt="matlab.png"   style="center" style="width: auto; height: auto;">

> **💡 提示**：`errorbar(x, y, e)` 中 `e` 表示对称误差；`errorbar(x, y, neg, pos)` 可以指定**不对称误差**（下方与上方分别不同）。误差棒图常用于展示多次实验的均值±标准差。

### 📦 箱线图

`boxplot` 命令绘制**箱线图（盒须图）**，用最小值、下四分位数、中位数、上四分位数、最大值五个统计量概括一组数据的分布，同时可以直观地发现**离群点**。

```matlab
data = randn(100, 3);               % 生成 3 组各 100 个正态分布随机数
boxplot(data), xlabel('组别'), ylabel('数值'), title('Box Plot')
```

**运行结果**

<img src="/images/post/matlab_plot/boxplot.png" width="100%" alt="matlab.png"   style="center" style="width: auto; height: auto;">

> **💡 提示**：箱线图中，箱体的上边界是上四分位数（75%）、下边界是下四分位数（25%）、中间红线是中位数，须的长度通常为四分位距的 1.5 倍，超出须的孤立点即为**离群点**。

---

## 🧩 子图与布局

当需要在一张图中对比多个子图时，可以使用 `subplot` 或 `tiledlayout` 对图形窗口进行分割布局。

### 🧩 生成子图（subplot）

`subplot(m, n, p)` 命令将图形窗口划分为 `m×n` 个子图区域，并激活第 `p` 个区域作为当前绘图区域。

```matlab
x = 0:0.01:5;
y = exp(-1.5*x).*sin(10*x);
subplot(1, 2, 1)
plot(x, y), xlabel('x'), ylabel('exp(–1.5x)*sin(10x)'), axis([0 5 -1 1])

y = exp(-2*x).*sin(10*x);
subplot(1, 2, 2)
plot(x, y), xlabel('x'), ylabel('exp(–2x)*sin(10x)'), axis([0 5 -1 1])
```

**运行结果**  
 <img src="/images/post/matlab_plot/subplot1.png" width="100%" alt="matlab.png"   style="center" style="width: auto; height: auto;">

> **💡 提示**：`subplot(1, 2, 1)` 表示创建 1 行 2 列的子图布局，并激活第 1 个子图；`subplot(1, 2, 2)` 则激活第 2 个子图。

### 🧱 tiledlayout 布局子图

从 MATLAB R2019b 开始，推荐使用 **`tiledlayout`** 进行子图布局。它比 `subplot` 更灵活：子图间距自动对齐、可以共享坐标轴、支持跨行跨列的子图。

```matlab
x = 0:0.01:5;
tiledlayout(1, 2)          % 创建 1 行 2 列的子图布局

nexttile                   % 激活第 1 个子图
plot(x, sin(x)), title('sin(x)')

nexttile                   % 激活第 2 个子图
plot(x, cos(x)), title('cos(x)')
```

**运行结果**

<img src="/images/post/matlab_plot/tilelayout1.png" width="100%" alt="matlab.png"   style="center" style="width: auto; height: auto;">

> **💡 提示**：`tiledlayout` 配合 `nexttile` 比 `subplot` 更适合需要**共享轴标签**或**统一坐标范围**的场合。

---

## 💾 保存与进阶技巧

绘图完成后，可以将图形导出为图片文件用于论文与报告，也可以通过 `set(gca)` 精细控制坐标轴的显示效果。

### 💾 图形保存与导出

绘图完成后，可以将图形保存为图片文件，用于论文、报告或演示。MATLAB 提供了 `saveas`、`print` 和 `exportgraphics` 三种常用方式。

|       命令       |            说明             | 示例                                |
| :--------------: | :-------------------------: | :---------------------------------- |
|     `saveas`     |     保存图形为多种格式      | `saveas(gcf, 'myplot.png')`         |
|     `print`      |    灵活控制分辨率与格式     | `print('myplot', '-dpng', '-r300')` |
| `exportgraphics` | 导出高质量矢量图（R2020a+） | `exportgraphics(gcf, 'myplot.pdf')` |

```matlab
x = 0:0.01:2*pi;
plot(x, sin(x))

saveas(gcf, 'myplot.png')          % 保存为 PNG 图片
saveas(gcf, 'myplot.fig')          % 保存为 .fig 源文件（可再次编辑）
print('myplot', '-dpng', '-r300')  % 以 300 dpi 分辨率保存 PNG
exportgraphics(gcf, 'myplot.pdf')  % 导出为 PDF 矢量图
```

> **💻 运行结果**
>
> 在当前目录生成 `myplot.png`、`myplot.fig` 与 `myplot.pdf` 等图形文件。

> **💡 提示**：`gcf` 表示**当前图形窗口**（Get Current Figure）。`.fig` 是 MATLAB 专属源文件格式，双击可以重新打开继续编辑。

### ⚙️ set(gca) 坐标轴属性设置

`gca` 表示**当前坐标轴**（Get Current Axes），`set(gca, ...)` 可以通过名称-值对精细控制坐标轴的字体、刻度、边框等属性。

```matlab
x = 0:0.01:10;
y = exp(-x) .* sin(10*x);
plot(x, y)

set(gca, 'FontSize', 12)               % 设置坐标轴字体大小
set(gca, 'XTick', 0:2:10)              % 设置 x 轴刻度为 0,2,4,...,10
set(gca, 'XGrid', 'on', 'YGrid', 'on') % 分别打开 x、y 方向网格线
```

**运行结果**

<img src="/images/post/matlab_plot/set.png" width="100%" alt="matlab.png"   style="center" style="width: auto; height: auto;">

> **💡 提示**：`set(gca, 'XTick', ...)` 设置刻度位置，`set(gca, 'XTickLabel', ...)` 可以自定义刻度上的文字标签。

---
