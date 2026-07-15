# Living curation and the autonomy ladder

**Status:** living curation in production (July 2026); the ladder is the roadmap toward supervised autonomy.

The machine reads rare-earth news from a curated basket of sources. Who decides what enters, and how does the machine earn the right to decide for itself? This document describes the model.

## Living curation

- **New sources collect before they are approved.** A candidate source is added ungated: the collector starts harvesting it immediately, but everything it brings arrives in a waiting state. Approval is then *informed by the harvest*: the curators judge a source by what it actually delivered, not by its reputation.
- **Evidence is computed live.** The curation surface shows, for every source, what it contributed to the store right now. No frozen snapshots: a stale number in a curation interface is a small lie, and small lies compound.
- **The human gate sits at triage.** Every collected item waits for a human decision before it can feed the novel. Sources from sensitive geopolitical positions remain gated at the source level by explicit co-authorial decision.

## The autonomy ladder

Curation is not overhead. Every human decision is training material. The ladder:

1. **Curate with recorded reasons.** Each approval or rejection is stored with its stated reason.
2. **Criteria memory.** The accumulated reasons become the classifier's working memory (few-shot criteria, not fine-tuning).
3. **Enforcement.** The machine starts applying the learned criteria to pre-sort.
4. **Mirror triage.** The machine triages in parallel with the humans, and concordance is measured continuously.
5. **The gate.** Autonomy requires sustained concordance (target: 90 percent or better over a meaningful volume of decisions).
6. **Low-cadence autonomy with audit.** Only then does the machine operate autonomously, at low cadence, with weekly human audits and full reversibility.

The point of the ladder is that autonomy is **earned, measured, and revocable**. The machine does not get to decide what the present is made of until it has demonstrated that it reads the present the way its authors do, and even then the audit never ends.
