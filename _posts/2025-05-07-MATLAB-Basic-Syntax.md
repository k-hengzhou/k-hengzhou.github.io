---
layout: post
title: "MATLAB 基本语法完全指南"
categories: matlab 编程 基础语法
description: "本文将详细介绍 MATLAB 的基本语法，包括变量、矩阵、运算符、控制结构、函数、输入输出和绘图功能，帮助你快速掌握 MATLAB 编程基础"
keywords: matlab, 基本语法, 变量, 矩阵, 运算符, 控制结构, 函数, 绘图
mermaid: false
sequence: false
flow: false
mathjax: true
mindmap: false
mindmap2: false
---

# 🚀 MATLAB 基本语法完全指南

> 本文将详细介绍 MATLAB 的基本语法，包括变量、矩阵、运算符、控制结构、函数、输入输出和绘图功能，帮助你快速掌握 MATLAB 编程基础。

## 📚 为什么学习 MATLAB 基本语法？

MATLAB 是科学计算和工程应用的重要工具，掌握基本语法是使用 MATLAB 的基础：

- 🔬 **科学计算**：矩阵运算、数值分析、算法实现
- 📊 **数据分析**：数据处理、统计分析、可视化
- 🎯 **工程应用**：控制系统、信号处理、图像处理
- 📈 **学术研究**：数学建模、仿真实验、论文写作

## 📝 MATLAB 基础语法

### 1️⃣ MATLAB 环境介绍

MATLAB 环境就像一个超级复杂的计算器。您可以在 `>>` 命令提示符下输入命令。MATLAB 是一个解释型环境，您给出一个命令，MATLAB 立即执行该命令。

### 2️⃣ 基本操作

```matlab
% 清空工作区、命令窗口和关闭图形窗口
clear; clc; close;
```

### 3️⃣ 动手练习

```matlab
5+5          % 加法运算
3^2          % 幂运算
sin(pi/2)    % 三角函数计算
7/0          % 除以零（结果为 Inf）
732*20.3     % 乘法运算
```

### 4️⃣ 使用分号（;）

分号（;）表示语句结束。如果要隐藏表达式的 MATLAB 输出，请在表达式后添加分号。

```matlab
x = 3;       % 赋值但不显示结果
y = x + 5;   % 计算但不显示结果
```

### 5️⃣ 添加注释

百分比符号（%）用于指示注释行。

```matlab
x = 9        % 将值 9 赋给 x
% 这是注释行，不会被执行
```

---

### 6️⃣ 使用省略号（…）表示行连续运算符

省略号（…）用于指示连续行连续运算符的开始。

```matlab
a = 3 ...      % 使用省略号继续到下一行
    + 5
```

### 7️⃣ 使用冒号（:）表示行连续运算符

冒号（:）用于指示连续行连续运算符的开始。

```matlab
1:1:10         % 生成 1 到 10 的序列，步长为 1
1:2:10         % 生成 1 到 10 的序列，步长为 2
```

## MATLAB 变量

### 特殊变量和常量

| 名称 | 意义                             |
| ---- | -------------------------------- |
| ans  | 最近计算的答案                   |
| eps  | 浮点精度                         |
| i, j | 虚数单位√-1                      |
| Inf  | 无穷                             |
| NaN  | 未定义的数值结果（not a number） |
| pi   | π                                |

---

### 命名变量

变量名称由字母组成，后跟任意数量的字母、数字或下划线。MATLAB是**case-sensitive**（区分大小写）。

变量名称可以是任意长度，但是MATLAB仅使用前N个字符，其中N由函数`namelengthmax`给定。

```matlab
a_1;
a2;
a2_;
% a#1;  % 错误：包含非法字符
% 1a;   % 错误：以数字开头
```

---

### MATLAB 变量初始化

在MATLAB环境中，每个变量都是矩阵。
**注意：**

1. 将变量输入系统后，您以后可以参考它。
2. 变量在使用前必须具有值。

```matlab
x = 3        % 定义x并用值初始化它
x = sqrt(16) % 定义x并用表达式初始化它
```

当表达式返回未分配给任何变量的结果时，系统会将其分配给名为`ans`的变量。

```matlab
sqrt(78)
9876/ans
%更多示例
x = 7 * 8;
y = x * 7.89
```

### 多项分配

您可以在同一行上进行多个分配。

```matlab
a = 2; b = 7; c = a * b
```

### format命令

默认情况下，MATLAB显示带有四个小数位值的数字（short format）。使用`format`命令提高精度。

