# Source curation panel

> **Historical note (October 2026).** Written during the research and rehearsal phase of the work, then called *Projeto 2047 / Arquivo Terra Viva*, and kept as process. Some of it no longer describes the work as it runs. For the current apparatus see `../03-field-notes/2026-09-restart-from-zero-and-the-2047-structure.md` and `../03-field-notes/2026-10-opening-at-casa-firjan.md`.

Public interface name: **Triagem de Fontes**

This file defines the source curation layer for **Projeto 2047 / Arquivo Terra Viva**.

The repository documents the architecture in English, but the operational interface language is Brazilian Portuguese.

## Core position

Not every signal deserves inscription.

The writing apparatus should not ingest an open news feed and immediately turn it into fiction.

Before a source can become a `source_packet`, it must pass through **Triagem de Fontes**.

```txt
candidate source
  -> triagem
  -> approved / refused / waiting / archived
  -> source packet
  -> Mesa de Inscrição
```

## Purpose

Triagem de Fontes protects the work from becoming:

- a trending-topic machine;
- a scraper with a printer;
- a disaster aestheticization engine;
- an untraceable news summarizer;
- a rights risk;
- a generic AI content pipeline.

It establishes a human and procedural threshold before writing.

## Relationship to Mesa de Inscrição

Triagem de Fontes happens before Mesa de Inscrição.

```txt
Triagem de Fontes
  -> approved source packet
  -> Mesa de Inscrição
  -> conto de calibração / recusa / silêncio / falha
  -> ledger
  -> comprovante público
```

Triagem de Fontes decides whether a signal may enter the writing apparatus.

Mesa de Inscrição performs what happens after entry.

## Interface language

Use pt-BR for operational labels.

Preferred title:

```txt
Triagem de Fontes
```

Possible subtitle:

```txt
camada de escuta, risco e autorização antes da inscrição
```

Avoid:

- admin dashboard;
- content manager;
- news feed;
- AI source inbox;
- trend monitor.

## Source lifecycle states

A candidate source should move through explicit states.

```txt
CANDIDATA
EM REVISÃO
APROVADA
RECUSADA
EM ESPERA
ARQUIVADA
EXPIRADA
USADA
```

### `CANDIDATA`

A source has been collected or suggested, but not reviewed.

### `EM REVISÃO`

The source is being evaluated for relevance, rights, risk, and relation to the work.

### `APROVADA`

The source may become a source packet for the writing apparatus.

### `RECUSADA`

The source should not be used.

Reasons may include:

- unclear rights;
- private material;
- weak source;
- sensationalism;
- personal data;
- lack of relation to the project;
- high risk of aestheticizing harm;
- insufficient traceability.

### `EM ESPERA`

The source is potentially relevant but not ready.

Use when:

- more context is needed;
- another source should corroborate it;
- timing is not right;
- co-authorial decision is needed.

### `ARQUIVADA`

The source is preserved as a reference but will not enter the writing apparatus now.

### `EXPIRADA`

The source was time-sensitive and is no longer useful as a signal.

### `USADA`

The source has already generated or contributed to a story packet.

## Actions

Operational actions in pt-BR:

- `Aprovar fonte`
- `Recusar fonte`
- `Manter em espera`
- `Arquivar sem uso`
- `Gerar source packet`
- `Marcar risco`
- `Marcar como fraca`
- `Marcar como sensacionalista`
- `Marcar como inadequada`
- `Enviar para Mesa de Inscrição`

## Required source fields

Each candidate source should include:

```json
{
  "candidate_id": "...",
  "status": "CANDIDATA",
  "title": "...",
  "source_name": "...",
  "url": "...",
  "published_at": "...",
  "collected_at": "...",
  "language": "...",
  "summary": "...",
  "territory": "...",
  "themes": [],
  "rights_status": "...",
  "allowed_use": "...",
  "risk_flags": [],
  "relation_to_2047": "...",
  "curation_decision": null,
  "decision_reason": null,
  "reviewed_by_role": null,
  "reviewed_at": null
}
```

Do not store private full text in a public candidate record.

## Risk flags

Suggested risk flags:

