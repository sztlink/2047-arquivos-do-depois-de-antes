# Model voice and training path

This file records a possible model strategy for a long-duration writing machine.

It is not a final training plan and not a rights clearance document.

## Core idea

The writing engine should not behave like a generic art-and-technology assistant.

If the work becomes a continuous book-writing apparatus across the exhibition period, the model should learn from a carefully cleared corpus connected to the authors' public writing, vocabulary, and conceptual fields.

The exact duration is not fixed in this file. The institutional material reviewed so far asks for confirmation of the exhibition period and daily operating hours, but does not establish a 100-day duration.

```txt
not a generic art-tech model
but a situated writing instrument for Projeto 2047
```

## What the model should learn

The model should learn:

- vocabulary;
- rhythm;
- conceptual pressure;
- recurring concerns;
- ways of connecting image, archive, technology, extraction, memory, and politics;
- how to sustain a long-form work across many days;
- how not to sound like a generic LLM.

It should not simply memorize text.

## Corpus principle

Use authored and cleared material.

Possible corpus layers:

1. Public or explicitly cleared writings by Giselle Beiguelman.
2. Public or explicitly cleared writings by Felipe Sztutman.
3. Sanitized szt.link material selected by Felipe.
4. Project-specific notes written for this archive.
5. Public references used only as context or retrieval sources, not as unlicensed voice cloning material.

## What not to train on directly

Chatbot conversations should not be treated as high-quality answer data.

They may be useful to extract:

- themes;
- questions;
- tensions;
- vocabulary gaps;
- prompts for human review;
- evaluation scenarios.

But raw GPT, Claude, Grok, or other model answers should not become the primary training target. Otherwise the model learns generic assistant style instead of the authors' thinking and the work's language.

## Dataset shape

A compact, curated dataset is preferable to a large mediocre one.

Possible training examples:

```json
{
  "instruction": "Transform this public signal into a 2047 short story fragment.",
  "context": {
    "source_summary": "...",
    "project_bible": "...",
    "style_constraints": ["restrained", "material", "archival", "no generic cyberpunk"],
    "score_constraints": {
      "density": "sparse",
      "line_width": 72,
      "silence_after_seconds": 90
    }
  },
  "response": {
    "story": "...",
    "score": {
      "tempo": "slow",
      "density": "sparse",
      "print_mode": "text"
    }
  }
}
```

## Fine-tuning versus RAG

Two paths may coexist.

### Fine-tuning

Fine-tuning can shape voice, style, response form, and project-specific behavior.

It is useful for:

- cadence;
- recurring structures;
- refusal behavior;
- short story form;
- score output;
- avoiding generic assistant language.

### Retrieval / external memory

Retrieval should preserve facts, references, sources, and evolving project memory.

It is useful for:

- public news signals;
- source ledger;
- project bible;
- daily archive state;
- previous printed stories;
- factual grounding.

## Training posture

A local training phase is plausible if the project uses available GPUs. The trained model may later be served locally or remotely.

A long-duration installation does not require the full model to run on the printer controller. The physical controller can call a hosted model through an API while keeping local state, source ledger, print ledger, score, fallback rules, and printer control.

## Rights and authorship boundary

Before training on any authored corpus, the project must clarify:

- permission;
- corpus scope;
- whether full texts or excerpts are used;
- whether outputs can be public;
- whether model weights can be shared;
- whether the model is private, local, hosted, or eventually archived.

Until then, this file describes a possible technical-artistic direction, not an authorization.

## Evaluation

The model should be evaluated with prompts that test:

- whether it writes short stories, not explanations;
- whether it preserves the 2047 frame;
- whether it avoids generic cyberpunk;
- whether it can output a sonic score;
- whether it refuses weak sources;
- whether it keeps source traceability;
- whether it can sustain variation across many days.

## Working position

```txt
The model is not the artwork.
The model is one instrument in the apparatus.
The book emerges from model, source, score, printer, paper, silence, and human calibration.
```

## Realized path, August 2026 (v0.3.0)

The strategy this file sketched has a first realization. A situated writing instrument now exists: a local base model shaped by a lightweight adapter for the work's voice, served on a host the work controls, called by the controller with reasoning disabled for a clean single pass.

Two points from this file held. The instrument is not a generic art-tech model, and a compact curated dataset beat the fantasy of scale, the training set being small, in the low hundreds of examples.

One point needs an honest correction. This file and `corpus-policy.md` warn against raw model output as a training target. The working adapter's corpus is dominantly curated synthetic chapters, generated under the voice contract and then filtered, anchored by the seven co-authored seed chapters. These are not raw assistant conversations. They are candidate chapters in the target form, selected by evaluation. Whether that distinction is enough to sit inside the published corpus policy is a co-authorial decision, recorded as open. The rights and authorship boundary stated above is unchanged. The weights stay private, and no clearance question is settled by the existence of a working research artifact.
