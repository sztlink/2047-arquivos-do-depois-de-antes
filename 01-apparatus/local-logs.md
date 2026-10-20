# Local logs

> **Historical note (October 2026).** Written during the research and rehearsal phase of the work, then called *Projeto 2047 / Arquivo Terra Viva*, and kept as process. Some of it no longer describes the work as it runs. For the current apparatus see `../03-field-notes/2026-10-lq-590-qr-and-declared-cost.md`, `../03-field-notes/2026-10-video-wall.md`, and `../03-field-notes/2026-10-opening-at-casa-firjan.md`.

This file defines the public logging model for the long-duration apparatus of **Projeto 2047 / Arquivo Terra Viva**.

It does not expose real deployment paths, private infrastructure, or institutional logistics.

## Purpose

Logs are not paperwork added after the work. Logs are how the apparatus knows what it has done.

The logging layer should preserve:

- cycles;
- packets;
- inscriptions;
- refusals;
- silences;
- faults;
- maintenance;
- receipts;
- configuration changes.

## Logging principle

```txt
If it changes the apparatus state, it should be logged.
If it prints, refuses, fails, or enters silence, it should be logged.
If it cannot be logged, it should not print.
```

## Log categories

### Controller log

Records state transitions.

Fields:

```txt
timestamp
state_from
state_to
packet_id
event
public_note
internal_note_reference, if private
```

### Packet log

Stores story packet JSON or references to it.

Fields:

```txt
packet_id
status
created_at
source_refs
story_id
score_id
inscription_id
receipt_id
review flags
```

### Source log

Records source packet metadata.

Must not store private full text in public logs.

Fields:

```txt
source_id
source_type
rights_status
allowed_use
classification
summary
url or citation if public
risk_note
```

### Print log

Records physical or simulated inscription.

Fields:

```txt
inscription_id
packet_id
mode
printer_profile
line_width
encoding
printable
result
line_count
fault_id, if any
```

### Refusal log

Records refusal.

Fields:

```txt
packet_id
source_refs
reason
public_note
rights_status
review_required
receipt_id
```

### Silence log

Records silence as an event.

Fields:

```txt
packet_id
reason
silence_seconds
source_refs
public_note
receipt_id
```

### Fault log

Records technical and mechanical failures.

Fields:

```txt
fault_id
packet_id
inscription_id
fault_type
public_note
maintenance_required
resolved_at
resolution_note
```

### Maintenance log

Records intervention.

Fields:

```txt
maintenance_id
timestamp
action
component
operator_role
public_note
result
related_fault_id
```

### Receipt index

Records public-safe receipts.

Fields:

```txt
receipt_id
packet_id
public_status
safe_to_publish
path_or_url
created_at
```

## Format

Recommended formats:

- JSONL for append-only operational logs;
- JSON for packets;
- Markdown for public receipts;
- TXT for dry-run spool.

Example layout:

```txt
runtime/
  packets/
  receipts/
  spool/
  logs/
    controller.jsonl
    source.jsonl
    print.jsonl
    refusal.jsonl
    silence.jsonl
    fault.jsonl
    maintenance.jsonl
    receipts.jsonl
```

This layout is conceptual. Public exports should be sanitized.

## Public versus private logs

Public logs may include:

- packet id;
- public status;
- public-safe source summary;
- score fields;
- print mode;
- receipt path;
- refusal/fault/silence public note.

Private logs may include operational details that should not be published.

Never publish:

- credentials;
- API keys;
- internal IPs or hostnames;
- private source text;
- e-mails;
- WhatsApp or chat logs;
- budget or supplier information;
- institutional logistics;
- personal data;
- unapproved corpus.

## Append-only posture

Operational logs should prefer append-only writing.

If correction is needed:

- append a correction event;
- do not silently rewrite prior records;
- preserve the fact of correction.

## Rotation and retention

Long-duration runs may produce many logs.

Suggested policy:

- rotate logs by day or size;
- preserve daily checksum if needed;
- keep packets and receipts separate from raw process logs;
- export public receipts selectively;
- back up ledgers before deleting local raw logs.

## Validation

A cycle is not complete unless logs include:

- packet entry;
- ledger entry;
- receipt entry;
- print/refusal/fault/silence event.

A physical print is invalid if print log or packet log is missing.

## Relationship to public archive

The GitHub repository should not become the live operational log.

The public archive should receive selected receipts, field notes, and sanitized research outputs.

Live logs belong to the runtime layer.

## Minimum v0.2 log prototype

The current smoke prototype generates:

- packet JSON files;
- receipt Markdown files;
- dry-run spool TXT files.

Location:

- `../06-prototypes/story-packets/`

This is enough to validate the shape of future logs without exposing live infrastructure.

## Working conclusion

Logs are not secondary. They are the archive-form of operation. Without logs, the apparatus is only output. With logs, it becomes accountable to its own inscriptions, refusals, failures, and silences.
