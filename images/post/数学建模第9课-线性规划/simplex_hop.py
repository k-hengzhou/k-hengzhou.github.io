# -*- coding: utf-8 -*-
"""Static diagram: simplex method hopping between feasible-region vertices.

One wide figure, two panels:
  ① 从一个顶点出发（x₁=x₂=0，什么都不生产），检验数为负 → 有改进空间
  ② 沿棱走到相邻的更优顶点，Z 从 0 → 1200 → 1800，直到检验数非负，停下

Output: assets/formulas/lp_simplex_hop.png
"""
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Polygon, FancyArrowPatch

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
RED_SOFT = "#FEF2F2"
INK = "#1C1917"
BODY = "#374151"
GREY = "#9CA3AF"
BLUE = "#2563EB"
GREEN = "#059669"

VERT = [(0, 0), (0, 30), (20, 20), (30, 0)]
ZVAL = {"O": 0, "A": 1200, "B": 1800, "C": 1500}


def styles(ax):
    ax.set_xlim(-3, 38)
    ax.set_ylim(-3, 36)
    ax.set_xticks(range(0, 36, 10))
    ax.set_yticks(range(0, 36, 10))
    ax.tick_params(labelsize=11, colors=BODY)
    for s in ax.spines.values():
        s.set_color("#E5E7EB")
    ax.grid(True, color="#F3F4F6", linewidth=1)
    ax.set_axisbelow(True)
    ax.set_xlabel("x₁", fontsize=12, color=BODY)
    ax.set_ylabel("x₂", fontsize=12, color=BODY)


plt.rcParams["font.size"] = 11
fig, axes = plt.subplots(1, 2, figsize=(13.0, 5.2), dpi=200)
fig.patch.set_facecolor("#FFFFFF")
xs = np.linspace(0, 30, 60)

for ax in axes:
    styles(ax)
    ax.add_patch(Polygon(VERT, closed=True, facecolor=RED, alpha=0.14,
                         edgecolor=RED, linewidth=2, zorder=2))
    ax.plot(xs, 60 - 2 * xs, color=BLUE, lw=1.3, alpha=0.45, zorder=1)
    ax.plot(xs, (120 - 2 * xs) / 4, color=GREEN, lw=1.3, alpha=0.45, zorder=1)

# ── ① start vertex, first hop ──────────────────────────────────────────────
ax = axes[0]
ax.plot([0], [0], "o", color=RED, ms=11, zorder=8)
ax.annotate("起点 O(0,0)\nZ = 0，什么也不生产", (0, 0), textcoords="offset points",
            xytext=(14, 6), fontsize=12, color=RED, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.35", fc=RED_SOFT, ec=RED, lw=1.3),
            zorder=9)
ax.plot([30], [0], "o", color=GREY, ms=7, zorder=6)
ax.annotate("C(30,0)", (30, 0), textcoords="offset points", xytext=(-4, 10),
            fontsize=11, color=GREY, fontweight="bold", ha="right")
ax.plot([20], [20], "o", color=RED, ms=9, zorder=8)
ax.annotate("B(20,20)\nZ = 1800", (20, 20), textcoords="offset points",
            xytext=(10, 8), fontsize=12, color=RED, fontweight="bold")
ax.add_patch(FancyArrowPatch((2, 1.2), (18, 18), arrowstyle="-|>",
                             mutation_scale=20, color=RED, lw=2.6,
                             connectionstyle="arc3,rad=0.12", zorder=7))
ax.text(4.5, 12.5, "沿棱走到\n相邻更优顶点", color=RED, fontsize=11,
        fontweight="bold", rotation=45)
ax.set_title("①  从顶点出发，沿棱「贪心」跳跃", fontsize=13.5, color=INK,
             fontweight="bold", pad=10)

# ── ② Z climbs along the path, stop at optimum ─────────────────────────────
ax = axes[1]
path = [(0, 0), (20, 20)]
ax.plot([p[0] for p in path], [p[1] for p in path], "--", color=RED, lw=2.2,
        zorder=7)
for (px, py), lbl in [((0, 0), "O  0"), ((20, 20), "B  1800")]:
    ax.plot([px], [py], "o", color=RED, ms=10, zorder=8)
    ax.annotate(lbl, (px, py), textcoords="offset points", xytext=(9, 9),
                fontsize=12, color=RED, fontweight="bold")
ax.plot([30], [0], "o", color=GREY, ms=7, zorder=6)
ax.annotate("C  1500", (30, 0), textcoords="offset points", xytext=(-4, 10),
            fontsize=11, color=GREY, fontweight="bold", ha="right")
ax.plot([0], [30], "o", color=GREY, ms=7, zorder=6)
ax.annotate("A  1200", (0, 30), textcoords="offset points", xytext=(10, -4),
            fontsize=11, color=GREY, fontweight="bold")
# plateau marker at B
ax.annotate("检验数不再为负\n→ 停，这就是最优解", (20, 20),
            textcoords="offset points", xytext=(16, -46), fontsize=12,
            color=INK, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.38", fc="#F0FDF4", ec=GREEN, lw=1.4),
            zorder=10)
ax.set_title("②  Z 一路上升，走不动即最优", fontsize=13.5, color=INK,
             fontweight="bold", pad=10)

fig.suptitle("单纯形法：在可行域的顶点之间跳跃", fontsize=17, fontweight="bold",
             color=INK, y=0.99)
fig.tight_layout(rect=[0, 0, 1, 0.93])
out = FDIR / "lp_simplex_hop.png"
fig.savefig(out, dpi=200, facecolor="#FFFFFF", bbox_inches="tight")
print("saved", out, out.stat().st_size // 1024, "KB")
