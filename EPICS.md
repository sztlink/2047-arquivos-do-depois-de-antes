# Epics

This roadmap organizes the public research archive for **Projeto 2047 / Arquivo Terra Viva**.

The project is no longer only an apparatus that prints AI output. It is a long-duration writing machine: a system that reads present signals, writes a continuous novel set in 2047 in chapters, calibrates their sonic cadence through szt.link, performs them through a dot-matrix printer, and accumulates paper as a living archive.

This file is a public roadmap. It does not expose private production material, institutional documents, budgets, or closed co-authorial process.

## Current target

Move the repository from **v0.2.0 (portal live, voice settled)** toward **v0.3.0: generative loop and controller proof**.

The next public milestone should demonstrate the logic of:

```txt
source -> chapter -> sonic score -> print simulation -> ledger record
```

before depending on the physical FX-2190.

---

## Epic 0 - Orientation and canon

**Status:** largely done.

**Goal**  
Create a fast entry point for visitors, curators, researchers, and future collaborators.

**Current outputs**

- `README.md`
- `START-HERE.md`
- Short thesis
- Public/private boundary
- Reading path

**Remaining outputs**

- Optional glossary of key terms.
- Optional v0.2 status block.

**Felipe input needed**

- What should a stranger understand in the first 3 minutes?
- Which phrase should lead as the project evolves?
- When should the repo stop saying preliminary and start saying active research archive?

**Definition of done**

A new reader can understand what the repo is, what it is not, and where to start without reading every file.

---

## Epic 1 - Dot-matrix printer as archive apparatus

**Status:** started.

**Goal**  
Document the printer as the material heart of the work, not as nostalgic scenography.

**Current outputs**

- `01-apparatus/dot-matrix-printer.md`
- `01-apparatus/printer-research/README.md`
- `01-apparatus/printer-research/dot-matrix-as-archive-apparatus.md`
- `01-apparatus/printer-research/fx-2190-calibration-notes.md`
- `01-apparatus/printer-research/cups-escp-pipeline.md`
- `01-apparatus/printer-research/continuous-paper.md`
- `01-apparatus/printer-research/encoding-and-typography.md`
- `01-apparatus/printer-research/failure-modes.md`

**Remaining outputs**

- Physical width test receipt.
- Accent proof receipt.
- Photo / scan of first public proof.
- Audio note or sonic observation from real printer output.

**Felipe input needed**

- Is the FX-2190 only the prototype or still a candidate final printer?
- Should Portuguese accent failure be solved invisibly or preserved as material evidence?
- How should paper accumulate in space?
- Should the printer be called witness, percussion, archive machine, bureaucratic machine, or something else after physical tests?

**Definition of done**

The printer reads as a conceptual, sonic, and technical apparatus with enough specificity to support prototypes and future exhibition decisions.

---

## Epic 2 - Peer field and related practices

**Status:** done for v0.1.0, expandable.

**Goal**  
Position the project near relevant artistic, technical, and theoretical fields without reducing it to influence lists.

**Current outputs**

- `00-concept/peer-field.md`
- Initial verified links for key references.

**Remaining outputs**

- Expand Latin American and Brazilian references.
- Add printer / teletype artworks.
- Add rare earth and urban mining references.
- Add generative literature and machine writing references.

**Felipe input needed**

- Which peers feel alive, not merely academically correct?
- Which references are too close, too distant, or distracting?
- Should this become a formal bibliography later?

**Definition of done**

A reader can locate the project among media art, AI criticism, archive studies, material computation, and extractive infrastructure without mistaking it for a derivative work.

---

## Epic 3 - Diagrams and visual grammar

**Status:** started.

**Goal**  
Give the repo visual clarity through public, redrawn diagrams.

**Current outputs**

- `05-diagrams/apparatus-flow.svg`
- `05-diagrams/archive-layers.svg`
- `05-diagrams/material-stack.svg`
- `05-diagrams/README.md`

**Remaining outputs**

