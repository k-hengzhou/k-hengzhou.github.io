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

% 示例 2：读取指定工作表
T = readtable('data.xlsx', 'Sheet', 'Sheet2');

% 示例 3：读取指定范围
T = readtable('data.xlsx', 'Range', 'A1:D100');

% 示例 4：指定变量名
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
% 方法 1：使用 readtable 的 MissingRule 选项
T = readtable('data.xlsx', 'MissingRule', 'fill', 'FillValue', 0);

% 方法 2：读取后处理
T = readtable('data.xlsx');
T = standardizeMissing(T, {'NA', 'NaN', ''});

% 方法 3：使用 fillmissing 函数
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
% 方法 1：使用列名
T = readtable('data.xlsx', 'SelectedVariableNames', {'姓名', '年龄', '成绩'});

% 方法 2：使用列索引
T = readtable('data.xlsx', 'SelectedVariableNames', [1, 3, 5]);

% 方法 3：使用 ImportOptions
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
% 使用 readtable 读取数据
filename = 'students.xlsx';
students = readtable(filename);

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
    for i = 3:6  % 成绩列
        col_name = students.Properties.VariableNames{i};
        students.(col_name) = fillmissing(students.(col_name), 'mean');
    end
end

%% 3. 统计分析
% 计算各科平均分
math_avg = mean(students.数学);
physics_avg = mean(students.物理);
chemistry_avg = mean(students.化学);
total_avg = mean(students.总分);

fprintf('\n=== 成绩统计分析 ===\n');
fprintf('数学平均分: %.2f\n', math_avg);
fprintf('物理平均分: %.2f\n', physics_avg);
fprintf('化学平均分: %.2f\n', chemistry_avg);
fprintf('总分平均分: %.2f\n', total_avg);

% 计算标准差
math_std = std(students.数学);
physics_std = std(students.物理);
chemistry_std = std(students.化学);

fprintf('\n=== 成绩标准差分析 ===\n');
fprintf('数学标准差: %.2f\n', math_std);
fprintf('物理标准差: %.2f\n', physics_std);
fprintf('化学标准差: %.2f\n', chemistry_std);

%% 4. 排名分析
% 按总分排序
[~, idx] = sort(students.总分, 'descend');
ranked_students = students(idx, :);

fprintf('\n=== 学生排名 ===\n');
for i = 1:height(ranked_students)
    fprintf('第%d名: %s (总分: %d)\n', i, ...
            ranked_students.姓名{i}, ranked_students.总分(i));
end

%% 5. 可视化分析
% 创建图形窗口
figure('Position', [100, 100, 1200, 600]);

% 子图1：各科成绩分布
subplot(1, 3, 1);
boxplot([students.数学, students.物理, students.化学], ...
        'Labels', {'数学', '物理', '化学'});
title('各科成绩分布箱线图');
ylabel('分数');
grid on;

% 子图2：学生总分柱状图
subplot(1, 3, 2);
bar(students.总分);
set(gca, 'XTickLabel', students.姓名);
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
            ranked_students.姓名{i}, ranked_students.学号{i}, ...
            ranked_students.总分(i));
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
                     ranked_students.学号, ranked_students.姓名, ...
                     ranked_students.数学, ranked_students.物理, ...
                     ranked_students.化学, ranked_students.总分, ...
                     'VariableNames', {'排名', '学号', '姓名', '数学', '物理', '化学', '总分'});
writetable(ranked_table, output_filename, 'Sheet', '排名结果');

fprintf('处理后的数据已保存到: %s\n', output_filename);

%% 8. 高级分析：相关性分析
fprintf('\n=== 科目相关性分析 ===\n');
correlation_matrix = corrcoef([students.数学, students.物理, students.化学]);
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

## 🚀 性能优化技巧

### 1️⃣ 大型文件处理

```matlab
% 方法 1：分块读取
opts = detectImportOptions('large_data.xlsx');
opts.DataRange = 'A1';
T = readtable('large_data.xlsx', opts, 'ReadVariableNames', true);

% 方法 2：只读取需要的列
opts.SelectedVariableNames = {'重要列1', '重要列2', '重要列3'};
T = readtable('large_data.xlsx', opts);

% 方法 3：使用 datastore（超大型文件）
ds = datastore('large_data.xlsx');
while hasdata(ds)
    T = read(ds);
    % 处理数据块
end
```

### 2️⃣ 内存优化

```matlab
% 清除不需要的变量
clear num txt raw

% 使用适当的数据类型
T.Score = int16(T.Score);  % 如果分数范围在 0-100

% 压缩数据
T = compress(T);
```

### 3️⃣ 批量处理多个文件

