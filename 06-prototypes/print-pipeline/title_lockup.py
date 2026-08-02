#!/usr/bin/env python3
"""FIGlet titles and the native-type cover lockup.

Width rule. A title that exceeds the page width splits at the best word
boundary, the partition that minimizes the widest line, two lines, three when
needed. A glyph is never cut. Stacked words receive extra blank lines between
them, except where the typeface joins vertically by design.

The cover lockup mixes two voices of the same printer. The word ARQUIVO prints
in the machine's native typeface at double height and double width. The words
TERRA VIVA print in a drawn relief typeface where leading and trailing spaces
render as continuation strokes, so the spaces are part of the drawing. One trap
is recorded in the apparatus notes. Indent spaces must print before double
width is enabled or the indent doubles too.

Usage
  title_lockup.py "ARQUIVO TERRA VIVA" --out payload.bin [--font larry3d]
  title_lockup.py --cover --out payload.bin
"""

import argparse
import sys

import pyfiglet

import escp_common as ep


def render(text, font):
  r = pyfiglet.figlet_format(text, font=font, width=400).rstrip("\n")
  ls = [l.rstrip() for l in r.split("\n")]
  while ls and not ls[0].strip():
    ls.pop(0)
  while ls and not ls[-1].strip():
    ls.pop()
  return ls


def width(text, font):
  ls = render(text, font)
  return max((len(l) for l in ls), default=0)


def partitions(words, n):
  if n == 1:
    yield [words]
    return
  for i in range(1, len(words) - n + 2):
    for rest in partitions(words[i:], n - 1):
      yield [words[:i]] + rest


def fit(text, font, cols, max_lines=3):
  words = text.split()
  for n in range(1, max_lines + 1):
    if n > len(words):
      break
    best = None
    for part in partitions(words, n):
      groups = [" ".join(g) for g in part]
      w = max(width(g, font) for g in groups)
      if best is None or w < best[0]:
        best = (w, groups)
    if best and best[0] <= cols:
      return best[1]
  return None


def stack(groups, font, leading=2):
  art = []
  for i, g in enumerate(groups):
    if i:
      art += [""] * leading
    art += render(g, font)
  return art


def cover_lockup():
  """ARQUIVO in native double type over TERRA VIVA in slant relief."""
  terra = render(" TERRA ", "slant_relief")
  viva = render("  VIVA  ", "slant_relief")
  block = terra + viva
  block_w = max(len(l) for l in block)
  center_in = (block_w / 2) / 17.1
  word_in = 7 * 2 / 10
  indent = max(0, round((center_in - word_in / 2) * 10))
  p = ep.CONDENSED_OFF + ep.ESC + b"P" + ep.ESC + b"2"
  p += b" " * indent
  p += ep.ESC + b"w\x01" + ep.ESC + b"W\x01" + b"ARQUIVO"
  p += ep.ESC + b"w\x00" + ep.ESC + b"W\x00" + b"\r\n\r\n"
  p += ep.CONDENSED_ON + ep.ESC + b"0"
  p += ep.text_block(block)
  return p


def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("text", nargs="?", default="ARQUIVO TERRA VIVA")
  ap.add_argument("--out", required=True)
  ap.add_argument("--font", default="larry3d")
  ap.add_argument("--cover", action="store_true")
  args = ap.parse_args()

  if args.cover:
    payload = ep.art_preamble() + cover_lockup() + ep.close_payload()
  else:
    groups = fit(args.text, args.font, ep.ART_COLS)
    if groups is None:
      sys.exit(f"'{args.text}' does not fit in 3 lines with font {args.font}")
    payload = ep.art_preamble() + ep.text_block([""] + stack(groups, args.font)) + ep.close_payload()
  with open(args.out, "wb") as fh:
    fh.write(payload)
  print(f"{len(payload)} bytes -> {args.out}")


if __name__ == "__main__":
  main()
