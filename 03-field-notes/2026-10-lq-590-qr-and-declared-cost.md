# Field note . October 2026 . A 24-pin printer, a QR per page, and a declared cost

Status. Field note, public and sanitized. Figures are measured, unless marked as estimates.

## The printer changes

On October 4, 2026 an **Epson LQ-590**, a 24-pin ESC/P2 dot-matrix printer, replaced the Epson FX-2190 as the printer of the work. The FX-2190, the 9-pin wide-carriage machine documented in `../01-apparatus/printer-research/`, printed the August rehearsals and remains as an emergency reserve. Going back to it is a single change in the score.

Four LQ-590 units were found and prepared. One prints in the room and another stands configured on site as the technical reserve.

The change answered an open question of the May research (`../01-apparatus/printer-research/dot-matrix-as-archive-apparatus.md`): a cleaner 24-pin head could carry a whole designed page, image included, and not only text.

## A page, not a printout

Each chapter is one page that crosses the perforation of two sheets of continuous form paper (240 by 140 mm each). The page layout was chosen on paper by Felipe Sztutman and reviewed by Giselle Beiguelman. From top to bottom:

- the mark of the work and a **16 mm QR code** that leads to the same chapter online, at `heretica.xyz/f/NNNN`;
- the chapter number and its address;
- the source, with the real headline, the publication, and the date;
- the title, in double width and height;
- an image of scene A;
- the text, in Roman pica, with the sentence anchored to scene B underlined and followed by the image of scene B;
- the **declared cost**, the signature of the authors, and a stamp.

The images are frames of the two video scenes of the chapter, in a paper variant on a white field, printed at 180 dpi. The QR follows the limits measured in `../01-apparatus/qr-at-the-needle-limit.md`, with one short fixed-length path per chapter.

## Printed in rhythm

There is no print queue. The page is composed into raw ESC/P2 and sent directly to the printer over USB, at a pace. The whole page is typed in rhythm, the text character by character and the images pass by pass, so a dark image takes longer than a light one. A chapter takes about twenty-five minutes on paper, which is the open day divided by twenty-three. The noise of the needle is part of the work, and the printer's quiet mode stays off.

A print that is interrupted is not lost. The page in progress keeps a journal, and after a power cut the machine waits for a human confirmation before it resumes.

## The declared cost

The foot of every page states what the chapter cost to exist.

- **Tokens** of generation, every attempt included, not only the one that was printed.
- **Watt-hours of video**, measured at the GPU while the two scenes were rendered.
- **Watt-hours of printing**, measured at the socket of the printer while the page was typed.

Averages over the first 109 chapters of the season, October 15 to 20, 2026:

| measure | average | range |
|---|---|---|
| printer, measured at the socket | 6.4 Wh | 5.7 to 7.3 |
| exhibition computer, measured at the socket during the page | 96 Wh | 36 to 109 |
| video, measured at the GPU | 86 Wh | 65 to 112 |
| tokens of generation per chapter | about 85 thousand | 28 thousand to 311 thousand |
| words per chapter | 769 | 498 to 1051 |

Water is not measured. It is **estimated** at 2 mL per thousand tokens of cloud generation, anchored on Jegham et al. (2025), with Li et al. (2023) as context. The site keeps the line between measured and estimated visible: local machines are measured, cloud models are estimated. The full account is at <https://heretica.xyz/consumo.html>.

The printer, the machine that makes the paper, is the cheapest part of the page by an order of magnitude. That asymmetry is the argument of the work at the scale of one chapter.