```matlab
% 批量读取多个 Excel 文件
files = dir('*.xlsx');
all_data = cell(length(files), 1);

for i = 1:length(files)
    fprintf('正在处理: %s\n', files(i).name);
    all_data{i} = readtable(files(i).name);
end

% 合并数据
combined_data = vertcat(all_data{:});
```

## 🔍 常见问题与解决方案

### 问题 1：中文乱码

**解决方案**：

```matlab
% 指定文件编码
T = readtable('data.xlsx', 'FileEncoding', 'UTF-8');

% 或者使用 ImportOptions
opts = detectImportOptions('data.xlsx', 'FileEncoding', 'UTF-8');
T = readtable('data.xlsx', opts);
```

### 问题 2：日期格式错误

**解决方案**：

```matlab
% 指定日期格式
opts = detectImportOptions('data.xlsx');
opts = setvaropts(opts, 'DateColumn', ...
                  'InputFormat', 'yyyy-MM-dd', ...
                  'DatetimeFormat', 'yyyy-MM-dd');
T = readtable('data.xlsx', opts);
```

### 问题 3：科学计数法问题

**解决方案**：

```matlab
% 使用 ImportOptions 指定数据类型
opts = detectImportOptions('data.xlsx');
opts = setvartype(opts, 'LargeNumberColumn', 'string');
T = readtable('data.xlsx', opts);

% 转换回数值（如果需要）
T.LargeNumberColumn = str2double(T.LargeNumberColumn);
```

### 问题 4：读取速度慢

**解决方案**：

```matlab
% 1. 使用 readmatrix 代替 readtable（纯数值数据）
M = readmatrix('data.xlsx');

% 2. 预定义 ImportOptions
opts = detectImportOptions('data.xlsx');
T = readtable('data.xlsx', opts);

% 3. 关闭自动类型检测
opts = detectImportOptions('data.xlsx', 'VariableNamingRule', 'preserve');
T = readtable('data.xlsx', opts);

% 4. 使用 datastore 处理超大文件
ds = datastore('large_data.xlsx');
data = readall(ds);
```

### 问题 5：内存不足

**解决方案**：

```matlab
% 1. 分块读取
chunk_size = 10000;
opts = detectImportOptions('large_data.xlsx');
opts.DataRange = sprintf('A1:A%d', chunk_size);
T = readtable('large_data.xlsx', opts);

% 2. 只读取需要的列
opts.SelectedVariableNames = {'Column1', 'Column2', 'Column3'};
T = readtable('data.xlsx', opts);

% 3. 使用适当的数据类型
T.SmallNumbers = int8(T.SmallNumbers);
T.MediumNumbers = int16(T.MediumNumbers);

% 4. 及时清除不需要的变量
clear large_data temp_data
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

## 🎯 实战演练：销售数据分析

### 案例需求

分析一个销售数据 Excel 文件 `sales.xlsx`，包含以下列：

- 日期 (Date)
- 产品名称 (Product)
- 销售数量 (Quantity)
- 单价 (Price)
- 销售员 (Salesperson)

### 实现代码

```matlab
%% 销售数据分析系统
clear all; clc;

%% 1. 读取销售数据
fprintf('正在读取销售数据...\n');
sales_data = readtable('sales.xlsx', 'DateLocale', 'zh_CN');

% 显示数据概览
fprintf('数据概览:\n');
fprintf('总记录数: %d\n', height(sales_data));
fprintf('数据列: %s\n', strjoin(sales_data.Properties.VariableNames, ', '));

%% 2. 数据清洗
% 检查缺失值
missing_summary = sum(ismissing(sales_data));
if any(missing_summary > 0)
    fprintf('发现缺失值，正在处理...\n');

    % 数值列用中位数填充
    numeric_cols = {'Quantity', 'Price'};
    for i = 1:length(numeric_cols)
        col = numeric_cols{i};
        if ismember(col, sales_data.Properties.VariableNames)
            sales_data.(col) = fillmissing(sales_data.(col), 'median');
        end
    end

    % 文本列用众数填充
    text_cols = {'Product', 'Salesperson'};
    for i = 1:length(text_cols)
        col = text_cols{i};
        if ismember(col, sales_data.Properties.VariableNames)
            sales_data.(col) = fillmissing(sales_data.(col), 'constant', '未知');
        end
    end
end

%% 3. 计算销售额
sales_data.TotalAmount = sales_data.Quantity .* sales_data.Price;

%% 4. 按产品分析
fprintf('\n=== 按产品分析 ===\n');
products = unique(sales_data.Product);
for i = 1:length(products)
    product_mask = strcmp(sales_data.Product, products{i});
    product_sales = sales_data(product_mask, :);

    total_quantity = sum(product_sales.Quantity);
    total_amount = sum(product_sales.TotalAmount);
    avg_price = mean(product_sales.Price);

    fprintf('产品: %s\n', products{i});
    fprintf('  总销量: %d\n', total_quantity);
    fprintf('  总销售额: ¥%.2f\n', total_amount);
    fprintf('  平均单价: ¥%.2f\n', avg_price);
    fprintf('  销售记录数: %d\n\n', height(product_sales));