```matlab
format long    % 将数字四舍五入到小数点后16位
x = 7 + 10/3 + 5 ^ 1.2

format short   % 将数字四舍五入到小数点后3位
x = 7 + 10/3 + 5 ^ 1.2

format bank    % 将数字四舍五入到小数点后两位
x = 7 + 10/3 + 5 ^ 1.2

format short e % 以科学计数法形式显示
x = 7 + 10/3 + 5 ^ 1.2

format long e  % 以指数形式显示
x = 7 + 10/3 + 5 ^ 1.2

format rat     % 给出由计算得出的最接近的有理表达式
x = 7 + 10/3 + 5 ^ 1.2
```

---

## 向量和矩阵

### 向量

向量是一维数字数组。MATLAB允许创建两种类型的向量：

- 行向量
- 列向量

**行向量**：通过将元素集括在方括号中并使用空格或逗号定界元素来创建。

```matlab
a = [1 2 3 4]
b = [1, 2, 3, 4]
c = a + b
```

**列向量**：通过将元素集括在方括号中并使用分号（;）分隔元素来创建，或使用转置。

```matlab
a = [1; 2; 3; 4]
b = [1 2 3 4]'
a + b
```

### 引用向量的元素

```matlab
a = [1 2 3 4];
a(3)          % 第3个元素

v = [1; 2; 3; 4; 5; 6];
v(:)          % 所有元素

rv = [1 2 3 4 5 6 7 8 9];
sub_rv = rv(3:7)      % 第3到第7个元素
sub_rv = rv(3:2:7)    % 第3,5,7个元素
```

### 向量运算

```matlab
clear;clc;
a= [1 2 3 4];b = [4 5 6 7];C = [4+1i 5 6 7];
a+b %两个向量相加
a-b %两个向量相减
3.*a % 向量的数乘
C'% 向量的共轭转置
C.'% 向量的非共轭转置
[a,b] % 向量的横追加
[a;b] % 向量的纵追加
a*b' % 向量的点乘
dot(a,b)% 向量的点乘
```

### 创建矩阵

矩阵是数字的二维数组。通过以空格或逗号分隔的元素的顺序输入每一行来创建矩阵，并用分号分隔行的结尾。

```matlab
m = [1 2 3; 4 5 6; 7 8 9]
m = [1, 2, 3; 4, 5, 6; 7, 8, 9]
```

### 引用矩阵的元素

```matlab
a = [1 2 3 4 5; 2 3 4 5 6; 3 4 5 6 7; 4 5 6 7 8];
a(2, 5)       % 第2行第5列
a(2, :)       % 第2行所有元素
a(:, 4)       % 第4列所有元素
a(:, 4:5)     % 第4到第5列所有元素
sa = a(2:3, 2:4)  % 第2-3行，第2-4列的子矩阵

% 删除行或列
a(4, :) = []  % 删除第4行
```

### 生成特殊矩阵

```matlab
a = ones(3, 3)    % 全是1的矩阵
b = zeros(3, 3)   % 全是0的矩阵
c = eye(3)        % 单位矩阵
R = rand(3, 3)    % 生成[0,1]区间的随机数矩阵
RN = randn(3, 3)  % 均值为0，方差为1的随机数矩阵
diagM = diag([1,2,3]) % 生成 对角线为[1,2,3]的矩阵
M = magic(3)      % 生成3x3的幻方矩阵
```

### 矩阵运算

```matlab
A = [1 2; 3 4]; B = [1 4; 3 2];
A + B        % 矩阵的加法
A - B        % 矩阵的减法
A * B        % 矩阵的乘法
A / B        % 右除 A/B = A*B^(-1)
A \ B        % 左除 A\B = A^(-1)*B
```

### 矩阵的标量运算

当您将一个矩阵加，减，乘或除以一个数字时，这称为scalar operation（标量运算）。
标量运算产生一个行数和列数相同的新矩阵，原始矩阵中的每个元素都与这个数相加、相减、相乘或相除。

```matlab
A = [1 2; 3 4]; b = 2;
A + b
A - b
A * b
A / b
```

### 矩阵的转置

```matlab
A = [1 2; 3 4];
B = [1+1i, 1-i; 2+1i, 2-i];
A'           % 共轭转置
A.'          % 非共轭转置
B'           % 共轭转置
B.'          % 非共轭转置
```

### 矩阵连接

您可以连接两个矩阵以创建更大的矩阵。这对方括号“ []”是串联运算符。

MATLAB允许两种类型的串联-

