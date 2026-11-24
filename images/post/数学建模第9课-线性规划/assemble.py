# -*- coding: utf-8 -*-
"""Assemble the red-white themed WeChat article HTML from 正文.md."""
import io, os, re

BASE = os.path.dirname(os.path.abspath(__file__))
sys_path = BASE
import importlib.util

spec = importlib.util.spec_from_file_location("bg", os.path.join(BASE, "build_gzh.py"))
bg = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bg)

md = io.open(os.path.join(BASE, "正文.md"), encoding="utf-8").read()

# strip frontmatter
md = re.sub(r"^---\n.*?\n---\n", "", md, flags=re.S)

# drop the top-level blockquote (used as the intro line) — captured separately
top_quote = "在数学建模比赛中，线性规划是最基础、也最常用的优化模型。"

parts = []

# ---------------- intro card (component 3 substitute: 引言卡) --------------
parts.append(bg.intro_card(
    "—— 分享有意思的数学内容",
    "线性规划：把「有限资源下做到最好」写成一组线性不等式",
    "从生产计划问题完整走一遍建模流程，看懂图解法与灵敏度分析。"))

# ---------------- 前言导读 (本文看点 — 3 chapters) -----------------------
parts.append(
    '<section style="margin:0 10px 30px;padding:18px 20px;background:' + bg.RED_SOFT +
    ';border-radius:12px;">'
    '<p style="font-size:14px;font-weight:800;color:' + bg.RED + ';margin:0 0 12px;">'
    '<span leaf="">📌 本文看点</span></p>'
    '<p style="font-size:14px;color:' + bg.BODY + ';margin:0 0 8px;line-height:1.8;">'
    '<span leaf="">1. 用一个生产计划问题，完整走一遍「建模→求解→分析」；</span></p>'
    '<p style="font-size:14px;color:' + bg.BODY + ';margin:0 0 8px;line-height:1.8;">'
    '<span leaf="">2. 看懂图解法：最优解为什么一定落在可行域的顶点上；</span></p>'
    '<p style="font-size:14px;color:' + bg.BODY + ';margin:0;line-height:1.8;">'
    '<span leaf="">3. 看懂灵敏度分析，知道方案在多大范围内是稳的。</span></p></section>')

parts.append(bg.quote([
    '<span leaf="">' + top_quote.replace("线性规划", bg.u("线性规划")) + '</span>']))

# ---------------- chapters (## headings) ---------------------------------
def txt(s):
    """convert a markdown inline fragment to themed html with span leaf wrap."""
    # inline formulas  $...$  -> handled by caller via placeholders
    return s


# We hand-map each chapter for control (only 6 chapters).
# helper to emit body paragraph with underline phrases already applied
def para(text):
    return bg.p(text)


# ============ 01 引言 ============
parts.append(bg.h2("01", "引言", "INTRODUCTION"))
parts.append(para(
    '<span leaf="">第五课我们以「矩形面积最大」问题认识了优化模型的通用格式与三要素：</span>'
    + bg.strong("决策变量、目标函数、约束条件") +
    '<span leaf="">。那一题的函数是二次的，属于非线性优化。而现实里更常见的一类问题，目标与约束都是</span>'
    + bg.tag("线性") +
    '<span leaf="">的——资源有限、关系简单、约束一目了然。这类问题，就是</span>'
    + bg.u("线性规划（Linear Programming，简称 LP）") + '<span leaf="">。</span>'))
parts.append(para(
    '<span leaf="">线性规划是运筹学中最成熟、求解最可靠的分支。生产计划、运输调度、配料选材、投资组合、人力排班……只要能把「在有限资源下把某个指标做到最优」写成一组线性不等式，它就落进了线性规划的射程。也正因为</span>'
    + bg.u("结构清晰、算法完备") + '<span leaf="">，它几乎成了数学建模比赛里的常客与保底工具。</span>'))
parts.append(bg.callout("线性规划的通用格式",
    '<span leaf="">沿用第五课的三要素提法，线性规划可以统一写成下面这样一组式子：</span>'))
