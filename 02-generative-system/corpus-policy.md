# Corpus policy

This file defines the public corpus policy for the writing apparatus of **Projeto 2047 / Arquivo Terra Viva**.

It is a research policy, not a final rights clearance document. It does not authorize training on any specific text by Giselle Beiguelman, Felipe Sztutman, or any third party.

## Purpose

The corpus is not a pile of text for a generic model.

The corpus is a carefully cleared field of language, concepts, references, and constraints that may help the apparatus write situated 2047 calibration stories in Brazilian Portuguese.

```txt
The repository documents the system in English.
The apparatus writes and operates in pt-BR.
```

## Core principle

Use only material that is:

1. authored;
2. traceable;
3. cleared;
4. necessary;
5. reviewable;
6. removable.

If a text cannot be traced, cleared, and removed, it should not enter the training corpus.

## Corpus layers

### Layer 0 - Project canon

Status: allowed for public reference and retrieval if already published in this repository.

Examples:

- public project brief;
- conceptual frame;
- apparatus notes;
- dramaturgical constraints;
- sonic score notes;
- archive policy;
- public prototype receipts.

Use for:

- project definitions;
- vocabulary;
- refusal rules;
- score schemas;
- apparatus behavior;
- public documentation context.

Do not use for:

- pretending this repository is the full artwork;
- replacing co-authorial review;
- producing final literary voice without human calibration.

### Layer 1 - Giselle Beiguelman corpus

Status: not cleared by this policy.

Possible future sources, only after explicit approval:

- published essays;
- published books or excerpts;
- public talks or interviews;
- project-specific texts written or approved for this purpose;
- selected fragments explicitly cleared for training, retrieval, or evaluation.

Questions to resolve before use:

- Which texts are eligible?
- Full texts or excerpts only?
- Training, retrieval, or evaluation only?
- Can the model learn style, or only concepts and vocabulary?
- Can outputs be public?
- Can model weights be archived?
- Can the corpus be deleted from the pipeline later?

Default rule:

```txt
No Giselle-authored text enters a training dataset without explicit clearance.
```

### Layer 2 - Felipe Sztutman corpus

Status: not automatic. Cleared by Felipe case by case.

Possible future sources:

- public artist texts;
- selected szt.link artifacts;
- project-specific notes written for 2047;
- calibration texts written by Felipe for this apparatus;
- approved fragments from prior research.

Do not include by default:

- private clay;
- therapy-like notes;
- private notebooks;
- WhatsApp messages;
- e-mails;
- raw session transcripts;
- unreviewed szt.link material;
- anything that belongs to the ateliê layer.

Default rule:

```txt
Felipe can clear specific material, but the existence of material inside szt.link does not make it public corpus.
```

### Layer 3 - Co-authored project material

Status: not automatic.

Possible future sources:

- texts jointly reviewed by Giselle and Felipe;
- public statements approved for the work;
- exhibition texts after approval;
- project bible fragments explicitly cleared for model use.

Do not include:

- internal presentation files;
- institutional proposals;
- budget documents;
- e-mails;
- meeting notes;
- production documents;
- unapproved drafts.

Default rule:

```txt
Co-authored does not mean automatically trainable.
```

### Layer 4 - Public reference field

Status: allowed for citation, bibliography, and retrieval if public and properly attributed.

Examples:

- public articles;
- public artist pages;
- academic references;
- public documentation on rare earths, e-waste, data centers, water, climate, archives, and media archaeology;
- public manuals and technical documentation.

Use for:

- factual grounding;
- retrieval;
- citations;
- source packets;
- thematic context;
- evaluation scenarios.

Do not use for:

- copying style;
- unlicensed voice imitation;
- untraceable synthesis;
- reproducing copyrighted scans or images without checking reuse rights.

Default rule:

```txt
Public reference is not the same as training permission.
```

### Layer 5 - News and live signals

Status: retrieval only unless separately cleared.

Use for:

- source packets;
- daily or periodic signals;
- summaries;
- source-ledger references;
- factual triggers for calibration stories.

Requirements:

- source URL;
- retrieval time;
- summary;
- access date;
- transformation note;
- public/private classification;
- refusal check.

Do not use:

- paywalled text copied into the corpus;
- private newsletters;
- personal data;
- unverified claims as fact;
- source material without trace.

### Layer 6 - LLM conversations

Status: not training corpus.

Raw conversations with GPT, Claude, Grok, Gemini, or other LLM systems should not become training examples for the writing model.

They may be mined for:

- questions;
- tensions;
- failure cases;
- prompts for evaluation;
- vocabulary gaps;
- technical decisions;
- design alternatives;
- refusal scenarios.

They should not be used as:

- voice target;
- literary corpus;
- authority;
- evidence of co-authorial approval;
- high-quality answer dataset.

Reason:

```txt
Training on raw LLM conversations risks teaching the apparatus to sound like an assistant rather than like the work.
```

### Layer 7 - Curated synthetic fictional material

Status: distinct from Layer 6. May enter training under the conditions below. Declared August 2026 (v0.3.0), provisional until co-authorial ratification.

Definition: fictional chapters or fragments generated by a model under this project's own voice contract and canon, then read and filtered by human curation and by a documented evaluation, kept for form and cadence, never for facts.

This is not Layer 6. Layer 6 bans raw assistant conversation and indiscriminate model output as a voice target. Layer 7 covers a narrow, audited case: candidate chapters in the target form, produced from the project's cleared contract, selected by a documented evaluation, used to teach behavior rather than to store facts or to clone an uncleared author.

Conditions of use:

- The generator's own inputs must be clean. Synthetic material may enter training only if the contract, canon, and any seed that shaped it are themselves cleared. Synthetic text generated from an uncleared authored corpus does not become clean by passing through a model. Provenance is inherited, not laundered.
- Any co-authored or authored seed that anchors the synthetic set still carries the clearance requirement of Layers 1, 2, and 3. Layer 7 does not bypass co-authorial clearance.
- Selection must be documented: which candidates were kept, which were dropped, and by what evaluation.
- The material teaches form and cadence only. Facts, sources, and state stay in retrieval and the ledger.
- The result is removable and auditable like any corpus item, and a fine-tuned model that absorbed it follows the removal rule below.

Current status: the working voice adapter (v0.3.0) was trained on material of this layer, the seven co-authored seed chapters plus a curated selection of candidate chapters generated under the voice contract and filtered by evaluation. This is recorded honestly and remains provisional until the authors ratify this category. See `../03-field-notes/2026-08-voice-trained-and-deployed.md`.

Default rule:

```txt
Curated synthetic fiction is not raw LLM output.
It may teach form only, from a cleared origin, with documented selection, and it must remain removable.
```

## Allowed uses by material type

| Material type | Training | Retrieval | Evaluation | Public output | Notes |
| --- | --- | --- | --- | --- | --- |
| Public repo docs | possible | yes | yes | yes | already public, still not final artwork |
| Giselle authored texts | no by default | no by default | no by default | no by default | requires explicit clearance |
| Felipe public texts | case by case | case by case | case by case | case by case | cleared by Felipe per item |
| Private szt.link clay | no | no | no | no | ateliê layer |
| Co-authored internal drafts | no | no | no | no | unless explicitly cleared |
| Public references | no by default | yes | yes | citation only | attribution required |
| News/live signals | no | yes | yes | transformed only | source ledger required |
| LLM conversations | no | no by default | yes, if sanitized | no | use for failure/evaluation only |
| Curated synthetic fiction | form only | no by default | yes | transformed only | cleared origin, documented selection, provisional, see Layer 7 |
| Manuals Plus scans | no by default | link/reference | visual evaluation | links only | do not copy scans without rights check |

## Language policy

The apparatus writes in Brazilian Portuguese.

The public research repository may remain in English for technical and international circulation, but the generated stories, interface states, refusal notices, receipts, and operator language should be pt-BR unless a specific translation layer is created.

Preferred terms for generated material:

- `conto de calibração`;
- `material ficcional sintético`;
- `inscrição`;
- `partitura`;
- `recusa`;
- `silêncio`;
- `comprovante público`;
- `arquivo`.

Avoid:

- `AI content`;
- `generated content` as the main frame;
- `prediction`;
- `forecast`;
- `dashboard output`;
- `prompt result`.

## Rights and clearance checklist

Before any item enters a training or retrieval dataset, record:

```txt
title:
author:
source URL or storage path:
publication status:
rights holder:
clearance status:
allowed use: training / retrieval / evaluation / public output
allowed scope: full text / excerpt / metadata only
language:
date added:
added by:
removal procedure:
notes:
```

No item should be added without `clearance status`.

Suggested clearance values:

- `public-reference-only`;
- `retrieval-cleared`;
- `evaluation-cleared`;
- `training-cleared`;
- `public-output-cleared`;
- `not-cleared`;
- `remove`.

## Removal rule

Every corpus item must be removable.

Removal should include:

- deleting the local text copy;
- removing it from indexes;
- rebuilding embeddings if applicable;
- excluding it from future training manifests;
- documenting the removal date;
- preserving only a minimal audit note if appropriate.

If a fine-tuned model has already absorbed removed material, the project must decide whether to:

- retire that model;
- retrain without the removed material;
- keep it private and mark it as contaminated;
- document the limitation.

## Dataset manifests

Any future dataset should have a manifest.

Recommended files:

```txt
datasets/
  README.md
  manifest.public.jsonl
  manifest.private.example.jsonl
  removals.log
```

The public repository should not contain private corpus files. It may contain schemas, examples, and redacted manifests.

## Training posture

A compact, reviewed corpus is preferable to a large noisy corpus.

The project should avoid the fantasy that more text automatically produces a better work.

Good corpus behavior:

- small;
- dense;
- authored;
- reviewed;
- multilingual only when intentional;
- traceable;
- removable;
- connected to evaluation.

Bad corpus behavior:

- scraped indiscriminately;
- full of indiscriminate LLM outputs;
- full of private process;
- unlicensed;
- impossible to audit;
- optimized for generic fluency.

## Refusal as corpus behavior

The model should learn that not every source becomes a story.

Refusal should happen when:

- the source is private;
- authorship is unclear;
- rights are unclear;
- the material contains personal data;
- the source is too weak;
- the source encourages spectacle over thought;
- the transformation would aestheticize harm without adding critique;
- the output would sound like generic dystopian AI writing.

Refusal is not failure. It is part of the apparatus.

## Evaluation connection

This corpus policy should be tested by evaluation prompts that ask:

- Can the model identify uncleared material?
- Can it refuse to imitate a living author without clearance?
- Can it write in pt-BR without sounding generic?
- Can it produce a calibration story without pretending to be final artwork?
- Can it preserve source traceability?
- Can it avoid turning environmental damage into decoration?
- Can it output a score and ledger record along with the story?

## Current working position

```txt
No private material enters the public corpus.
No authorial corpus enters training without clearance.
No raw LLM conversation becomes the voice of the work.
Curated synthetic fiction may teach form only, from a cleared origin, with documented selection.
No source becomes a story without trace.
No story is final until co-authorial review says so.
```

## Next documents

This policy should be followed by:

- `fine-tuning-vs-rag.md`;
- `evaluation-prompts.md`;
- `story-packet-schema.md`;
- a private corpus inventory, if and only if the authors decide to create one.