水平串联

垂直串联

当您通过使用逗号分隔两个矩阵来连接它们时，它们只是水平附加。这称为水平串联。

或者，如果使用分号将两个矩阵分开，则它们将垂直附加。这称为垂直串联

```matlab
A = [1 2; 3 4]; B = [1 4; 3 2];
[A, B]       % 水平连接
[A; B]       % 垂直连接
```

### 矩阵的行列式和逆矩阵

```matlab
a = [1 2 3; 2 3 4; 1 2 5];
det(a)       % 行列式

A = [1 2 3; 2 3 4; 1 2 5];
A^(-1)       % 逆矩阵
inv(A)       % 逆矩阵
```

### 多维数组

具有两个以上维的数组在MATLAB中称为多维数组。

```matlab
format short
b = rand(4, 3, 2)  % 4x3x2的三维数组
```

---

## MATLAB 单元格数组

单元格数组（Cell Array）是MATLAB中一种特殊的数据结构，可以存储不同类型和尺寸的数据。与普通数组不同，单元格数组的每个元素（称为单元格）可以包含任意类型的数据，包括数值、字符串、矩阵、结构体，甚至其他单元格数组。

### 创建单元格数组

#### 使用花括号创建

```matlab
% 创建1x3的单元格数组
C = {'MATLAB', [1 2 3; 4 5 6], 3.14}

% 创建2x2的单元格数组
C2 = {'姓名', '年龄'; '张三', 25; '李四', 30}

% 创建空单元格数组
empty_cell = cell(3, 2)  % 3x2的空单元格数组
```

#### 使用cell函数创建

```matlab
% 创建指定大小的空单元格数组
C = cell(2, 3)      % 2x3的空单元格数组
C = cell(1, 4)      % 1x4的空单元格数组
C = cell(3, 3, 2)   % 3x3x2的三维单元格数组
```

### 访问单元格内容

#### 使用花括号访问单元格内容

```matlab
C = {'MATLAB', [1 2 3; 4 5 6], 3.14};

% 访问第一个单元格的内容
content1 = C{1}      % 返回字符串 'MATLAB'

% 访问第二个单元格的内容
content2 = C{2}      % 返回矩阵 [1 2 3; 4 5 6]

% 访问第三个单元格的内容
content3 = C{3}      % 返回数值 3.14

% 访问多个单元格
contents = C{1:2}    % 返回前两个单元格的内容
```

#### 使用圆括号访问单元格（返回单元格数组）

```matlab
C = {'MATLAB', [1 2 3; 4 5 6], 3.14};

% 访问第一个单元格（返回单元格数组）
cell1 = C(1)         % 返回包含 'MATLAB' 的1x1单元格数组

% 访问子单元格数组
sub_cell = C(1:2)    % 返回包含前两个单元格的1x2单元格数组

```

#### 访问嵌套单元格

{% raw %}

```matlab
% 创建嵌套单元格数组
nested_cell = {{'a', 'b', 'c'}, [1 2 3], {1, 2, {3, 4}}}

% 访问嵌套内容
level1 = nested_cell{1}        % 返回单元格数组 {'a', 'b', 'c'}
level2 = nested_cell{1}{2}     % 返回字符串 'b'
level3 = nested_cell{3}{3}{2}  % 返回数值 4
```

{% endraw %}

### 修改单元格内容

```matlab
C = cell(2, 2);  % 创建2x2的空单元格数组

% 为单元格赋值
C{1, 1} = '姓名';
C{1, 2} = '年龄';
C{2, 1} = '张三';
C{2, 2} = 25;

% 修改现有单元格
C{2, 2} = 26;    % 将年龄从25改为26

% 添加新行
C{3, 1} = '李四';
C{3, 2} = 30;

% 删除行
C(3, :) = [];    % 删除第三行
```

### 单元格数组操作

#### 连接单元格数组

```matlab
C1 = {'A', 'B', 'C'};
C2 = {1, 2, 3};

% 水平连接
C_horizontal = [C1, C2]    % {'A', 'B', 'C', 1, 2, 3}

% 垂直连接
C_vertical = [C1; C2]      % {'A', 'B', 'C'; 1, 2, 3}
```

#### 重塑单元格数组

```matlab
C = {'A', 'B', 'C', 'D', 'E', 'F'};

% 重塑为2x3单元格数组
C_reshaped = reshape(C, 2, 3)

% 重塑为3x2单元格数组
C_reshaped2 = reshape(C, 3, 2)
```

### 常用单元格函数