parts.append(bg.formula("f_lp_general"))
parts.append(para(
    '<span leaf="">其中 </span>' + bg.chip("f_lp_general", 0) if False else
    '<span leaf="">其中 </span><strong style="color:' + bg.INK + ';"><span leaf="">x₁, x₂, …, xₙ</span></strong>'
    '<span leaf=""> 是决策变量；目标函数与所有约束条件都是这些变量的</span>'
    + bg.u("线性表达式") +
    '<span leaf="">；最后一行的非负约束，是绝大多数实际问题的天然限制（产量、时间、数量不为负）。</span>'))

# ============ 02 生产计划 ============
parts.append(bg.h2("02", "从生产计划问题认识线性规划", "A PRODUCTION PLANNING CASE"))
parts.append(para(
    '<span leaf="">先看一个规模很小的例子，它包含了线性规划的</span>'
    + bg.u("全部要素") +
    '<span leaf="">，也足够让我们把求解过程走一遍。</span>'))
parts.append(bg.h3_("问题提出"))
parts.append(para('<span leaf="">某工厂生产甲、乙两种产品，相关数据如下表：</span>'))
parts.append(bg.table(
    ["产品", "每件利润（元）", "每件耗材 A（kg）", "每件耗材 B（kg）"],
    [["甲", "50", "2", "2"], ["乙", "40", "1", "4"]]))
parts.append(para(
    '<span leaf="">工厂每天可提供的原料 A 为 60 kg、原料 B 为 120 kg。问：甲、乙各生产多少件，才能使每天的</span>'
    + bg.strong("总利润最大") + '<span leaf="">？</span>'))
parts.append(bg.h3_("问题分析"))
parts.append(para(
    '<span leaf="">这是一个典型的</span>' + bg.tag("资源分配") +
    '<span leaf="">问题。我们要决定的是产量，要最大化的是利润，受到的是原料总量的限制。三个要素一一对应：</span>'))
parts.append(bg.ul([
    bg.strong("决策变量") + '<span leaf="">：甲、乙两种产品的日产量；</span>',
    bg.strong("目标函数") + '<span leaf="">：总利润，等于两种产品利润之和；</span>',
    bg.strong("约束条件") + '<span leaf="">：两种原料的消耗量分别不能超过各自库存。</span>']))
parts.append(para(
    '<span leaf="">此外还有一个容易被忽略、却必须写上的条件：</span>'
    + bg.u("产量不能为负") +
    '<span leaf="">。这不是废话——非负约束正是线性规划标准形式的一部分。</span>'))

parts.append(bg.h3_("建立模型"))
parts.append(para('<span leaf="">先列出符号说明：</span>'))
parts.append(bg.table(
    ["符号", "含义", "说明"],
    [["x₁", "产品甲的日产量", "决策变量"],
     ["x₂", "产品乙的日产量", "决策变量"],
     ["Z", "每天的利润总额", "目标函数"]]))
parts.append(para(
    '<span leaf="">先写</span>' + bg.strong("目标函数") +
    '<span leaf="">。甲每件赚 50 元、乙每件赚 40 元，总利润为 </span>'
    + bg.strong("Z = 50x₁ + 40x₂") + '<span leaf="">。</span>'))
parts.append(para(
    '<span leaf="">再写</span>' + bg.strong("约束条件") +
    '<span leaf="">。原料 A 每天最多用 60 kg，甲每件耗 2 kg、乙每件耗 1 kg；原料 B 每天最多用 120 kg，甲每件耗 2 kg、乙每件耗 4 kg。于是两条不等式为 </span>'
    + bg.strong("2x₁ + x₂ ≤ 60") + '<span leaf=""> 与 </span>'
    + bg.strong("2x₁ + 4x₂ ≤ 120") + '<span leaf="">。</span>'))
parts.append(para(
    '<span leaf="">加上非负约束 </span>' + bg.strong("x₁ ≥ 0, x₂ ≥ 0") +
    '<span leaf="">，得到完整的数学模型：</span>'))
parts.append(bg.formula("f_ex1_model"))
parts.append(para(
    '<span leaf="">这就是一个标准的</span>' + bg.u("二元线性规划模型") + '<span leaf="">。</span>'))