```txt
unclear_rights
private_or_restricted
personal_data
weak_source
sensationalist
paywalled_copy
unverified_claim
too_generic
too_far_from_project
aestheticizes_harm
requires_context
requires_coauthor_review
```

A source may have multiple risk flags.

## Theme vocabulary

Initial themes:

- rare earths;
- mining;
- water;
- data centers;
- energy;
- e-waste;
- AI infrastructure;
- Amazon;
- territory;
- environmental justice;
- climate;
- logistics;
- archive;
- obsolete media;
- public policy;
- extractive finance.

This vocabulary should remain editable.

## Approval criteria

A source may be approved when it is:

- public;
- traceable;
- relevant to 2047;
- rights-safe for the intended use;
- specific enough to sustain transformation;
- not purely sensationalist;
- not dependent on personal/private data;
- capable of becoming a source packet without copying protected text.

## Refusal criteria

A source should be refused when:

- rights are unclear;
- source is private or restricted;
- it contains personal data not needed for the work;
- it is a weak or unverified claim;
- it would push the apparatus toward spectacle;
- it has no real relation to extraction, infrastructure, archive, computation, territory, or 2047;
- it cannot be summarized without reproducing protected text;
- it invites imitation of an uncleared authorial voice.

## Waiting criteria

A source should be placed `EM ESPERA` when:

- more context is needed;
- the source is relevant but too early;
- a stronger source may appear;
- co-authorial review is needed;
- the same theme was recently used and repetition risk is high;
- the current apparatus state calls for silence.

## Source packet conversion

Only approved sources can become source packets.

A converted source packet should include:

```json
{
  "source_id": "source_...",
  "source_type": "news_signal | public_reference | project_canon | approved_corpus_fragment",
  "title": "...",
  "summary": "...",
  "url": "...",
  "retrieved_at": "...",
  "rights_status": "public-reference-only",
  "allowed_use": "retrieval | evaluation | print_candidate",
  "public_private_classification": "public",
  "risk_note": "...",
  "curation_status": "APROVADA",
  "curation_reason": "..."
}
```

The source packet should not include full copyrighted article text unless explicitly cleared.

## Human decision role

A model may assist with summarization, risk flagging, clustering, or deduplication.

A model should not be the sole authority for approval.

At minimum, sources that will drive public stories should have human review or a very strict pre-approved rule.

## Relationship to news sources

The project has not yet selected its final source list.

Triagem de Fontes should support both:

1. curated source baskets;
2. occasional manually added sources.

An open automatic feed should not be the first implementation.

Preferred initial posture:

```txt
curated public sources
  -> manual or semi-manual triage
  -> approved source packets
```

## Candidate source categories

Possible categories to curate later:

- Brazilian environmental journalism;
- Amazon and territory monitoring;
- climate science;
- water and river systems;
- mining and rare earths;
- e-waste and recycling;
- AI infrastructure;
- data centers and energy;
- public datasets;
- technical manuals and obsolete media references.

## Public/private boundary

Triagem de Fontes must not publish:

- private notes;
- full paywalled texts;
- private e-mails;
- WhatsApp or chat logs;
- budget or supplier details;
- institutional documents;
- personal data;
- unapproved corpus fragments.

Public receipts may include:

- title;
- source name;
- URL;
- summary;
- themes;
- curation decision;
- public-safe reason.

## Minimal v0.2 implementation

A first non-interface implementation can be a JSON fixture and checklist.

Suggested files:

```txt
06-prototypes/source-triage/
  README.md
  candidates.demo.json
  triage-demo.js
  output/
    approved-source-packet.demo.json
    refused-source.demo.json
    waiting-source.demo.json
```

This does not require live scraping or model calls.

## Open decisions

- Which source baskets should be used first?
- Who can approve a source?
- Should approval be daily, weekly, or event-based?
- Can the audience ever see rejected sources?
- Should source citations appear on printed paper or only in the ledger?
- Should a source expire after a time window?
- Should the apparatus avoid repeated themes within the same day?

## Working conclusion

The writing begins before the story.

It begins at the threshold where the apparatus decides what may be heard, what must be refused, what should wait, and what can become inscription.
