# Printer connection

> **Historical note (October 2026).** Written during the research and rehearsal phase of the work, then called *Projeto 2047 / Arquivo Terra Viva*, and kept as process. Some of it no longer describes the work as it runs. For the current apparatus see `../03-field-notes/2026-10-lq-590-qr-and-declared-cost.md`, `../03-field-notes/2026-10-video-wall.md`, and `../03-field-notes/2026-10-opening-at-casa-firjan.md`.

This file documents the current public connection strategy for the dot-matrix printer layer of **Projeto 2047 / Arquivo Terra Viva**.

It does not confirm the final exhibition printer. It treats the Epson FX-2190 as a current prototype and research reference.

## Current position

Use the simplest reliable path first.

```txt
controller -> USB -> CUPS or raw print path -> ESC/P text -> FX-2190 prototype
```

Parallel connection remains historically relevant, but it is not the first automation path unless testing proves a need.

Serial connection should be treated as optional and only considered if the actual interface hardware is validated.

## Why USB first

USB is preferred for prototype automation because it is:

- available on modern controllers;
- easier to test from Linux/macOS environments;
- compatible with CUPS workflows;
- easier to replace if controller hardware changes;
- less dependent on rare adapters and legacy ports.

The conceptual value of parallel or serial connection should not override runtime reliability.

## Printer status

Prototype printer:

```txt
Epson FX-2190
```

Public role:

```txt
current prototype, not final validated exhibition printer
```

Conceptual role:

```txt
printer as witness
printer as inscription apparatus
printer as sonic/mechanical score performer
```

## Known prototype parameters

From prior research notes:

```txt
DOC mode: 80 columns at 10 cpi
ASCII/WIDE target: 100 columns at 12 cpi
ESC/P preamble candidate: ESC @ + DC2 + ESC M
```

There is still an unresolved width contradiction between earlier 100-column tests and a later narrower effective width observation.

Do not treat final line width as confirmed until a new physical proof is made.

## Encoding position

The apparatus writes in pt-BR, but the printer path may require encoding discipline.

Potential paths:

1. UTF-8 to rendered image or PDF, then print.
2. UTF-8 transliteration to ASCII-safe text.
3. ESC/P code page configuration for accented characters.
4. Hybrid: preserve pt-BR in ledger, print ASCII-safe variant if needed.

The public archive should preserve the difference between:

- authored text;
- printer-safe inscription text;
- ledger text;
- public receipt text.

Accent failure may become material evidence, but it should not be accidental. It must be an artistic and technical decision.

## Print modes

Possible modes:

### Terminal simulation

Used now.

No physical printer. Text is rendered in UI or terminal as simulated inscription.

### Dry-run spool

Formats printable text and writes a spool file, but does not send it to the printer.

Useful for:

- line width tests;
- encoding tests;
- receipt proofing;
- controller validation.

### Physical print

Sends output to the printer.

Requires explicit approval and runtime readiness.

Minimum checks:

- printer connected;
- paper loaded;
- ribbon usable;
- line width selected;
- encoding selected;
- story packet validated;
- `approved_for_physical_print = true`;
- ledger writable.

### No-print receipt

Used for refusal, silence, or fault.

May produce a public receipt without printing paper.

Future decision: whether refusal and silence should ever be printed physically.

## Inscription contract

The printer connection should consume only the `inscription` section of a story packet plus the printable story body.

Relevant fields:

```json
{
  "mode": "terminal_simulation | dry_run_spool | physical_print | no_print",
  "printer_profile": "simulation | fx-2190",
  "paper": "continuous | simulated | unknown",
  "encoding": "utf-8 | ascii-safe | escp",
  "line_width": 72,
  "printable": true,
  "reason_not_printable": null
}
```

The printer layer should not decide authorship, rights, source validity, or story quality. Those belong to controller validation and review.

## Faults to detect or record

Minimum fault vocabulary:

- printer not found;
- printer offline;
- paper path interrupted;
- paper out;
- ribbon weak;
- encoding mismatch;
- line width overflow;
- spool failure;
- CUPS failure;
- partial print;
- manual stop;
- controller restart during print.

Each fault should produce:

- timestamp;
- packet id if applicable;
- inscription id;
- printer profile;
- public-safe note;
- maintenance action if known.

## Paper constraints

The physical paper is not only a substrate. It defines the literary form.

The writing engine should respect:

- line width;
- blank line policy;
- story length;
- page/feed rhythm;
- silence after print;
- accumulation in space.

A story that does not fit paper constraints is not ready for inscription.

## Sonic constraints

The printer produces sound.

The print path should preserve enough timing information for the score:

- slow pulse;
- sparse density;
- burst;
- silence before;
- silence after;
- pauses between blocks;
- fault interruption.

If the technical print path buffers too much and erases rhythm, the sonic score may need to move to the controller layer rather than relying on printer mechanics alone.

## Public proof requirements

Before treating the FX-2190 path as validated, produce public-safe proof receipts:

1. Character width proof.
2. Accent proof.
3. Continuous paper feed proof.
4. Slow pulse / cadence proof.
5. Fault or manual stop proof.
6. Ledger to print proof.

Each proof should record:

- date;
- printer profile;
- connection path;
- line width;
- encoding;
- text sample type;
- result;
- failure if any;
- next action.

Do not include private text in printer proofs.

## Recommended next technical test

Without touching the physical printer:

```txt
story packet JSON
  -> validate
  -> wrap text at target line width
  -> write printer-safe TXT spool
  -> render receipt
```

With the physical printer, after approval:

```txt
ASCII-safe calibration story
  -> dry-run spool
  -> physical FX-2190 proof
  -> scan or photo
  -> public receipt
```

## Open decisions

These remain open:

- final exhibition printer;
- final line width;
- whether accents must print correctly or may fail materially;
- whether refusal/silence produces paper output;
- whether the controller is next to the printer;
- whether print timing should be controlled line by line;
- whether printed source citations appear on paper, ledger only, or both.

## Working conclusion

The printer connection is not only an output path. It is the interface between language, score, paper, failure, and public archive.
