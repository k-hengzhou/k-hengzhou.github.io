# -*- coding: utf-8 -*-
"""Animated demo of the graphical (graphic) solution to the LP model.

Two panels:
  left  — the feasible region and the two constraint lines being drawn in
  right — full view with the objective line Z = 50x1 + 40x2 sweeping outward
          until it touches the optimal vertex B(20,20)

Output: assets/fig-src/lp_graphic_demo.gif  (then copied to assets/formulas/ as mp4/gif)
"""
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Polygon
from PIL import Image

BASE = Path(__file__).resolve().parent
SRC = BASE / "assets" / "fig-src"
SRC.mkdir(parents=True, exist_ok=True)

# ── Chinese font ────────────────────────────────────────────────────────────
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

# ── model ───────────────────────────────────────────────────────────────────
# max Z = 50 x1 + 40 x2
# s.t. 2x1 + x2 <= 60 ; 2x1 + 4x2 <= 120 ; x1,x2 >= 0
C = (50.0, 40.0)
VERT = [(0, 0), (0, 30), (20, 20), (30, 0)]
ZOPT = 1800.0

W, H = 1280, 640
FPS = 12
HOLD = int(FPS * 1.6)


def zval(x1, x2):
    return C[0] * x1 + C[1] * x2


def draw_base(ax, show_region, region_alpha=1.0, labels=True):
    ax.set_xlim(-3, 38)
    ax.set_ylim(-3, 36)
    ax.set_xticks(range(0, 36, 5))
    ax.set_yticks(range(0, 36, 5))
    ax.tick_params(labelsize=11, colors=BODY)
    for s in ax.spines.values():
        s.set_color("#E5E7EB")
    ax.grid(True, color="#F3F4F6", linewidth=1)
    ax.set_axisbelow(True)
    ax.set_xlabel("x₁（甲产品日产量）", fontsize=13, color=BODY)
    ax.set_ylabel("x₂（乙产品日产量）", fontsize=13, color=BODY)
    if show_region:
        poly = Polygon(VERT, closed=True, facecolor=RED, alpha=region_alpha * 0.16,
                       edgecolor=RED, linewidth=2, zorder=3)
        ax.add_patch(poly)
        if labels:
            for (px, py), nm in zip(VERT[1:], ["A(0,30)", "B(20,20)", "C(30,0)"]):
                ax.plot([px], [py], "o", color=RED, ms=7, zorder=6)
                ax.annotate(nm, (px, py), textcoords="offset points",
                            xytext=(7, 7), fontsize=13, color=RED, fontweight="bold")


