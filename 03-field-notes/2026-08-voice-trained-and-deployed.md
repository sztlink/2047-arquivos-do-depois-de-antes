# Field note, August 2026: the voice is trained and the machine moves to its own host

The July note left two threads open: the voice was still settling, and the machine still ran on ateliê infrastructure with a migration only planned. This note closes both. The novel now has a trained voice, and it runs on a dedicated host that the work controls.

## The comparison the architecture asked for

`../02-generative-system/fine-tuning-vs-rag.md` had prescribed a path. Before training anything, run a comparison. Build an evaluation set, build a small cleared corpus, weigh base-plus-prompt against a lightweight adapter, and decide whether training is a demonstrated need rather than an assumption. That comparison was run.

Four candidate corpora were generated, each a hundred chapters written to the same voice contract by a different large model. They were read against each other on craft: fidelity to the source news, discipline of the punctuation contract, refusal of spectacle, whether the material consequence stayed material instead of becoming atmosphere. A reading pass ranked them and named the failure mode of each: one model's mannerism, another's tendency to let a character drift out of the world. The comparison produced a clear ordering and, more useful, a map of what each model did well enough to keep.

## The adapter

The decision the architecture reserved for a demonstrated need was made. A lightweight adapter (LoRA) for form and cadence, exactly the narrow use the architecture note allowed, with nothing about facts or memory placed inside the weights.

The training corpus is a hybrid, and honesty about its composition matters for a project that argues about extraction and consent. It combines the seven co-authored seed chapters, the gold written with the co-author, with a curated selection of the machine's own candidate chapters: synthetic material generated under the voice contract and then filtered, the weak and off-canon chapters dropped, a small traceable slice kept for the way it held the real news on the page. The dominant signal is curated synthetic text, anchored by human seeds and human curation. This sits in tension with the published corpus policy, which reserves training for cleared authored material and keeps raw model output out. Reconciling the two, whether by naming a formal category for curated synthetic fiction or by holding the adapter as a private research artifact, is a co-authorial decision, not a technical one, and it stays open. See `../02-generative-system/corpus-policy.md`.

The adapter was trained and backed up. The weights stay private.

## The voice held

Read blind, the model with the adapter writes in the work's voice and the base model without it does not. The base writes generic, ornamental, run-on. The adapter writes the vale: the verifier measuring a tap that reads zero, the keeper of an offline memory box, the closed-loop cooling that saves no water and only moves the thirst to someone off the panel, the narrator that knows it was trained on work taken without asking and does not exempt itself. The punctuation contract holds in the raw output, before the deterministic filter runs, which means the model learned the constraint instead of having it imposed after the fact.

## The machine moves to its own host

The migration the July note called planned and staged is done. The model and its adapter run on a dedicated host that the work controls, not on shared ateliê infrastructure. The dot-matrix printer moved with it, connected directly, driven locally.

The full apparatus ran end to end on this host. A real news item about data centers built on drought land entered as a source, the local model with the adapter metabolized it into a chapter, the deterministic filter checked the punctuation contract and found nothing to fix because the model had already obeyed, the text was wrapped to the carriage width, and the dot-matrix inscribed it on continuous paper. The event is recorded in the operating ledger.

## Resilience is earned, not assumed

The move was not clean. During an earlier test the host failed in a way that only a human hand could recover. For a work meant to run unattended for weeks, a failure that needs a human hand is a real threat, so it produced a hardening study rather than only a fix: a guardian layer that watches the machine and can bring it back without a visit. The apparatus is learning to survive its own duration. This extends the recovery and supervision notes already in the archive. See `../01-apparatus/controller-recovery.md` and `../01-apparatus/process-supervision.md`.

## Leaner than the first sketch

The working motor is simpler than the structured packet the early architecture drew. Instead of asking the model to return a self-scored record with score and ledger fields, the motor generates prose and a deterministic filter enforces the contract after the fact. The score and refusal machinery from the early notes remains a design reserve, not the current path. The apparatus is converging on a leaner shape than it was first drawn, which is the normal direction of a thing that has begun to actually run.
