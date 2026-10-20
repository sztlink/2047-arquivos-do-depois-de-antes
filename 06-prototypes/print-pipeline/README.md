# print-pipeline

> **Historical note (October 2026).** Written during the research and rehearsal phase of the work, then called *Projeto 2047 / Arquivo Terra Viva*, and kept as process. Some of it no longer describes the work as it runs. For the current apparatus see `../../03-field-notes/2026-10-lq-590-qr-and-declared-cost.md`, `../../03-field-notes/2026-10-video-wall.md`, and `../../03-field-notes/2026-10-opening-at-casa-firjan.md`.

Working tools for the printed visual register of **Projeto 2047 / Arquivo Terra Viva**. Everything here targets a 9-pin ESC/P dot-matrix printer on 240x140mm continuous forms and emits a raw ESC/P payload file. Send the payload to a raw print queue or device untouched. No driver should reinterpret it.

The measured presets behind these tools are documented in `01-apparatus/escp-print-presets.md` and `01-apparatus/qr-at-the-needle-limit.md`.

## Tools

| tool | what it prints |
|---|---|
| `ascii_register.py` | a chapter image as ASCII, density ramp, rotated banner, or 4-level serigraphy |
| `data_collage.py` | the data register, a seeded multi-source collage with typographic overlay |
| `title_lockup.py` | FIGlet titles with optimal word splitting, and the native-type cover lockup |
| `escp_qr.py` | QR codes in `ESC L` bit-image mode down to the 2x1 dot module |
| `compositor.py` | a whole chapter composed for print, header and body in one continuous flow |

## Dependencies

```txt
pillow numpy pyfiglet qrcode
```

All pure Python. All output is deterministic under a fixed seed.

## Shared preset

All payloads open with the ART preamble. Reset, condensed 17.1 cpi, 8 lines per inch, page length 44 lines (one form), left margin 8 columns, 124 usable columns.

## Rules encoded here

1. Text is drawn by code, never by the diffusion model.
2. A title that exceeds the page width splits at the best word boundary, two lines, three when needed, and never cuts a glyph.
3. QR payloads are short fixed-length redirects, never raw source URLs.
4. Verdicts about print quality come from paper. Screen previews of dot-matrix output mislead in both directions.
5. A chapter is one continuous object. Header and body share the same form, and the only form feed comes after the colophon. An earlier draft gave the header a form of its own and wasted two thirds of a sheet per chapter.
6. Chapter numbers are padded to four digits. The redirect payload stays at 27 characters and every code in the run is version 3. Three digits would start the run at version 2 and jump to version 3 at chapter 1000, mid exhibition.
