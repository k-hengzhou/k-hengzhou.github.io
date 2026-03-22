---
layout: post
title: "MATLAB 读取 Excel 文件完全指南"
categories: matlab excel 数据处理
description: "本文将详细介绍 MATLAB 读取 Excel 文件的多种方法，包括基本读取、高级选项、数据清洗和实战案例"
keywords: matlab, excel, xlsread, readtable, readmatrix, 数据导入
mermaid: false
sequence: false
flow: false
mathjax: true
mindmap: false
mindmap2: false
---

# 📊 MATLAB 读取 Excel 文件完全指南

> 本文将详细介绍 MATLAB 读取 Excel 文件的多种方法，包括基本读取、高级选项、数据清洗和实战案例，帮助你高效处理 Excel 数据。

## 🚀 为什么需要 MATLAB 读取 Excel？

Excel 是数据存储和交换的常用格式，MATLAB 提供了强大的 Excel 读取功能：

- 📈 **数据分析**：将 Excel 数据导入 MATLAB 进行统计分析
- 🔬 **科学研究**：处理实验数据、测量结果
- 📊 **商业应用**：财务报表、销售数据分析
- 🎯 **工程计算**：仿真参数、测试数据导入

## 📚 MATLAB 读取 Excel 的主要函数

### 1️⃣ `xlsread` 函数（传统方法）

`xlsread` 是 MATLAB 传统的 Excel 读取函数，支持多种数据格式：

```matlab
% 基本语法
[num, txt, raw] = xlsread(filename, sheet, range)
```

- **参数说明**：
  - `filename`：Excel 文件名（包含路径）
  - `sheet`：工作表名称或索引（可选）
  - `range`：读取范围（可选，如 'A1:C10'）

- **返回值**：
  - `num`：数值数据矩阵
  - `txt`：文本数据单元格数组
  - `raw`：原始数据（混合类型）

#### 示例代码

```matlab
% 示例 1：读取整个工作表
[num, txt, raw] = xlsread('data.xlsx');

% 示例 2：读取指定工作表
[num, txt, raw] = xlsread('data.xlsx', 'Sheet2');

% 示例 3：读取指定范围
[num, txt, raw] = xlsread('data.xlsx', 'Sheet1', 'A1:D100');

% 示例 4：只读取数值数据
num = xlsread('data.xlsx');
```

### 2️⃣ `readtable` 函数（推荐方法）

`readtable` 是 MATLAB R2013b 引入的现代函数，返回表格数据类型：

```matlab
% 基本语法
T = readtable(filename, 'Sheet', sheet, 'Range', range)
```

- **优势**：
  - 自动识别列名
  - 支持混合数据类型
  - 更好的数据组织
  - 支持更多选项

#### 示例代码

```matlab
% 示例 1：读取整个 Excel 文件
T = readtable('data.xlsx');
% 示例 2：中文列名
data = readtable('student.xlsx', 'VariableNamingRule', 'preserve');
% 示例 3：读取指定工作表
T = readtable('data.xlsx', 'Sheet', 'Sheet2');

% 示例 4：读取指定范围
T = readtable('data.xlsx', 'Range', 'A1:D100');

% 示例 5：指定变量名
T = readtable('data.xlsx', 'VariableNamingRule', 'preserve');

```

### 3️⃣ `readmatrix` 函数（纯数值数据）

`readmatrix` 专门用于读取数值矩阵：

```matlab
% 基本语法
M = readmatrix(filename, 'Sheet', sheet, 'Range', range)
```

- **特点**：
  - 只读取数值数据
  - 忽略文本和空单元格
  - 返回标准矩阵

#### 示例代码

```matlab
% 示例 1：读取数值矩阵
M = readmatrix('data.xlsx');

% 示例 2：读取指定范围的数值
M = readmatrix('data.xlsx', 'Range', 'B2:F50');

% 示例 3：处理缺失值
M = readmatrix('data.xlsx', 'MissingRule', 'fill');
```

### 4️⃣ `readcell` 函数（混合数据）

`readcell` 读取所有数据为单元格数组：

```matlab
% 基本语法
C = readcell(filename, 'Sheet', sheet, 'Range', range)
```

- **适用场景**：
  - 混合数据类型
  - 需要保留原始格式
  - 不确定数据类型的文件

#### 示例代码

```matlab
% 示例 1：读取所有数据为单元格
C = readcell('data.xlsx');

% 示例 2：读取指定工作表
C = readcell('data.xlsx', 'Sheet', 'Sheet2');

% 示例 3：处理日期格式
C = readcell('data.xlsx', 'DateLocale', 'zh_CN');
```

## 🔧 高级读取选项

### 1️⃣ 处理缺失值

```matlab


% 方法 1：读取后处理
T = readtable('data.xlsx');
T = standardizeMissing(T, {'NA', 'NaN', ''});

% 方法 2：使用 fillmissing 函数
T = readtable('data.xlsx');
T.Var1 = fillmissing(T.Var1, 'constant', 0);
```

### 2️⃣ 数据类型转换

