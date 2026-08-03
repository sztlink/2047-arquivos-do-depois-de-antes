#!/usr/bin/env python3
"""QR codes in ESC/P bit-image mode, down to the needle floor.

ESC L prints 120 dots per inch horizontally in bands of 8 pins, pin rows at
1/72 inch, band feed at 24/216 inch. The smallest module the hardware can form
is 2 dots wide by 1 pin row tall, 0.42 x 0.35mm, and it still scans on a phone.
Default is that floor with a double pass for ribbon wear.

Payload discipline. Encode short fixed-length redirects, never raw source URLs.
A survey of 464 accepted source URLs measured 21 to 680 characters, which spans
QR versions 2 through 21. A fixed 27-character redirect pins every chapter code
at version 3, 37x37 modules, 16x13mm on paper.

Usage
  escp_qr.py "https://example.org/f/042" --out payload.bin [--mw 2 --mh 1] [--single]
"""

import argparse

import qrcode

import escp_common as ep

MARGIN_DOTS = 96


def matrix(payload):
  qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, border=4)
  qr.add_data(payload)
  qr.make(fit=True)
  return qr.get_matrix(), qr.version


def qr_bands(m, mw, mh, double_pass, lead_dots=MARGIN_DOTS):
  """lead_dots desloca o codigo na linha. Passe o calculo do chamador para
  encostar o codigo na margem direita do bloco de texto."""
  n = len(m)
  width = n * mw
  rows = []
  for r in range(n):
    for _ in range(mh):
      rows.append([1 if m[r][c] else 0 for c in range(n) for _ in range(mw)])
  while len(rows) % 8:
    rows.append([0] * width)
  p = ep.ESC + b"3" + bytes([24])
  for b0 in range(0, len(rows), 8):
    cols = bytearray(b"\x00" * lead_dots)
    for c in range(width):
      byte = 0
      for k in range(8):
        if rows[b0 + k][c]:
          byte |= 0x80 >> k
      cols.append(byte)
    t = len(cols)
    band = ep.ESC + b"L" + bytes([t % 256, t // 256]) + bytes(cols)
    p += (band + b"\r" + band + b"\r\n") if double_pass else (band + b"\r\n")
  p += ep.ESC + b"2"
  return p


def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("payload")
  ap.add_argument("--out", required=True)
  ap.add_argument("--mw", type=int, default=2)
  ap.add_argument("--mh", type=int, default=1)
  ap.add_argument("--single", action="store_true")
  ap.add_argument("--caption", default=None)
  args = ap.parse_args()

  m, ver = matrix(args.payload)
  n = len(m)
  wmm = n * args.mw / 120 * 25.4
  hmm = n * args.mh / 72 * 25.4
  p = ep.art_preamble()
  p += qr_bands(m, args.mw, args.mh, not args.single)
  if args.caption:
    p += b"\r\n" + args.caption[:ep.ART_COLS].encode("ascii", "replace") + b"\r\n"
  p += ep.close_payload()
  with open(args.out, "wb") as fh:
    fh.write(p)
  print(f"QR v{ver} {n}x{n} . {wmm:.0f}x{hmm:.0f}mm . module {args.mw}x{args.mh} -> {args.out}")


if __name__ == "__main__":
  main()
