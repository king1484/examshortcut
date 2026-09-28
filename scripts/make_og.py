"""Generate the default Open Graph image (1200x630) — code-driven, brand-matched."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
BG = "#f7f5f0"
INK = "#111827"
INK2 = "#6b7280"
BRAND = "#e8590c"
LINE = "#e3dfd6"

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# subtle top accent bar
d.rectangle([0, 0, W, 10], fill=BRAND)

bold = lambda s: ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", s)
reg = lambda s: ImageFont.truetype(r"C:\Windows\Fonts\arial.ttf", s)

# logo: rounded square + check, same shape as the site logo
lx, ly, ls = 96, 150, 132
d.rounded_rectangle([lx, ly, lx + ls, ly + ls], radius=32, fill=BRAND)
d.line([(lx + 34, ly + 70), (lx + 58, ly + 96), (lx + 100, ly + 38)], fill="#ffffff", width=16, joint="curve")

# wordmark
fx, fy = 268, 150
f_word = bold(112)
d.text((fx, fy), "Exam", font=f_word, fill=INK)
w_exam = d.textlength("Exam", font=f_word)
d.text((fx + w_exam, fy), "Shortcut", font=f_word, fill=BRAND)

# tagline
d.text((268, 296), "SSC, Railway & entrance exam preparation", font=reg(44), fill=INK2)
d.text((268, 356), "Notes · Shortcuts · Mocks · Cutoffs · Current affairs", font=reg(36), fill=INK2)

# domain pill
pill_text = "examshortcut.in"
f_pill = bold(40)
pw = d.textlength(pill_text, font=f_pill)
px, py, ph = 268, 452, 84
d.rounded_rectangle([px, py, px + pw + 72, py + ph], radius=ph // 2, fill="#ffffff", outline=LINE, width=2)
d.text((px + 36, py + 18), pill_text, font=f_pill, fill=BRAND)

img.save(r"C:\Users\Vinay Singirikonda\Desktop\examshortcut\public\og.png", optimize=True)
print("og.png written:", img.size)
