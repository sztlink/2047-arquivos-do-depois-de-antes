# Fine-tuning versus RAG

> **Historical note (October 2026).** Written during the research and rehearsal phase of the work, then called *Projeto 2047 / Arquivo Terra Viva*, and kept as process. Some of it no longer describes the work as it runs. For the current apparatus see `../03-field-notes/2026-09-restart-from-zero-and-the-2047-structure.md` and `../03-field-notes/2026-10-opening-at-casa-firjan.md`.

This file defines the working architecture for the writing apparatus of **Projeto 2047 / Arquivo Terra Viva**.

It should be read together with:

- `model-voice-and-training.md`
- `corpus-policy.md`
- `source-ledger.md`
- `print-ledger-schema.md`

This is a technical-artistic research note, not a final implementation plan.

## Core position

The apparatus should not rely on a single model call to do everything.

A long-duration writing machine needs different layers for different responsibilities:

```txt
fine-tuning or adapters -> form, cadence, behavior
retrieval -> sources, references, facts
ledger -> memory of what happened
controller -> time, state, printing, refusal, fallback
human calibration -> authorship, direction, limits
```

The goal is not to build a smarter chatbot.

The goal is to build a situated writing instrument that can produce **contos de calibração** in Brazilian Portuguese, with source traceability, score, refusal, silence, and archive behavior.

## Why not only prompt engineering

Prompting is useful for early prototypes, but it is fragile as the only strategy.

Prompt-only systems tend to:

- drift toward generic LLM style;
- forget project-specific constraints;
- over-explain instead of writing;
- ignore score and ledger requirements;
- treat refusal as an error;
- produce too much text;
- imitate the dominant style of the base model;
- fail differently across model versions.

Prompting can remain part of the apparatus, but it should not carry the whole work.

## Why not only fine-tuning

Fine-tuning is not a database, not a rights solution, and not a memory system.

Fine-tuning should not be used to store:

- live news;
- factual source data;
- daily exhibition state;
- printer history;
- private documents;
- unclear rights material;
- source citations;
- institutional details;
- anything that may need removal.

If a fact must be traceable, updateable, or removable, it belongs in retrieval or ledger, not inside model weights.

## Why not only RAG

Retrieval can ground the model in sources, but it does not automatically create a voice, form, rhythm, or refusal behavior.

RAG-only systems tend to:

- summarize instead of transform;
- sound like a research assistant;
- over-cite;
- follow the language of retrieved documents too closely;
- produce reports instead of stories;
- treat source retrieval as the whole artwork;
- make the output depend too heavily on whatever source ranked first.

Retrieval should feed the apparatus. It should not become the author.

## What fine-tuning or adapters are for

Fine-tuning, adapters, LoRA, or other lightweight model-shaping methods may be useful for behavior and form.

Use them for:

- pt-BR operating language;
- short story form;
- restrained fictional tone;
- recurring 2047 structure;
- refusal behavior;
- score output discipline;
- ledger output discipline;
- line-length awareness;
- avoiding generic cyberpunk;
- avoiding product language;
- avoiding assistant explanations;
- keeping the model inside the apparatus role.

Fine-tuning should teach the model how to behave, not what facts to remember.

### Good fine-tuning target

```txt
Given a cleared source packet and apparatus constraints,
write a conto de calibração in pt-BR,
produce a score,
produce ledger fields,
or refuse with a reason.
```

### Bad fine-tuning target

```txt
Memorize private project documents.
Memorize news articles.
Imitate a living author without clearance.
Store exhibition logistics.
Store source citations inside weights.
```

## What retrieval is for

Retrieval should provide the context that must remain traceable.

Use retrieval for:

- public source packets;
- news and live signals;
- public references;
- selected project canon;
- approved corpus fragments;
- previous public receipts;
- archive state;
- glossary and constraints;
- Manuals Plus reference links;
- source provenance.

Retrieval should return structured packets, not undifferentiated text dumps.

A retrieved source packet should include:

```txt
source_id
source_type
title
url or citation
retrieved_at
summary
rights status
public/private classification
relevance note
risk note
allowed use
```

The model should never be asked to invent these fields.

## What the ledger is for

The ledger records what the apparatus actually did.

It is not the same as the corpus and not the same as retrieval.

The ledger should preserve:

- source packets used;
- generated calibration story id;
- score id;
- print or simulation id;
- refusal events;
- silence events;
- fault events;
- maintenance events;
- timestamps;
- model version;
- controller version;
- printer state;
- public receipt status.

The ledger is the memory of operation.

It should be append-oriented, auditable, and resistant to silent rewriting.

## What the controller is for

The controller is the runtime conductor.

It should decide and record:

- when a cycle starts;
- which source packet is eligible;
- whether the apparatus should write, refuse, wait, or enter silence;
- which model endpoint to call;
- which retrieval context to attach;
- which score preset to use;
- whether to print, simulate, pause, or fallback;
- how to log success, refusal, fault, and maintenance;
- how to recover after interruption.

The controller should not be confused with the model.

The model writes.  
The controller operates.  
The ledger remembers.  
The printer inscribes.  
The authors calibrate.

## Hybrid architecture

Recommended architecture:

```txt
source intake
  -> source ledger
  -> retrieval packet
  -> apparatus constraints
  -> model call
      -> story candidate
      -> score candidate
      -> refusal or fault suggestion
  -> controller validation
  -> print or simulation
  -> print ledger
  -> public receipt
```

The model should receive only the context needed for the current cycle.

The controller should validate that the response contains:

- pt-BR output;
- story or refusal;
- score fields;
- ledger fields;
- source references;
- no private material;
- no false claim of final artwork status.