#### cellfun函数：对每个单元格应用函数

```matlab
C = {'MATLAB', 'Programming', 'Language'};

% 获取每个字符串的长度
lengths = cellfun(@length, C)    % 返回 [6, 11, 8]

% 检查每个单元格是否为字符串
is_str = cellfun(@ischar, C)     % 返回 [1, 1, 1] (true)

% 将字符串转换为大写
upper_cells = cellfun(@upper, C, 'UniformOutput', false)
```

#### 处理混合数据类型

```matlab
% 创建包含混合数据类型的单元格数组
mixed_cell = {'姓名', 25, [1 2 3], true, struct('a', 1)};

% 显示每个单元格的数据类型
for i = 1:length(mixed_cell)
    fprintf('单元格 %d: %s\n', i, class(mixed_cell{i}));
end

% 使用cellfun获取所有单元格的类型
types = cellfun(@class, mixed_cell, 'UniformOutput', false)
```

### 单元格数组与结构体的转换

```matlab
% 创建单元格数组
C = {'姓名', '年龄', '成绩'; '张三', 25, 85; '李四', 30, 92};

% 将单元格数组转换为结构体数组
% 第一行作为字段名
S = cell2struct(C(2:end, :), C(1, :), 2)

% 访问结构体数据
disp(S(1).姓名)    % 显示 '张三'
disp(S(1).年龄)    % 显示 25
disp(S(1).成绩)    % 显示 85

% 将结构体数组转换回单元格数组
C_new = struct2cell(S)'
```

### 实用示例：学生信息管理

```matlab
%% 学生信息管理系统
clear; clc;

%% 1. 创建学生信息单元格数组
students = {
    '学号', '姓名', '年龄', '数学', '物理', '化学';
    '001', '张三', 20, 85, 90, 88;
    '002', '李四', 21, 92, 88, 95;
    '003', '王五', 19, 78, 85, 80;
    '004', '赵六', 22, 95, 92, 90
};

%% 2. 显示学生信息
disp('=== 学生信息表 ===');
for i = 1:size(students, 1)
    if i == 1
        fprintf('%6s %6s %4s %6s %6s %6s\n', students{i, :});
        fprintf('%s\n', repmat('-', 1, 40));
    else
        fprintf('%6s %6s %4d %6d %6d %6d\n', students{i, :});
    end
end

%% 3. 计算各科平均分
math_scores = [students{2:end, 4}];
physics_scores = [students{2:end, 5}];
chemistry_scores = [students{2:end, 6}];

math_avg = mean(math_scores);
physics_avg = mean(physics_scores);
chemistry_avg = mean(chemistry_scores);

fprintf('\n=== 各科平均分 ===\n');
fprintf('数学: %.2f\n', math_avg);
fprintf('物理: %.2f\n', physics_avg);
fprintf('化学: %.2f\n', chemistry_avg);

%% 4. 查找最高分学生
total_scores = math_scores + physics_scores + chemistry_scores;
[max_score, max_idx] = max(total_scores);
top_student = students{max_idx+1, 2};  % +1因为第一行是标题

fprintf('\n=== 最高分学生 ===\n');
fprintf('姓名: %s\n', top_student);
fprintf('总分: %d\n', max_score);
fprintf('数学: %d, 物理: %d, 化学: %d\n', ...
        math_scores(max_idx), physics_scores(max_idx), chemistry_scores(max_idx));

%% 5. 添加新学生
new_student = {'005', '钱七', 23, 88, 85, 90};
students = [students; new_student];

fprintf('\n=== 添加新学生后 ===\n');
disp('学生总数:');
disp(size(students, 1) - 1);  % 减去标题行

%% 6. 保存到文件
% 保存为MAT文件
save('students_data.mat', 'students');

% 保存为文本文件
fid = fopen('students_info.txt', 'w', 'n', 'UTF-8');
fprintf(fid, '学生信息表\n\n');
for i = 1:size(students, 1)
    if i == 1
        fprintf(fid, '%s\t%s\t%s\t%s\t%s\t%s\n', students{i, :});
        fprintf(fid, '%s\n', repmat('-', 1, 50));
    else
        fprintf(fid, '%s\t%s\t%d\t%d\t%d\t%d\n', students{i, :});
    end
end
fclose(fid);

fprintf('\n数据已保存到文件:\n');
fprintf('1. students_data.mat\n');
fprintf('2. students_info.txt\n');
```

### 单元格数组的优势和应用场景

#### 优势

