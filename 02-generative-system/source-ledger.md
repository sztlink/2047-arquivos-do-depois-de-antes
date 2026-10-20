# Source ledger

> **Historical note (October 2026).** Written during the research and rehearsal phase of the work, then called *Projeto 2047 / Arquivo Terra Viva*, and kept as process. Some of it no longer describes the work as it runs. For the current apparatus see `../03-field-notes/2026-09-restart-from-zero-and-the-2047-structure.md` and `../03-field-notes/2026-10-opening-at-casa-firjan.md`.

The source ledger records signals from the present before they become fictional material.

It is not a public news database. It is a traceability layer for the apparatus.

## Why a source ledger

The work transforms present signals into stories from 2047. Without a ledger, the system risks becoming generic. With a ledger, each printed story can remain connected to the present being mined.

## Source record

Draft schema:

```json
{
  "source_id": "src_2026_000001",
  "retrieved_at": "2026-05-17T00:00:00Z",
  "source_type": "news | report | manual | archive | sensor | system",
  "public_url": "https://example.org/...",
  "title": "...",
  "publisher_or_origin": "...",
  "keywords": ["rare earths", "e-waste", "AI infrastructure"],
  "themes": ["extraction", "memory", "water", "labor"],
  "use_status": "candidate | used | rejected | quarantined",
  "why_used": "...",
  "why_rejected": null,
  "redaction": "none | partial | private",
  "notes": "..."
}
```

## Public versus private sources

Public sources may be cited or logged.

Private sources must not be published. If a private source shapes the system, the public archive should only record a redacted category, not the source itself.

## Use status

### candidate

The source is available to the system but has not shaped a printed story.

### used

The source influenced at least one generated or printed story.

### rejected

The source was reviewed and rejected.

### quarantined

The source is relevant but too sensitive, unstable, misleading, or private for direct use.

## Relationship to fiction

The printed story does not need to cite sources on paper.

However, the internal system should know which present signals shaped the story. The source ledger protects the work from becoming free-floating dystopia.

## Open questions

- Should public URLs ever appear in the printed archive?
- Should source categories be printed instead of source names?
- Should a story be allowed to combine many weak sources, or only a few strong ones?
- Should manually introduced sources be marked as human intervention?
