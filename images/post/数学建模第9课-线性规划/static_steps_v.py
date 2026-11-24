# -*- coding: utf-8 -*-
"""Vertical single-column version of the three-step graphical solution.

Three stacked panels (phone-friendly, large fonts):
  ① 画出约束，围出可行域
  ② 等值线向外平移
  ③ 卡在顶点 B(20,20)，Z=1800

Output: assets/formulas/lp_graphic_steps_v.png
"""
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Polygon

BASE = Path(__file__).resolve().parent
FDIR = BASE / "assets" / "formulas"
FDIR.mkdir(parents=True, exist_ok=True)

for fp in ["C:/Windows/Fonts/msyh.ttc", "C:/Windows/Fonts/msyhbd.ttc",
           "C:/Windows/Fonts/simhei.ttf"]:
    if Path(fp).is_file():
        try:
            font_manager.fontManager.addfont(fp)
        except Exception:
            pass
plt.rcParams["font.sans-serif"] = ["Microsoft YaHei", "SimHei", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

RED = "#DC2626"
INK = "#1C1917"
BODY = "#374151"
GREY = "#9CA3AF"
BLUE = "#2563EB"
GREEN = "#059669"

VERT = [(0, 0), (0, 30), (20, 20), (30, 0)]


def styles(ax):
    ax.set_xlim(-3, 38)
    ax.set_ylim(-3, 36)
    ax.set_xticks(range(0, 36, 10))
    ax.set_yticks(range(0, 36, 10))
    ax.tick_params(labelsize=15, colors=BODY)
    for s in ax.spines.values():
        s.set_color("#E5E7EB")
    ax.grid(True, color="#F3F4F6", linewidth=1)
    ax.set_axisbelow(True)
    ax.set_xlabel("x₁", fontsize=17, color=BODY)
    ax.set_ylabel("x₂", fontsize=17, color=BODY)
    ax.set_aspect("equal")


plt.rcParams["font.size"] = 16
fig, axes = plt.subplots(3, 1, figsize=(6.2, 16.2), dpi=200)
fig.patch.set_facecolor("#FFFFFF")

xs = np.linspace(0, 30, 60)

# ── ① constraints only ─────────────────────────────────────────────────────
ax = axes[0]
styles(ax)
ax.plot(xs, 60 - 2 * xs, color=BLUE, lw=3.0)
ax.plot(xs, (120 - 2 * xs) / 4, color=GREEN, lw=3.0)
ax.text(15.5, 60 - 31 + 1.2, "2x₁+x₂=60", color=BLUE, fontsize=16, fontweight="bold")
ax.text(5.5, (120 - 11) / 4 + 1.2, "2x₁+4x₂=120", color=GREEN, fontsize=16,
        fontweight="bold")
ax.text(0.03, 0.93, "非负约束：x₁≥0, x₂≥0", transform=ax.transAxes, fontsize=14,
        color=GREY)
ax.set_title("①  画出约束，围出可行域", fontsize=19, color=INK,
             fontweight="bold", pad=12)

# ── ② region + objective line family ───────────────────────────────────────
ax = axes[1]
styles(ax)
ax.add_patch(Polygon(VERT, closed=True, facecolor=RED, alpha=0.16,
                     edgecolor=RED, linewidth=3, zorder=3))
ax.plot(xs, 60 - 2 * xs, color=BLUE, lw=2.0, alpha=0.55)
ax.plot(xs, (120 - 2 * xs) / 4, color=GREEN, lw=2.0, alpha=0.55)
for (px, py), nm in zip(VERT[1:], ["A(0,30)", "B(20,20)", "C(30,0)"]):
    ax.plot([px], [py], "o", color=RED, ms=9, zorder=6)
    ax.annotate(nm, (px, py), textcoords="offset points", xytext=(7, 7),
                fontsize=16, color=RED, fontweight="bold")
for Z, al in [(600, 0.35), (1200, 0.6), (1800, 1.0)]:
    ys = (Z - 50 * xs) / 40
    ax.plot(xs, ys, color=RED, lw=2.8, ls="--", alpha=al, zorder=5)
ax.text(0.6, 34.3, "Z 增大 ↗", color=RED, fontsize=16, fontweight="bold")
ax.set_title("②  等值线向外平移", fontsize=19, color=INK,
             fontweight="bold", pad=12)

# ── ③ optimal vertex ───────────────────────────────────────────────────────
ax = axes[2]
styles(ax)
ax.add_patch(Polygon(VERT, closed=True, facecolor=RED, alpha=0.16,
                     edgecolor=RED, linewidth=3, zorder=3))
ax.plot(xs, 60 - 2 * xs, color=BLUE, lw=2.0, alpha=0.55)
ax.plot(xs, (120 - 2 * xs) / 4, color=GREEN, lw=2.0, alpha=0.55)
for (px, py), nm in zip(VERT[1:], ["A(0,30)", "C(30,0)"]):
    ax.plot([px], [py], "o", color=GREY, ms=7, zorder=6)
    ax.annotate(nm, (px, py), textcoords="offset points", xytext=(7, 7),
                fontsize=15, color=GREY, fontweight="bold")
ys = (1800 - 50 * xs) / 40
ax.plot(xs, ys, color=RED, lw=3.2, ls="--", zorder=6)
ax.plot([20], [20], "*", color=RED, ms=34, zorder=9)
ax.annotate("最优解 B(20,20)\nZ = 1800", (20, 20), textcoords="offset points",
            xytext=(12, -52), fontsize=17, color=RED, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.4", fc="#FEF2F2", ec=RED, lw=1.6),
            zorder=10)
ax.set_title("③  卡在顶点，读出最优解", fontsize=19, color=INK,
             fontweight="bold", pad=12)

fig.suptitle("线性规划图解法：Z = 50x₁ + 40x₂ 的最大化", fontsize=22,
             fontweight="bold", color=INK, y=0.995)
fig.tight_layout(rect=[0, 0, 1, 0.972], h_pad=3.0)
out = FDIR / "lp_graphic_steps_v.png"
fig.savefig(out, dpi=200, facecolor="#FFFFFF", bbox_inches="tight")
print("saved", out, out.stat().st_size // 1024, "KB")