- Continue design research from `06-prototypes/command-center/DESIGN-DIRECTION.md`.
- `05-diagrams/generative-loop.svg`
- `05-diagrams/sonic-score.svg`
- `05-diagrams/controller-runtime.svg`
- `05-diagrams/printer-archive-flow.svg`
- Optional future physical layout diagram only after public clearance.

**Felipe input needed**

- Should the next diagram be about score, controller, or generative loop?
- Should diagrams remain warm editorial SVGs or become more schematic/technical?
- Should the old server / e-waste body appear in diagrams before the hardware is chosen?

**Definition of done**

The repo has diagrams that can travel into a presentation, article, or future publication without exposing private material.

---

## Epic 4 - Generative dramaturgy and sonic score

**Status:** started.

**Goal**  
Define how the machine writes short stories without becoming an unconstrained chatbot, and how szt.link calibrates their sonic performance.

**Current outputs**

- `02-generative-system/pipeline.md`
- `02-generative-system/source-curation-panel.md`
- `02-generative-system/memory-and-state.md`
- `02-generative-system/dramaturgical-constraints.md`
- `02-generative-system/sonic-cadence-and-score.md`
- `02-generative-system/source-ledger.md`
- `02-generative-system/print-ledger-schema.md`
- `02-generative-system/fallback-modes.md`
- `02-generative-system/story-packet-schema.md`
- `02-generative-system/score-vocabulary.md`

**Remaining outputs**

- Public receipts from future physical tests
- `02-generative-system/refusal-policy.md`
- `03-field-notes/YYYY-MM-generative-loop-smoke.md`

**Felipe input needed**

- What makes a 2047 story good enough to print?
- How much literary beauty is allowed before the work becomes ornamental?
- How dry or poetic should the machine be?
- Should the score be visible in the printed output or only internal?
- What is the role of silence: listening, refusal, mourning, suspense, or all of these?

**Definition of done**

The generative layer has a clear form: short story plus score plus ledger plus refusal. The printer is treated as performance, not output device only.

---

## Epic 5 - Model voice and corpus

**Status:** started.

**Goal**  
Define whether and how the project uses a situated model voice rather than a generic art-and-technology assistant.

**Current outputs**

- `02-generative-system/model-voice-and-training.md`
- `02-generative-system/corpus-policy.md`
- `02-generative-system/fine-tuning-vs-rag.md`
- `02-generative-system/evaluation-prompts.md`

**Remaining outputs**

- `02-generative-system/rights-and-clearance.md`
- Optional private corpus inventory, not for this public repo unless fully cleared.

**Felipe input needed**

- Which texts by Giselle are cleared for model training, if any?
- Which texts by Felipe are cleared for model training?
- Which szt.link material can be sanitized and used?
- Should the model weights remain private?
- Is the goal voice, reasoning pattern, output schema, cadence, or all of these?
- What must not be imitated?

**Definition of done**

The repo distinguishes training, retrieval, corpus, rights, evaluation, and authorship. It does not treat LLM conversations as the primary training target.

---

## Epic 6 - Long-duration local controller

**Status:** started.

**Goal**  
Specify the physical runtime machine that stays with the printer across the exhibition period.

The duration is **not confirmed** in the public archive. Do not assume 100 days or 6 months until institutional confirmation.

**Current outputs**

- `01-apparatus/local-controller.md`
- `01-apparatus/runtime-requirements.md`
- `01-apparatus/printer-connection.md`
- `01-apparatus/controller-recovery.md`
- `01-apparatus/process-supervision.md`
- `01-apparatus/local-logs.md`
- controller notes inside `01-apparatus/system-overview.md`

**Remaining outputs**

- Public runtime receipts from future tests

**Felipe input needed**

- Is the controller a mini PC, old enterprise server, recovered computer, or Raspberry Pi-class device?
- Should the functioning controller be visible?
- What is acceptable downtime during the exhibition?
- What must happen if internet fails?
- What must happen if the printer jams?
- Who can physically restart or stop the machine?

**Definition of done**