```matlab
% 指定列的数据类型
opts = detectImportOptions('data.xlsx');
opts = setvartype(opts, {'Var1', 'Var2'}, 'double');
opts = setvartype(opts, 'Var3', 'string');
T = readtable('data.xlsx', opts);

% 自动检测数据类型
T = readtable('data.xlsx', 'VariableNamingRule', 'preserve');
```

### 3️⃣ 读取特定列

```matlab

% 方法 1：使用 ImportOptions
opts = detectImportOptions('data.xlsx');
opts.SelectedVariableNames = {'Column1', 'Column3', 'Column5'};
T = readtable('data.xlsx', opts);
```

### 4️⃣ 处理日期和时间

```matlab
% 读取日期数据
T = readtable('data.xlsx', 'DateLocale', 'zh_CN');

% 指定日期格式
opts = detectImportOptions('data.xlsx');
opts = setvaropts(opts, 'DateColumn', 'InputFormat', 'yyyy-MM-dd');
T = readtable('data.xlsx', opts);

% 转换日期格式
T.DateColumn = datetime(T.DateColumn, 'InputFormat', 'dd/MM/yyyy');
```

## 📊 实战案例：学生成绩分析

### 案例背景

假设有一个 Excel 文件 `students.xlsx`，包含以下数据：

| 学号 | 姓名 | 数学 | 物理 | 化学 | 总分 |
| ---- | ---- | ---- | ---- | ---- | ---- |
| 001  | 张三 | 85   | 90   | 88   | 263  |
| 002  | 李四 | 92   | 88   | 95   | 275  |
| 003  | 王五 | 78   | 85   | 80   | 243  |
| 004  | 赵六 | 95   | 92   | 90   | 277  |

### 实现代码