1. **灵活性**：可以存储不同类型和大小的数据
2. **组织性**：便于组织和管理复杂数据
3. **兼容性**：与MATLAB大多数函数兼容
4. **效率**：对于混合数据类型，比结构体更高效

#### 应用场景

1. **数据表格**：存储具有不同数据类型的表格数据
2. **文本处理**：存储和处理字符串数组
3. **函数参数**：传递可变数量的参数
4. **结果收集**：收集不同迭代的结果
5. **GUI开发**：存储界面控件和数据

#### 性能注意事项

```matlab
% 预分配单元格数组以提高性能
n = 1000;
preallocated_cell = cell(n, 1);  % 推荐：预分配

% 不推荐：动态扩展
dynamic_cell = {};
for i = 1:n
    dynamic_cell{i} = i;  % 每次迭代都会重新分配内存
end
```

---

## 运算符

运算符是一个符号，告诉编译器执行特定的数学或逻辑操作。MATLAB设计为主要在整个矩阵和数组上运行。因此，MATLAB中的运算符既可以处理标量数据，也可以处理非标量数据。MATLAB允许以下类型的基本运算

> 算术运算符
> 关系运算符
> 逻辑运算符
> 按位运算符
> 集合运算符

### 关系运算符

| 序号 | 运算符和说明      |
| ---- | ----------------- |
| 1    | **<** 小于        |
| 2    | **<=** 小于或等于 |
| 3    | **>** 大于        |
| 4    | **>=** 大于或等于 |
| 5    | **==** 等于       |
| 6    | **~=** 不等于     |

```matlab
2 == 3
2 >= 3
2 <= 3
2 ~= 3
```

### 逻辑运算符

MATLAB提供两种类型的逻辑运算符和函数：

- 元素级：这些运算符对逻辑数组的相应元素进行操作
- 短路：这些运算符对标量和逻辑表达式进行运算

```matlab
2 == 3 & 2 ~= 3   % & 表示且
2 == 3 | 2 ~= 3   % | 表示或
~(2 == 3)         % ~ 表示非
```

### 集合运算符

| 序号 | 功能说明                                                                     |
| ---- | ---------------------------------------------------------------------------- |
| 1    | `intersect(A,B)` 设置两个数组的交集；返回A和B的公共值                        |
| 2    | `intersect(A,B,'rows')` 将A的每一行和B的每一行视为单个实体，返回A和B共用的行 |
| 3    | `ismember(A,B)` 返回一个与A大小相同的数组，其中包含1(true)表示A的元素在B中   |
| 4    | `ismember(A,B,'rows')` 将A的每一行和B的每一行视为单个实体                    |
| 5    | `issorted(A)` 如果元素按排序顺序排列，则返回逻辑1(true)                      |
| 6    | `issorted(A, 'rows')` 如果二维矩阵A的行按排序顺序排列，则返回逻辑1(true)     |
| 7    | `setdiff(A,B)` 设置两个数组的差值；返回A中不在B中的值                        |
| 8    | `setdiff(A,B,'rows')` 将A的每一行和B的每一行视为单个实体                     |
| 9    | `setxor` 两个数组的异或                                                      |
| 10   | `union` 两个数组的并集                                                       |
| 11   | `unique` 数组中的唯一值                                                      |

```matlab
% 创建集合
A = [1, 2, 3, 4];
B = [3, 4, 5, 6];

% 并集
U = union(A, B)      % [1 2 3 4 5 6]

% 交集
I = intersect(A, B)  % [3 4]

% 差集
D = setdiff(A, B)    % [1 2]

% 去重
C = unique([A, B])   % [1 2 3 4 5 6]
```

---

## 输入输出

### 常用命令

| 命令    | 目的                   |
| ------- | ---------------------- |
| clc     | 清除命令窗口           |
| clear   | 从内存中删除变量       |
| help    | 搜索帮助主题           |
| type    | 打出文件内容           |
| lookfor | 在帮助条目中搜索关键字 |
| quit    | 停止MATLAB             |

```matlab
clear
help sin
help pi
help type
type sin.m
```

### 输入输出命令

| 命令    | 目的                         |
| ------- | ---------------------------- |
| disp    | 显示数组或字符串的内容       |
| fscanf  | 从文件中读取格式化的数据     |
| format  | 控制屏幕显示格式             |
| fprintf | 执行对屏幕或文件的格式化写入 |
| input   | 显示提示并等待输入           |
| ;       | 禁止打印                     |

### disp函数

