---
layout: post
title: "数学建模第十一课：用 MATLAB 和 LINGO 求解线性规划"
categories: 数学建模入门课
tags: [数学建模, 线性规划, 单纯形法, MATLAB, LINGO]
description: "上一课手算单纯形表看清了算法，这一课交给软件：MATLAB 的 linprog 矩阵式与 optimproblem 问题式两种写法，LINGO 的公式式建模，同一道生产计划题跑出同样的 20、20、1800，再把两边的输出一行一行读懂——包括 LINGO 那份统计信息和参数表该怎么看。"
keywords: 数学建模, 线性规划, 单纯形法, MATLAB, linprog, optimproblem, LINGO
mermaid: false
---

## 引言

上一课手动推演了三张单纯形表，完整走过 O → C → B 这条换基路径。这样做的目的是看清算法内部在做什么，而非以手算作为实际求解手段。

在实际的建模比赛或工程问题中，决策变量常有几十乃至上百个，约束也有几十条，手工推演单纯形表并不现实，需要借助求解器。本课沿用上一课的例题，分别使用两种常用工具求解：

- **MATLAB**：通用数值计算平台，`linprog` 一行解线性规划，还能把优化嵌进更大的计算流程；
- **LINGO**：专为优化模型设计的建模语言，模型可以几乎按数学公式原样写进去。

工具不同，背后的算法是同一个。所以判断软件跑对没跑对，标准也很简单：**它给出的最优解和迭代次数，必须和上一课手算的结果对得上。**

例题还是那道生产计划题：

$$ \max \quad Z = 50x_1 + 40x_2 $$

$$ \text{s.t.} \quad 2x_1 + x_2 \leq 60 $$

$$ \quad 2x_1 + 4x_2 \leq 120 $$

$$ x_1 \geq 0, \quad x_2 \geq 0 $$

上一课的最优解为甲 20 件、乙 20 件，最大利润 1800 元，共经两轮换基。本课要验证的是：两个软件能否精确复现这三个数值。

## 用 MATLAB 求解

上一课手动推演三张表，是为了理解算法本身。实际建模与工程计算中，求解通常交由求解器完成。MATLAB 中求解线性规划的标准函数是 `linprog`，其内部采用单纯形法及其变体（新版默认调用内点法、对偶单纯形等现代实现），所得最优解应与手算结果一致。

### linprog 的标准调用形式

`linprog` 只认**最小化**和**小于等于**这两种形式：

$$ \min_{x} \quad f^{T}x \quad \text{s.t.} \quad A x \leq b, \quad A_{eq} x = b_{eq}, \quad lb \leq x \leq ub $$

因此本课的最大化问题需先将目标函数取负：求 `max Z = 50x₁ + 40x₂`，等价于求 `min (-50x₁ - 40x₂)`，求得结果后再取负还原。这一步是常见的错误来源：若遗漏取负，得到的将是最小值，数值看似合理而符号相反。

### 完整代码

```matlab
% 数学建模第十一课：线性规划例题（生产计划）
% max Z = 50*x1 + 40*x2
% s.t.  2*x1 +   x2 <= 60
%       2*x1 + 4*x2 <= 120
%       x1, x2 >= 0

clear; clc;

f = [-50, -40];              % 最大化取负，转成最小化
A = [2, 1;                  % 原料 A 的消耗
     2, 4];                 % 原料 B 的消耗
b = [60; 120];               % 两种原料的日供应上限
lb = [0; 0];                 % 非负约束
ub = [];                     % 无上界

[x, fval, exitflag, output] = linprog(f, A, b, [], [], lb, ub);

Z = -fval;                   % 取负还原成最大利润
fprintf('exitflag = %d\n', exitflag);
fprintf('x1 = %.4f 件\n', x(1));
fprintf('x2 = %.4f 件\n', x(2));
fprintf('Z  = %.4f 元\n', Z);
fprintf('迭代次数 = %d\n', output.iterations);
```

### 运行结果

```text
exitflag = 1
x1 = 20.0000 件
x2 = 20.0000 件
Z  = 1800.0000 元
迭代次数 = 2
```

逐条对照：

- **`exitflag = 1`** 表示求解成功、找到最优解。若返回 0 说明达到迭代上限，-2 说明无可行解，-3 说明问题无界——这三种情况都要回头检查模型，而不是直接拿结果写论文。
- **`x1 = 20`、`x2 = 20`、`Z = 1800`**，与手算的顶点 B 完全一致。
- **迭代次数 = 2**，正好对应手算的两轮换基：O → C → B。软件并未采用不同的路径，只是将行变换交由机器执行。

### 也可以用问题式写法