```matlab
%% 学生成绩分析系统
clear all; clc;

%% 1. 读取 Excel 数据
% 使用 readtable 读取数据，保留中文列名
filename = 'students.xlsx';
students = readtable(filename, 'VariableNamingRule', 'preserve');

% 显示数据
disp('原始数据：');
disp(students);

%% 2. 数据预处理
% 检查缺失值
missing_values = sum(ismissing(students));
disp('缺失值统计：');
disp(missing_values);

% 如果有缺失值，用平均值填充
if any(missing_values > 0)
    % 定义成绩列名
    score_columns = {'数学', '物理', '化学', '总分'};

    for i = 1:length(score_columns)
        col_name = score_columns{i};
        if ismember(col_name, students.Properties.VariableNames)
            students.(col_name) = fillmissing(students.(col_name), 'mean');
        end
    end
end

%% 3. 统计分析
% 计算各科平均分 - 使用字符串访问列名
math_avg = mean(students.("数学"));
physics_avg = mean(students.("物理"));
chemistry_avg = mean(students.("化学"));
total_avg = mean(students.("总分"));

fprintf('\n=== 成绩统计分析 ===\n');
fprintf('数学平均分: %.2f\n', math_avg);
fprintf('物理平均分: %.2f\n', physics_avg);
fprintf('化学平均分: %.2f\n', chemistry_avg);
fprintf('总分平均分: %.2f\n', total_avg);

% 计算标准差
math_std = std(students.("数学"));
physics_std = std(students.("物理"));
chemistry_std = std(students.("化学"));

fprintf('\n=== 成绩标准差分析 ===\n');
fprintf('数学标准差: %.2f\n', math_std);
fprintf('物理标准差: %.2f\n', physics_std);
fprintf('化学标准差: %.2f\n', chemistry_std);

%% 4. 排名分析
% 按总分排序
[~, idx] = sort(students.("总分"), 'descend');
ranked_students = students(idx, :);

fprintf('\n=== 学生排名 ===\n');
for i = 1:height(ranked_students)
    fprintf('第%d名: %s (总分: %d)\n', i, ...
            ranked_students.("姓名")(i), ranked_students.("总分")(i));
end

%% 5. 可视化分析
% 创建图形窗口
figure('Position', [100, 100, 1200, 600]);

% 子图1：各科成绩分布
subplot(1, 3, 1);
boxplot([students.("数学"), students.("物理"), students.("化学")], ...
        'Labels', {'数学', '物理', '化学'});
title('各科成绩分布箱线图');
ylabel('分数');
grid on;

% 子图2：学生总分柱状图
subplot(1, 3, 2);
bar(students.("总分"));
set(gca, 'XTickLabel', students.("姓名"));
title('学生总分柱状图');
xlabel('学生姓名');
ylabel('总分');
grid on;
xtickangle(45);

% 子图3：各科平均分饼图
subplot(1, 3, 3);
scores = [math_avg, physics_avg, chemistry_avg];
labels = {'数学', '物理', '化学'};
pie(scores, labels);
title('各科平均分比例');

%% 6. 输出分析报告
% 创建分析报告
report_filename = '成绩分析报告.txt';
fid = fopen(report_filename, 'w', 'n', 'UTF-8');

fprintf(fid, '========== 学生成绩分析报告 ==========\n\n');
fprintf(fid, '分析时间: %s\n\n', datetime('now'));

fprintf(fid, '一、基本统计信息\n');
fprintf(fid, '----------------------------------------\n');
fprintf(fid, '学生总数: %d人\n', height(students));
fprintf(fid, '数学平均分: %.2f\n', math_avg);
fprintf(fid, '物理平均分: %.2f\n', physics_avg);
fprintf(fid, '化学平均分: %.2f\n', chemistry_avg);
fprintf(fid, '总分平均分: %.2f\n\n', total_avg);

fprintf(fid, '二、学生排名\n');
fprintf(fid, '----------------------------------------\n');
for i = 1:height(ranked_students)
    fprintf(fid, '第%d名: %s (学号: %s, 总分: %d)\n', i, ...
            string(ranked_students.("姓名")(i)), string(ranked_students.("学号")(i)), ...
            ranked_students.("总分")(i));
end


fprintf(fid, '\n三、建议\n');
fprintf(fid, '----------------------------------------\n');
fprintf(fid, '1. 数学成绩标准差较大，建议加强基础教学\n');
fprintf(fid, '2. 物理成绩整体较好，可适当增加难度\n');
fprintf(fid, '3. 化学成绩相对稳定，保持当前教学节奏\n');

fclose(fid);
fprintf('\n分析报告已保存到: %s\n', report_filename);

%% 7. 保存处理后的数据
% 将处理后的数据保存到新 Excel 文件
output_filename = 'processed_students.xlsx';
writetable(students, output_filename, 'Sheet', '处理后的数据');

% 添加排名信息
ranked_table = table((1:height(ranked_students))', ...
                     ranked_students.("学号"), ranked_students.("姓名"), ...
                     ranked_students.("数学"), ranked_students.("物理"), ...
                     ranked_students.("化学"), ranked_students.("总分"), ...
                     'VariableNames', {'排名', '学号', '姓名', '数学', '物理', '化学', '总分'});
writetable(ranked_table, output_filename, 'Sheet', '排名结果');

fprintf('处理后的数据已保存到: %s\n', output_filename);

%% 8. 高级分析：相关性分析
fprintf('\n=== 科目相关性分析 ===\n');
correlation_matrix = corrcoef([students.("数学"), students.("物理"), students.("化学")]);
corr_table = array2table(correlation_matrix, ...
                        'VariableNames', {'数学', '物理', '化学'}, ...
                        'RowNames', {'数学', '物理', '化学'});
disp(corr_table);

% 可视化相关性矩阵
figure('Position', [100, 100, 800, 600]);
heatmap({'数学', '物理', '化学'}, {'数学', '物理', '化学'}, correlation_matrix);
title('科目成绩相关性热图');
colormap('jet');
colorbar;

%% 9. 性能优化建议
fprintf('\n=== 性能优化建议 ===\n');
fprintf('1. 对于大型 Excel 文件，建议使用 ImportOptions 预定义导入参数\n');
fprintf('2. 如果只需要部分数据，使用 SelectedVariableNames 减少内存占用\n');
fprintf('3. 对于纯数值数据，使用 readmatrix 比 readtable 更快\n');
fprintf('4. 考虑将 Excel 转换为 .mat 格式以提高后续读取速度\n');

%% 10. 错误处理示例
try
    % 尝试读取不存在的文件
    test_data = readtable('nonexistent.xlsx');
catch ME
    fprintf('\n错误处理示例：\n');
    fprintf('错误信息: %s\n', ME.message);
    fprintf('建议：检查文件路径和文件名是否正确\n');
end

fprintf('\n=== 分析完成 ===\n');
```

## 📈 最佳实践总结

### 1️⃣ 选择合适的函数

| 场景         | 推荐函数     | 理由                       |
| ------------ | ------------ | -------------------------- |
| 需要表格操作 | `readtable`  | 自动识别列名，支持表格操作 |
| 纯数值数据   | `readmatrix` | 速度快，内存占用小         |
| 混合数据类型 | `readcell`   | 保留原始格式               |
| 向后兼容     | `xlsread`    | 旧版本 MATLAB 支持         |

### 2️⃣ 性能优化建议

1. **预处理 ImportOptions**：

   ```matlab
   opts = detectImportOptions('data.xlsx');
   % 配置选项...
   T = readtable('data.xlsx', opts);
   ```

2. **减少内存占用**：
   - 只读取需要的列
   - 使用适当的数据类型
   - 及时清除不需要的变量

3. **处理大型文件**：
   - 使用 `datastore` 分块读取
   - 考虑转换为 `.mat` 格式
   - 使用 `readmatrix` 替代 `readtable`

### 3️⃣ 错误处理策略

```matlab
try
    % 尝试读取文件
    T = readtable('data.xlsx');
catch ME
    % 错误处理
    fprintf('读取文件失败: %s\n', ME.message);

    % 尝试其他方法
    try
        T = readmatrix('data.xlsx');
    catch
        fprintf('所有方法都失败了\n');
        return;
    end
end
```