The controller is specified as runtime infrastructure: replaceable, observable, recoverable, connected to printer, and capable of running the archive without exposing private infrastructure.

---

## Epic 7 - Hardware and e-waste body

**Status:** started conceptually, not yet specified.

**Goal**  
Specify the material body of the installation without turning e-waste into generic cyberpunk decoration.

This epic is separate from the local controller. The controller is functional runtime infrastructure. The e-waste body is material argument, scenography, and evidence. They may overlap, but they are not the same layer.

**Current outputs**

- `01-apparatus/hardware-ewaste-scenography.md`
- related notes in `01-apparatus/local-controller.md`

**Remaining outputs**

- `01-apparatus/hardware-body.md`
- `01-apparatus/e-waste-sourcing-ethics.md`
- `01-apparatus/living-and-dead-hardware.md`
- Public checklist of possible components by category, without suppliers or negotiation details.

**Felipe input needed**

- Which dead components matter visually or historically?
- Should provenance labels be part of the work?
- How much should the work confess remote computation if cloud APIs are used?
- Should the old server be alive, dead, or both through paired machines?

**Definition of done**

The hardware body is described as material argument, not decoration.

---

## Epic 8 - Prototype receipts

**Status:** started.

**Goal**  
Document tests as receipts: small, factual, reproducible fragments of the apparatus becoming material.

**Current outputs**

- `03-field-notes/2026-05-command-center-smoke.md`
- `03-field-notes/2026-05-story-packet-smoke.md`
- `assets/prototype-screenshots/command-center-v2-2026-05-17.png`
- `06-prototypes/story-packets/`

**Remaining outputs**

- `03-field-notes/YYYY-MM-generative-loop-smoke.md`
- `03-field-notes/YYYY-MM-terminal-print-simulation.md`
- `03-field-notes/YYYY-MM-printer-smoke-test.md`
- `03-field-notes/YYYY-MM-paper-archive-test.md`
- Optional public media folder for sanitized photos, scans, audio notes.

**Recommended first receipt**

A no-printer generative loop smoke test:

```txt
source
  -> short story
  -> sonic score JSON
  -> terminal print simulation
  -> ledger record
```

**Felipe input needed**

- Which first test matters most: terminal simulation, model output, score, ledger, or printer?
- Can generated sample stories be public?
- Should failed generated stories be preserved as evidence?
- What minimum test would make the project feel real in the body?

**Definition of done**

The repository contains at least one public receipt with setup, input, output, score, failure or refusal, observation, and next action.

---

## Epic 9 - Citation, release, and preservation layer

**Status:** v0.1.0 done.

**Goal**  
Make the repo citable as a stable public research artifact.

**Current outputs**

- `CHANGELOG.md`
- `CITATION.cff`
- `MANIFEST.md`
- Git tag `v0.1.0`
- GitHub Release `v0.1.0`

**Remaining outputs**

- `v0.2.0` release after first generative-loop receipt or controller proof.
- Optional Zenodo DOI later, only after review.
- Expanded manifest for future media artifacts.

**Felipe input needed**

- What deserves v0.2.0: generative-loop smoke, model/corpus policy, controller spec, or printer receipt?
- When should this become DOI-citable?
- Should release notes stay technical or become more essayistic?

**Definition of done**

The archive has stable versions that can be referenced in academic, curatorial, or public contexts.

---

## Suggested working order from here

1. Epic 8 - no-printer generative-loop smoke test.
2. Epic 4 - story packet schema and score vocabulary.
3. Epic 6 - controller runtime requirements.
4. Epic 5 - corpus policy and fine-tuning versus RAG.
5. Epic 7 - hardware and e-waste body.
6. Epic 1 - physical FX-2190 receipt.
7. Epic 9 - v0.2.0 release.

## Rule for all epics

Do not publish private process.  
Do not publish institutional material.  
Do not assume exhibition duration before confirmation.  
Do not freeze the artwork prematurely.  
Make the apparatus legible.  
Let caveats travel with the artifacts.