end

%% 5. 按销售员分析
fprintf('\n=== 按销售员分析 ===\n');
salespersons = unique(sales_data.Salesperson);
salesperson_stats = table();

for i = 1:length(salespersons)
    person_mask = strcmp(sales_data.Salesperson, salespersons{i});
    person_sales = sales_data(person_mask, :);

    total_amount = sum(person_sales.TotalAmount);
    avg_amount = mean(person_sales.TotalAmount);
    transaction_count = height(person_sales);

    % 添加到统计表
    new_row = table({salespersons{i}}, total_amount, avg_amount, transaction_count, ...
                    'VariableNames', {'Salesperson', 'TotalAmount', 'AvgAmount', 'TransactionCount'});
    salesperson_stats = [salesperson_stats; new_row];
end

% 按总销售额排序
salesperson_stats = sortrows(salesperson_stats, 'TotalAmount', 'descend');
disp(salesperson_stats);

%% 6. 时间序列分析
fprintf('\n=== 时间序列分析 ===\n');

% 按月份汇总
sales_data.Month = month(sales_data.Date);
sales_data.Year = year(sales_data.Date);

monthly_sales = groupsummary(sales_data, {'Year', 'Month'}, 'sum', 'TotalAmount');
monthly_sales.Properties.VariableNames{'sum_TotalAmount'} = 'MonthlyTotal';

% 显示月度销售数据
fprintf('月度销售汇总:\n');
disp(monthly_sales);

%% 7. 可视化分析
figure('Position', [100, 100, 1400, 800]);

% 子图1：产品销售额饼图
subplot(2, 3, 1);
product_totals = zeros(length(products), 1);
for i = 1:length(products)
    product_mask = strcmp(sales_data.Product, products{i});
    product_totals(i) = sum(sales_data.TotalAmount(product_mask));
end
pie(product_totals, products);
title('产品销售额占比');

% 子图2：销售员业绩柱状图
subplot(2, 3, 2);
bar(salesperson_stats.TotalAmount);
set(gca, 'XTickLabel', salesperson_stats.Salesperson);
title('销售员业绩对比');
xlabel('销售员');
ylabel('总销售额 (元)');
xtickangle(45);
grid on;

% 子图3：月度销售趋势
subplot(2, 3, 3);
monthly_sales.MonthYear = datetime(monthly_sales.Year, monthly_sales.Month, 1);
plot(monthly_sales.MonthYear, monthly_sales.MonthlyTotal, 'o-', 'LineWidth', 2);
title('月度销售趋势');
xlabel('月份');
ylabel('销售额 (元)');
grid on;
datetick('x', 'yyyy-mm', 'keepticks');

% 子图4：价格分布直方图
subplot(2, 3, 4);
histogram(sales_data.Price, 20);
title('产品价格分布');
xlabel('价格 (元)');
ylabel('频数');
grid on;

% 子图5：销量与价格散点图
subplot(2, 3, 5);
scatter(sales_data.Price, sales_data.Quantity, 50, 'filled', 'MarkerFaceAlpha', 0.6);
title('价格 vs 销量');
xlabel('价格 (元)');
ylabel('销量');
grid on;

% 子图6：热力图 - 销售员 vs 产品
subplot(2, 3, 6);
% 创建交叉表
heatmap_data = zeros(length(salespersons), length(products));
for i = 1:length(salespersons)
    for j = 1:length(products)
        mask = strcmp(sales_data.Salesperson, salespersons{i}) & ...
               strcmp(sales_data.Product, products{j});
        heatmap_data(i, j) = sum(sales_data.TotalAmount(mask));
    end
end
imagesc(heatmap_data);
colorbar;
set(gca, 'XTick', 1:length(products), 'XTickLabel', products);
set(gca, 'YTick', 1:length(salespersons), 'YTickLabel', salespersons);
title('销售员-产品销售额热力图');
xlabel('产品');
ylabel('销售员');
xtickangle(45);

%% 8. 生成分析报告
report_filename = '销售分析报告.txt';
fid = fopen(report_filename, 'w', 'n', 'UTF-8');

fprintf(fid, '========== 销售数据分析报告 ==========\n\n');
fprintf(fid, '报告生成时间: %s\n\n', datetime('now'));

fprintf(fid, '一、数据概览\n');
fprintf(fid, '----------------------------------------\n');
fprintf(fid, '总销售记录数: %d\n', height(sales_data));
fprintf(fid, '总销售额: ¥%.2f\n', sum(sales_data.TotalAmount));
fprintf(fid, '平均每单金额: ¥%.2f\n', mean(sales_data.TotalAmount));
fprintf(fid, '产品种类数: %d\n', length(products));
fprintf(fid, '销售员人数: %d\n\n', length(salespersons));

