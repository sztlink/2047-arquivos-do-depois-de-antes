# Memory and state

> **Historical note (October 2026).** Written during the research and rehearsal phase of the work, then called *Projeto 2047 / Arquivo Terra Viva*, and kept as process. Some of it no longer describes the work as it runs. For the current apparatus see `../03-field-notes/2026-09-restart-from-zero-and-the-2047-structure.md` and `../03-field-notes/2026-10-opening-at-casa-firjan.md`.

The generative system should not rely only on a long prompt. It should maintain explicit external memory.

## Why external state

A long context window can contain information without causing the model to use it correctly. For a live artwork, this matters because the system must preserve continuity, avoid uncontrolled drift, and remain accountable to the work's language.

## State layers

Possible state layers:

- **Project bible:** stable conceptual rules and vocabulary.
- **Fictional world state:** names, events, dates, places, institutions, and recurring motifs from 2047.
- **Source ledger:** public signals that influenced generated stories.
- **Story ledger:** generated, edited, approved, rejected, and unprinted stories.
- **Score ledger:** cadence, density, line width, silence, repetition, and print rhythm.
- **Print ledger:** what was printed, when, under which system state, and with which score.
- **Silence ledger:** listening, refusal, mourning, printer pause, and no-signal intervals.
- **Failure ledger:** printer errors, network errors, model failures, interruptions.
- **Daily digest:** compressed state for the next cycle.

## Traceability

Every printed fragment should ideally be traceable to:

- generation time;
- source conditions;
- system version;
- memory state;
- score parameters;
- output destination;
- whether it was printed, refused, skipped, or failed.

## Archive question

The system should decide what becomes public evidence and what remains operational residue.

Not every log should be public. Not every trace should be preserved forever. The archive policy is part of the artwork's ethics.
