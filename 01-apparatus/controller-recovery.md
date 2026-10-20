# Controller recovery

> **Historical note (October 2026).** Written during the research and rehearsal phase of the work, then called *Projeto 2047 / Arquivo Terra Viva*, and kept as process. Some of it no longer describes the work as it runs. For the current apparatus see `../03-field-notes/2026-10-lq-590-qr-and-declared-cost.md`, `../03-field-notes/2026-10-video-wall.md`, and `../03-field-notes/2026-10-opening-at-casa-firjan.md`.

This file defines recovery behavior for the long-duration controller of **Projeto 2047 / Arquivo Terra Viva**.

It is public research documentation. It does not expose private infrastructure, credentials, hostnames, IPs, or deployment details.

## Purpose

The controller must fail in a way that preserves the apparatus.

Recovery is not only uptime. Recovery is the ability to know what happened, what was printed, what was refused, what failed, and what must not be repeated silently.

## Recovery principle

```txt
Do not print without a valid packet.
Do not print without a writable ledger.
Do not resume without knowing the last state.
Do not hide failure from the archive.
```

## State snapshot

The controller should persist a small state snapshot after every state transition.

Suggested fields:

```json
{
  "controller_version": "...",
  "current_state": "REPOUSO | ESCUTA | ENTRADA | ESCRITA | PARTITURA | INSCRIÇÃO | SILÊNCIO | RECUSA | FALHA | MANUTENÇÃO | ARQUIVO",
  "last_packet_id": "...",
  "last_inscription_id": "...",
  "last_receipt_id": "...",
  "last_successful_state": "...",
  "printer_profile": "simulation | fx-2190",
  "printer_state": "unknown | ready | printing | fault | offline",
  "ledger_writable": true,
  "requires_maintenance": false,
  "updated_at": "..."
}
```

## Startup behavior

On startup, the controller should:

1. Load configuration.
2. Check ledger path.
3. Read last state snapshot.
4. Inspect last packet if present.
5. Check whether the last cycle was complete.
6. Check printer availability if in physical mode.
7. Enter one of:
   - `REPOUSO`;
   - `MANUTENÇÃO`;
   - `FALHA`;
   - `ARQUIVO` repair mode.

It should not immediately print after restart.

## Interrupted cycle recovery

If a cycle was interrupted before inscription:

- preserve packet;
- mark event as interrupted;
- do not print automatically;
- require controller validation before retry.

If interrupted during physical inscription:

- mark possible partial print;
- do not reprint automatically;
- require human maintenance or explicit retry policy;
- append fault ledger entry.

If interrupted after print but before receipt:

- generate receipt from packet and print ledger if possible;
- mark receipt as reconstructed;
- preserve audit note.

## Printer fault recovery

Fault states:

- offline;
- paper out;
- paper path interrupted;
- weak ribbon;
- spool failed;
- partial print;
- encoding mismatch;
- unknown.

Recovery behavior:

1. Stop print queue.
2. Preserve current packet.
3. Write fault ledger entry.
4. Generate public-safe fault receipt if possible.
5. Enter `MANUTENÇÃO`.
6. Wait for explicit reset or maintenance action.

## Ledger failure recovery

If ledger is not writable:

- stop cycle;
- do not print;
- enter `FALHA`;
- write emergency local note if possible;
- require maintenance.

A physical print without ledger is invalid for this apparatus.

## Model or retrieval failure recovery

If model call fails:

- retry only within a small limit;
- if still failing, enter `SILÊNCIO` or `FALHA` depending on context;
- do not write from untraceable memory;
- log model failure.

If retrieval fails:

- do not invent sources;
- use approved project canon only if policy allows;
- otherwise enter `SILÊNCIO`;
- log retrieval failure.

## Manual maintenance actions

Maintenance actions should be logged as events:

- paper loaded;
- paper path cleared;
- ribbon changed;
- printer restarted;
- controller restarted;
- ledger repaired;
- network restored;
- model endpoint restored;
- test print performed.

Each action should record:

```txt
timestamp
action
operator role, not personal identity if public
packet affected, if any
result
public-safe note
```

## What not to recover automatically

Do not automatically:

- reprint a story after unknown interruption;
- print a held candidate without validation;
- bypass source or rights checks;
- ignore a ledger write failure;
- turn private source into fallback text;
- switch to a new model without logging it;
- hide maintenance from the archive.

## Public receipt behavior

Faults and recovery events may produce public receipts if safe.

Public receipts should never expose:

- private source contents;
- credentials;
- internal host details;
- personal maintenance details;
- institutional logistics.

## Minimum v0.2 recovery test

A public-safe dry run should test:

1. Valid packet completes.
2. Refusal packet logs and does not print.
3. Fault packet generates no-print receipt.
4. Silence packet generates no-print receipt.
5. Missing ledger causes stop.
6. Interrupted cycle is not auto-printed.

The first four are represented by:

- `../06-prototypes/story-packets/`

## Working conclusion

The controller should recover like an archivist, not like a content service. Its job is to preserve the truth of the apparatus event, including interruption.
