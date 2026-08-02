# print-pipeline

Working tools for the printed visual register of **Projeto 2047 / Arquivo Terra Viva**. Everything here targets a 9-pin ESC/P dot-matrix printer on 240x140mm continuous forms and emits a raw ESC/P payload file. Send the payload to a raw print queue or device untouched. No driver should reinterpret it.

The measured presets behind these tools are documented in `01-apparatus/escp-print-presets.md` and `01-apparatus/qr-at-the-needle-limit.md`.

## Tools

| tool | what it prints |
|---|---|
| `ascii_register.py` | a chapter image as ASCII, density ramp, rotated banner, or 4-level serigraphy |
| `data_collage.py` | the data register, a seeded multi-source collage with typographic overlay |
| `title_lockup.py` | FIGlet titles with optimal word splitting, and the native-type cover lockup |
| `escp_qr.py` | QR codes in `ESC L` bit-image mode down to the 2x1 dot module |

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
