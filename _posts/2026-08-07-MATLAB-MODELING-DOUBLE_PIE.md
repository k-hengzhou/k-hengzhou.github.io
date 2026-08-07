---
layout: post
title: MATLAB 数学建模：2024高校社杯C题展示论文双重饼图复现
categories: 数学建模
tags: [MATLAB, 数学建模, 绘图, 饼图]
description: "本文以 2024 高教社杯 C 题为例，讲解如何用 MATLAB 复现论文中的双重饼图：读取含中文列名的 Excel 数据、按地块类型分组统计面积，并通过嵌套坐标轴绘制内外圈饼图、放置百分比标签，助你掌握双重饼图的完整绘制流程。"
keywords: matlab, 数学建模, 双重饼图, 双饼图, pie, readtable, 数据可视化, 绘图, 2024高教社杯
mermaid: false
sequence: false
flow: false
mathjax: true
mindmap: false
mindmap2: false
---

## 引言

这篇文章我们将使用 MATLAB 复现在 [2024高教社杯全国大学生数学建模竞赛C题论文展示](https://dxs.moe.gov.cn/zx/a/hd_sxjm_sxjmlw_2024qgdxssxjmjslwzs_2024ctlw/241104/1977952.shtml) 中绘制的双重饼图。具体来说：我们将一步一步讲解如何读取 2024 高教社杯全国大学生数学建模竞赛 C 题附件 1.xlsx，并根据附件 1.xlsx 中提供的数据绘制如下的双重饼图：

<img src="/images/post/double_pie.jpg" width="100%" alt="double_pie">

绘制的思路如下：创建两个不同大小的坐标轴，分别绘制外圈和内圈饼图，然后通过控制坐标轴的 `Position` 实现大小嵌套。

---

## 基本数据处理

### 📂 Excel 表格的读取

MATLAB 中提供多种方法来读取 Excel 表格，包括 `readtable`、`xlsread`、`xlsreadtable` 等。其中 `readtable` 是 MATLAB R2013b 引入的现代函数，返回表格数据类型。

```matlab
T = readtable(filename, 'Sheet', sheet, 'Range', range)
```

**优势：**

1. 自动识别列名
2. 支持混合数据类型
3. 更好的数据组织
4. 支持更多选项
5. 支持中文列名

所以这里我们选用 `readtable` 函数来读取 Excel 表格。因为在附件 1.xlsx 中的列名存在中文，所以在读取附件 1.xlsx 时，我们需要指定 `'VariableNamingRule'` 属性为 `'preserve'`。

```matlab
data = readtable('附件1.xlsx', 'VariableNamingRule', 'preserve');
head(data(:, 1:3), 5) % 查看前3列前5行数据
```

> **💻 运行结果**
>
> ```
> >>head(data(:, 1:3), 5)
>    地块名称     地块类型     地块面积/亩
>    _______    _________    __________
>
>    {'A1'}     {'平旱地'}        80
>    {'A2'}     {'平旱地'}        55
>    {'A3'}     {'平旱地'}        35
>    {'A4'}     {'平旱地'}        72
>    {'A5'}     {'平旱地'}        68
> ```

> [!WARNING]
> **⚠️ 注意**
> 在读取附件 1.xlsx 时，一定要记得先把附件 1.xlsx 复制到 MATLAB 工作目录下。
> [2024高教社杯全国大学生数学建模竞赛真题下载链接](https://www.mcm.edu.cn/html_cn/node/03c91a444e62eee81a3740fa97a461a6.html)

### 📊 数据处理

我们需要计算每种类型地的总面积，同时需要把相同类型的地块分组保存起来，方便后续的绘制双重饼图。

**第一步：确定要提取的地块类型和绘制顺序**

```matlab
target_names = {'水浇地','山坡地', '梯田', '平旱地'};
```

**第二步：分组保存地块类型并计算总面积**

接下来我们使用 `strcmp` 函数来判断每个地块的类型，然后根据类型将地块分组保存起来，并使用 `sum` 函数来计算每个类型的总面积。

```matlab
inner_vals = zeros(1, length(target_names));
outer_vals_cell = cell(length(target_names), 1);
% 4. 提取对应面积
for i = 1:length(target_names)
     idx = strcmp(data.("地块类型"), target_names{i});
     outer_vals_cell{i} = data.("地块面积/亩")(idx);     % 仅存入该类型的面积数值数组
     inner_vals(i) = sum(outer_vals_cell{i});
end

outer_vals = vertcat(outer_vals_cell{:});

```

> [!IMPORTANT]
> **注意点**
>
> 1. **预先分配内存**：预先分配内存，避免在循环中动态分配内存，提高效率。
> 2. **中文列名的访问**：因为列名是中文，所以在使用 `strcmp` 函数时，需要使用双引号来包裹列名（`data.("地块类型")`），不能直接使用点号来访问列名。
> 3. **垂直拼接**：使用 `vertcat` 函数将所有类型的面积数值数组垂直拼接起来，方便后续的绘制。

这样我们就得到了需要的数据，可以开始绘制双重饼图了。

---

## 绘制双重饼图

### 🎨 定义颜色

对于内外圈饼图，我们需要采用不同方式来定义颜色

#### 内圈饼图颜色

对于内圈饼图，我们直接使用矩阵定义不同的颜色来表示不同的地块类型。

```matlab
inner_colors = [
    0.88, 0.48, 0.44;   % 红色/粉色
    0.58, 0.48, 0.72;  %  紫色
    0.20, 0.65, 0.38;  % 绿色
    0.96, 0.80, 0.20;  %  黄色
];
```

如果你有其他颜色方案，也可以根据需要修改 `inner_colors` 矩阵。或者你想知道更多科研绘图的颜色方案，可以参考 [科研色彩探索平台](https://color.amfe.space/),里面有非常多的顶级期刊的配色方案。

#### 外圈饼图颜色

对于外圈饼图，我们采用渐变色来定义，渐变的公式如下：

$$\text{Color} = \text{blend_factor} \times \text{base_col} + (1 - \text{blend_factor}) \times [1, 1, 1]$$

其中 $\text{base_col}$ 为对应的内圈饼图的颜色，$\text{blend_factor}$ 为渐变因子，取值范围为 $0.9$ 到 $0.4$，按相同类型地块的数量进行线性采样。最后我们将所有类型的渐变色垂直拼接起来，方便后续的绘制。

```matlab
outer_colors = cell(1, length(inval));
for i = 1:length(inval)
    n_sub = length(outer_vals{i});
    base_col = inner_colors(i, :);
    blend_factor = linspace(0.9, 0.4, n_sub)';
    outer_colors{i} = blend_factor * base_col + (1 - blend_factor) * [1 1 1];
end
outer_colors = vertcat(outer_colors{:});
```

### ⭕ 绘制外圈饼图

绘制前，我们需要先创建一个 `figure` 对象，设置其颜色为白色，位置为 `[100, 100, 600, 600]`，并创建一个坐标轴 `ax_outer`，设置其位置为 `[0.1, 0.1, 0.8, 0.8]`，作为外圈饼图的坐标轴。并设置 `'DataAspectRatio'` 属性为 `[1 1 1]`，确保饼图的大小是等比例的。

```matlab
figure('Color', 'w', 'Position', [100, 100, 600, 600]);
ax_outer = axes('Position', [0.1 0.1 0.8 0.8], 'DataAspectRatio', [1 1 1]);
```

> [!TIP]
> **`Position` 属性详解**
>
> `'Position', [100, 100, 600, 600]` 表示 `figure` 对象：
>
> - 左边缘距离电脑屏幕最左侧的距离为 100 像素；
> - 图形窗口的底边缘距离电脑屏幕最底部的距离为 100 像素；
> - 宽度为 600，高度为 600。
>
> `'Position', [0.1, 0.1, 0.8, 0.8]` 表示 `ax_outer` 坐标轴：
>
> - 左边缘距离图形窗口左侧边缘的距离，占整个窗口宽度的 10%；
> - 坐标轴的底边缘距离图形窗口底部边缘的距离，占整个窗口高度的 10%；
> - 坐标轴本身的总宽度占整个窗口宽度的 80%；
> - 总高度占整个窗口高度的 80%。

然后我们在坐标轴 `ax_outer` 上使用 `pie` 函数来绘制外圈饼图。使用 `repmat` 来使每个饼图的标签为空字符串，从而隐藏标签。

```matlab
pie(ax_outer,outer_vals, repmat({''}, size(outer_vals)))
```

#### 设置外圈饼图颜色和边框

接下来我们来设置外圈饼图的颜色和边框。使用 `findobj` 函数来找到 `ax_outer` 坐标轴上的所有类型的 `patch` 对象（即多边形对象），在这里就是我们刚刚绘制的饼图，然后使用 `set` 函数来设置颜色和边框颜色。

- **`FaceColor`**：设置多边形的填充颜色。
- **`EdgeColor`**：设置多边形的边框颜色。
- **`LineWidth`**：设置多边形的边框宽度。

```matlab
h_outer = findobj(ax_outer, 'Type', 'patch');
set(h_outer, {'FaceColor'}, num2cell(flipud(outer_colors), 2));
set(h_outer, 'EdgeColor', 'white', 'LineWidth', 0.6);
```

> [!WARNING]
> **⚠️ 注意**
>
> 1. MATLAB 的 `pie` 函数返回的图形对象（patch）顺序是倒序的（第一个对象对应最后一个数据），因此设置颜色时必须用 `flipud()` 翻转颜色矩阵，否则颜色分组会错位。
> 2. 我们使用 `num2cell()` 将颜色矩阵转换为元胞数组，把颜色矩阵按行（维度 2）进行切分，把每一行（即每一个 RGB 颜色）单独打包进一个 cell 单元里，最终变成一个由多个 RGB 数组组成的元胞数组。

我们可以先查看目前的效果，如下所示：

<img src="/images/post/double_pie_out.jpg" width="100%" alt="double_pie_out">

接下来我们要在另一个坐标轴 `ax_inner` 上绘制内圈饼图，直接覆盖外圈饼图，形成我们想要的双重饼图的效果。

### ⭕ 绘制内圈饼图

我们定义内圈饼图的坐标轴 `ax_inner`，通过 `inner_size` 定义内圈饼图的大小，并根据大小设置偏移量 `offset`，来确保内圈饼图的中心与外圈饼图的中心重合。计算的示意图如下：

<img src="/images/post/double_pie_offset.jpg" width="100%" alt="double_pie_offset">

```matlab
inner_size = 0.56;  % 内圈相对大小，调小可让外圈更宽
offset = (1 - inner_size) / 2;
ax_inner = axes('Position', [offset offset inner_size inner_size],'DataAspectRatio', [1 1 1]);
```

现在我们在坐标轴 `ax_inner` 上使用 `pie` 函数来绘制内圈饼图。使用 `repmat` 来使每个饼图的标签为空字符串，从而隐藏标签。并设置颜色为定义的内圈饼图的颜色，边框颜色为白色，边框宽度为 1.2。

```matlab
h = pie(ax_inner,inner_vals,repmat({''}, size(inner_vals)));
% 设置外圈颜色（注意：pie返回的patch顺序是倒序，必须翻转）;
h_inner = findobj(ax_inner, 'Type', 'patch');
set(h_inner, {'FaceColor'}, num2cell(flipud(inner_colors), 2));
set(h_inner, 'EdgeColor', 'white', 'LineWidth', 1.2);
```

> [!IMPORTANT]
>
> `pie` 的函数句柄 `h` 的奇数项是多边形对象，偶数项是标签对象。我们这里将内圈饼图的函数句柄赋值保存下来，方便添加标签。

现在我们来查看一下效果：

<img src="/images/post/double_pie_inter.jpg" width="100%" alt="double_pie_inter">

---

## 添加标签

现在离我们想要的效果已经很近了，我们只需要添加标签即可。但是 MATLAB 中的 `pie` 的标签的位置是自动的，我们需要手动调整标签的位置，才能使标签位于扇形内。下面我们对于每一个扇形进行处理。

### 📍 标签的位置

我们先使用 `pie` 的函数句柄 `h` 获取第 `i` 个扇形的多边形对象的 x 坐标和 y 坐标。

```matlab
patch_obj = h(2*i - 1);
x = patch_obj.XData;
y = patch_obj.YData;
```

我们可以画出这个多边形来查看效果：

```matlab
plot(x,y,'r--o')
```

结果如下：

<img src="/images/post/double_pie_scater.jpg" width="100%" alt="double_pie_scater">

可以看见，MATLAB 就是通过绘制这些散点围成的多边形来实现绘制扇形的。

接下来我们计算扇形的中心位置。首先我们计算扇形的中心角度，计算方法如下：

1. 我们先去掉 x 坐标和 y 坐标都为 0 的点，因为这些点在圆心，我们不需要计算。
2. 我们计算剩余点的平均点的角度，即扇形的中心角度。

代码如下：

```matlab
mask = ~(x == 0 & y == 0);
x_arc = x(mask);
y_arc = y(mask);
mid_angle = atan2(mean(y_arc), mean(x_arc));
```

接下来因为 `pie` 在坐标系中默认半径为 1，所以我们令标签所在的位置的半径为 `r_internal = 0.55`，来保证标签位于扇形内。最后使用极坐标来计算标签的位置。

```matlab
r_internal = 0.55;
text_x = r_internal * cos(mid_angle);
text_y = r_internal * sin(mid_angle);
```

### ✍️ 写标签

标签属性位于 `pie` 函数句柄 `h` 的偶数项，所以我们需要使用 `h(2*i)` 来获取标签对象。使用 `sprintf` 来格式化标签字符串，包括标签的名称和百分比（对于 `sprintf` 的用法可以查看文章 [MATLAB 基本语法指南](https://k-hengzhou.github.io/posts/MATLAB-Basic-Syntax/#fprintf-%E5%87%BD%E6%95%B0)）。最后使用 `set` 设置标签属性：

1. **String**：标签字符串
2. **Position**：标签的位置
3. **HorizontalAlignment**：标签的水平对齐方式
4. **VerticalAlignment**：标签的垂直对齐方式
5. **Color**：标签的颜色
6. **FontSize**：标签的字体大小

```matlab
text_obj = h(2*i);
    str_label = sprintf('%s\n%.1f%%', target_names{i}, ...
        inner_vals(i)/total_val*100);% total_val 总面积
set(text_obj, ...
    'String', str_label, ...
    'Position', [text_x, text_y, 0], ...
    'HorizontalAlignment', 'center', ...
    'VerticalAlignment', 'middle', ...
    'Color', 'black', ...
    'FontSize', 8);
```

### 📜 完整的循环过程

```matlab
r_internal = 0.55;
total_val = sum(inner_vals);
for i = 1:length(inner_vals)
    patch_obj = h(2*i - 1);
    x = patch_obj.XData;
    y = patch_obj.YData;
    mask = ~(x == 0 & y == 0);
    x_arc = x(mask);
    y_arc = y(mask);
    mid_angle = atan2(mean(y_arc), mean(x_arc));
    text_x = r_internal * cos(mid_angle);
    text_y = r_internal * sin(mid_angle);
    text_obj = h(2*i);
    str_label = sprintf('%s\n%.1f%%', target_names{i}, ...
        inner_vals(i)/total_val*100);
    set(text_obj, ...
        'String', str_label, ...
        'Position', [text_x, text_y, 0], ...
        'HorizontalAlignment', 'center', ...
        'VerticalAlignment', 'middle', ...
        'Color', 'black', ...
        'FontSize', 8);
end
```

现在我们来看看效果：

<img src="/images/post/double_pie.jpg" width="100%" alt="double_pie">

这样就已经实现了我们想要的效果。

---

## 不足

2024高教社杯全国大学生数学建模竞赛C题论文展示中的双重饼图：

<img src="/images/post/image_722373.jpg" width="100%" alt="image_722373">

我们在外围饼图颜色的变化没有完美复现出来。现在我还无法知道如何使用 MATLAB 实现完全一样的外围颜色效果。如果有深入研究的大佬，欢迎指导。