fprintf(fid, '二、销售员排名\n');
fprintf(fid, '----------------------------------------\n');
for i = 1:height(salesperson_stats)
    fprintf(fid, '第%d名: %s (销售额: ¥%.2f, 平均单额: ¥%.2f, 成交数: %d)\n', ...
            i, salesperson_stats.Salesperson{i}, ...
            salesperson_stats.TotalAmount(i), ...
            salesperson_stats.AvgAmount(i), ...
            salesperson_stats.TransactionCount(i));
end

fprintf(fid, '\n三、产品分析\n');
fprintf(fid, '----------------------------------------\n');
for i = 1:length(products)
    product_mask = strcmp(sales_data.Product, products{i});
    product_sales = sales_data(product_mask, :);

    fprintf(fid, '产品: %s\n', products{i});
    fprintf(fid, '  销售额: ¥%.2f\n', sum(product_sales.TotalAmount));
    fprintf(fid, '  销量: %d\n', sum(product_sales.Quantity));
    fprintf(fid, '  平均价格: ¥%.2f\n', mean(product_sales.Price));
    fprintf(fid, '  销售记录数: %d\n\n', height(product_sales));
end

fprintf(fid, '四、建议\n');
fprintf(fid, '----------------------------------------\n');
fprintf(fid, '1. 重点关注销售额最高的产品\n');
fprintf(fid, '2. 奖励表现优秀的销售员\n');
fprintf(fid, '3. 分析月度销售趋势，制定营销策略\n');
fprintf(fid, '4. 优化价格策略以提高销量\n');

fclose(fid);
fprintf('\n分析报告已保存到: %s\n', report_filename);

%% 9. 保存处理结果
% 保存处理后的数据
output_filename = 'processed_sales_data.xlsx';
writetable(sales_data, output_filename, 'Sheet', '销售数据');

% 保存销售员统计
writetable(salesperson_stats, output_filename, 'Sheet', '销售员统计');

% 保存月度汇总
writetable(monthly_sales, output_filename, 'Sheet', '月度汇总');

fprintf('处理结果已保存到: %s\n', output_filename);

%% 10. 高级分析：预测模型（示例）
fprintf('\n=== 销售预测模型（示例） ===\n');

% 准备时间序列数据（简化示例）
if height(monthly_sales) >= 3
    % 使用简单移动平均进行预测
    monthly_totals = monthly_sales.MonthlyTotal;

    % 计算3个月移动平均
    if length(monthly_totals) >= 3
        ma3 = movmean(monthly_totals, 3);
        fprintf('3个月移动平均预测:\n');
        for i = 1:length(ma3)
            fprintf('  月份 %d: 实际 %.2f, 预测 %.2f\n', ...
                    i, monthly_totals(i), ma3(i));
        end
    end
else
    fprintf('数据不足，无法进行预测分析\n');
end

fprintf('\n=== 分析完成 ===\n');
```

## 🎓 学习资源推荐

### 1️⃣ 官方文档

- [MATLAB 读取电子表格文件](https://ww2.mathworks.cn/help/matlab/import_export/ways-to-import-spreadsheets.html)
- [readtable 函数文档](https://ww2.mathworks.cn/help/matlab/ref/readtable.html)
- [detectImportOptions 函数文档](https://ww2.mathworks.cn/help/matlab/ref/detectimportoptions.html)

### 2️⃣ 在线教程

- MATLAB 官方教程：数据导入与导出
- MathWorks 在线课程：MATLAB 数据处理
- 中文社区：MATLAB 中文论坛

### 3️⃣ 推荐书籍

- 《MATLAB 从入门到精通》
- 《MATLAB 数据分析与挖掘实战》
- 《MATLAB 工程应用》

## 📝 总结

通过本文的学习，你应该掌握了：

1. **多种读取方法**：`xlsread`、`readtable`、`readmatrix`、`readcell`
2. **高级选项配置**：ImportOptions、数据类型转换、缺失值处理
3. **实战案例分析**：学生成绩分析、销售数据分析
4. **性能优化技巧**：大型文件处理、内存优化、批量处理
5. **问题解决方案**：中文乱码、日期格式、科学计数法等常见问题

MATLAB 读取 Excel 文件是数据分析和科学计算的基础技能，掌握这些技巧将大大提高你的工作效率。建议结合实际项目进行练习，逐步掌握各种高级功能。

**记住**：选择合适的方法比使用最复杂的方法更重要。根据数据特点和需求选择最简单的解决方案。

---

_最后更新：2025年3月22日_
_作者：MATLAB 数据分析专家_