def frame(fi, total):
    """three phases: draw constraints -> fade in region -> sweep objective."""
    p1 = total * 0.30          # constraint lines drawn
    p2 = total * 0.48          # region faded in
    p3 = total * 0.92          # objective sweep done

    fig, (axL, axR) = plt.subplots(1, 2, figsize=(W / 100, H / 100), dpi=100)
    fig.patch.set_facecolor("#FFFFFF")

    # ---------- LEFT: constraint drawing ----------
    draw_base(axL, show_region=False)
    axL.set_title("① 画出约束，围出可行域", fontsize=15, color=INK,
                  fontweight="bold", pad=12)
    if fi <= p1:
        t = fi / max(1, p1)
        # line 1: 2x1 + x2 = 60
        if t > 0:
            s = min(1.0, t / 0.5)
            xs = np.linspace(0, 30 * s, 60)
            axL.plot(xs, 60 - 2 * xs, color=BLUE, lw=2.4, zorder=5)
            axL.text(24 * s, (60 - 2 * 24 * s) + 1.2, "2x₁+x₂=60",
                     color=BLUE, fontsize=12, fontweight="bold", alpha=min(1, s * 1.4))
        # line 2: 2x1 + 4x2 = 120
        if t > 0.5:
            s = min(1.0, (t - 0.5) / 0.5)
            xs = np.linspace(0, 30 * s, 60)
            axL.plot(xs, (120 - 2 * xs) / 4, color=GREEN, lw=2.4, zorder=5)
            axL.text(11 * s, (120 - 2 * 11 * s) / 4 + 1.2, "2x₁+4x₂=120",
                     color=GREEN, fontsize=12, fontweight="bold", alpha=min(1, s * 1.4))
        axL.text(0.03, 0.94, "非负约束：x₁≥0, x₂≥0", transform=axL.transAxes,
                 fontsize=12, color=GREY)
    else:
        # lines fully drawn
        xs = np.linspace(0, 30, 60)
        axL.plot(xs, 60 - 2 * xs, color=BLUE, lw=2.4, zorder=5)
        axL.plot(xs, (120 - 2 * xs) / 4, color=GREEN, lw=2.4, zorder=5)
        axL.text(24, 60 - 48 + 1.2, "2x₁+x₂=60", color=BLUE, fontsize=12, fontweight="bold")
        axL.text(11, (120 - 22) / 4 + 1.2, "2x₁+4x₂=120", color=GREEN, fontsize=12, fontweight="bold")
        if fi > p2:
            t = min(1.0, (fi - p2) / max(1, (total * 0.08)))
            draw_region_only(axL, t)
            axL.text(0.03, 0.90, "可行域是凸多边形（四边形）", transform=axL.transAxes,
                     fontsize=13, color=RED, fontweight="bold")
        else:
            axL.text(0.03, 0.90, "两条直线与坐标轴围出公共区域", transform=axL.transAxes,
                     fontsize=13, color=BODY)

    # ---------- RIGHT: objective sweep ----------
    draw_base(axR, show_region=True, region_alpha=min(1.0, max(0, (fi - p2) / max(1, total * 0.05))))
    axR.set_title("② 目标函数等值线向外平移，碰到的最后顶点即最优解", fontsize=15,
                  color=INK, fontweight="bold", pad=12)
    if fi > p2:
        t = min(1.0, (fi - p2) / max(1, p3 - p2))
        t = 1 - (1 - t) ** 2  # ease-out
        # Z from a small value up past ZOPT so the line visibly reaches B
        Z = ZOPT * (0.15 + 0.85 * t) * 1.02
        # line 50x1+40x2=Z  ->  x2 = (Z-50x1)/40
        xs = np.linspace(0, 40, 60)
        ys = (Z - 50 * xs) / 40
        axR.plot(xs, ys, color=RED, lw=2.4, ls="--", zorder=6)
        # intercept label
        yint = Z / 40
        axR.plot([0], [yint], "o", color=RED, ms=6, zorder=7)
        axR.text(0.6, min(yint, 34) + 0.6, f"Z={int(Z)}", color=RED, fontsize=13,
                 fontweight="bold", zorder=8)
        # current best vertex marker
        if t >= 0.985:
            axR.plot([20], [20], "*", color=RED, ms=26, zorder=9)
            axR.annotate("最优解 B(20,20)\nZ=1800", (20, 20), textcoords="offset points",
                         xytext=(12, -34), fontsize=14, color=RED, fontweight="bold",
                         bbox=dict(boxstyle="round,pad=0.35", fc="#FEF2F2",
                                   ec=RED, lw=1.2), zorder=10)
    else:
        axR.text(0.5, 0.5, "等待可行域…", transform=axR.transAxes, ha="center",
                 fontsize=15, color=GREY)

    fig.suptitle("线性规划图解法：Z = 50x₁ + 40x₂ 的最大化", fontsize=19,
                 fontweight="bold", color=INK, y=0.975)
    fig.tight_layout(rect=[0, 0, 1, 0.94])

    fig.canvas.draw()
    w, h = fig.canvas.get_width_height()
    img = Image.frombytes("RGBA", (w, h), bytes(fig.canvas.buffer_rgba())).convert("RGB")
    plt.close(fig)
    return img


def draw_region_only(ax, t):
    verts = VERT
    poly = Polygon(verts, closed=True, facecolor=RED, alpha=0.16 * min(1, t * 1.5),
                   edgecolor=RED, linewidth=2, zorder=3)
    ax.add_patch(poly)
    if t > 0.5:
        for (px, py), nm in zip(verts[1:], ["A(0,30)", "B(20,20)", "C(30,0)"]):
            ax.plot([px], [py], "o", color=RED, ms=7, zorder=6)
            ax.annotate(nm, (px, py), textcoords="offset points", xytext=(7, 7),
                        fontsize=13, color=RED, fontweight="bold")


def main():
    total = 150
    frames = [frame(fi, total) for fi in range(total)]
    frames = frames + [frames[-1]] * HOLD
    gif = SRC / "lp_graphic_demo.gif"
    pal = [f.convert("P", palette=Image.ADAPTIVE, colors=128) for f in frames]
    pal[0].save(gif, save_all=True, append_images=pal[1:],
                duration=int(1000 / FPS), loop=0, optimize=True, disposal=2)
    print("GIF:", gif, gif.stat().st_size // 1024, "KB", len(frames), "frames",
          frames[0].size)


if __name__ == "__main__":
    main()
