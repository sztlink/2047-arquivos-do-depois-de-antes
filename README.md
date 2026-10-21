# 2047: Arquivos do depois de antes

**Technical-artistic research archive**  
Giselle Beiguelman and Felipe Sztutman

This repository documents the public, sanitized research layer of **2047: Arquivos do depois de antes**, an artwork by Giselle Beiguelman and Felipe Sztutman about artificial intelligence, extractive futures, rare earths, e-waste, obsolete media, and the material politics of computation.

The title is the work's only title, in Portuguese and in English. Until August 2026 the project ran under the working title *Projeto 2047 / Arquivo Terra Viva*, which is how the older notes in this archive still name it.

The repository focuses on Felipe Sztutman's technical-artistic process: the installation apparatus, the generative system, the dot-matrix printer, the video wall, the hardware body, and archive policy.

## Status

**On view.** The work opened on October 15, 2026 at Casa Firjan, Rio de Janeiro, and runs until November 15, 2026.

- The work online: <https://heretica.xyz> (chapters, videos, characters, sources, declared cost, credits, in Portuguese and English)
- Current milestone (October 2026, v0.5.0): the work opened. See `03-field-notes/2026-10-opening-at-casa-firjan.md`.

A machine writes a novel set in 2047, one chapter at a time, narrated by a synthetic narrator called Herética Ablation. Each chapter starts from a real news item of the present. During opening hours an Epson LQ-590 dot-matrix printer types each chapter as a full page on continuous paper, with a QR code that leads to the same chapter online and a declared cost at the foot of the page, measured in tokens and watt-hours. A video wall shows two scenes per chapter, generated locally, and captions the sentence the printer head is writing at that moment. The structure is 89 notebooks of 23 chapters, 2047 chapters in total, and 23 chapters fill one day of the room.

Older material is kept as process. Notes that describe the rehearsal apparatus (the Epson FX-2190, the print server, the short-story format, the command-center prototype, the local voice adapter) carry a historical banner and point to the current notes.

Historical surfaces, still online:

- Former portal of the machine (July to August 2026): <https://2047.szt.link>
- Command center prototype (May 2026): <https://sztlink.github.io/2047-arquivos-do-depois-de-antes/06-prototypes/command-center/>

Materials here are partial, redacted, and versioned as field notes. They are meant to preserve process without exposing private conversations, institutional negotiations, budgets, or closed documents.

## Short thesis

```txt
The machine does not produce the future.
It reveals the present being mined.
```

The sign in the exhibition room says it in one line: *the future is being mined now*.

## What this repository is

- A public research archive for the technical and material development of the work.
- A notebook for the apparatus: printer, video wall, generative pipeline, paper archive, and hardware body.
- A place to document references, diagrams, and decisions that can survive beyond a single exhibition context.
- A boundary object between artistic practice, media archaeology, AI systems, and archive politics.

## What this repository is not

- Not the full artwork. The novel lives on paper in the room and online at heretica.xyz.
- Not an official institutional press kit.
- Not a budget or procurement folder.
- Not a dump of private process.
- Not a publication of internal e-mails, messages, presentations, contracts, or closed curatorial material.
- Not a place for the coauthor's voice rules, which belong to her authorship.

## Repository map

```txt
README.md, START-HERE.md, EPICS.md, CHANGELOG.md
NOTICE.md, LICENSE.md, CITATION.cff, MANIFEST.md

00-concept/
  project-brief.md
  conceptual-frame.md
  peer-field.md
  references.md

01-apparatus/
  system-overview.md
  dot-matrix-printer.md
  escp-print-presets.md
  qr-at-the-needle-limit.md
  local-controller.md
  runtime-requirements.md
  controller-recovery.md
  process-supervision.md
  local-logs.md
  printer-connection.md
  hardware-ewaste-scenography.md
  printer-research/          (FX-2190 rehearsal research, historical)

02-generative-system/
  pipeline.md
  source-curation-panel.md
  curation-autonomy-ladder.md
  continuous-novel.md
  voice-construction-method.md
  memory-and-state.md
  dramaturgical-constraints.md
  sonic-cadence-and-score.md
  score-vocabulary.md
  model-voice-and-training.md
  corpus-policy.md
  fine-tuning-vs-rag.md
  evaluation-prompts.md
  story-packet-schema.md
  source-ledger.md
  print-ledger-schema.md
  fallback-modes.md

03-field-notes/
  2026-05-initial-development.md
  2026-05-command-center-smoke.md
  2026-05-story-packet-smoke.md
  2026-07-portal-live-and-voice-settling.md
  2026-08-voice-trained-and-deployed.md
  2026-08-image-and-print-engine.md
  2026-08-restart-and-coauthorial-calibration.md
  2026-09-title-and-narrator.md
  2026-09-restart-from-zero-and-the-2047-structure.md
  2026-10-lq-590-qr-and-declared-cost.md
  2026-10-video-wall.md
  2026-10-opening-at-casa-firjan.md

04-archive-policy/
  public-private-layers.md
  redaction-policy.md

05-diagrams/
  README.md
  apparatus-flow.svg
  archive-layers.svg
  material-stack.svg

06-prototypes/
  command-center/            (May 2026, historical)
  story-packets/             (May 2026, historical)
  print-pipeline/            (August 2026 compositor for the FX-2190)

assets/
  concept-visuals/
  prototype-screenshots/
```

## Authorship and scope

**2047: Arquivos do depois de antes** is an artwork by Giselle Beiguelman and Felipe Sztutman. Herética Ablation, the synthetic narrator, is a character created by both authors.

This repository is maintained by Felipe Sztutman as a public research archive for his technical-artistic layer of the process. It does not replace shared authorship, curatorial framing, or institutional materials.

## Public and private layers

The project has several layers of visibility:

- **Private process:** conversations, drafts, budgets, contracts, internal documents, production details, character sheets, maintenance camera images.
- **Research archive:** sanitized public notes, system diagrams, references, apparatus documentation.
- **Artwork and exhibition:** the printed paper in the room and the public site at heretica.xyz.

Only the research archive layer belongs here.

## License

All texts, concepts, diagrams, and images are **all rights reserved** unless explicitly stated otherwise.

Code in `06-prototypes/` has no open-source license yet. The video engine study is published separately, with its own license, at <https://github.com/sztlink/h3-consumer-bench>.
