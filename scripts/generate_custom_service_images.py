from pathlib import Path
import math

from PIL import Image, ImageDraw, ImageFilter


OUT_DIR = Path("static/images")
SIZE = (1200, 800)


def vertical_gradient(top, bottom):
    img = Image.new("RGB", SIZE, top)
    draw = ImageDraw.Draw(img)
    height = SIZE[1]
    for y in range(height):
        ratio = y / (height - 1)
        color = tuple(int(top[i] * (1 - ratio) + bottom[i] * ratio) for i in range(3))
        draw.line([(0, y), (SIZE[0], y)], fill=color)
    return img


def soft_shadow(base, xy, radius=22, opacity=75):
    shadow = Image.new("RGBA", SIZE, (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle(xy, radius=radius, fill=(0, 0, 0, opacity))
    shadow = shadow.filter(ImageFilter.GaussianBlur(22))
    base.alpha_composite(shadow)


def draw_solar_panel(draw, x, y, w, h, angle=0):
    panel = Image.new("RGBA", (w + 24, h + 24), (0, 0, 0, 0))
    pd = ImageDraw.Draw(panel)
    pd.rounded_rectangle((12, 12, w + 12, h + 12), radius=14, fill=(20, 52, 80), outline=(207, 229, 238), width=4)
    cols, rows = 4, 3
    gap = 8
    cell_w = (w - gap * (cols + 1)) / cols
    cell_h = (h - gap * (rows + 1)) / rows
    for row in range(rows):
        for col in range(cols):
            cx = 12 + gap + col * (cell_w + gap)
            cy = 12 + gap + row * (cell_h + gap)
            pd.rounded_rectangle((cx, cy, cx + cell_w, cy + cell_h), radius=5, fill=(37, 101, 139))
            pd.line((cx + 8, cy + 8, cx + cell_w - 8, cy + cell_h - 8), fill=(117, 176, 202), width=2)
    rotated = panel.rotate(angle, expand=True, resample=Image.Resampling.BICUBIC)
    return rotated, (x, y)


def make_alternative_energy():
    img = vertical_gradient((188, 226, 230), (241, 246, 239)).convert("RGBA")
    draw = ImageDraw.Draw(img)

    draw.ellipse((850, 70, 1030, 250), fill=(255, 203, 91, 235))
    for i in range(18):
        angle = math.radians(i * 20)
        x1 = 940 + math.cos(angle) * 115
        y1 = 160 + math.sin(angle) * 115
        x2 = 940 + math.cos(angle) * 150
        y2 = 160 + math.sin(angle) * 150
        draw.line((x1, y1, x2, y2), fill=(255, 211, 106, 155), width=5)

    draw.polygon([(0, 535), (350, 325), (760, 535)], fill=(103, 112, 107))
    draw.polygon([(350, 325), (1200, 475), (760, 535)], fill=(72, 86, 92))
    draw.rectangle((0, 535, 1200, 800), fill=(219, 223, 214))

    for x, y, w, h, angle in [(180, 372, 285, 165, -10), (500, 422, 285, 165, -10), (755, 436, 260, 150, 7)]:
        panel, pos = draw_solar_panel(draw, x, y, w, h, angle)
        soft = Image.new("RGBA", SIZE, (0, 0, 0, 0))
        soft.alpha_composite(panel, pos)
        img.alpha_composite(soft)

    draw.rectangle((190, 625, 260, 765), fill=(41, 76, 83))
    draw.ellipse((190, 560, 260, 630), fill=(228, 178, 119))
    draw.polygon([(170, 598), (280, 598), (255, 642), (195, 642)], fill=(241, 181, 62))
    draw.rectangle((205, 650, 245, 770), fill=(244, 184, 65))
    draw.line((245, 662, 315, 603), fill=(49, 66, 72), width=9)
    draw.line((205, 662, 150, 612), fill=(49, 66, 72), width=9)
    draw.rectangle((148, 610, 175, 635), fill=(55, 103, 112))
    draw.line((300, 610, 362, 584), fill=(79, 95, 98), width=6)

    for x in range(70, 1120, 95):
        draw.line((x, 695, x + 48, 705), fill=(183, 190, 181), width=3)

    img = img.convert("RGB")
    img.save(OUT_DIR / "service-alternative-energy.jpg", quality=92, optimize=True)


def make_wallpaper():
    img = vertical_gradient((246, 238, 226), (226, 232, 224)).convert("RGBA")
    draw = ImageDraw.Draw(img)

    draw.rectangle((0, 0, 820, 800), fill=(233, 223, 209))
    for x in range(0, 850, 90):
        draw.line((x, 0, x, 800), fill=(214, 199, 183), width=3)
    for y in range(70, 760, 130):
        for x in range(35, 795, 90):
            draw.arc((x, y, x + 46, y + 46), 200, 520, fill=(164, 136, 116), width=3)
            draw.ellipse((x + 18, y + 18, x + 28, y + 28), fill=(139, 118, 103))

    draw.rectangle((820, 0, 1200, 800), fill=(206, 218, 213))
    for y in range(0, 800, 70):
        draw.line((820, y, 1200, y + 35), fill=(179, 197, 190), width=4)

    soft_shadow(img, (690, 145, 850, 710), radius=20, opacity=55)
    draw.rounded_rectangle((690, 145, 850, 710), radius=20, fill=(247, 242, 232), outline=(190, 173, 156), width=5)
    for y in range(185, 675, 80):
        draw.line((705, y, 835, y), fill=(210, 190, 173), width=3)
        draw.ellipse((745, y - 18, 795, y + 32), outline=(164, 136, 116), width=3)

    soft_shadow(img, (900, 500, 1095, 735), radius=24, opacity=65)
    draw.rounded_rectangle((920, 500, 1030, 735), radius=32, fill=(242, 232, 220), outline=(155, 132, 113), width=5)
    draw.rectangle((975, 500, 1095, 735), fill=(184, 123, 100))
    draw.rounded_rectangle((975, 500, 1095, 735), radius=30, outline=(155, 90, 75), width=5)
    draw.ellipse((945, 540, 1005, 604), fill=(223, 212, 200), outline=(155, 132, 113), width=4)

    draw.rectangle((465, 640, 760, 682), fill=(103, 83, 70))
    draw.rounded_rectangle((420, 604, 565, 704), radius=18, fill=(208, 166, 80), outline=(122, 92, 58), width=4)
    for x in range(438, 550, 18):
        draw.line((x, 616, x + 12, 690), fill=(112, 84, 57), width=3)
    draw.rectangle((555, 632, 760, 668), fill=(60, 74, 80))

    draw.rectangle((0, 730, 1200, 800), fill=(184, 163, 141))
    draw.line((0, 730, 1200, 730), fill=(134, 113, 95), width=5)

    img = img.convert("RGB")
    img.save(OUT_DIR / "service-wallpaper.jpg", quality=92, optimize=True)


if __name__ == "__main__":
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    make_alternative_energy()
    make_wallpaper()
    print("Generated service-alternative-energy.jpg and service-wallpaper.jpg")
