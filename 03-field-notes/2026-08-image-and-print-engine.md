# Field note, August 2026. Image and print engine

> **Historical note (October 2026).** Written during the research and rehearsal phase of the work, then called *Projeto 2047 / Arquivo Terra Viva*, and kept as process. Some of it no longer describes the work as it runs. For the current apparatus see `./2026-10-lq-590-qr-and-declared-cost.md`, `./2026-10-video-wall.md`, and `./2026-10-opening-at-casa-firjan.md`.

This note records the week the visual side of **Projeto 2047 / Arquivo Terra Viva** became sovereign, and the week the printer became an organ of the machine.

It is public research documentation. It does not expose private infrastructure, credentials, hostnames, IPs, or deployment details.

## The image engine runs where the writer runs

The scene generator is a 12.9B turbo diffusion transformer quantized to 4-bit weights and 4-bit activations, running on the same 24GB GPU that hosts the writer model. The quantization runtime and its receipts are public in the companion repositories [krea2-nunchaku](https://github.com/sztlink/krea2-nunchaku) and [dead-channel](https://github.com/sztlink/dead-channel).

Measured on the exhibition GPU, warm.

| operation | time | peak VRAM |
|---|---|---|
| 512px, 8 steps | 2.7s | 18.4GB |
| 512px, 2 steps | 0.8s | 18.4GB |
| 1024px, 8 steps | 9.1s | 21.7GB |
| native 1920x1088, 8 steps | 22.5s | 17.2GB |
| hires chain per full-HD frame | ~15s | 17.2GB |

Native full HD fits because the text encoder is dropped from VRAM after the prompt is encoded once. Writer and image model do not coexist on the card. They alternate through checkpointed swaps, and the image pool for the exhibition is produced in studio sessions before opening. Cloud generation exists only as a named emergency, off by default.

## Structure from the coauthor, variation from the machine

Plain text-to-image lost the signature elements of the valley. Image-to-image over the coauthor's reference frames recovered them in one move, the terraced mine with muddy channels, the rain column over the datacenter wall, the tropical forest edge. The reference sets the structure and the seed sets the variation. There is no img2img pipeline for this architecture in the upstream library, so the SDEdit path was implemented directly against the flow-matching scheduler, noise injected at the strength sigma, packed latents passed through.

## The data register is a collage, not a filter

The second visual register composes rectangular fragments from a source bank, satellite storm imagery from the public record, generated scenes, procedural contour lines extracted from the images themselves, thermal blooms, and seeded corruption passes that stitch the fragments. Real headlines from the collector ride on top as a typographic ticker. All text is drawn by code after diffusion, never by the model, because diffusion corrupts letterforms and the machine should not fake its own records.

## The printer week

The 9-pin printer moved to direct USB on the exhibition host, and the print path became local to the machine that writes. Out of that week came the measured ESC/P presets (see `01-apparatus/escp-print-presets.md`), the chapter image rendered as ASCII on continuous form, the title lockup that mixes the printer's native double-height typeface with drawn relief lettering, and a scannable QR at the physical floor of the needle (see `01-apparatus/qr-at-the-needle-limit.md`).

The working tools are in `06-prototypes/print-pipeline/`.

Paper is the judge of everything in this register. The screen kept lying all week.
