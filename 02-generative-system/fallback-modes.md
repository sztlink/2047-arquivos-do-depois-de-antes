# Fallback modes

> **Historical note (October 2026).** Written during the research and rehearsal phase of the work, then called *Projeto 2047 / Arquivo Terra Viva*, and kept as process. Some of it no longer describes the work as it runs. For the current apparatus see `../03-field-notes/2026-09-restart-from-zero-and-the-2047-structure.md` and `../03-field-notes/2026-10-opening-at-casa-firjan.md`.

A live generative artwork must know how to fail.

The system should not print continuously just because it can. It should have fallback modes for weak sources, bad generations, network failure, printer failure, and excessive density in the room.

## No internet

If public signals are unavailable:

- use local memory only;
- mark sources as unavailable;
- print from a pre-approved reserve only if cadence requires it;
- otherwise enter listening silence.

Do not hallucinate current events.

## API or model failure

If the generative engine fails:

- do not print error dumps;
- log the failure internally;
- optionally print a short failure fragment only if it has been designed as part of the work;
- preserve the distinction between technical failure and fictional failure.

## Weak source cluster

If sources are shallow, repetitive, or too generic:

- reject the generation;
- wait;
- request stronger source material;
- print nothing.

Silence is better than generic dystopia.

## Generic story

If the story sounds like generic climate fiction or generic cyberpunk:

- reject;
- lower temperature or change constraints;
- re-anchor in source ledger;
- shorten;
- increase material specificity;
- require a score revision.

## Printer unavailable

If the printer is paused, jammed, offline, or out of paper:

- stop sending jobs;
- log the printer state;
- preserve generated story as unprinted;
- do not flush a backlog blindly when the printer returns;
- rescore the queue before printing.

## Encoding failure

If accents or symbols fail:

- preserve the failed proof;
- switch to ASCII fallback if needed;
- mark the encoding mode;
- do not print long text until proof is validated.

Encoding failure may become evidence, but it should not become uncontrolled noise.

## Sonic over-density

If the printer has been too active:

- increase silence;
- shorten future fragments;
- reduce density;
- print only headers or one-line fragments;
- or refuse output.

The room should not become a background office.

## Refusal mode

The system may explicitly decide not to print.

A refusal can be caused by:

- weak source;
- generic writing;
- private material risk;
- unresolved authorship boundary;
- excessive sonic density;
- printer instability;
- contradiction in memory;
- lack of meaningful transformation.

## Refusal record

Draft schema:

```json
{
  "event_id": "refusal_2047_000001",
  "time": "2026-05-17T00:00:00Z",
  "reason": "generic_story",
  "source_refs": ["src_2026_000004"],
  "action": "no_print",
  "silence_seconds": 240,
  "notes": "Text explained the concept instead of becoming a story."
}
```

## Rule

```txt
A failed print can become archive.
A generic print should not.
```
