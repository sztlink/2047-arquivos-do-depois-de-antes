# Story packet schema

> **Historical note (October 2026).** Written during the research and rehearsal phase of the work, then called *Projeto 2047 / Arquivo Terra Viva*, and kept as process. Some of it no longer describes the work as it runs. For the current apparatus see `../03-field-notes/2026-09-restart-from-zero-and-the-2047-structure.md` and `../03-field-notes/2026-10-opening-at-casa-firjan.md`.

This file defines the minimum packet exchanged between the writing engine, controller, Mesa de Inscrição, printer, and ledgers.

A story packet is not only a generated text. It is the full operational record of one apparatus cycle.

```txt
source packet
  -> conto de calibração or refusal/fault/silence
  -> score
  -> inscription instruction
  -> ledger fields
  -> public receipt
```

This is a conceptual schema for research and prototyping. It is not a final software API.

## Purpose

The story packet exists to prevent the apparatus from treating text as the only output.

Each cycle must carry:

- source trace;
- language;
- status;
- story or non-story event;
- score;
- inscription constraints;
- rights status;
- ledger fields;
- public receipt fields;
- review flags.

If any of these are missing, the controller should not print.

## Status values

A story packet must have one of four status values:

```txt
story_ready
refusal
fault
silence
```

### `story_ready`

A conto de calibração was produced and may proceed to inscription if validation passes.

### `refusal`

The apparatus refused to write or inscribe because of rights, privacy, weak source, authorship risk, or conceptual risk.

### `fault`

The apparatus could not proceed because of technical or mechanical failure.

### `silence`

The apparatus entered silence because the source was below threshold, repetition was too high, timing required pause, or silence was selected as the correct response.

## Required top-level fields

```json
{
  "packet_id": "...",
  "schema_version": "2047-story-packet-v0.1",
  "status": "story_ready | refusal | fault | silence",
  "language": "pt-BR",
  "created_at": "...",
  "apparatus_context": {},
  "source_packet": {},
  "story": {},
  "score": {},
  "inscription": {},
  "ledger": {},
  "receipt": {},
  "review": {}
}
```

## Field definitions

### `packet_id`

Unique id for the full cycle packet.

Suggested format:

```txt
pkt_2047_YYYYMMDD_HHMMSS_slug
```

### `schema_version`

Schema identifier.

Current value:

```txt
2047-story-packet-v0.1
```

### `status`

One of:

- `story_ready`
- `refusal`
- `fault`
- `silence`

### `language`

Default:

```txt
pt-BR
```

The apparatus operates in Brazilian Portuguese even if repository documentation is in English.

### `created_at`

ISO timestamp for packet creation.

### `apparatus_context`

Records runtime context.

```json
{
  "interface": "Mesa de Inscrição",
  "controller_version": "...",
  "model_version": "...",
  "retrieval_version": "...",
  "printer_profile": "simulation | fx-2190 | other",
  "run_mode": "simulation | physical_print | dry_run",
  "exhibition_day": null
}
```

`exhibition_day` should remain `null` until exhibition duration is confirmed.

### `source_packet`

A structured source reference.

```json
{
  "source_id": "source_...",
  "source_type": "fictional_public_signal_cluster | public_reference | news_signal | project_canon | approved_corpus_fragment",
  "title": "...",
  "summary": "...",
  "url": null,
  "retrieved_at": "...",
  "rights_status": "synthetic_public_demo | public-reference-only | retrieval-cleared | training-cleared | not-cleared",
  "allowed_use": "evaluation | retrieval | public_demo | print_candidate",
  "public_private_classification": "public | private | restricted | synthetic",
  "risk_note": "..."
}
```

The story packet should not contain full private sources.

### `story`

For `story_ready`, this contains the calibration story.

```json
{
  "story_id": "story_...",
  "type": "conto_de_calibracao",
  "title": "...",
  "fictional_date": "2047-...",
  "body": "...",
  "line_width_target": 72,
  "final_artwork_claim": false
}
```

For `refusal`, `fault`, or `silence`, `story` should be `null` or contain only a held candidate marked as not printable.

### `score`

The sonic and mechanical score.

```json
{
  "score_id": "score_...",
  "pulse": "slow | medium | burst | none",
  "density": "sparse | medium | dense | silence",
  "line_width": 72,
  "silence_before_seconds": 3,
  "silence_after_seconds": 90,
  "blank_line_policy": "breathing | compact | none",
  "print_rhythm_note": "..."
}
```