If validation fails, the controller should refuse, retry with a stricter instruction, or enter silence.

## Model output contract

A future model call should return a structured packet.

Example shape:

```json
{
  "status": "story_ready",
  "language": "pt-BR",
  "story": {
    "type": "conto_de_calibracao",
    "title": "...",
    "fictional_date": "2047-...",
    "body": "..."
  },
  "score": {
    "pulse": "slow",
    "density": "sparse",
    "line_width": 72,
    "silence_before_seconds": 3,
    "silence_after_seconds": 90
  },
  "ledger": {
    "source_refs": ["source_..."],
    "rights_status": "public-reference-only",
    "model_version": "...",
    "requires_human_review": true
  }
}
```

Refusal example:

```json
{
  "status": "refusal",
  "language": "pt-BR",
  "reason": "source rights unclear",
  "public_note": "A inscrição foi recusada porque a origem do material não está liberada.",
  "score": {
    "pulse": "none",
    "density": "silence",
    "line_width": 72,
    "silence_before_seconds": 0,
    "silence_after_seconds": 180
  },
  "ledger": {
    "source_refs": ["source_..."],
    "event_type": "refusal",
    "requires_human_review": false
  }
}
```

## Failure cases

The architecture should expect failure.

### Failure: generic assistant voice

Symptom:

- output explains the project instead of writing a story.

Response:

- reject output;
- tighten instruction;
- evaluate whether fine-tuning examples are needed.

### Failure: report instead of story

Symptom:

- output summarizes source material as an essay or briefing.

Response:

- mark as failed calibration;
- retry with stricter story form;
- adjust evaluation prompts.

### Failure: untraceable fact

Symptom:

- output includes a factual claim with no source reference.

Response:

- reject or remove claim;
- require source ledger link;
- do not print.

### Failure: imitation without clearance

Symptom:

- output imitates a living author too directly or claims authorial voice.

Response:

- refuse;
- log authorship risk;
- revise corpus and prompts.

### Failure: aestheticized harm

Symptom:

- environmental damage becomes atmospheric decoration.

Response:

- reject;
- require material consequence;
- require archive, extraction, or infrastructure trace.

### Failure: private material leakage

Symptom:

- output includes private names, logistics, budgets, internal documents, or non-public process.

Response:

- stop cycle;
- log fault;
- remove source packet;
- review retrieval index;
- do not print.

## Rights and authorship boundary

Fine-tuning changes model behavior and may make removal difficult.

Therefore:

- do not fine-tune on Giselle-authored material without explicit clearance;
- do not fine-tune on private Felipe/szt.link material by default;
- do not fine-tune on co-authored internal drafts without approval;
- do not fine-tune on raw LLM conversations as voice examples;
- do not share weights unless rights and authorship are resolved.

Retrieval is easier to audit and remove, but it still requires clearance.

The model should not be described as an author replacing the artists.

Working formulation:

```txt
The model is one instrument in the apparatus.
Authorship remains with the artistic process.
The apparatus writes through constraints, sources, score, paper, silence, and calibration.
```

## Recommended path for v0.2

For the next public milestone, do not train a model yet.

Use a prompt-based mock or local script with structured packets to test the architecture:

1. Create a fictional or public-safe source packet.
2. Produce a pt-BR conto de calibracao.
3. Produce a score JSON.
4. Produce a ledger record.
5. Simulate inscription in the Mesa de Inscrição.
6. Save a public receipt.
7. Test refusal and fault paths.

This validates the apparatus contract before any corpus or training risk.

## Recommended path after v0.2

After the architecture is tested:

1. Build an evaluation set.
2. Build a small cleared calibration corpus.
3. Compare base model plus prompt against RAG plus prompt.
4. Compare RAG plus prompt against lightweight adapter or fine-tune.
5. Evaluate pt-BR quality, refusal, score discipline, source traceability, and non-generic voice.
6. Decide whether training is necessary.

Training should be a response to a demonstrated need, not an assumption.

## Open decisions for Giselle and Felipe

- Should the model learn a shared project voice, or only obey constraints?
- Can any Giselle-authored text be used for training, retrieval, or evaluation?
- Can any Felipe-authored text be used for training, retrieval, or evaluation?
- Should the model weights remain private?
- Can calibration stories be public before co-authorial review?
- Should refusal be operable, structural, or both?
- How much of the technical chain should be visible in the public interface?
- Should source citations appear on paper, in the ledger, or only internally?

## Current working position

```txt
Use RAG for traceable context.
Use fine-tuning only for behavior and form, if needed.
Use the ledger for operational memory.
Use the controller for state and accountability.
Use human calibration for authorship and limits.
```

## Resolution, August 2026 (v0.3.0)

The comparison prescribed above was run. See `../03-field-notes/2026-08-voice-trained-and-deployed.md`. The outcome confirmed the hybrid position rather than overturning it.

- A base model with prompt-only instruction drifts toward generic literary style, the failure this note predicted.
- A lightweight adapter (LoRA) trained for form and cadence carries the voice reliably, and the punctuation contract survives in the raw output before any deterministic pass.

The adapter was adopted for behavior and form only, consistent with the good fine-tuning target above. No facts, sources, news, or state live inside the weights. Those remain the job of retrieval and the ledger.

One simplification is worth recording. The deployed motor does not ask the model for the structured self-scored packet sketched under Model output contract. It generates prose, and a deterministic filter enforces the punctuation contract after generation. The structured score and refusal packet stays a design reserve. The working apparatus is leaner than the first drawing.

The corpus the adapter learned from is addressed in the field note and remains subject to the open question in `corpus-policy.md` about curated synthetic material.
