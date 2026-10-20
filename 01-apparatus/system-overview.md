# System overview

> **Historical note (October 2026).** Written during the research and rehearsal phase of the work, then called *Projeto 2047 / Arquivo Terra Viva*, and kept as process. Some of it no longer describes the work as it runs. For the current apparatus see `../03-field-notes/2026-10-lq-590-qr-and-declared-cost.md`, `../03-field-notes/2026-10-video-wall.md`, and `../03-field-notes/2026-10-opening-at-casa-firjan.md`.

This is a preliminary apparatus map. It describes a possible technical structure, not a final exhibition specification.

## Functional blocks

```txt
public signals / curated sources
          |
          v
source collector
          |
          v
local project memory + dramaturgical rules
          |
          v
generative text engine
          |
          +--------------------+
          |                    |
          v                    v
dot-matrix printer      visual generation layer
          |                    |
          v                    v
continuous paper        screen / projection / future display
          |
          v
physical archive in formation
```

## Controller

The controller is the operational computer that coordinates sources, state, generation requests, sonic score, printing, logging, and optional visual output.

At this stage, the controller is not assumed to run all AI models locally. The system may be:

- remote API based;
- hybrid;
- local-first;
- fully local only if hardware, budget, stability, and exhibition constraints allow it.

For a full exhibition run, the controller should be understood as physical runtime infrastructure: it stays with the printer, keeps local ledgers, manages silence and failure, and sends print jobs. The model host may be somewhere else. The exact duration is not fixed in this public archive yet.

See `local-controller.md`.

## Printer

The dot-matrix printer is the primary material output device. It converts generative short stories into mechanical rhythm, ink, paper, and cumulative archive.

For the current Epson FX-2190 prototype, USB is the preferred practical connection path. Parallel belongs to the printer's historical media context but is not the preferred automation path for the first stable system.

## Hardware body

The installation may include a visible hardware body: rack, controller, dead switches, old drives, memory modules, cables, labels, and electronic debris.

The goal is not decoration. The goal is to expose computation as material infrastructure.

## Offline and failure posture

The apparatus should fail visibly and recoverably. If network access is unstable, the printer should still be able to continue from local memory, fallback fragments, or stored state.

The archive should preserve traces of the system's limits instead of hiding all instability.