For refusal and silence, score may specify `pulse: none` and `density: silence`.

### `inscription`

Defines what the printer or simulation should do.

```json
{
  "inscription_id": "insc_...",
  "mode": "terminal_simulation | physical_print | no_print",
  "printer_profile": "simulation | fx-2190",
  "paper": "continuous | simulated | unknown",
  "encoding": "utf-8 | ascii-safe | escp",
  "line_width": 72,
  "printable": true,
  "reason_not_printable": null
}
```

`printable` must be `false` for refusal, fault, and silence unless a non-story receipt is intentionally printed.

### `ledger`

Fields to append to source and print ledgers.

```json
{
  "event_type": "story_ready | refusal | fault | silence | printed | simulated",
  "source_refs": ["source_..."],
  "story_id": "story_...",
  "score_id": "score_...",
  "inscription_id": "insc_...",
  "model_version": "...",
  "controller_version": "...",
  "rights_status": "...",
  "requires_human_review": true,
  "public_receipt": true
}
```

The ledger should record non-production events too.

### `receipt`

Public-safe summary.

```json
{
  "receipt_id": "rcpt_...",
  "public_title": "...",
  "public_status": "calibration story | refusal | fault | silence",
  "public_note": "...",
  "include_story_excerpt": false,
  "include_source_summary": true,
  "safe_to_publish": true
}
```

The receipt must not include private material.

### `review`

Human and co-authorial review status.

```json
{
  "human_review_required": true,
  "coauthor_review_required": true,
  "approved_for_public_archive": false,
  "approved_for_physical_print": false,
  "notes": "..."
}
```

A packet may be technically valid but still not approved for public or physical inscription.

## Example 1 - story ready

```json
{
  "packet_id": "pkt_2047_20260517_001_canal_resfriamento",
  "schema_version": "2047-story-packet-v0.1",
  "status": "story_ready",
  "language": "pt-BR",
  "created_at": "2026-05-17T22:00:00Z",
  "apparatus_context": {
    "interface": "Mesa de Inscrição",
    "controller_version": "controller-prototype-v0.1",
    "model_version": "prompt-mock-v0.1",
    "retrieval_version": "none",
    "printer_profile": "simulation",
    "run_mode": "simulation",
    "exhibition_day": null
  },
  "source_packet": {
    "source_id": "source_demo_001",
    "source_type": "fictional_public_signal_cluster",
    "title": "Cluster ficcional: data centers, água, lixo eletrônico",
    "summary": "Entrada sintética para teste público. Nenhum evento real é citado.",
    "url": null,
    "retrieved_at": "2026-05-17T22:00:00Z",
    "rights_status": "synthetic_public_demo",
    "allowed_use": "public_demo",
    "public_private_classification": "synthetic",
    "risk_note": "Não usar como evidência factual."
  },
  "story": {
    "story_id": "story_demo_001",
    "type": "conto_de_calibracao",
    "title": "O Canal de Resfriamento",
    "fictional_date": "2047-08-13",
    "body": "O canal não tinha nome no arquivo municipal...",
    "line_width_target": 72,
    "final_artwork_claim": false
  },
  "score": {
    "score_id": "score_demo_001",
    "pulse": "slow",
    "density": "sparse",
    "line_width": 72,
    "silence_before_seconds": 3,
    "silence_after_seconds": 90,
    "blank_line_policy": "breathing",
    "print_rhythm_note": "Inscrição lenta, com pausas entre blocos."
  },
  "inscription": {
    "inscription_id": "insc_demo_001",
    "mode": "terminal_simulation",
    "printer_profile": "simulation",
    "paper": "simulated",
    "encoding": "utf-8",
    "line_width": 72,
    "printable": true,
    "reason_not_printable": null
  },
  "ledger": {
    "event_type": "simulated",
    "source_refs": ["source_demo_001"],
    "story_id": "story_demo_001",
    "score_id": "score_demo_001",
    "inscription_id": "insc_demo_001",
    "model_version": "prompt-mock-v0.1",
    "controller_version": "controller-prototype-v0.1",
    "rights_status": "synthetic_public_demo",
    "requires_human_review": true,
    "public_receipt": true
  },
  "receipt": {
    "receipt_id": "rcpt_demo_001",
    "public_title": "Conto de calibração - O Canal de Resfriamento",
    "public_status": "calibration story",
    "public_note": "Material ficcional sintético para teste do aparato.",
    "include_story_excerpt": true,
    "include_source_summary": true,
    "safe_to_publish": true
  },
  "review": {
    "human_review_required": true,
    "coauthor_review_required": true,
    "approved_for_public_archive": false,
    "approved_for_physical_print": false,
    "notes": "Demonstração pública, não voz final da obra."
  }
}
```

