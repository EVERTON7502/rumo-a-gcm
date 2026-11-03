"""Gera os ícones do app (escudo com "GCM" sobre azul-marinho) com Pillow.

Uso:  python tools/gerar_icones.py
Saída: icons/icon-192.png, icon-512.png, icon-maskable-192.png, icon-maskable-512.png,
       apple-touch-icon.png (180), favicon-32.png e og-image.png (1200x630).
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "icons"
OUT.mkdir(exist_ok=True)

NAVY_TOP, NAVY_BOTTOM = (10, 29, 92), (5, 11, 34)
BLUE, CYAN = (37, 99, 235), (34, 211, 238)
FONTS = ["C:/Windows/Fonts/segoeuib.ttf", "C:/Windows/Fonts/arialbd.ttf",
         "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
         "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]


def font(size):
    for f in FONTS:
        if Path(f).exists():
            return ImageFont.truetype(f, size)
    return ImageFont.load_default(size)


def gradient(size, top, bottom):
    img = Image.new("RGB", (size, size), top)
    d = ImageDraw.Draw(img)
    for y in range(size):
        t = y / (size - 1)
        d.line([(0, y), (size, y)], fill=tuple(round(top[i] + (bottom[i] - top[i]) * t) for i in range(3)))
    return img


def shield_points(cx, top, w, h):
    # escudo: topo reto com cantos, laterais e ponta inferior arredondada por polígono denso
    pts = []
    hw = w / 2
    pts += [(cx - hw, top + h * 0.10), (cx - hw * 0.55, top), (cx + hw * 0.55, top), (cx + hw, top + h * 0.10)]
    steps = 40
    for i in range(steps + 1):  # lado direito descendo até a ponta
        t = i / steps
        x = cx + hw * (1 - t ** 2.6)
        y = top + h * (0.10 + 0.90 * t)
        pts.append((x, y))
    for i in range(steps, -1, -1):  # lado esquerdo subindo
        t = i / steps
        x = cx - hw * (1 - t ** 2.6)
        y = top + h * (0.10 + 0.90 * t)
        pts.append((x, y))
    return pts


def icon(size, maskable=False, rounded=True):
    s = size * 4  # supersampling para bordas suaves
    bg = gradient(s, NAVY_TOP, NAVY_BOTTOM)
    glow = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse([s * 0.15, s * 0.05, s * 0.85, s * 0.75], fill=(56, 162, 255, 120))
    bg.paste(glow.filter(ImageFilter.GaussianBlur(s * 0.12)), (0, 0), glow.filter(ImageFilter.GaussianBlur(s * 0.12)))
    scale = 0.62 if maskable else 0.80  # área segura do maskable
    w, h = s * scale * 0.82, s * scale
    top = (s - h) / 2
    layer = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    outer = shield_points(s / 2, top, w, h)
    d.polygon(outer, fill=CYAN)
    inset = s * 0.022
    inner = shield_points(s / 2, top + inset * 1.4, w - inset * 2.6, h - inset * 2.8)
    grad = gradient(s, (40, 110, 245), (12, 40, 140)).convert("RGBA")
    mask = Image.new("L", (s, s), 0)
    ImageDraw.Draw(mask).polygon(inner, fill=255)
    layer.paste(grad, (0, 0), mask)
    shadow = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    ImageDraw.Draw(shadow).polygon(outer, fill=(34, 211, 238, 150))
    bg = bg.convert("RGBA")
    bg.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(s * 0.04)))
    bg.alpha_composite(layer)
    d = ImageDraw.Draw(bg)
    f = font(int(h * 0.215))
    text = "GCM"
    bb = d.textbbox((0, 0), text, font=f)
    tx, ty = s / 2 - (bb[2] - bb[0]) / 2 - bb[0], top + h * 0.43 - (bb[3] - bb[1]) / 2 - bb[1]
    d.text((tx, ty), text, font=f, fill=(255, 255, 255))
    # estrela pequena acima do texto
    cy, r = top + h * 0.17, h * 0.055
    import math
    star = [(s / 2 + (r if i % 2 == 0 else r * 0.45) * math.sin(i * math.pi / 5),
             cy - (r if i % 2 == 0 else r * 0.45) * math.cos(i * math.pi / 5)) for i in range(10)]
    d.polygon(star, fill=(255, 210, 80))
    img = bg.resize((size, size), Image.LANCZOS)
    if rounded and not maskable:
        m = Image.new("L", (size * 4, size * 4), 0)
        ImageDraw.Draw(m).rounded_rectangle([0, 0, size * 4 - 1, size * 4 - 1], radius=size * 4 * 0.22, fill=255)
        img.putalpha(m.resize((size, size), Image.LANCZOS))
    return img


for sz in (192, 512):
    icon(sz).save(OUT / f"icon-{sz}.png")
    icon(sz, maskable=True).save(OUT / f"icon-maskable-{sz}.png")
icon(180, rounded=False).convert("RGB").save(OUT / "apple-touch-icon.png")
icon(32).save(OUT / "favicon-32.png")

og = gradient(1200, NAVY_TOP, NAVY_BOTTOM).crop((0, 0, 1200, 630)).convert("RGBA")
og.alpha_composite(icon(360), (90, 135))
d = ImageDraw.Draw(og)
d.text((510, 210), "Rumo à GCM Salvador", font=font(64), fill=(255, 255, 255))
d.text((512, 300), "Plano de estudos · Edital nº 02/2026 · FGV", font=font(34), fill=(160, 205, 255))
d.text((512, 360), "Cronômetro, revisões, questões e simulados", font=font(34), fill=(160, 205, 255))
og.convert("RGB").save(OUT / "og-image.png", optimize=True)
print("ícones gerados em", OUT)
