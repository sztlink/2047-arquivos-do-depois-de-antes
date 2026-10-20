# Runtime requirements

> **Historical note (October 2026).** Written during the research and rehearsal phase of the work, then called *Projeto 2047 / Arquivo Terra Viva*, and kept as process. Some of it no longer describes the work as it runs. For the current apparatus see `../03-field-notes/2026-10-lq-590-qr-and-declared-cost.md`, `../03-field-notes/2026-10-video-wall.md`, and `../03-field-notes/2026-10-opening-at-casa-firjan.md`.

This file defines public technical requirements for the physical runtime of **Projeto 2047 / Arquivo Terra Viva**.

It does not specify final exhibition logistics, final hardware, budget, suppliers, institutional constraints, or private infrastructure.

The exact exhibition duration is not confirmed in this archive. Requirements are therefore written for a **long-duration exhibition run**, not for a fixed number of days.

## Purpose

The runtime is the layer that keeps the apparatus alive.

It coordinates:

- source intake;
- story packet generation;
- score timing;
- printer or simulation state;
- ledgers;
- receipts;
- refusal;
- silence;
- fault;
- recovery.

The model is not the runtime.

```txt
The model writes.
The controller operates.
The ledger remembers.
The printer inscribes.
The authors calibrate.
```

## Runtime roles

### Controller

The controller conducts each cycle.

Responsibilities:

- start and stop cycles;
- load source packets;
- call model or mock generator;
- validate story packets;
- decide print, no-print, refusal, fault, or silence;
- send inscription instructions;
- append ledger records;
- produce public receipts;
- expose public-safe state to the Mesa de Inscrição.

### Model host

The model host may be:

- local;
- remote;
- hybrid;
- replaced by a deterministic mock during testing.

The runtime must not assume that model hosting and printer control happen on the same machine.

### Printer controller

The printer controller handles physical inscription.

Responsibilities:

- maintain printer connection;
- format text for paper width;
- apply encoding or ESC/P constraints;
- detect or record print faults;
- pause safely;
- resume or request maintenance.

### Ledger store

The ledger store records operation.

Minimum ledgers:

- source ledger;
- story packet log;
- print ledger;
- refusal log;
- fault log;
- receipt index.

### Public surface

The public surface may be:

- Mesa de Inscrição;
- printed paper;
- public receipt files;
- public research archive.

It must not expose private corpus, institutional documents, credentials, internal IPs, budgets, or unapproved material.

## Required runtime states

The runtime must represent these states:

```txt
REPOUSO
ESCUTA
ENTRADA
ESCRITA
PARTITURA
INSCRIÇÃO
SILÊNCIO
RECUSA
FALHA
MANUTENÇÃO
ARQUIVO
```

State transitions should be logged.

## Cycle contract

A normal simulated cycle:

```txt
REPOUSO
  -> ESCUTA
  -> ENTRADA
  -> ESCRITA
  -> PARTITURA
  -> INSCRIÇÃO
  -> SILÊNCIO
  -> ARQUIVO
```

A refusal cycle:

```txt
REPOUSO
  -> ESCUTA
  -> ENTRADA
  -> RECUSA
  -> ARQUIVO
```

A fault cycle:

```txt
REPOUSO or INSCRIÇÃO
  -> FALHA
  -> MANUTENÇÃO
  -> REPOUSO or ARQUIVO
```

A silence cycle:

```txt
REPOUSO
  -> ESCUTA
  -> SILÊNCIO
  -> ARQUIVO
```

## Story packet validation

Before inscription, the controller must validate the packet described in:

- `../02-generative-system/story-packet-schema.md`

Minimum validation:

- status is allowed;
- language is `pt-BR`;
- source rights match intended use;
- story is marked as `conto_de_calibracao` if present;
- `final_artwork_claim` is false;
- score exists;
- inscription exists;
- ledger exists;
- receipt is public-safe;
- physical print is explicitly approved before printer output.

If validation fails, the controller should refuse, retry, or enter silence.

## No automatic physical print

A story packet being valid does not automatically mean it can be printed physically.

For physical print, require:

```txt
review.approved_for_physical_print = true
inscription.printable = true
inscription.mode = physical_print
```

During prototype stages, generated packets should default to:

```txt
approved_for_physical_print = false
```

## Data persistence

The runtime should preserve:

- packet JSON;
- receipt markdown or JSON;
- controller logs;
- print logs;
- fault logs;
- refusal logs;
- configuration snapshots;
- software version or commit hash.

Suggested local structure:

```txt
runtime/
  config/
  packets/
  receipts/
  ledgers/
  logs/
  spool/
  faults/
```

This folder is not necessarily public. Public exports should be sanitized.

## Recovery requirements

The runtime should recover from:

- power loss;
- network loss;
- model API failure;
- printer disconnect;
- paper jam;
- full disk;
- invalid story packet;
- missing source;
- interrupted cycle.

After restart, the controller should know:

- last completed packet;
- last attempted inscription;
- printer state if available;
- whether a packet was printed, partially printed, refused, or held;
- whether human maintenance is required.

## Fallback behavior

If model host fails:

- enter silence;
- or use deterministic fallback text only if pre-approved;
- log model failure;
- do not invent source.

If retrieval fails:

- do not write from untraceable memory;
- enter silence or use project canon only if allowed;
- log retrieval failure.

If printer fails:

- stop physical inscription;
- log fault;
- preserve packet;
- produce no-print receipt if public-safe;
- request maintenance.

If disk logging fails:

- stop cycle;
- do not print without ledger;
- log to emergency channel if available.

## Observability

The runtime should expose public-safe state:

- current state;
- last public receipt;
- line count;
- printer mode;
- silence timer;
- fault or refusal status;
- uptime or runtime status;
- no private source content.

Internal logs may contain more detail, but public surfaces should remain sanitized.

## Maintenance requirements

Maintenance events should be first-class records.

Examples:

- paper replaced;
- ribbon replaced;
- printer reset;
- paper path cleared;
- controller restarted;
- model endpoint changed;
- retrieval index rebuilt;
- ledger backup verified.

Maintenance is not outside the work. It is part of the apparatus history.

## Security and privacy

The runtime must not expose:

- credentials;
- API keys;
- internal IPs;
- private source content;
- e-mails;
- WhatsApp or chat logs;
- budgets;
- supplier contacts;
- institutional documents;
- unapproved corpus.

Public receipts must be checked against this rule.

## Minimum viable runtime for v0.2

The next non-final runtime prototype can be entirely local and simulated.

Minimum v0.2 runtime:

1. Load demo story packets.
2. Validate packets.
3. Render receipts.
4. Simulate inscription in terminal or static UI.
5. Log story, refusal, fault, and silence.
6. Avoid model calls and private corpus.

This is already partially represented by:

- `../06-prototypes/story-packets/`

## Open decisions

These require human/co-authorial or institutional decision:

- final exhibition duration;
- daily operating hours;
- whether the controller is visible;
- whether the Mesa de Inscrição is public, internal, or part of the installation;
- what downtime is acceptable;
- who performs maintenance;
- whether remote model hosting is acceptable;
- what is printed publicly;
- whether silence or refusal prints a receipt on paper.

## Working conclusion

The runtime is not just infrastructure. It is the discipline that prevents the apparatus from becoming a chatbot attached to a printer.