```matlab
disp("x is a sb")
disp(4)
disp("x is " + num2str(4))
```

### input函数

```matlab
x = input("输入一个数:");
disp("x is " + num2str(x))
```

### fprintf函数

```matlab
fprintf("x is %d\n", 4)
```

### 格式化代码

| 格式代码 | 目的                             |
| -------- | -------------------------------- |
| %s       | 格式化为字符串                   |
| %d       | 格式化为整数                     |
| %f       | 格式化为浮点值                   |
| %e       | 以科学计数形式格式化为浮点值     |
| %g       | 以最紧凑的格式进行格式化：%f或%e |
| \n       | 在输出字符串中插入新行           |
| \t       | 在输出字符串中插入一个选项卡     |

### 文件写入

````matlab
fid = fopen('test.txt', 'w', 'n', 'UTF-8');
fprintf(fid, "x is %d\n", 4);
fclose(fid);
`b`

---

## 控制结构

### 条件语句

#### if...end语句

```matlab
clear; clc;
x = 3;
if x == 3
    disp("x is 3")
end
````

#### if...else...end语句

```matlab
clear; clc;
x = 3;
if x == 3
    disp("x is 3")
else
    disp("x is not 3")
end
```

#### if...elseif...else...end语句

```matlab
clear; clc;
x = 6;
if x == 3
    disp("x is 3")
elseif x == 5
    disp("x is 5")
else
    disp("x is not 3 or 5")
end
```

#### switch语句

```matlab
clear; clc;
x = 3;
switch x
    case 3
        disp("x is 3")
    case 5
        disp("x is 5")
    otherwise
        disp("x is not 3 or 5")
end
```

### 循环语句

#### for循环

```matlab
for i = 1:2:10
    disp("i is " + num2str(i))
end
```

#### 嵌套for循环

```matlab
for i = 1:2:10
    for j = 1:2:3
        disp("i = " + num2str(i) + " j = " + num2str(j) + " i+j =" + num2str(i+j))
    end
end
```

### 循环控制语句

#### break语句

```matlab
for i = 1:1:10
    if i == 5
        break
    end
    disp("i = " + num2str(i))
end
```

#### continue语句

```matlab
for i = 1:1:10
    if i == 5
        continue
    end
    disp("i = " + num2str(i))
end
```

---

## MATLAB M文件

MATLAB允许您将一系列命令写入文件并以完整的单元形式执行文件，例如编写函数和调用它。
文件 `file_write.m`：

```matlab
for i= 1:1:10
    if i == 5
        continue
    end
    disp("i = " + num2str(i))
end
```

调用m文件：

```matlab
file_write
```

---

### 函数

#### 函数定义

函数是一起执行任务的一组语句。在MATLAB中，函数是在单独的文件中定义的。文件名和函数名应该相同。

函数语句的语法是：

```matlab
function [out1, out2, ..., outN] = myfun(in1, in2, in3, ..., inN)
```

#### 示例函数

文件 `a2b3.m`：

```matlab
function [c, d] = a2b3(a, b)
    c = a * 2;
    d = b * 3;
end
```

调用函数：

```matlab
[c, d] = a2b3(2, 3)
```

#### 匿名函数

匿名函数就像传统编程语言中的内联函数一样，是在单个MATLAB语句中定义的。

```matlab
power = @(x, n) x.^n;
result1 = power(7, 3)
result2 = power(49, 0.5)
result3 = power(10, -10)
result4 = power(4.5, 1.5)
```

#### 主和子函数

必须在文件中定义除匿名函数以外的任何函数。每个函数文件都包含一个首先出现的必需主函数，以及在主函数之后并由其使用的任意数量的可选子函数。

文件 `a4b5.m`：

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

```matlab
x = -100:1:100;
y = x.^2;
plot(x, y)
```

### 添加标题、标签、网格线和缩放

```matlab
x = 0:0.01:10;
y = sin(x);
plot(x, y), xlabel('x'), ylabel('Sin(x)'), title('Sin(x) Graph'),
grid on        % 允许您将网格线放在图形上
axis equal     % 命令生成一个正方形图
```

### 在同一图形上绘制多个函数

```matlab
x = 0:0.01:10;
y = sin(x);
g = cos(x);
plot(x, y, x, g), legend('Sin(x)', 'Cos(x)')
```

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

### 设定轴比例

```matlab
x = 0:0.01:10;
y = exp(-x).* sin(2*x + 3);
plot(x, y), axis([0 10 -1 1])
```

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

### 绘制条形图

```matlab
clear; clc; close all;
x = 1:10;
y = [75, 58, 90, 87, 50, 85, 92, 75, 60, 95];
bar(x, y), xlabel('Student'), ylabel('Score'), title('First Sem:')
```

### 三维图

三维图显示了由函数定义的两个变量 g = f(x, y) 的曲面。

```matlab
[x, y] = meshgrid(-2:.2:2);
z = x .* exp(-x.^2 - y.^2);
surf(x, y, z)
```

---

## MATLAB 字符串

```matlab
s = "x is 4"
```

### 连接字符串

```matlab
% 字符串单元格数组
str_array = {'red', 'blue', 'green', 'yellow', 'orange'}

