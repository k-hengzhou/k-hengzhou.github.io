# -*- coding: utf-8 -*-
"""Build the WeChat-ready HTML for 数学建模第9课 线性规划.

Reads 正文.md, applies the red-white theme (theme-red-white.md) component
templates, assigns chapter numbers, underlines keywords per paragraph,
then inlines the KaTeX-rendered formula PNGs from assets/formulas/.

Output: 公众号排版.html  (pure <section> fragment)
"""
import base64, io, os, re, sys

BASE = os.path.dirname(os.path.abspath(__file__))
FDIR = os.path.join(BASE, "assets", "formulas")
MD = os.path.join(BASE, "正文.md")
OUT = os.path.join(BASE, "公众号排版.html")

# ---------------------------------------------------------------- theme vars
RED = "#DC2626"
RED_SOFT = "#FEF2F2"
RED_BORDER = "#FEE2E2"
INK = "#1C1917"
BODY = "#374151"
GREY = "#6B7280"
DIVIDER = "#F3F4F6"


def uri(name):
    p = os.path.join(FDIR, name + ".png")
    if not os.path.exists(p):
        raise SystemExit("missing formula png: " + p)
    with open(p, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode()


def chip(name, h=40):
    """inline formula chip — height in px (rendered at 3x, so ~13px display)"""
    return ('<img src="' + uri(name) + '" style="height:' + str(h) +
            'px;width:auto;vertical-align:-10px;display:inline-block;margin:0 2px;">')


def block(name):
    """centered display formula card"""
    return ('<section style="text-align:center;margin:16px 0 20px;padding:14px 10px;'
            'background:' + RED_SOFT + ';border-radius:10px;border:1px solid ' + RED_BORDER + ';">'
            '<img src="' + uri(name) + '" style="max-width:100%;height:auto;display:block;margin:0 auto;">'
            '</section>')


# ---------------------------------------------------------------- components
def p(text, **kw):
    """plain body paragraph; text already contains inline html"""
    return ('<p style="font-size:15px;color:' + BODY +
            ';margin:0 0 18px;line-height:1.9;letter-spacing:0.2px;">' + text + '</p>')


def u(text):
    """underline marker (component 7d 淡粉下划线)"""
    return ('<span style="background:linear-gradient(to top,' + RED_SOFT +
            ' 45%,transparent 45%);font-weight:600;color:' + INK + ';">'
            '<span leaf="">' + text + '</span></span>')


def tag(text):
    """red keyword tag (component 7b)"""
    return ('<span style="background:' + RED_SOFT + ';color:' + RED +
            ';padding:1px 7px;border-radius:4px;font-size:14px;font-weight:700;">'
            '<span leaf="">' + text + '</span></span>')


def strong(text):
    return '<strong style="color:' + RED + ';"><span leaf="">' + text + '</span></strong>'


def h2(num, cn, en):
    return ('<section style="margin:40px 0 22px;">'
            '<p style="font-size:13px;color:' + RED + ';font-weight:800;letter-spacing:2px;'
            'margin:0 0 6px;text-transform:uppercase;"><span leaf="">' + en + '</span></p>'
            '<section style="display:flex;align-items:center;">'
            '<span style="font-size:26px;color:' + RED + ';font-weight:900;font-style:italic;'
            'margin-right:10px;line-height:1;"><span leaf="">' + num + '</span></span>'
            '<p style="font-size:20px;color:' + INK + ';font-weight:800;margin:0;line-height:1.4;">'
            '<span leaf="">' + cn + '</span></p></section>'
            '<section style="height:3px;width:44px;background:' + RED +
            ';border-radius:2px;margin-top:10px;"><span leaf=""><br></span></section>'
            '</section>')


def quote(lines):
    body = "".join(
        '<p style="font-size:15px;color:' + BODY + ';margin:0 0 10px;line-height:1.9;">' + l + '</p>'
        for l in lines[:-1])
    body += '<p style="font-size:15px;color:' + BODY + ';margin:0;line-height:1.9;">' + lines[-1] + '</p>'
    return ('<section style="background:' + RED_SOFT + ';border-left:4px solid ' + RED +
            ';border-radius:0 8px 8px 0;padding:16px 18px;margin:0 0 22px;">' + body + '</section>')


def callout(title, text):
    return ('<section style="background:#FFFBEB;border:1px solid #FDE68A;border-radius:10px;'
            'padding:14px 16px;margin:0 0 22px;">'
            '<p style="font-size:14px;font-weight:800;color:#B45309;margin:0 0 6px;">'
            '<span leaf="">💡 ' + title + '</span></p>'
            '<p style="font-size:14px;color:#78350F;margin:0;line-height:1.85;">' + text + '</p></section>')


def ol(items):
    out = []
    for i, it in enumerate(items, 1):
        out.append(
            '<section style="display:flex;align-items:flex-start;gap:10px;margin-bottom:12px;">'
            '<span style="display:inline-flex;align-items:center;justify-content:center;width:22px;'
            'height:22px;background:' + RED + ';color:#fff;font-size:12px;font-weight:700;'
            'border-radius:50%;flex-shrink:0;margin-top:3px;"><span leaf="">' + str(i) + '</span></span>'
            '<p style="font-size:15px;color:' + BODY + ';margin:0;line-height:1.85;flex:1;">' + it + '</p>'
            '</section>')
    return '<section style="margin-bottom:22px;">' + "".join(out) + '</section>'


def ul(items):
    out = []
    for it in items:
        out.append(
            '<section style="display:flex;align-items:flex-start;gap:10px;margin-bottom:10px;">'
            '<span style="color:' + RED + ';font-size:16px;line-height:1.7;flex-shrink:0;">'
            '<span leaf="">●</span></span>'
            '<p style="font-size:15px;color:' + BODY + ';margin:0;line-height:1.85;flex:1;">' + it + '</p>'
            '</section>')
    return '<section style="margin-bottom:22px;">' + "".join(out) + '</section>'


def formula(name):
    return block(name)


def divider():
    return ('<section style="height:2px;width:100%;margin:30px 0;'
            'background:linear-gradient(90deg,transparent,' + RED + ',transparent);opacity:0.5;">'
            '<span leaf=""><br></span></section>')


def intro_card(kicker, title, sub):
    return ('<section style="margin:10px 10px 32px;background:#fff;border-radius:12px;'
            'box-shadow:0 4px 24px -4px rgba(220,38,38,0.15);padding:28px 24px 22px;overflow:hidden;">'
            '<p style="font-size:42px;color:' + RED + ';font-weight:900;margin:0;line-height:0.6;">'
            '<span leaf="">“</span></p>'
            '<p style="font-size:16px;font-weight:800;color:' + INK + ';margin:12px 0 8px;'
            'line-height:1.75;padding-left:4px;"><span leaf="">' + title + '</span></p>'
            '<p style="font-size:14px;color:' + GREY + ';margin:0;line-height:1.8;padding-left:4px;">'
            '<span leaf="">' + sub + '</span></p>'
            '<section style="height:1px;background:' + DIVIDER + ';margin:16px 0 12px;">'
            '<span leaf=""><br></span></section>'
            '<p style="font-size:13px;color:' + RED + ';font-weight:700;margin:0;padding-left:4px;">'
            '<span leaf="">' + kicker + '</span></p></section>')


def sign_block():
    return ('<section style="margin:36px 0 10px;padding:22px 20px;background:' + RED_SOFT +
            ';border-radius:12px;">'
            '<p style="font-size:14px;color:' + BODY + ';margin:0 0 8px;line-height:1.9;">'
            '<span leaf="">我是 </span>'
            '<span style="color:' + RED + ';font-weight:800;"><span leaf="">{{作者名}}</span></span>'
            '<span leaf="">，{{一句话简介，如：热衷于把数学讲得有意思}}。</span></p>'
            '<p style="font-size:14px;color:' + BODY + ';margin:0;line-height:1.9;">'
            '<span leaf="">如果你觉得今天这篇有收获，欢迎</span>'
            '<strong style="color:' + RED + ';"><span leaf="">点赞、在看、转发</span></strong>'
            '<span leaf="">三连，我们下篇见。</span></p></section>'
            '<p style="text-align:center;font-size:12px;color:' + GREY + ';margin:18px 0 0;'
            'letter-spacing:3px;"><span leaf="">— END —</span></p>')


def _leafify(cell):
    cell = cell.strip()
    if cell.startswith("<"):
        return cell
    return '<span leaf="">' + cell + '</span>'


def table(headers, rows, highlight=None):
    """theme component 12 — data table."""
    highlight = highlight or set()
    th = "".join(
        '<th style="padding:9px 10px;font-size:13px;color:#fff;background:' + RED +
        ';font-weight:700;text-align:center;"><span leaf="">' + c + '</span></th>'
        for c in headers)
    trs = []
    for ri, row in enumerate(rows):
        tds = []
        for ci, c in enumerate(row):
            bg = RED_SOFT if (ri, ci) in highlight else ("#fff" if ri % 2 == 0 else "#FAFAFA")
            fw = "700" if (ri, ci) in highlight else "400"
            col = RED if (ri, ci) in highlight else BODY
            tds.append('<td style="padding:9px 10px;font-size:13px;color:' + col +
                       ';background:' + bg + ';font-weight:' + fw + ';text-align:center;'
                       'border-bottom:1px solid ' + DIVIDER + ';">' + _leafify(c) + '</td>')
        trs.append('<tr>' + "".join(tds) + '</tr>')
    return ('<section style="margin:0 0 24px;overflow:hidden;border-radius:10px;'
            'border:1px solid ' + DIVIDER + ';">'
            '<table style="width:100%;border-collapse:collapse;">'
            '<thead><tr>' + th + '</tr></thead><tbody>' + "".join(trs) + '</tbody>'
            '</table></section>')


def anim(src, caption):
    """inline animation block: GIF as data URI + caption (component 14 图片/GIF)."""
    import base64 as _b64
    p = os.path.join(BASE, "assets", "fig-src", src)
    with open(p, "rb") as f:
        data = _b64.b64encode(f.read()).decode()
    return ('<section style="margin:20px 0 24px;">'
            '<section style="border-radius:12px;overflow:hidden;border:1px solid ' + RED_BORDER +
            ';background:#fff;">'
            '<img src="data:image/gif;base64,' + data + '" alt="线性规划图解法动态演示" '
            'style="max-width:100%;height:auto;display:block;margin:0 auto;">'
            '</section>'
            '<p style="font-size:13px;color:' + GREY + ';text-align:center;margin:10px 0 0;'
            'line-height:1.7;"><span leaf="">' + caption + '</span></p></section>')


def figure(name, alt, caption):
    """static diagram from assets/formulas/<name>.<ext> + caption."""
    stem, ext = name.rsplit(".", 1)
    mime = "image/gif" if ext == "gif" else "image/png"
    p = os.path.join(BASE, "assets", "formulas", name)
    with open(p, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    return ('<section style="margin:20px 0 24px;">'
            '<img src="data:' + mime + ';base64,' + data + '" alt="' + alt + '" '
            'style="max-width:100%;height:auto;display:block;margin:0 auto;'
            'border:1px solid ' + RED_BORDER + ';border-radius:10px;">'
            '<p style="font-size:13px;color:' + GREY + ';text-align:center;margin:10px 0 0;'
            'line-height:1.7;"><span leaf="">' + caption + '</span></p></section>')


def h3_(text):
    """sub-heading (component: 左竖条小标题 3a)"""
    return ('<section style="display:flex;align-items:center;margin:26px 0 14px;">'
            '<span style="width:4px;height:18px;background:' + RED +
            ';border-radius:2px;margin-right:10px;flex-shrink:0;">'
            '<span leaf=""><br></span></span>'
            '<p style="font-size:16px;font-weight:800;color:' + INK + ';margin:0;">'
            '<span leaf="">' + text + '</span></p></section>')
