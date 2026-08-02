#!/usr/bin/env python3
"""The data register. A seeded multi-source collage for screen or print.

Rectangular fragments from a source bank (generated scenes plus public-record
satellite imagery), procedural contour lines extracted from the images
themselves, thermal blooms, and corruption passes that stitch the fragments.
One seed per chapter reproduces the same collage forever.

All typography rides on top by code. Diffusion never draws text, because
diffusion corrupts letterforms and the machine should not fake its own records.
The optional headlines file is a JSON list of objects with keys t, v, ts, taken
from the machine's own collector.

Usage
  data_collage.py BANK_DIR --out collage.png --seed 7 [--headlines h.json]
"""

import argparse
import json
import os

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1920, 1080
AMBER = (255, 176, 0)
SILVER = (208, 226, 218)
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"


def load_bank(bank_dir):
  out = []
  for f in sorted(os.listdir(bank_dir)):
    if f.lower().endswith((".png", ".jpg", ".jpeg")):
      out.append(Image.open(os.path.join(bank_dir, f)).convert("RGB"))
  return out


def grade(arr, rs, keep_warm):
  f = arr.astype(np.float32) / 255.0
  lum = f.mean(axis=2, keepdims=True)
  if keep_warm:
    f = f * 0.80 + lum * np.array([0.55, 0.45, 0.28]) * 0.25
  else:
    f = f * 0.62 + lum * np.array([0.24, 0.55, 0.46]) * 0.42
  return (np.power(np.clip(f * 1.05, 0, 1), 1.04) * 255).astype(np.uint8)


def crop(src, fw, fh, rs):
  sw, sh = src.size
  scale = max(fw / sw, fh / sh) * rs.uniform(1.0, 2.2)
  rw, rh = max(int(sw * scale), fw + 2), max(int(sh * scale), fh + 2)
  r = src.resize((rw, rh), Image.LANCZOS)
  x, y = rs.randint(0, rw - fw), rs.randint(0, rh - fh)
  return np.asarray(r.crop((x, y, x + fw, y + fh)))


def contours(src, rs):
  g = src.convert("L").resize((W, H), Image.LANCZOS)
  g = g.filter(ImageFilter.GaussianBlur(rs.randint(10, 26)))
  a = np.asarray(g).astype(np.float32)
  q = np.floor(a / 256.0 * rs.randint(7, 13))
  e = np.zeros((H, W), dtype=bool)
  e[:, 1:] |= q[:, 1:] != q[:, :-1]
  e[1:, :] |= q[1:, :] != q[:-1, :]
  return e | np.roll(e, 1, 0) | np.roll(e, 1, 1)


