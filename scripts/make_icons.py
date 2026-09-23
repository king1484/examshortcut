"""Generate PNG app icons (regular + maskable) matching public/icon.svg."""
from PIL import Image, ImageDraw

ORANGE = (232, 89, 12, 255)   # #e8590c
WHITE = (255, 255, 255, 255)
OUT = r"C:\Users\Vinay Singirikonda\Desktop\examshortcut\public"


def check_points(size, scale=1.0):
    """The icon.svg checkmark (M136 272 L232 368 L384 168) scaled about center."""
    pts = [(136, 272), (232, 368), (384, 168)]
    cx = cy = 256
    s = size / 512
    return [((cx + (x - cx) * scale) * s, (cy + (y - cy) * scale) * s) for (x, y) in pts]


def draw_check(d, size, pts, width_512):
    """Two thick segments with round caps at every vertex (PIL has no round joins)."""
    w = max(2, round(width_512 * size / 512))
    d.line([pts[0], pts[1]], fill=WHITE, width=w)
    d.line([pts[1], pts[2]], fill=WHITE, width=w)
    r = w / 2
    for (cx, cy) in pts:
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=WHITE)


# Regular icons: rounded square + check, same geometry as icon.svg
for size in (192, 512):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, size - 1, size - 1], radius=round(size * 96 / 512), fill=ORANGE)
    draw_check(d, size, check_points(size), 56)
    img.save(rf"{OUT}\icon-{size}.png")

# Maskable: full-bleed square (launcher applies its own mask), check inside
# the ~80% safe zone -> scale to 72%
for size in (192, 512):
    img = Image.new("RGBA", (size, size), ORANGE)
    d = ImageDraw.Draw(img)
    draw_check(d, size, check_points(size, scale=0.72), 56 * 0.72)
    img.save(rf"{OUT}\icon-{size}-maskable.png")

print("wrote icon-192.png icon-512.png icon-192-maskable.png icon-512-maskable.png")