% 将单元格数组中的字符串合并为单个字符串
str1 = strjoin(str_array, "-")
str2 = strjoin(str_array, ",")
```

### 查找和替换字符串

```matlab
students = 'Reva Dutta';

% strrep函数搜索并替换子字符串
new_student = strrep(students, 'Reva', 'Poulomi')
```

### 比较字符串

```matlab
str1 = 'This is test';
str2 = 'This is text';
if strcmp(str1, str2) == 0
   fprintf('%s and %s are equal', str1, str2);
else
   fprintf('%s and %s are not equal', str1, str2);
end
```

## 📊 实战案例：矩阵运算与数据可视化

### 案例背景

假设我们需要处理一个简单的数学问题：计算二次函数 \( f(x) = ax^2 + bx + c \) 在指定区间内的值，并进行可视化分析。

### 实现代码

```matlab
%% MATLAB 基本语法实战案例：二次函数分析
clear all; clc; close all;

%% 1. 定义参数和变量
a = 2;      % 二次项系数
b = -3;     % 一次项系数
c = 1;      % 常数项

% 定义 x 的取值范围
x = -10:0.1:10;  % 从 -10 到 10，步长为 0.1

%% 2. 计算函数值
% 使用向量化计算
y = a * x.^2 + b * x + c;

%% 3. 数据分析
% 找到最大值和最小值
[max_y, max_idx] = max(y);
[min_y, min_idx] = min(y);
max_x = x(max_idx);
min_x = x(min_idx);

% 计算平均值和标准差
mean_y = mean(y);
std_y = std(y);

%% 4. 输出分析结果
fprintf('=== 二次函数分析结果 ===\n');
fprintf('函数: f(x) = %.1fx^2 + %.1fx + %.1f\n', a, b, c);
fprintf('最大值: f(%.2f) = %.2f\n', max_x, max_y);
fprintf('最小值: f(%.2f) = %.2f\n', min_x, min_y);
fprintf('平均值: %.2f\n', mean_y);
fprintf('标准差: %.2f\n', std_y);

%% 5. 数据可视化
% 创建图形窗口
figure('Position', [100, 100, 1200, 600]);

% 子图1：函数曲线
subplot(1, 2, 1);
plot(x, y, 'b-', 'LineWidth', 2);
hold on;
plot(max_x, max_y, 'ro', 'MarkerSize', 10, 'MarkerFaceColor', 'r');
plot(min_x, min_y, 'go', 'MarkerSize', 10, 'MarkerFaceColor', 'g');
xlabel('x');
ylabel('f(x)');
title('二次函数曲线');
legend('f(x)', '最大值', '最小值', 'Location', 'best');
grid on;

