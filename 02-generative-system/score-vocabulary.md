# Score vocabulary

> **Historical note (October 2026).** Written during the research and rehearsal phase of the work, then called *Projeto 2047 / Arquivo Terra Viva*, and kept as process. Some of it no longer describes the work as it runs. For the current apparatus see `../03-field-notes/2026-09-restart-from-zero-and-the-2047-structure.md` and `../03-field-notes/2026-10-opening-at-casa-firjan.md`.

This file defines a first controlled vocabulary for the sonic and mechanical score of **Projeto 2047 / Arquivo Terra Viva**.

The score is the bridge between story, printer, silence, and archive.

```txt
The story is the literary layer.
The cadence is the sonic layer.
szt.link calibrates the score between them.
```

## Purpose

A score vocabulary prevents the apparatus from treating printing as a neutral output operation.

Each story packet should carry score fields that shape:

- when inscription begins;
- how dense the printed text feels;
- how much silence surrounds it;
- whether the printer behaves as witness, recorder, interruption, or refusal;
- how ledger and receipt represent the event.

## Core score fields

From `story-packet-schema.md`:

```json
{
  "pulse": "slow | medium | burst | none",
  "density": "sparse | medium | dense | silence",
  "line_width": 72,
  "silence_before_seconds": 3,
  "silence_after_seconds": 90,
  "blank_line_policy": "breathing | compact | none",
  "print_rhythm_note": "..."
}
```

## Pulse

Pulse describes the perceived strike rhythm.

### `slow`

Use when the story should feel like testimony, witness, or bureaucratic delay.

Expected behavior:

- slow line release;
- pauses between blocks;
- strong presence of mechanical sound;
- useful for grief, evidence, maintenance, or aftermath.

### `medium`

Use for ordinary operation.

Expected behavior:

- readable mechanical pace;
- no dramatic acceleration;
- balanced silence.

### `burst`

Use for pressure, overload, interruption, or sudden signal.

Expected behavior:

- short dense emission;
- possible abrupt stop;
- should not become spectacle by default.

### `none`

Use for refusal, silence, or fault.

Expected behavior:

- no narrative inscription;
- possible receipt only;
- silence becomes the event.

## Density

Density describes how much text and sound occupies time and paper.

### `sparse`

Use for:

- short fragments;
- high silence;
- strong paper presence;
- archival restraint.

### `medium`

Use for:

- standard calibration story;
- moderate line count;
- balanced narrative and score.

### `dense`

Use rarely.

Potential use:

- overload;
- bureaucracy;
- accumulation;
- data pressure.

Risk:

- may turn into report, spectacle, or visual noise.

### `silence`

Use for:

- refusal;
- weak signal;
- paper fault;
- intentional pause;
- source below threshold.

## Silence

Silence is not empty time.

Silence can mean:

- listening;
- refusal;
- mourning;
- maintenance;
- cooling;
- source absence;
- ethical limit;
- apparatus recovery.

### `silence_before_seconds`

Time before inscription.

Use to represent:

- listening;
- source digestion;
- hesitation;
- calibration.

### `silence_after_seconds`

Time after inscription.

Use to represent:

- archive cooling;
- paper becoming record;
- refusal to immediately produce again;
- space for the printed event to settle.

## Blank line policy

### `breathing`

Default for calibration stories.

Allows blank lines between blocks, giving paper and sound time to breathe.

### `compact`

Use when density is intentional.

Risk: may feel like report or data dump.

### `none`

Use for receipt-only events, refusal, fault, or silence.

## Presets

### `witness_slow`

```json
{
  "pulse": "slow",
  "density": "sparse",
  "silence_before_seconds": 3,
  "silence_after_seconds": 90,
  "blank_line_policy": "breathing"
}
```

Use for most calibration stories.

### `bureaucratic_accumulation`

```json
{
  "pulse": "medium",
  "density": "dense",
  "silence_before_seconds": 1,
  "silence_after_seconds": 45,
  "blank_line_policy": "compact"
}
```

Use when the story should feel like administrative residue or inventory.

### `signal_burst`

```json
{
  "pulse": "burst",
  "density": "medium",
  "silence_before_seconds": 0,
  "silence_after_seconds": 120,
  "blank_line_policy": "breathing"
}
```

Use for sudden source pressure. Avoid overuse.

### `refusal_silence`

```json
{
  "pulse": "none",
  "density": "silence",
  "silence_before_seconds": 0,
  "silence_after_seconds": 180,
  "blank_line_policy": "none"
}
```

Use when the correct response is not to write.

### `maintenance_fault`

```json
{
  "pulse": "none",
  "density": "silence",
  "silence_before_seconds": 0,
  "silence_after_seconds": 60,
  "blank_line_policy": "none"
}
```

Use when mechanical interruption becomes the event.

## Score selection rules

Choose `witness_slow` when:

- source is valid;
- story is restrained;
- material consequence matters;
- paper should be felt.

Choose `bureaucratic_accumulation` when:

- repetition, inventory, or administrative residue is conceptually important;
- the apparatus should sound busier;
- the text is intentionally list-like.

Choose `signal_burst` when:

- the source has sudden urgency;
- the text is short;
- the print should interrupt the room.

Choose `refusal_silence` when:

- rights are unclear;
- source is private;
- authorship risk is high;
- the material would aestheticize harm;
- the source is too weak.

Choose `maintenance_fault` when:

- printer path fails;
- paper jams;
- controller cannot log;
- print would be unsafe or unverifiable.

## Anti-spectacle rule

The score should not make crisis entertaining.

Avoid using burst or dense modes just to create drama.

The apparatus should sound accountable, not theatrical by default.

## Relationship to printer

The score may be expressed through:

- actual printer timing;
- line release timing in the controller;
- pauses between text blocks;
- no-print silence;
- receipt timing;
- fault interruption.

If the physical printer buffers text and erases line timing, the controller should preserve score timing before or between print jobs.

## Relationship to Mesa de Inscrição

The Mesa de Inscrição can render score as:

- calibration table;
- pulse indicator;
- silence timer;
- state transition;
- public receipt field;
- line count;
- fault/refusal state.

The score should be visible enough to show that cadence is part of the work.

## Evaluation checks

A score is weak if:

- it is missing;
- it contradicts the story;
- it ignores refusal;
- it makes everything dramatic;
- it treats silence as zero;
- it cannot be rendered by printer or simulation;
- it has no ledger consequence.

A score is strong if:

- it changes the apparatus behavior;
- it matches story and source pressure;
- it respects paper constraints;
- it can refuse or remain silent;
- it can be logged and repeated as a test.

## Open decisions

- Should the final score vocabulary remain this small?
- Should score presets be visible to the audience?
- Should paper receipts include the score?
- Should silence be audible, visible, printed, or only logged?
- Should faults produce printed receipts after recovery?

## Working conclusion

The score is not metadata. It is the way the apparatus gives time, sound, and restraint to the act of inscription.