若所用 MATLAB 为 **R2017b 或更新版本**，可直接用 `optimproblem` 按公式原样描述模型，无需自行构造矩阵：

```matlab
prob = optimproblem('ObjectiveSense', 'maximize');
x = optimvar('x', 2, 'LowerBound', 0);
prob.Objective = 50*x(1) + 40*x(2);
prob.Constraints.cons1 = 2*x(1) + x(2) <= 60;
prob.Constraints.cons2 = 2*x(1) + 4*x(2) <= 120;

[sol, fval, exitflag, output] = solve(prob);
fprintf('exitflag = %d\n', exitflag);
disp('x1 ='); disp(sol.x(1));
disp('x2 ='); disp(sol.x(2));
fprintf('Z  = %.4f 元\n', fval);
```

运行结果：

```text
Solving problem using linprog.

Optimal solution found.

    exitflag = 1
x1 =
    20
x2 =
    20
Z  = 1800.0000 元
```

逐行说明：

- `optimproblem('ObjectiveSense', 'maximize')`：建立一个优化问题对象，并直接声明求解方向为最大化——**此处无需取负**，MATLAB 自动处理方向，这是它与 `linprog` 最主要的区别；
- `optimvar('x', 2, 'LowerBound', 0)`：声明一个长度为 2 的变量向量，下界统一设为 0，非负约束由此一条语句完成，不必另写 `lb`；
- `prob.Objective = ...`：目标函数照数学式子写，`50*x(1) + 40*x(2)`，与题目里的 `50x₁ + 40x₂` 一一对应；
- `prob.Constraints.cons1 = ...`：约束逐条命名，`<=` 按原样书写，不必把 `2x₁ + x₂ ≤ 60` 拆成矩阵的一行；
- `solve(prob)`：求解。返回值里 `sol.x` 是变量取值，`fval` 是目标函数值，`exitflag` 与 `output` 的含义和 `linprog` 一致。

输出中的 `Solving problem using linprog.` 值得注意：**`optimproblem` 只改变了模型的书写方式，实际调用的仍是 `linprog`**。它将变量、目标与约束转换为矩阵形式，再交给同一个求解器。因此 20、20、1800 三个数与前述结果完全一致，这在预期之内——两者使用的是同一套算法与同一个入口，并非两套算法偶然得到相同结果。

两版代码的差别仅在于写法：

- 矩阵式需自行维护 `f`、`A`、`b`、`lb` 四个数组，模型一旦修改，数组的行列位置也须同步调整；
- 问题式可直接写入 `2*x(1) + x(2) <= 60`，改动仅限于表达式本身。

代价是问题式多了一层对象封装，在数千次循环中反复建模时会略慢于直接调用 `linprog`；若只求解单次问题，这一差异可以忽略。

两种写法结果相同。矩阵式（`linprog`）书写紧凑、便于批量处理；问题式（`optimproblem`）更贴近数学模型，修改约束时不易出现行列错位。建模比赛中建议先用问题式把模型写正确，再视需要转为矩阵式。

需注意的是：`optimproblem` 自 **MATLAB R2017b** 起提供，且需安装 Optimization Toolbox。查看版本可在启动界面确认，也可在命令行输入 `ver`，首行即为版本号。版本早于 R2017b 或未安装该工具箱时，应使用 `linprog`——`linprog` 出现较早，绝大多数版本均包含。

### MATLAB 这一段要记住什么

- 最大化问题必须**取负转最小化**，算完再取负回来；
- 约束要整理成 `A*x <= b` 的形式，`>=` 的约束两边乘 −1；
- 拿到结果先看 `exitflag`，再看数值；
- 新版可用 `optimproblem` 直接写「最大化」，不必手动取负。

## 用 LINGO 求解

MATLAB 是通用数值工具，LINGO（Linear Interactive and General Optimizer）则是专门为优化模型设计的建模语言。其主要优势在于：**模型几乎可按数学公式原样书写**，无需将目标函数与约束转换为矩阵。建模比赛中常用它快速检验模型是否正确。

### 完整 LINGO 模型

```text
MODEL:
! 数学建模第十一课：线性规划例题（生产计划）;
! max Z = 50*x1 + 40*x2;

MAX = 50 * x1 + 40 * x2;

! 原料 A 的约束;
2 * x1 + 1 * x2 <= 60;

! 原料 B 的约束;
2 * x1 + 4 * x2 <= 120;

! 默认所有变量非负，无需显式声明;
END
```

将上述模型粘贴到 LINGO 的模型窗口，执行求解（Solve），输出如下：