## Example 2 - refusal

```json
{
  "packet_id": "pkt_2047_20260517_002_recusa_email_privado",
  "schema_version": "2047-story-packet-v0.1",
  "status": "refusal",
  "language": "pt-BR",
  "created_at": "2026-05-17T22:05:00Z",
  "apparatus_context": {
    "interface": "Mesa de Inscrição",
    "controller_version": "controller-prototype-v0.1",
    "model_version": "prompt-mock-v0.1",
    "retrieval_version": "none",
    "printer_profile": "simulation",
    "run_mode": "simulation",
    "exhibition_day": null
  },
  "source_packet": {
    "source_id": "source_private_001",
    "source_type": "restricted_project_material",
    "title": "Private e-mail fragment",
    "summary": "Private source. Full content withheld.",
    "url": null,
    "retrieved_at": null,
    "rights_status": "not-cleared",
    "allowed_use": "none",
    "public_private_classification": "private",
    "risk_note": "Private process cannot become public story source."
  },
  "story": null,
  "score": {
    "score_id": "score_refusal_001",
    "pulse": "none",
    "density": "silence",
    "line_width": 72,
    "silence_before_seconds": 0,
    "silence_after_seconds": 180,
    "blank_line_policy": "none",
    "print_rhythm_note": "Recusa sem inscrição narrativa."
  },
  "inscription": {
    "inscription_id": "insc_refusal_001",
    "mode": "no_print",
    "printer_profile": "simulation",
    "paper": "simulated",
    "encoding": "utf-8",
    "line_width": 72,
    "printable": false,
    "reason_not_printable": "Source is private and not cleared."
  },
  "ledger": {
    "event_type": "refusal",
    "source_refs": ["source_private_001"],
    "story_id": null,
    "score_id": "score_refusal_001",
    "inscription_id": "insc_refusal_001",
    "model_version": "prompt-mock-v0.1",
    "controller_version": "controller-prototype-v0.1",
    "rights_status": "not-cleared",
    "requires_human_review": false,
    "public_receipt": true
  },
  "receipt": {
    "receipt_id": "rcpt_refusal_001",
    "public_title": "Recusa de inscrição",
    "public_status": "refusal",
    "public_note": "A inscrição foi recusada porque a origem do material não está liberada.",
    "include_story_excerpt": false,
    "include_source_summary": false,
    "safe_to_publish": true
  },
  "review": {
    "human_review_required": false,
    "coauthor_review_required": false,
    "approved_for_public_archive": true,
    "approved_for_physical_print": false,
    "notes": "Public receipt may record refusal without exposing source."
  }
}
```

## Example 3 - fault

```json
{
  "packet_id": "pkt_2047_20260517_003_falha_papel",
  "schema_version": "2047-story-packet-v0.1",
  "status": "fault",
  "language": "pt-BR",
  "created_at": "2026-05-17T22:10:00Z",
  "apparatus_context": {
    "interface": "Mesa de Inscrição",
    "controller_version": "controller-prototype-v0.1",
    "model_version": "none",
    "retrieval_version": "none",
    "printer_profile": "fx-2190",
    "run_mode": "physical_print",
    "exhibition_day": null
  },
  "source_packet": null,
  "story": null,
  "score": {
    "score_id": "score_fault_001",
    "pulse": "none",
    "density": "silence",
    "line_width": 72,
    "silence_before_seconds": 0,
    "silence_after_seconds": 60,
    "blank_line_policy": "none",
    "print_rhythm_note": "Falha mecânica. Sem inscrição."
  },
  "inscription": {
    "inscription_id": "insc_fault_001",
    "mode": "no_print",
    "printer_profile": "fx-2190",
    "paper": "continuous",
    "encoding": "escp",
    "line_width": 72,
    "printable": false,
    "reason_not_printable": "Paper path interrupted."
  },
  "ledger": {
    "event_type": "fault",
    "source_refs": [],
    "story_id": null,
    "score_id": "score_fault_001",
    "inscription_id": "insc_fault_001",
    "model_version": "none",
    "controller_version": "controller-prototype-v0.1",
    "rights_status": "not_applicable",
    "requires_human_review": false,
    "public_receipt": true
  },
  "receipt": {
    "receipt_id": "rcpt_fault_001",
    "public_title": "Falha de inscrição",
    "public_status": "fault",
    "public_note": "O caminho do papel foi interrompido. O ciclo foi pausado.",
    "include_story_excerpt": false,
    "include_source_summary": false,
    "safe_to_publish": true
  },
  "review": {
    "human_review_required": false,
    "coauthor_review_required": false,
    "approved_for_public_archive": true,
    "approved_for_physical_print": false,
    "notes": "Mechanical fault can be archived as apparatus event."
  }
}
```

