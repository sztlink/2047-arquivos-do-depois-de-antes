# QR at the needle limit

> **Historical note (October 2026).** Written during the research and rehearsal phase of the work, then called *Projeto 2047 / Arquivo Terra Viva*, and kept as process. Some of it no longer describes the work as it runs. For the current apparatus see `../03-field-notes/2026-10-lq-590-qr-and-declared-cost.md`, `../03-field-notes/2026-10-video-wall.md`, and `../03-field-notes/2026-10-opening-at-casa-firjan.md`.

This file records how small a scannable QR code can be printed on a 9-pin dot-matrix printer, and how **Projeto 2047 / Arquivo Terra Viva** uses that limit.

It is public research documentation. It does not expose private infrastructure, credentials, hostnames, IPs, or deployment details.

## Why a QR on continuous form

Each printed chapter can carry a code that points back to the source article that originated it. The paper edition and the living archive stay linked. The reader scans with their own phone.

## Character mode, the baseline

The first test rendered QR modules as text, two characters per module, using the full block glyph of code page 850. At condensed pitch and 8 lines per inch one module measures about 3.0x3.2mm and a version 2 code spans roughly 10cm. It scanned on the first try, single pass and double pass. It is also far too large for a chapter header.

## Graphics mode

The real instrument is the bit-image command `ESC L`, 120 dots per inch horizontally, printed in bands of 8 pins with a 24/216 inch line feed. Pin rows sit at 1/72 inch. Module geometry is chosen in printed dots per module, width times height.

| module (dots) | module size | full code (v2 with quiet zone) | scan result |
|---|---|---|---|
| 5x3 | 1.06 x 1.06mm | ~35mm | reads |
| 3x2 | 0.64 x 0.71mm | ~21mm | reads |
| 2x1 | 0.42 x 0.35mm | ~14mm | reads, single and double pass |

The 2x1 module is the floor of the hardware. One dot column, one pin row. The needle cannot form a smaller mark, and the phone still reads it. Ink spread fills the module and helps rather than hurts.

For a long exhibition run the preset uses 2x1 with a double pass, since ribbons fade and the second pass costs nothing.

## The URL length problem

Raw source URLs cannot go on paper. A survey of 464 accepted source URLs from the collector measured lengths from 21 to 680 characters, median 127, ninetieth percentile 337. At error level M that spread produces QR versions 2 through 21. The lucky chapter would carry a 21mm code and the unlucky one a dense monster past 5cm that a 9-pin printer cannot render reliably.

## Fixed-version design

Every chapter code therefore encodes a short fixed-length redirect under the public archive domain, one path per chapter. The payload is always about 27 characters, the code is always version 3, 37x37 modules, printed at 16x13mm. Uniform on every chapter, printable at the needle floor.

Chapter numbers in the redirect are padded to four digits. The padding is not cosmetic. At three digits the payload is 26 characters, which is exactly the ceiling of version 2, so the code would print at version 2 until chapter 999 and jump to version 3 at chapter 1000. A run at the slow cadence passes that mark, so the jump would land in the middle of the exhibition and split the printed archive into two code geometries. Four digits fix every code in the run at version 3.

The redirect adds what the raw link cannot hold. The intermediate page carries provenance, the article title, the outlet, the date, the original URL. When the source article rots offline, the redirect keeps pointing at the archived record. The paper never points at a void.
