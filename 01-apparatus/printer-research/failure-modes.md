# Failure modes

> **Historical note (October 2026).** Written during the research and rehearsal phase of the work, then called *Projeto 2047 / Arquivo Terra Viva*, and kept as process. Some of it no longer describes the work as it runs. For the current apparatus see `../../03-field-notes/2026-10-lq-590-qr-and-declared-cost.md`, `../../03-field-notes/2026-10-video-wall.md`, and `../../03-field-notes/2026-10-opening-at-casa-firjan.md`.

The printer apparatus will fail. The question is which failures must be prevented, which must be logged, and which may become part of the work.

## Technical failures to prevent

### Uncontrolled paper output

A misconfigured print path can cause program text or printer commands to be printed literally, wasting paper and losing control of the apparatus.

Prevention:

- use known-safe raw payloads for the artwork;
- test with short jobs;
- clear queue before long runs;
- avoid generic desktop print paths for continuous output.

### Wrong encoding

Accented text can become mojibake.

Prevention:

- print accent proofs;
- choose explicit encoding;
- keep ASCII-only fallback mode.

### Persistent printer state

Dot-matrix printers may keep modes between jobs: condensed, CPI, margins, line spacing, page length.

Prevention:

- always send a preamble;
- include reset;
- verify width with a short proof;
- record current preset.

### Width collapse

A wide ASCII layout may collapse into a narrower physical area if condensed mode, margins, page settings, or hardware limits interfere.

Prevention:

- print width test before artwork;
- measure physical output;
- document character count;
- do not assume previous state still holds.

## Physical failures to expect

- paper misalignment;
- tractor feed drift;
- ribbon wear;
- faint output;
- jams;
- missing dots;
- uneven density;
- pause / offline panel state;
- tear-off mismatch;
- overheating or mechanical fatigue in long runs.

## Failures that may matter artistically

Some failures expose the apparatus:

- repeated lines;
- faded ribbon;
- partial fragments;
- broken accents;
- misregistration;
- interrupted output;
- paper scars;
- operator marks;
- queue timestamps.

These should not be romanticized automatically. But they should be documented before being discarded.

## Receipt format for future tests

Every prototype test should record:

```txt
date:
printer:
mode:
preamble:
encoding:
paper:
input source:
payload summary:
expected output:
actual output:
failure observed:
photo/scan:
next action:
```

## Current open failure

The most important unresolved issue is printable width. The FX-2190 remains the current prototype, but it needs another measured width test before it can be treated as the final printer body.
