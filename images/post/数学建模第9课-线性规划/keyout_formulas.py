# -*- coding: utf-8 -*-
"""Chroma-key the magenta-background KaTeX screenshots into transparent PNGs."""
from PIL import Image
import glob, os

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, "assets", "formulas_raw")
DST = os.path.join(BASE, "assets", "formulas")
os.makedirs(DST, exist_ok=True)

KEY = (255, 0, 255)


def key_out(im):
    im = im.convert("RGBA")
    w, h = im.size
    px = im.load()
    out = Image.new("RGBA", (w, h))
    op = out.load()
    for y in range(h):
        for x in range(w):
            r, g, b, a = px[x, y]
            d = max(abs(r - KEY[0]), abs(g - KEY[1]), abs(b - KEY[2]))
            if d < 30:
                op[x, y] = (0, 0, 0, 0)
            else:
                alpha = 255 if d > 90 else int(255 * (d - 30) / 60.0)
                op[x, y] = (r, g, b, alpha)
    return out


for p in sorted(glob.glob(os.path.join(SRC, "*.png"))):
    name = os.path.basename(p)
    im = key_out(Image.open(p))
    bb = im.getbbox()
    if bb:
        x0, y0, x1, y1 = bb
        pad = 10
        im = im.crop((max(0, x0 - pad), max(0, y0 - pad),
                      min(im.width, x1 + pad), min(im.height, y1 + pad)))
    im.save(os.path.join(DST, name))
    print(name, "->", im.size)
print("done")
