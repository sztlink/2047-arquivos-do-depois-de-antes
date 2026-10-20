# Print ledger schema

> **Historical note (October 2026).** Written during the research and rehearsal phase of the work, then called *Projeto 2047 / Arquivo Terra Viva*, and kept as process. Some of it no longer describes the work as it runs. For the current apparatus see `../03-field-notes/2026-09-restart-from-zero-and-the-2047-structure.md` and `../03-field-notes/2026-10-opening-at-casa-firjan.md`.

The print ledger records what becomes paper.

A story exists in the system before it is printed. Printing is a threshold. The ledger preserves that threshold.

## Print record

Draft schema:

```json
{
  "print_id": "prt_2047_000001",
  "story_id": "story_2047_000001",
  "printed_at": "2026-05-17T00:00:00Z",
  "fictional_date": "2047-...",
  "mode": "short_story | archive_fragment | testimony | bulletin | failure | silence",
  "source_refs": ["src_2026_000001"],
  "system_version": "v0.1.0",
  "prompt_version": "dramaturgy_v0.1",
  "score_version": "score_v0.1",
  "printer": {
    "model": "Epson FX-2190",
    "mode": "ascii-wide | doc | raw-text | unknown",
    "line_width": 72,
    "encoding": "ascii | cp850 | cp860 | iso-8859-1 | utf-8 | unknown",
    "form_feed": false
  },
  "score": {
    "tempo": "slow | medium | burst",
    "density": "sparse | regular | dense",
    "silence_before_seconds": 30,
    "silence_after_seconds": 90,
    "blank_line_policy": "breathing | compact | ledger",
    "repetition": "none | phrase | line | header"
  },
  "status": "printed | failed | skipped | refused",
  "failure_reason": null,
  "paper_position": null,
  "public_receipt": false,
  "notes": "..."
}
```

## Story versus print

The system should distinguish:

- generated story;
- approved story;
- scored story;
- printed story;
- failed print;
- refusal to print;
- silence event.

This distinction matters because the artwork is not only text. It is text crossing into machine, sound, paper, and archive.

## Silence record

Silence can be logged as an event:

```json
{
  "print_id": "silence_2047_000012",
  "mode": "silence",
  "reason": "refusal | listening | mourning | printer_pause | no_signal",
  "duration_seconds": 180,
  "system_version": "v0.1.0",
  "notes": "No story printed after weak source cluster."
}
```

## Public receipts

Not every print record becomes public. A public receipt may include:

- date;
- mode;
- redacted source categories;
- score summary;
- photo or scan;
- observed failure;
- next action.

It should not include private sources, credentials, internal addresses, or institutional details.
