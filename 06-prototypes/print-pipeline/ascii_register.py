#!/usr/bin/env python3
"""Chapter image as ASCII on continuous form.

Three conversion modes, judged on paper in July 2026.

  density     equalized luminance over a 13-level ramp, the mode that won on paper
  banner      image rotated 90 degrees, the scene runs along the paper (about 4x
              the resolution of a single form, spans 2 to 3 forms)
  serigraphy  heavy median filter and 4 flat tone planes, boldest at distance

Ink follows light by default. Night scenes leave the paper white where the sky
is dark and spend the ribbon on datacenter lights and rain.

Usage
  ascii_register.py IMAGE --out payload.bin [--mode density] [--cap N] [--no-invert]
"""

import argparse

import numpy as np
from PIL import Image, ImageFilter, ImageOps

import escp_common as ep

RAMP = " .':-=+*x#%@M"


def grid(img, cols, invert, blur=0, rows=None):
  g = img.convert("L")
  if blur:
    g = g.filter(ImageFilter.GaussianBlur(blur))
  if rows is None:
    rows = max(8, int(round(cols * (img.height / img.width) / ep.CELL_ASPECT)))
  a = np.asarray(g.resize((cols, rows), Image.LANCZOS)).astype(np.float32) / 255.0
  if not invert:
    a = 1.0 - a
  return a


def stretch(a, lo=2, hi=98):
  p1, p2 = np.percentile(a, lo), np.percentile(a, hi)
  return np.clip((a - p1) / max(p2 - p1, 1e-6), 0, 1)


def ramp_map(a, ramp):
  idx = np.clip((a * (len(ramp) - 1)).round().astype(int), 0, len(ramp) - 1)
  return ["".join(ramp[i] for i in row) for row in idx]


def mode_density(img, cols, invert):
  g = ImageOps.equalize(img.convert("L"))
  return ramp_map(grid(Image.merge("RGB", (g, g, g)), cols, invert), RAMP)


def mode_banner(img, cols, invert):
  rot = img.rotate(-90, expand=True)
  rows = int(round(cols * (rot.height / rot.width) * (8.0 / 17.1)))
  a = np.power(stretch(grid(rot, cols, invert, blur=2, rows=rows)), 1.25)
  return ramp_map(a, " .:-=x#%@")


def mode_serigraphy(img, cols, invert):
  g = img.convert("L").filter(ImageFilter.MedianFilter(9)).filter(ImageFilter.GaussianBlur(3))
  a = stretch(grid(Image.merge("RGB", (g, g, g)), cols, invert))
  levels = np.digitize(a, [0.3, 0.55, 0.8])
  return ["".join(" .x@"[v] for v in row) for row in levels]


MODES = {"density": mode_density, "banner": mode_banner, "serigraphy": mode_serigraphy}


def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("image")
  ap.add_argument("--out", required=True)
  ap.add_argument("--mode", choices=MODES, default="density")
  ap.add_argument("--cols", type=int, default=ep.ART_COLS)
  ap.add_argument("--cap", type=int, default=None)
  ap.add_argument("--no-invert", action="store_true")
  args = ap.parse_args()

  img = Image.open(args.image).convert("RGB")
  art = MODES[args.mode](img, args.cols, not args.no_invert)
  head = f"cap {args.cap:03d}" if args.cap is not None else "visual record"
  lines = ["", f"ARQUIVO TERRA VIVA . visual record . {head}", "-" * args.cols] + art
  payload = ep.art_preamble() + ep.text_block(lines) + ep.close_payload()
  with open(args.out, "wb") as fh:
    fh.write(payload)
  print(f"{len(art)} rows x {args.cols} cols . mode {args.mode} . {len(payload)} bytes -> {args.out}")


if __name__ == "__main__":
  main()
