# Changelog

All notable public changes to this research archive will be documented here.

This repository follows semantic-ish research archive versions: `vMAJOR.MINOR.PATCH`, where minor versions may mark new public research blocks rather than software features.

## [v0.5.0] - 2026-10-20

The work opened. **2047: Arquivos do depois de antes** is on view at Casa Firjan, Rio de Janeiro, from October 15 to November 16, 2026, and online at <https://heretica.xyz>.

### Changed

- The repository is renamed from `2047-terra-viva-archive` to `2047-arquivos-do-depois-de-antes`. The old address redirects. The GitHub Pages address of the command center prototype changed with it.
- README, START-HERE, NOTICE, EPICS, and CITATION rewritten for the current title, the exhibition, and the live site. *Projeto 2047 / Arquivo Terra Viva* is recorded as the working title until August 2026.
- Research-phase files in `00-concept/`, `01-apparatus/`, `02-generative-system/`, and `06-prototypes/` carry a historical banner pointing to the current notes. Their content is kept as process.
- Diagrams name the Epson LQ-590 and the split between cloud writing and local triage and video.
- MANIFEST regenerated for every tracked file.

### Added

- Field notes:
  - `03-field-notes/2026-09-title-and-narrator.md` (from working title to title, and Herética Ablation)
  - `03-field-notes/2026-09-restart-from-zero-and-the-2047-structure.md` (restart from zero on August 22, the writing moves to a cloud model, 89 notebooks of 23, four vertices, the base of the season)
  - `03-field-notes/2026-10-lq-590-qr-and-declared-cost.md` (the 24-pin printer, the designed page, the QR per page, the declared cost and its first averages)
  - `03-field-notes/2026-10-video-wall.md` (two scenes per chapter, the local video engine, the wall program, the second screen)
  - `03-field-notes/2026-10-opening-at-casa-firjan.md` (the opening, the room, the machines by role, the site, first figures)

### Removed from the public text

- The coauthor's punctuation recipes in `02-generative-system/voice-construction-method.md`. The voice rules belong to her authorship.
- Internal hardening and compute details in `03-field-notes/2026-08-voice-trained-and-deployed.md`, as the v0.3.0 boundary already promised.
- The internal routine of the August calibration loop in `03-field-notes/2026-08-restart-and-coauthorial-calibration.md`.
- A reference to the content of institutional material in `02-generative-system/model-voice-and-training.md`.

### Recorded late

These were published on August 2 and 3, 2026 without a changelog entry: `01-apparatus/escp-print-presets.md`, `01-apparatus/qr-at-the-needle-limit.md`, `03-field-notes/2026-08-image-and-print-engine.md`, and `06-prototypes/print-pipeline/`. The tag `v0.4.0` was added to the commit of August 6, 2026.

## [v0.4.0] - 2026-08-06

The novel restarts from chapter 1 inside a daily coauthorial calibration loop.

### Added

- Field note:
  - `03-field-notes/2026-08-restart-and-coauthorial-calibration.md` (the coauthor's close reading distilled into engine rules, the sharpened world premise, the daily ten-chapter loop with blind-mixed engines, rehearsal material reclassified)

## [v0.3.0] - 2026-08-02

The voice is trained and the machine runs on its own host.

### Added

- Field note:
  - `03-field-notes/2026-08-voice-trained-and-deployed.md` (the model comparison the architecture prescribed, the voice adapter, deployment on the dedicated host, the complete apparatus running end to end, resilience after a real failure)

### Changed

- `02-generative-system/fine-tuning-vs-rag.md`: added the resolution of the prescribed comparison (a lightweight adapter adopted for form and cadence; the deployed pipeline is leaner than the structured-packet sketch).
- `02-generative-system/model-voice-and-training.md`: added the realized path and an honest correction on corpus composition.
- `02-generative-system/corpus-policy.md`: drafted Layer 7 (curated synthetic fictional material), a provisional category distinct from raw LLM output, with a cleared-origin condition and documented selection; updated the material-type table and the working position.
- README: status updated for the trained voice and the dedicated host.

### Open

- Layer 7 (curated synthetic fictional material) is declared provisional and awaits co-authorial ratification, since the working adapter's corpus is dominantly curated synthetic material anchored by co-authored seeds. The category names the reconciliation rather than closing it.

### Public boundary

- The novel's text, the adapter weights, live infrastructure details, and internal hardening specifics remain outside this repository.

## [v0.2.0] - 2026-07-14

The portal is live and the voice settles.

### Added

- Field note:
  - `03-field-notes/2026-07-portal-live-and-voice-settling.md`
- Generative system notes:
  - `02-generative-system/continuous-novel.md` (from fragments to one continuous novel set in 2047; cast, arc, news as pressure)
  - `02-generative-system/voice-construction-method.md` (the empirical voice loop: corpus with clearance, dosage versions, co-authorial lapidation, settled voice contract)
  - `02-generative-system/curation-autonomy-ladder.md` (living curation, evidence computed live, autonomy earned, measured, and revocable)
- Printer research:
  - `01-apparatus/printer-research/scout-references-2026-06.md` (scouted references on continuous printing and reactivated technical chains)

### Changed

- README: live portal link (<https://2047.szt.link>); repository map updated.
- EPICS: the machine writes a continuous novel in chapters, not short stories; current target moved to v0.3.0 (generative loop and controller proof).
- `.gitignore`: hardened against local secrets and nested private working clones.

## [v0.1.0] - 2026-05-17

Initial public research archive.

### Added

- Public README and scope boundary.
- `START-HERE.md` orientation file.
- `EPICS.md` roadmap.
- Concept files:
  - `00-concept/project-brief.md`
  - `00-concept/conceptual-frame.md`
  - `00-concept/peer-field.md`
  - `00-concept/references.md`
- Apparatus files:
  - `01-apparatus/system-overview.md`
  - `01-apparatus/dot-matrix-printer.md`
  - `01-apparatus/hardware-ewaste-scenography.md`
- Printer research block for the Epson FX-2190 prototype:
  - `01-apparatus/printer-research/README.md`
  - `01-apparatus/printer-research/dot-matrix-as-archive-apparatus.md`
  - `01-apparatus/printer-research/fx-2190-calibration-notes.md`
  - `01-apparatus/printer-research/cups-escp-pipeline.md`
  - `01-apparatus/printer-research/continuous-paper.md`
  - `01-apparatus/printer-research/encoding-and-typography.md`
  - `01-apparatus/printer-research/failure-modes.md`
- Generative system notes:
  - `02-generative-system/pipeline.md`
  - `02-generative-system/memory-and-state.md`
- Initial field note:
  - `03-field-notes/2026-05-initial-development.md`
- Archive policy:
  - `04-archive-policy/public-private-layers.md`
  - `04-archive-policy/redaction-policy.md`
- Public SVG diagrams:
  - `05-diagrams/apparatus-flow.svg`
  - `05-diagrams/archive-layers.svg`
  - `05-diagrams/material-stack.svg`
- Concept visuals:
  - `assets/concept-visuals/2047-printer-apparatus-concept.jpg`
  - `assets/concept-visuals/2047-paper-archive-concept.jpg`
  - `assets/concept-visuals/2047-generated-image-concept.jpg`
- `NOTICE.md` and `LICENSE.md`.
- `CITATION.cff` and `MANIFEST.md`.

### Public boundary

This release intentionally excludes private conversations, institutional documents, budgets, supplier details, internal infrastructure details, and unpublished third-party material.