% 添加文本标注
text(max_x, max_y, sprintf('最大值\n(%.2f, %.2f)', max_x, max_y), ...
     'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'center');
text(min_x, min_y, sprintf('最小值\n(%.2f, %.2f)', min_x, min_y), ...
     'VerticalAlignment', 'top', 'HorizontalAlignment', 'center');

% 子图2：数据统计
subplot(1, 2, 2);
stats = [max_y, min_y, mean_y, std_y];
labels = {'最大值', '最小值', '平均值', '标准差'};
bar(stats);
set(gca, 'XTickLabel', labels);
ylabel('数值');
title('统计指标');
grid on;

% 在柱状图上添加数值标签
for i = 1:length(stats)
    text(i, stats(i), sprintf('%.2f', stats(i)), ...
         'VerticalAlignment', 'bottom', 'HorizontalAlignment', 'center');
end

%% 6. 保存结果
% 保存图形
saveas(gcf, 'quadratic_function_analysis.png');

% 保存数据到文件
data = [x' y'];
save('quadratic_data.mat', 'data', 'a', 'b', 'c');
csvwrite('quadratic_data.csv', data);

fprintf('\n分析完成！\n');
fprintf('图形已保存为: quadratic_function_analysis.png\n');
fprintf('数据已保存为: quadratic_data.mat 和 quadratic_data.csv\n');

%% 7. 扩展功能：交互式输入
% 允许用户输入不同的参数
choice = input('是否要尝试不同的参数？(y/n): ', 's');
if lower(choice) == 'y'
    a = input('请输入二次项系数 a: ');
    b = input('请输入一次项系数 b: ');
    c = input('请输入常数项 c: ');

    % 重新计算并绘图
    y = a * x.^2 + b * x + c;

    figure;
    plot(x, y, 'r-', 'LineWidth', 2);
    xlabel('x');
    ylabel('f(x)');
    title(sprintf('f(x) = %.1fx^2 + %.1fx + %.1f', a, b, c));
    grid on;

    fprintf('新函数图形已显示！\n');
end

%% 8. 性能优化建议
fprintf('\n=== 性能优化建议 ===\n');
fprintf('1. 使用向量化运算代替循环，提高计算效率\n');
fprintf('2. 预分配数组大小，避免动态扩展\n');
fprintf('3. 使用内置函数代替自定义函数\n');
fprintf('4. 及时清除不需要的变量，释放内存\n');

%% 9. 错误处理示例
try
    % 尝试除以零
    test_result = 1 / 0;
catch ME
    fprintf('\n错误处理示例：\n');
    fprintf('错误信息: %s\n', ME.message);
    fprintf('建议：检查除数是否为零\n');
end

fprintf('\n=== 案例完成 ===\n');
```

## 📈 最佳实践总结

### 1️⃣ 代码组织建议

| 实践     | 说明                 | 示例                        |
| -------- | -------------------- | --------------------------- |
| 模块化   | 将代码分为逻辑模块   | 使用 `%%` 分隔不同功能模块  |
| 注释     | 添加详细注释         | 使用 `%` 解释代码功能       |
| 变量命名 | 使用有意义的变量名   | `student_scores` 而不是 `x` |
| 向量化   | 使用向量运算代替循环 | `y = a * x.^2` 而不是循环   |

### 2️⃣ 调试技巧

1. **使用 `disp` 和 `fprintf`**：

   ```matlab
   disp('当前变量值:');
   disp(x);
   fprintf('x = %f\n', x);
   ```

2. **设置断点**：
   - 在代码行左侧点击设置断点
   - 使用 `dbstop if error` 在错误时暂停

3. **检查变量**：
   ```matlab
   whos           % 查看工作区变量
   size(x)        % 查看数组大小
   class(x)       % 查看变量类型
   ```

### 3️⃣ 学习资源推荐

1. **官方文档**：MATLAB 帮助文档 (`help function_name`)
2. **在线教程**：MathWorks 官方网站教程
3. **社区支持**：MATLAB Central 论坛
4. **书籍推荐**：
   - 《MATLAB 编程与工程应用》
   - 《MATLAB 数值计算》
   - 《MATLAB 图形与可视化》

## 🎯 总结

这个教程涵盖了 MATLAB 的基础语法和核心功能，包括：

### 1️⃣ 基础概念

- MATLAB 环境介绍和基本操作
- 变量定义和数据类型
- 运算符和特殊字符

### 2️⃣ 数据结构

- 向量和矩阵的创建与操作
- 多维数组的使用
- 单元格数组（Cell Array）的创建与操作
- 字符串处理

### 3️⃣ 编程结构

### 4️⃣ 输入输出

- 基本 I/O 操作
- 文件读写
- 数据格式化

### 5️⃣ 数据可视化

- 2D 和 3D 绘图
- 图形属性设置
- 子图和图形保存

### 6️⃣ 实战应用

- 矩阵运算和分析
- 数据可视化案例
- 性能优化建议

MATLAB 是一个强大的数值计算和数据可视化工具，掌握这些基础知识将为您进一步学习 MATLAB 高级功能打下坚实的基础。通过本教程的学习，您应该能够：

1. ✅ 理解 MATLAB 的基本语法和编程结构
2. ✅ 熟练使用向量和矩阵进行数值计算
3. ✅ 编写简单的 MATLAB 函数和脚本
4. ✅ 创建基本的数据可视化图形
5. ✅ 应用 MATLAB 解决简单的工程和科学问题

继续深入学习 MATLAB 的高级功能，如信号处理、图像处理、控制系统设计等，将帮助您在科学研究和工程应用中发挥 MATLAB 的强大能力。
