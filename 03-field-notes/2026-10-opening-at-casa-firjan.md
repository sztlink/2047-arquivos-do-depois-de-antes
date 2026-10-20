# Field note . October 2026 . The work opens at Casa Firjan

Status. Field note, public and sanitized. Figures are from the work's own print log, as of October 20, 2026.

## Opening

**2047: Arquivos do depois de antes** opened on October 15, 2026 at Casa Firjan, in Rio de Janeiro. It is on view until November 16, 2026. The installation was mounted in the days before the opening, and photographs of the room are on the site, in the Instalação section of <https://heretica.xyz>.

At the turn of the season the exhibition machine began a clean book. Chapter 0001, *Os quatro pequis*, follows Ilva, the verifier of the valley's water. The pages printed during the rehearsals of August and September remain archived as process. They do not count as the work and are not on the site.

## The room

- An Epson LQ-590 types the chapters on continuous paper, twenty-three a day, each page with its QR code and its declared cost (see `2026-10-lq-590-qr-and-declared-cost.md`).
- A projected video wall plays the two scenes of each chapter and captions the sentence being printed (see `2026-10-video-wall.md`).
- A laptop shows the public screen of what the narrator did not record.
- A LED sign carries the line of the work, *o futuro está sendo minerado agora*, the future is being mined now.
- The paper accumulates. The archive grows in the room at the speed of the needle.

## The machines, by role

The work is spread over a few machines, named here only by what they do.

- **The exhibition machine**, in the room. It holds the printer, renders video on one GPU and plays the wall on another, triages the news, keeps the diary of the season, watches itself, and restarts by itself after a power cut.
- **A render server in the studio**, in São Paulo, a second GPU for video.
- **A relay in the studio** that publishes the site every thirty minutes and supervises the room from afar.
- **An archive server** for backup and alerts.
- **The network of the room**, a 5G modem with a 4G reserve, and smart sockets that measure the printer and the computer and can restart the reserve modem when it hangs.

The writing is the only part that leaves the building, to a cloud model (see `2026-09-restart-from-zero-and-the-2047-structure.md`). Everything else happens in the room or in the studio.

## The site

<https://heretica.xyz> holds the novel as it is printed. A chapter enters the site together with its page in the room.

- **Capítulos**, every chapter at its own address, `/f/NNNN/`, with its text, scenes, source, and cost.
- **Vídeos**, the two scenes of every chapter.
- **Personagens**, the character sheets, which separate what the text said from what the agent completed and from the image that was approved.
- **Banco de dados**, the news the machine read, each linked to its origin.
- **Consumo**, the cost of the page, in water, energy, and tokens.
- **Créditos**, every model and machine involved, and what is measured or estimated.
- An English edition of everything, under `/en/`.

## First figures

By October 20, 2026, five days into the season:

- 109 chapters printed, numbered 0001 to 0109.
- 3512 news items in the source bank.
- Averages per chapter of 6.4 Wh at the printer, 86 Wh of video at the GPU, and about 85 thousand tokens of generation.

The novel will end at chapter 2047. At twenty-three chapters a day the exhibition will close long before that. What the room keeps is the beginning of a book whose arithmetic is already written, and the paper of every day it was open.
