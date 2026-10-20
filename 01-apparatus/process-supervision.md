# Process supervision

> **Historical note (October 2026).** Written during the research and rehearsal phase of the work, then called *Projeto 2047 / Arquivo Terra Viva*, and kept as process. Some of it no longer describes the work as it runs. For the current apparatus see `../03-field-notes/2026-10-lq-590-qr-and-declared-cost.md`, `../03-field-notes/2026-10-video-wall.md`, and `../03-field-notes/2026-10-opening-at-casa-firjan.md`.

This file defines public process supervision requirements for the long-duration runtime of **Projeto 2047 / Arquivo Terra Viva**.

It does not prescribe a final deployment stack. It defines what must be supervised regardless of implementation.

## Purpose

A long-duration apparatus needs supervision without becoming a corporate monitoring dashboard.

Process supervision should protect:

- continuity;
- recoverability;
- ledger integrity;
- printer safety;
- public/private boundaries;
- maintenance visibility.

## Processes to supervise

Minimum processes:

1. Controller runtime.
2. Story packet validator.
3. Receipt renderer.
4. Printer/spool worker.
5. Ledger writer.
6. Public state exporter for Mesa de Inscrição.
7. Optional model client.
8. Optional retrieval client.

Each process should have:

- name;
- version;
- status;
- last heartbeat;
- last error;
- restart policy;
- public-safe state.

## Heartbeat

Each active process should write a heartbeat.

Suggested heartbeat fields:

```json
{
  "process": "controller",
  "version": "...",
  "status": "ok | warning | fault | stopped",
  "state": "REPOUSO",
  "last_packet_id": "...",
  "updated_at": "...",
  "public_note": "..."
}
```

Heartbeat files should not contain secrets or private source text.

## Restart policy

Automatic restart is acceptable for stateless helper processes.

Automatic restart is risky for inscription.

Suggested policy:

| Process | Auto-restart | Notes |
| --- | --- | --- |
| public state exporter | yes | safe if read-only |
| receipt renderer | yes | deterministic |
| validator | yes | deterministic |
| model client | limited | log model/version changes |
| retrieval client | limited | do not invent sources |
| controller | cautious | must read recovery snapshot |
| printer worker | no or manual | avoid duplicate/partial print |
| ledger writer | no | stop if ledger unavailable |

## Public status vocabulary

Use apparatus language:

- `REPOUSO`
- `ESCUTA`
- `ENTRADA`
- `ESCRITA`
- `PARTITURA`
- `INSCRIÇÃO`
- `SILÊNCIO`
- `RECUSA`
- `FALHA`
- `MANUTENÇÃO`
- `ARQUIVO`

Avoid public status labels like:

- `healthy`;
- `degraded SaaS service`;
- `customer impact`;
- `KPI`;
- `AI throughput`.

## Alerts

Alerts should be generated for:

- ledger not writable;
- printer offline in physical mode;
- paper path interrupted;
- repeated invalid packets;
- model failures beyond retry limit;
- retrieval failures beyond retry limit;
- disk near full;
- public state exporter exposing restricted fields;
- unexpected physical print request.

Alerts should be operationally useful, not public spectacle.

## Logs

Supervision logs should record:

- process start/stop;
- restart;
- validation failure;
- print request;
- no-print decision;
- fault;
- maintenance;
- receipt generation;
- configuration change.

See:

- `local-logs.md`

## Minimal v0.2 supervision

For v0.2, no daemon is required.

A local smoke supervision pass is enough:

```txt
run-smoke.js
  -> generate packets
  -> validate packets
  -> render receipts
  -> render dry-run spool
  -> exit non-zero on failure
```

This is implemented in:

- `../06-prototypes/story-packets/run-smoke.js`

## Future implementation options

Possible later implementations:

- systemd user services;
- launchd on macOS;
- Node process supervisor;
- Python supervisor;
- small local web controller;
- hardware watchdog;
- manual operator checklist.

This public archive does not choose final infrastructure yet.

## Working conclusion

Supervision should not optimize content production. It should keep the apparatus accountable to state, paper, ledger, fault, refusal, and silence.
