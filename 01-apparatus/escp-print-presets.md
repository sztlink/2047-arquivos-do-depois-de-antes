# ESC/P print presets

> **Historical note (October 2026).** Written during the research and rehearsal phase of the work, then called *Projeto 2047 / Arquivo Terra Viva*, and kept as process. Some of it no longer describes the work as it runs. For the current apparatus see `../03-field-notes/2026-10-lq-590-qr-and-declared-cost.md`, `../03-field-notes/2026-10-video-wall.md`, and `../03-field-notes/2026-10-opening-at-casa-firjan.md`.

This file records the measured print presets for **Projeto 2047 / Arquivo Terra Viva**.

It is public research documentation. It does not expose private infrastructure, credentials, hostnames, IPs, or deployment details.

## Context

The novel prints on a 9-pin wide-carriage dot-matrix printer, on continuous form paper of 240x140mm per page. The printer is attached by USB directly to the exhibition host and receives raw ESC/P. Every value below was calibrated on paper, across three test sheets, in July 2026.

## The ART preset

The visual register of each chapter (image, title, QR) uses one fixed ESC/P preamble.

| command | bytes | effect |
|---|---|---|
| reset | `ESC @` | known state |
| condensed on | `SI` | 17.1 characters per inch |
| 8 lines per inch | `ESC 0` | tighter vertical grid for image work |
| page length | `ESC C 44` | 44 lines at 1/8 inch equals 139.7mm, one continuous form |
| left margin | `ESC l 8` | clears the preprinted edge zone of surplus form stock |
| art width | 124 columns | total 132 columns, about 197mm, centered on the form |

The 124-column width is deliberately narrower than the maximum. A wider block printed clean on the first load and overflowed into the sprocket zone after the paper was reloaded. The narrower block survives tractor repositioning.

## Calibration receipts

Three sheets fixed three distinct failures.

1. Sheet one printed across the form fold. Top of form was misaligned, the header landed on the perforation, and the form feed advanced by the printer default page length, skipping most of a blank form. `ESC C 44` pins the feed to exactly one form.
2. Sheet two validated page length and margin. The ruler line and header printed whole, and the form feed stopped at the top of the next form.
3. Sheet three, printed after a paper jam and manual reload, overflowed on the right. The tractor had shifted. The narrower 124-column block with an 8-column margin absorbed the shift.

## Paper overrules screen

Eight conversion styles of the same image were compared on screen and then on paper. On screen the 1-bit Floyd-Steinberg halftone looked strongest. On paper the plain density ramp won and the halftone fell apart. The needle adds its own texture and the ribbon adds its own weight, and no preview shows either. Judge dot-matrix work on paper or not at all.

## Native type

The printer carries its own typeface, and the cover lockup uses it. Double-height double-width native characters (`ESC w 1`, `ESC W 1`) sit above a drawn ASCII-relief title block. One trap is worth recording. Indent spaces printed after enabling double width are themselves doubled. Indent first, then enable width.

In the relief typeface used for the title block, leading and trailing spaces render as continuation strokes. Space becomes a drawing element. The title recipe therefore specifies its spaces explicitly, one before and one after the first word, two before and two after the second, with no blank line between the stacked words so the relief joins vertically.