## Example 4 - silence

```json
{
  "packet_id": "pkt_2047_20260517_004_silencio",
  "schema_version": "2047-story-packet-v0.1",
  "status": "silence",
  "language": "pt-BR",
  "created_at": "2026-05-17T22:15:00Z",
  "apparatus_context": {
    "interface": "Mesa de Inscrição",
    "controller_version": "controller-prototype-v0.1",
    "model_version": "prompt-mock-v0.1",
    "retrieval_version": "none",
    "printer_profile": "simulation",
    "run_mode": "simulation",
    "exhibition_day": null
  },
  "source_packet": {
    "source_id": "source_weak_001",
    "source_type": "fictional_public_signal_cluster",
    "title": "Weak signal",
    "summary": "The source was too generic to justify inscription.",
    "url": null,
    "retrieved_at": "2026-05-17T22:15:00Z",
    "rights_status": "synthetic_public_demo",
    "allowed_use": "evaluation",
    "public_private_classification": "synthetic",
    "risk_note": "Below threshold."
  },
  "story": null,
  "score": {
    "score_id": "score_silence_001",
    "pulse": "none",
    "density": "silence",
    "line_width": 72,
    "silence_before_seconds": 0,
    "silence_after_seconds": 240,
    "blank_line_policy": "none",
    "print_rhythm_note": "Silêncio como resposta."
  },
  "inscription": {
    "inscription_id": "insc_silence_001",
    "mode": "no_print",
    "printer_profile": "simulation",
    "paper": "simulated",
    "encoding": "utf-8",
    "line_width": 72,
    "printable": false,
    "reason_not_printable": "Source below threshold."
  },
  "ledger": {
    "event_type": "silence",
    "source_refs": ["source_weak_001"],
    "story_id": null,
    "score_id": "score_silence_001",
    "inscription_id": "insc_silence_001",
    "model_version": "prompt-mock-v0.1",
    "controller_version": "controller-prototype-v0.1",
    "rights_status": "synthetic_public_demo",
    "requires_human_review": false,
    "public_receipt": true
  },
  "receipt": {
    "receipt_id": "rcpt_silence_001",
    "public_title": "Silêncio do aparato",
    "public_status": "silence",
    "public_note": "O sinal não sustentou uma inscrição. O aparato entrou em silêncio.",
    "include_story_excerpt": false,
    "include_source_summary": true,
    "safe_to_publish": true
  },
  "review": {
    "human_review_required": false,
    "coauthor_review_required": false,
    "approved_for_public_archive": true,
    "approved_for_physical_print": false,
    "notes": "Silence is a valid apparatus event."
  }
}
```

## Validation checklist

Before printing or publishing, validate:

- `language` is `pt-BR`;
- `status` is one of the allowed values;
- source rights are clear for the intended use;
- story is marked as `conto_de_calibracao` if present;
- `final_artwork_claim` is false;
- score exists;
- inscription exists;
- ledger exists;
- receipt is public-safe;
- private material is absent;
- human/co-author review flags are correct.

## Relationship to Mesa de Inscrição

The Mesa de Inscrição should be able to render any story packet.

Mapping:

| Packet field | Mesa de Inscrição panel |
| --- | --- |
| `source_packet` | Entrada / sinal do mundo |
| `story` | Digestão / composição em 4 canais |
| `score` | Partitura / calibração |
| `inscription` | Inscrição / impressora matricial |
| `ledger` | Arquivo / registrador |
| `status: refusal` | Manutenção / recusa |
| `status: fault` | Manutenção / recusa |
| `receipt` | Comprovante público |

## Relationship to ledgers

The story packet does not replace specialized ledgers.

It is a transfer object that can append to:

- source ledger;
- print ledger;
- refusal ledger;
- fault ledger;
- public receipt index.

A future controller should split the packet into the appropriate logs.

## Next prototype step

Create a local smoke script that produces one JSON packet for each status:

```txt
story_ready
refusal
fault
silence
```

Then use those packets to drive the Mesa de Inscrição prototype and save receipts.