parts.append(bg.h3_("模型求解（图解法）"))
parts.append(para(
    '<span leaf="">决策变量只有两个，可以用</span>' + bg.tag("图解法") +
    '<span leaf="">直观求解——把每个约束画在平面上，看可行解落在哪片区域，再让目标函数「扫」过去。</span>'))
parts.append(para(
    '<span leaf="">第一步，画出</span>' + bg.strong("可行域") +
    '<span leaf="">。把两个不等式取等号，得到两条直线 </span>'
    + bg.strong("2x₁ + x₂ = 60") + '<span leaf="">、</span>'
    + bg.strong("2x₁ + 4x₂ = 120") +
    '<span leaf="">。它们与坐标轴围出的公共区域，就是所有</span>'
    + bg.u("可行解") + '<span leaf="">的集合。由于约束都是「小于等于」，可行域是一个</span>'
    + bg.u("凸多边形") + '<span leaf="">——在本例中是一个四边形。</span>'))
parts.append(bg.quote([
    '<span leaf="">线性规划的可行域必是</span>' + bg.strong("凸集") +
    '<span leaf="">（任意两个可行点连线仍在域内），这是它求解可靠的根本原因，后面还会用到。</span>']))
parts.append(para(
    '<span leaf="">第二步，找目标函数的「等值线」。目标函数 </span>'
    + bg.strong("Z = 50x₁ + 40x₂") +
    '<span leaf=""> 取不同值时，是一族互相平行的直线。Z 越大，直线离原点越远。于是问题变成：</span>'
    + bg.u("在可行域内，让这条直线尽量往外推，能推到多远") + '<span leaf="">？</span>'))
parts.append(bg.anim(
    "lp_graphic_demo_opt.gif",
    "图解法动图：左图两条约束直线围出可行域，右图目标函数等值线向外平移，最后卡在顶点 B 上"))
parts.append(para(
    '<span leaf="">这两步里，约束怎么画、直线怎么推，一张静态图可以看得更全：</span>'))
parts.append(bg.figure(
    "lp_graphic_steps.png", "线性规划图解法三步示意",
    "图解法三步：① 画约束围出可行域 → ② 等值线向外平移 → ③ 卡在顶点 B(20,20)，Z=1800"))
parts.append(para(
    '<span leaf="">第三步，确定最优解所在的顶点。直线往外平移，最后接触可行域的位置，一定是可行域的某个</span>'
    + bg.strong("顶点") + '<span leaf="">（角点）。把三个顶点代进目标函数比较：</span>'))
parts.append(para(
    '<span leaf="">只有两个决策变量时，这一步可以直接穷举。可行域的顶点有限，'
    '把每个顶点都算一遍，取 Z 最大的那个就是答案——这也正是</span>'
    + bg.u("二元线性规划一定可以用图解法解到底") +
    '<span leaf="">的原因，不需要任何迭代算法。</span>'))
parts.append(bg.table(
    ["顶点", "坐标 (x₁, x₂)", "利润 Z"],
    [["A", "(0, 30)", "1200"], ["B", "(20, 20)", "1800"], ["C", "(30, 0)", "1500"]],
    highlight={(1, 2)}))
parts.append(para(
    '<span leaf="">比较可得，在顶点 </span>' + bg.strong("B(20, 20)") +
    '<span leaf=""> 处利润最大：</span>'))
parts.append(bg.formula("f_optimal"))
parts.append(para(
    '<span leaf="">即：每天生产</span>' + bg.u("甲 20 件、乙 20 件") +
    '<span leaf="">，可获得最大利润 </span>' + bg.strong("1800 元") + '<span leaf="">。</span>'))
parts.append(para(
    '<span leaf="">回头再看第一步那条结论：可行域是凸多边形，而线性目标函数沿任何方向都单调变化，'
    '所以它平移到最后一定「卡」在某个顶点上，而不会落在边的中间——这就是</span>'
    + bg.u("二元线性规划的最优解必在顶点取得") +
    '<span leaf="">。图解法要做的，只是确认是哪个顶点。</span>'))