```text
Global optimal solution found.
  Objective value:                              1800.000
  Infeasibilities:                              0.000000
  Total solver iterations:                             2
  Elapsed runtime seconds:                          0.05

  Model Class:                                        LP

  Total variables:                      2
  Nonlinear variables:                  0
  Integer variables:                    0

  Total constraints:                    3
  Nonlinear constraints:                0

  Total nonzeros:                       6
  Nonlinear nonzeros:                   0



                                Variable           Value        Reduced Cost
                                      X1        20.00000            0.000000
                                      X2        20.00000            0.000000

                                     Row    Slack or Surplus      Dual Price
                                       1        1800.000            1.000000
                                       2        0.000000            20.00000
                                       3        0.000000            5.000000
```

输出上半段的统计信息描述的是**模型本身**的结构，与最优解数值无关，但可据此判断模型是否书写正确：

- **`Model Class: LP`**：模型被识别成线性规划。若此处显示 `NLP`（非线性），说明存在非线性表达式，通常源于变量相乘或出现 `x^2` 一类写法，需要返回检查；
- **`Total variables: 2`、`Total constraints: 3`**：2 个决策变量、3 条约束。除两条原料约束外，LINGO 将变量的非负约束也计入约束总数；
- **`Nonlinear variables: 0`、`Integer variables: 0`**：无非线性变量，也无整数变量。两者均为 0，表明这是标准的连续线性规划，正是单纯形法的适用范围；
- **`Total nonzeros: 6`**：约束矩阵中共 6 个非零系数，即 2×2 消耗矩阵中的四个元素，加上目标函数中的 2 个系数；
- **`Elapsed runtime seconds: 0.05`**：求解耗时 0.05 秒。本题规模极小，耗时已接近可测量下限。

上述统计量在建模比赛中较为实用：模型规模变大后，先检查 `Model Class` 与 `Nonlinear variables`，可在结果出现异常之前发现模型本身不属于线性规划这类根本性错误。

下半段为结果表。

逐条说明：

- **Objective value = 1800**，与手算、MATLAB 一致；
- **X1 = 20、X2 = 20**，最优解的变量取值；
- **Reduced Cost = 0**，表示两个变量均已取正值并进入基，继续增加不会再改善目标函数；
- **Slack or Surplus 第 2、3 行为 0**，表示两条原料约束均已取到上限，对应顶点 B 处两条直线同时取等号；该列名为「松弛或剩余」，表示各约束的剩余量，取值 0 即无剩余；
- **Total solver iterations = 2**，同样对应两轮换基。

第 1 行是目标函数行而非约束：其 Slack or Surplus 位显示目标值 1800，右侧一列恒为 1。这是 LINGO 的固定输出格式，不应作为约束解读。

### 两种软件，各管一段

同一道题，两种定位：

- **MATLAB**：通用计算平台，适合将优化嵌入更大的计算流程，例如批量求解 100 组参数、绘制参数变化曲线、进行蒙特卡洛模拟；
- **LINGO**：专用建模工具，适合把模型书写清楚，修改约束如同修改公式，不易出现矩阵错位。

建模比赛中常见的分工是：先用 LINGO 将模型书写正确并求出结果，确认思路无误；再用 MATLAB 做参数扫描与绘图。两者结果一致时，可基本排除求解环节的错误。

## 小结

同一道题、两种工具、同一组答案：`x1 = 20`、`x2 = 20`、`Z = 1800`，迭代 2 次，与上一课手算的三张表完全一致。

**MATLAB 这一段要记住：**

- `linprog` 只接受最小化与 `A*x <= b` 形式，最大化问题需取负，`>=` 约束需两边同乘 −1；
- 结果应先检查 `exitflag`（1 成功、0 达迭代上限、−2 无可行解、−3 无界），再读数值；
- R2017b 之后可用 `optimproblem` 按公式原样建模，修改约束时不易出现行列错位。

**LINGO 这一段要记住：**

- 模型按公式书写，`MAX =` 与 `<=` 直接对应数学模型，变量默认非负；
- 输出中重点关注三项：`Objective value`、`Slack or Surplus`、`Total solver iterations`；
- 输出上半段先看 `Model Class` 是不是 `LP`，再读下半段的结果表。

**两者的分工：** 先用 LINGO 将模型书写正确并求出结果以确认思路，再用 MATLAB 做参数扫描与绘图。两条路径结果一致，可作为求解无误的依据。

最后一点：单纯形法只是线性规划的起点。整数规划、目标规划、非线性规划各有专门算法，但「从一个可行解出发，按某个判据改进，直到无法继续改进」这一思路贯穿其中——单纯形表中的检验数与最小比值规则，之后会以其他名称反复出现。
