# -*- coding: utf-8 -*-
"""KaTeX -> HTML (node) -> headless Chrome screenshot on magenta key -> transparent PNG.

Same pipeline as the previous project (考研数学三个反直觉知识点), adapted: the
formulas here are long aligned display blocks, so we screenshot at a wide window
and tighten the crop afterwards.
"""
import base64, json, os, re, subprocess

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "assets", "formulas")
RAW = os.path.join(BASE, "assets", "formulas_raw")
os.makedirs(OUT, exist_ok=True)
os.makedirs(RAW, exist_ok=True)

KATEX = os.path.join(BASE, "node_modules", "katex")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# id -> (latex, display_mode)
FORMULAS = [
    # 引言：线性规划通用格式
    ("f_lp_general", r"\begin{aligned}\max \text{ 或 } \min \quad & \text{目标函数}=c_1x_1+\cdots+c_nx_n \\ \text{s.t.} \quad & \text{一组线性等式或不等式约束}\end{aligned}", 1),
    # 例 1 模型
    ("f_ex1_model", r"\begin{aligned}\max \quad & Z = 50x_1 + 40x_2 \\ \text{s.t.} \quad & 2x_1 + x_2 \le 60 \\ & 2x_1 + 4x_2 \le 120 \\ & x_1 \ge 0,\quad x_2 \ge 0\end{aligned}", 1),
    # 可行域两条直线
    ("f_ex1_lines", r"2x_1 + x_2 = 60,\qquad 2x_1 + 4x_2 = 120", 1),
    # 三个顶点
    ("f_ex1_vertex", r"A(0,30),\qquad B(20,20),\qquad C(30,0)", 1),
    # 顶点代入
    ("f_ex1_eval", r"\begin{aligned}Z_A &= 50\times 0 + 40\times 30 = 1200 \\ Z_B &= 50\times 20 + 40\times 20 = 1800 \\ Z_C &= 50\times 30 + 40\times 0 = 1500\end{aligned}", 1),
    # 标准形
    ("f_standard", r"\begin{aligned}\max \quad & Z = \boldsymbol{c}^{\mathrm T}\boldsymbol{x} \\ \text{s.t.} \quad & A\boldsymbol{x} \le \boldsymbol{b} \\ & \boldsymbol{x} \ge \boldsymbol{0}\end{aligned}", 1),
    # 松弛变量
    ("f_slack", r"\begin{aligned}2x_1 + x_2 + s_1 &= 60 \\ 2x_1 + 4x_2 + s_2 &= 120\end{aligned}", 1),
    # 单纯形表
    ("f_tableau", r"\begin{array}{c|ccccc|c} & x_1 & x_2 & s_1 & s_2 & & b \\ \hline s_1 & 2 & 1 & 1 & 0 & & 60 \\ s_2 & 2 & 4 & 0 & 1 & & 120 \\ \hline & -50 & -40 & 0 & 0 & & 0 \end{array}", 1),
    # 第一次迭代
    ("f_iter1", r"\begin{aligned}x_1 &: \tfrac{60}{2} = 30, \qquad \tfrac{120}{2} = 60 \;\Rightarrow\; 30 \\ x_2 &: \tfrac{60}{1} = 60, \qquad \tfrac{120}{4} = 30 \;\Rightarrow\; 30\end{aligned}", 1),
    # 最优解
    ("f_optimal", r"x_1^* = 20,\qquad x_2^* = 20,\qquad Z^* = 1800", 1),
    # 斜率比较
    ("f_slope", r"-\frac{c_1}{c_2} = -\frac{5}{4},\qquad -2 < -\frac{5}{4} < -\frac{1}{2}", 1),
    # 敏感性
    ("f_sens", r"k < \frac{5}{2}", 1),
    # 对偶
    ("f_dual", r"\begin{aligned}\min \quad & W = \boldsymbol{b}^{\mathrm T}\boldsymbol{y} \\ \text{s.t.} \quad & A^{\mathrm T}\boldsymbol{y} \ge \boldsymbol{c} \\ & \boldsymbol{y} \ge \boldsymbol{0}\end{aligned}", 1),
]

with open(os.path.join(KATEX, "dist", "katex.min.css"), encoding="utf-8") as f:
    katex_css = f.read()

fonts_dir = os.path.join(KATEX, "dist", "fonts")


def inline_fonts(css):
    def repl(m):
        url = m.group(1)
        name = url.split("/")[-1].split("?")[0].split("#")[0]
        path = os.path.join(fonts_dir, name)
        if not os.path.exists(path):
            return m.group(0)
        ext = name.split(".")[-1]
        mime = {"woff2": "font/woff2", "woff": "font/woff", "ttf": "font/ttf"}.get(
            ext, "application/octet-stream")
        with open(path, "rb") as fh:
            b64 = base64.b64encode(fh.read()).decode()
        return "url(data:%s;base64,%s)" % (mime, b64)
    return re.sub(r"url\(([^)]+)\)", repl, css)


katex_css = inline_fonts(katex_css)

node_render = os.path.join(BASE, "_render_katex.js")
with open(node_render, "w", encoding="utf-8") as f:
    f.write('''
const katex = require("katex");
const fs = require("fs");
const data = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
const out = data.map(item => ({
  id: item.id,
  html: katex.renderToString(item.latex, {
    displayMode: !!item.display, throwOnError: true,
    output: "html", strict: false
  })
}));
fs.writeFileSync(process.argv[3], JSON.stringify(out), "utf8");
''')

data = [{"id": i, "latex": lx, "display": dm} for i, lx, dm in FORMULAS]
din = os.path.join(BASE, "_formulas_in.json")
dout = os.path.join(BASE, "_formulas_out.json")
with open(din, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)

subprocess.run(["node", node_render, din, dout], check=True, cwd=BASE)
rendered = json.load(open(dout, encoding="utf-8"))

COLOR = "#1F2937"

for item in rendered:
    fid, html = item["id"], item["html"]
    doc = (
        '<!DOCTYPE html><html><head><meta charset="utf-8">'
        '<style>'
        + katex_css +
        'html,body{margin:0;padding:0;background:#FF00FF;}'
        '#wrap{display:inline-block;padding:20px 30px;background:#FF00FF;}'
        '.katex{color:' + COLOR + ';font-size:36px;}'
        '</style></head><body><div id="wrap">' + html + '</div></body></html>'
    )
    hpath = os.path.join(BASE, "_f_" + fid + ".html")
    with open(hpath, "w", encoding="utf-8") as f:
        f.write(doc)

    png = os.path.join(RAW, fid + ".png")
    cmd = [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
           "--force-device-scale-factor=3",
           "--window-size=2400,1200",
           "--screenshot=" + png, "file:///" + hpath.replace("\\", "/")]
    subprocess.run(cmd, check=True, cwd=BASE)
    print("rendered", fid, os.path.getsize(png) if os.path.exists(png) else "MISSING")

print("done")
