"""Shared ESC/P constants and the ART preamble for the 2047 print pipeline.

Target is a 9-pin wide-carriage ESC/P printer on 240x140mm continuous forms.
Values calibrated on paper, July 2026. See 01-apparatus/escp-print-presets.md.
"""

ESC = b"\x1b"
CONDENSED_ON = b"\x0f"
CONDENSED_OFF = b"\x12"

PAGE_LINES = 44        # ESC C 44 at 8 lpi equals 139.7mm, one form
LEFT_MARGIN = 8        # columns, clears preprinted edge stock
ART_COLS = 124         # survives tractor repositioning
CELL_ASPECT = 17.1 / 8.0


def art_preamble():
  p = ESC + b"@"
  p += CONDENSED_ON
  p += ESC + b"0"
  p += ESC + b"C" + bytes([PAGE_LINES])
  p += ESC + b"l" + bytes([LEFT_MARGIN])
  return p


def close_payload():
  return b"\x0c" + ESC + b"@"


def text_block(lines):
  return ("\r\n".join(l[:ART_COLS] for l in lines) + "\r\n").encode("ascii", "replace")
