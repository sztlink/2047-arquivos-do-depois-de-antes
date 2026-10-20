# Encoding and typography

> **Historical note (October 2026).** Written during the research and rehearsal phase of the work, then called *Projeto 2047 / Arquivo Terra Viva*, and kept as process. Some of it no longer describes the work as it runs. For the current apparatus see `../../03-field-notes/2026-10-lq-590-qr-and-declared-cost.md`, `../../03-field-notes/2026-10-video-wall.md`, and `../../03-field-notes/2026-10-opening-at-casa-firjan.md`.

Dot-matrix printing makes character encoding visible.

A modern system often treats text as Unicode by default. Older printer protocols do not. Accents, symbols, line endings, and code pages can become material failures.

## ASCII first

For early apparatus tests, pure ASCII is the safest mode.

ASCII makes width, spacing, and printer state easier to diagnose. It also connects directly to the visual language of mechanical text output.

## Accents are not trivial

Portuguese text with accents should not be sent as raw UTF-8 without testing.

Characters such as:

```txt
á é í ó ú ã õ ç Á É Ó Ç
```

may print incorrectly depending on:

- printer character table;
- CUPS filter path;
- raw versus driver mode;
- code page;
- operating system;
- persistent printer state.

## Candidate encodings

Previous tests considered common legacy encodings such as:

- ISO-8859-1;
- CP850;
- CP860;
- printer-specific Epson character tables.

No public final winner is declared here yet. The next physical validation should print a short accent proof and document the result visually.

## Accent proof

A minimal proof text:

```txt
Teste de acentos: acao / ação, coracao / coração, Joao / João,
Sao Paulo / São Paulo, cafe / café, ciencia / ciência, maca / maçã,
C cedilha / Ç, A agudo / Á, E agudo / É, O agudo / Ó.
```

## Typography as constraint

The project should not treat typography as a styling layer added later. On this apparatus, typography is constrained by:

- character cell;
- CPI;
- line spacing;
- ribbon density;
- paper feed;
- code page;
- mechanical registration;
- text wrapping;
- printer state.

## Artistic question

Encoding errors can be bugs, but they can also reveal the violence of translation between contemporary AI text and older mechanical inscription systems.

Open question:

```txt
Should accent failure be fully corrected, or can some failures remain visible as material evidence?
```

Current posture: solve encoding for controlled operation, but preserve failed proofs as research evidence.
