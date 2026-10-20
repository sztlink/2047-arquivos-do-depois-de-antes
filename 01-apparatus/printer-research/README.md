# Printer research

> **Historical note (October 2026).** Written during the research and rehearsal phase of the work, then called *Projeto 2047 / Arquivo Terra Viva*, and kept as process. Some of it no longer describes the work as it runs. For the current apparatus see `../../03-field-notes/2026-10-lq-590-qr-and-declared-cost.md`, `../../03-field-notes/2026-10-video-wall.md`, and `../../03-field-notes/2026-10-opening-at-casa-firjan.md`.

This folder documents the dot-matrix printer as an archive apparatus.

The current prototype printer is an **Epson FX-2190** installed at AYA Studio and connected through a Raspberry Pi print server running CUPS. Operational network details, credentials, internal IP addresses, device serials, and production-specific configuration are intentionally omitted from this public archive.

## Why this matters

The printer is not a decorative vintage object. It is the first physical instrument through which the generative system can become paper, sound, timing, friction, error, and accumulation.

## Current public state

- Prototype printer: **Epson FX-2190**.
- Print server layer: Raspberry Pi + CUPS.
- Physical medium: continuous fanfold paper.
- Working mode: text / raw ESC/P payloads.
- Artistic target: wide ASCII / continuous archive output.
- Status: usable as a prototype, not yet validated as final exhibition hardware.

## Recovered calibration threads

Internal tests before this repository produced four useful public conclusions:

1. **CUPS can spool to the FX-2190 reliably.**
2. **Raw ESC/P payloads are preferable for controlled text and ASCII output.**
3. **ASCII art needs an explicit ESC/P preamble.** In particular: reset, condensed-off, and 12 cpi mode.
4. **Width behavior remains a critical open issue.** Earlier tests found a promising 100-column wide mode; later diagnostics suggested a persistent physical or firmware width limit around 149 mm. This contradiction is now treated as part of the printer research, not as a resolved fact.

## Documents

- `dot-matrix-as-archive-apparatus.md` - conceptual and material role of the printer.
- `fx-2190-calibration-notes.md` - recovered technical findings from previous tests.
- `cups-escp-pipeline.md` - public summary of the CUPS / ESC-P pipeline.
- `continuous-paper.md` - paper as archive, not leftover material.
- `encoding-and-typography.md` - accents, ASCII, code pages, typography.
- `failure-modes.md` - failures that matter technically and artistically.

## Public boundary

This folder does not publish credentials, internal addresses, vendor details, private messages, or production instructions that could expose the studio infrastructure.