parts.append(bg.h3_("结果分析"))
parts.append(bg.ul([
    bg.strong("可行性验证") + '<span leaf="">：2 × 20 + 20 = 60 ≤ 60，2 × 20 + 4 × 20 = 120 ≤ 120，'
    '且 x₁, x₂ ≥ 0，所有约束都满足，故该解是可行解；</span>',
    bg.strong("最优性说明") + '<span leaf="">：目标函数是线性的，沿任何方向移动 Z 都单调变化；'
    '直线族平移到最后必然「卡」在可行域边界的一个顶点上，因此</span>'
    + bg.u("比较所有顶点即可锁定最优解") + '<span leaf="">；</span>',
    bg.strong("现实解读") + '<span leaf="">：两种原料中，原料 A 恰好用尽（=60），原料 B 也恰好用尽（=120）。'
    '这两个「取等号」的约束，正是限制利润继续增长的</span>'
    + bg.tag("紧约束（瓶颈资源）") + '<span leaf="">。</span>']))

# 第 03 章（单纯形法）已移除，本篇聚焦二维变量的图解法

# ============ 04 灵敏度分析 ============
parts.append(bg.h2("03", "结果评估：灵敏度分析", "SENSITIVITY ANALYSIS"))
parts.append(para(
    '<span leaf="">模型里的数据（利润、耗材、库存）都是</span>' + bg.tag("估计值") +
    '<span leaf="">，现实中难免有波动。我们关心的不是「参数精确等于多少」，而是</span>'
    + bg.u("参数变一点，最优解会不会变") + '<span leaf="">。这就是</span>'
    + bg.strong("灵敏度分析（sensitivity analysis）") + '<span leaf="">。</span>'))
parts.append(para(
    '<span leaf="">以本例为例：设产品甲的单价利润从 50 元变为一个可变的 k 元，其余不变。'
    '目标函数变为 </span>' + bg.strong("Z = kx₁ + 40x₂") +
    '<span leaf="">，它的斜率随 k 改变。只要斜率仍处于可行域在顶点 B 处的</span>'
    + bg.u("两条边界斜率之间") +
    '<span leaf="">，最优点就还停在 B；一旦越界，最优点会跳到相邻顶点。在本例中，B 保持最优的条件是：</span>'))
parts.append(bg.formula("f_sens"))
parts.append(para(
    '<span leaf="">也就是说：产品甲的利润涨到约</span>' + bg.strong("2.5 倍以内") +
    '<span leaf="">，最优生产方案（甲 20、乙 20）都不用调整。这类「参数允许变化的范围」，'
    '比一个孤立的数字更有决策价值——它告诉决策者，方案在多大范围内是稳的。</span>'))

# ============ 05 小结 ============
parts.append(bg.h2("04", "小结", "SUMMARY"))
parts.append(para('<span leaf="">本文以「生产计划」问题为例，完整走了一遍线性规划的建模与求解：</span>'))
parts.append(bg.ol([
    bg.strong("建立模型") + '<span leaf="">：明确决策变量、目标函数与约束条件，写出线性规划模型；</span>',
    bg.strong("模型求解") + '<span leaf="">：本题只有两个决策变量，用</span>' + bg.tag("图解法") +
    '<span leaf="">最直观，画出可行域、平移等值线，最优解必在顶点；</span>',
    bg.strong("结果分析") + '<span leaf="">：验证可行性与最优性，识别瓶颈（紧约束）；</span>',
    bg.strong("结果评估") + '<span leaf="">：用</span>' + bg.tag("灵敏度分析") +
    '<span leaf="">考察参数波动的容许范围。</span>']))
parts.append(para(
    '<span leaf="">回到第五课的思路，无论模型多复杂，起点永远是那三要素：</span>'
    + bg.u("要决定什么、要优化什么、被什么限制") +
    '<span leaf="">。线性规划之所以值得先学，是因为它把这三点讲成了最干净的形式——'
    '而在数学建模比赛中，它既是能拿分的保底模型，也是理解更复杂优化模型'
    '（整数规划、非线性规划、多目标优化）的第一块基石。</span>'))

parts.append(bg.sign_block())

html = "".join(parts)
io.open(os.path.join(BASE, "公众号排版.html"), "w", encoding="utf-8").write(html)
print("written", len(html), "chars")
