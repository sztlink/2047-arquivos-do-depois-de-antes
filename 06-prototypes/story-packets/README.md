# Story packet smoke prototype

> **Historical note (October 2026).** Written during the research and rehearsal phase of the work, then called *Projeto 2047 / Arquivo Terra Viva*, and kept as process. Some of it no longer describes the work as it runs. For the current apparatus see `../../03-field-notes/2026-10-lq-590-qr-and-declared-cost.md`, `../../03-field-notes/2026-10-video-wall.md`, and `../../03-field-notes/2026-10-opening-at-casa-firjan.md`.

This folder contains a public-safe technical smoke test for the Projeto 2047 writing apparatus.

It does not call AI models, does not use private corpus, does not access the network, and does not print. It only generates deterministic JSON fixtures that follow the conceptual story packet schema.

Related document:

- `../../02-generative-system/story-packet-schema.md`

## Purpose

The smoke test turns the conceptual architecture into testable artifacts:

```txt
schema document
  -> demo JSON packets
  -> validation pass/fail
  -> public markdown receipts
```

This prepares the path for a future controller and for the Mesa de Inscrição to read packets instead of hardcoded demo data.

## Files

```txt
generate-demo-packets.js
validate-demo-packets.js
render-demo-receipts.js
render-inscription-spool.js
run-smoke.js
output/
  story-ready.demo.json
  refusal.demo.json
  fault.demo.json
  silence.demo.json
receipts/
  story-ready.receipt.md
  refusal.receipt.md
  fault.receipt.md
  silence.receipt.md
spool/
  story-ready.spool.txt
  refusal.spool.txt
  fault.spool.txt
  silence.spool.txt
```

## Run

From this folder:

```bash
node run-smoke.js
```

Or from the repository root:

```bash
node 06-prototypes/story-packets/run-smoke.js
```

## Packet statuses

The smoke test covers four valid statuses:

- `story_ready`
- `refusal`
- `fault`
- `silence`

## Public boundary

All data is synthetic or generic.

The demo packets do not include:

- private conversations;
- institutional documents;
- budgets;
- supplier data;
- internal infrastructure;
- credentials;
- final artwork text;
- model training corpus;
- unapproved co-authorial material.

## Validation

The validator checks the basic apparatus contract:

- schema version;
- status;
- pt-BR language;
- required top-level fields;
- story requirements for `story_ready`;
- non-printability for `refusal`, `fault`, and `silence`;
- public-safe receipt flag;
- no physical print approval.

It is intentionally lightweight and dependency-free. A stricter JSON Schema validator may be added later.

## Dry-run spool

The smoke test also renders `.spool.txt` files. These are printer-safe inspection artifacts only. They do not send anything to a physical printer.

For `story_ready`, the spool contains the calibration story wrapped to the packet line width.

For `refusal`, `fault`, and `silence`, the spool records a no-print event.

## Next steps

- Connect Mesa de Inscrição to load one of these packets when interface work resumes.
- Add an explicit JSON Schema file if needed.
- Add receipt export to the controller.
- Use evaluation prompts before calling any model.