def region(rs):
  m = np.zeros((H, W), dtype=np.float32)
  for _ in range(rs.randint(2, 4)):
    x0, y0 = rs.randint(0, W // 2), rs.randint(0, H // 2)
    m[y0:min(H, y0 + rs.randint(H // 3, H)), x0:min(W, x0 + rs.randint(W // 3, W))] = 1.0
  return np.asarray(Image.fromarray((m * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(60)), dtype=np.float32) / 255.0


def compose(bank, seed):
  rs = np.random.RandomState(seed)
  canvas = np.zeros((H, W, 3), dtype=np.float32)
  canvas[..., 0], canvas[..., 1], canvas[..., 2] = 8, 18, 15
  canvas += rs.normal(0, 2.5, (H, W, 3))
  order = list(rs.permutation(len(bank)))
  for placed in range(rs.randint(26, 34)):
    src = bank[order[placed % len(order)]]
    tier = rs.rand()
    if tier < 0.25:
      fw, fh = rs.randint(520, 780), rs.randint(330, 470)
    elif tier < 0.65:
      fw, fh = rs.randint(290, 520), rs.randint(190, 330)
    else:
      fw, fh = rs.randint(150, 290), rs.randint(110, 190)
    x = int(np.clip(rs.randint(-40, W - fw + 40), 0, W - fw))
    y = int(np.clip(rs.randint(-30, H - fh + 30), 0, H - fh))
    frag = grade(crop(src, fw, fh, rs), rs, rs.rand() < 0.30)
    if rs.rand() < 0.45:
      for _ in range(rs.randint(1, 4)):
        y0 = rs.randint(0, fh - 12)
        bh = rs.randint(6, max(7, fh // 5))
        frag[y0:y0 + bh] = np.roll(frag[y0:y0 + bh], rs.randint(-40, 40), axis=1)
    a = 1.0 if rs.rand() < 0.7 else rs.uniform(0.72, 0.92)
    canvas[y:y + fh, x:x + fw] = canvas[y:y + fh, x:x + fw] * (1 - a) + frag.astype(np.float32) * a
  cont = np.zeros((H, W), dtype=np.float32)
  for _ in range(2):
    cont = np.maximum(cont, contours(bank[order[rs.randint(0, len(order))]], rs).astype(np.float32) * region(rs) * rs.uniform(0.55, 0.8))
  canvas = canvas * (1 - cont[..., None] * 0.85) + np.array([205, 225, 215], dtype=np.float32) * cont[..., None]
  yg, xg = np.ogrid[:H, :W]
  for _ in range(rs.randint(3, 6)):
    cx, cy = rs.randint(0, W), rs.randint(0, H)
    rx, ry = rs.randint(60, 190), rs.randint(45, 130)
    blob = np.exp(-(((xg - cx) / rx) ** 2 + ((yg - cy) / ry) ** 2) * 1.6)
    color = np.array([255, 40, 140]) if rs.rand() < 0.7 else np.array([160, 70, 255])
    canvas += blob[..., None] * color * rs.uniform(0.55, 0.85)
  return np.clip(canvas, 0, 255)


def seams(base, seed):
  rs = np.random.RandomState(seed * 7919 + 1)
  fr = base.copy()
  for _ in range(rs.randint(6, 12)):
    y0 = rs.randint(0, H - 16)
    bh = rs.randint(2, 14)
    fr[y0:y0 + bh] = np.roll(fr[y0:y0 + bh], rs.randint(-180, 180), axis=1)
  fr[..., 0] = np.roll(fr[..., 0], 3, axis=1)
  fr[..., 2] = np.roll(fr[..., 2], -3, axis=1)
  fr[(np.arange(H) % 3 == 0)] *= 0.86
  fr += np.random.RandomState(seed).normal(0, 3.0, (H, W, 3))
  return np.clip(fr, 0, 255).astype(np.uint8)


def overlay(arr, seed, headlines):
  rs = np.random.RandomState(seed + 31337)
  im = Image.fromarray(arr)
  dr = ImageDraw.Draw(im, "RGBA")
  f_h = ImageFont.truetype(MONO, 20)
  hs = [h for h in headlines if not any(len(w) > 24 for w in h["t"].split())]
  rs.shuffle(hs)
  n = min(4, len(hs))
  if n:
    y0 = H - 24 - n * 26
    dr.rectangle([0, y0 - 10, W, H - 12], fill=(4, 10, 8, 175))
    for i, h in enumerate(hs[:n]):
      line = f"{h.get('ts', '')}  {h.get('v', '').lower():<16.16}  {h.get('t', '').lower()}"
      dr.text((40, y0 + i * 26), line, font=f_h, fill=AMBER + (235,))
  return np.asarray(im)


def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("bank")
  ap.add_argument("--out", required=True)
  ap.add_argument("--seed", type=int, required=True)
  ap.add_argument("--headlines", default=None)
  args = ap.parse_args()

  bank = load_bank(args.bank)
  img = seams(compose(bank, args.seed), args.seed)
  heads = json.load(open(args.headlines)) if args.headlines else []
  if heads:
    img = overlay(img, args.seed, heads)
  Image.fromarray(img).save(args.out)
  print(f"{len(bank)} sources . seed {args.seed} -> {args.out}")


if __name__ == "__main__":
  main()
