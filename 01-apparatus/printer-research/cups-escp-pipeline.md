# CUPS and ESC/P pipeline

> **Historical note (October 2026).** Written during the research and rehearsal phase of the work, then called *Projeto 2047 / Arquivo Terra Viva*, and kept as process. Some of it no longer describes the work as it runs. For the current apparatus see `../../03-field-notes/2026-10-lq-590-qr-and-declared-cost.md`, `../../03-field-notes/2026-10-video-wall.md`, and `../../03-field-notes/2026-10-opening-at-casa-firjan.md`.

The current prototype uses a print server layer rather than direct USB from the main workstation.

## Public architecture

```txt
workstation / szt.link process
  -> print payload
  -> CUPS / IPP print server
  -> raw or filtered queue
  -> Epson FX-2190
  -> continuous paper
```

## Two possible paths

### Raw ESC/P path

Best for controlled text and ASCII output.

```txt
ESC/P preamble + plain text body -> raw print job -> printer
```

Advantages:

- predictable printer state;
- direct control over CPI and condensed mode;
- better for ASCII art;
- lower risk of accidental PostScript being printed as text when configured correctly.

Risks:

- encoding must be explicit;
- no layout engine;
- printer state can persist across jobs;
- physical panel settings still matter.

### Driver / PostScript path

Useful for normal computer printing, but riskier for the artwork unless fully controlled.

A previous failure mode occurred when a PostScript-like job reached the printer without the correct conversion path. The printer interpreted the code as text and began printing literal program text, producing uncontrolled paper output.

Public lesson:

```txt
For the artwork, do not assume a generic desktop printing path is safe.
```

## ESC/P preamble for ASCII

Previous tests showed the need to force printer state before sending ASCII art.

Conceptual preamble:

```txt
reset
condensed off
12 cpi
payload
```

Representative ESC/P sequence:

```txt
ESC @
DC2
ESC M
```

This should be treated as a starting point, not a final driver.

## Form feed policy

Documents may use form feed.

Artwork should avoid automatic form feed by default. Continuous paper should behave as an accumulating strip, not a stack of isolated office pages.

## Safety posture

Before any long print run:

1. Clear pending jobs.
2. Confirm the queue is accepting jobs.
3. Print a short safe test.
4. Confirm paper alignment physically.
5. Confirm encoding.
6. Only then send continuous output.

## What remains to build

A future project-specific print tool should support:

- `status`;
- `clear-queue`;
- `print-safe-test`;
- `print-width-test`;
- `print-accent-test`;
- `print-ascii`;
- `print-continuous-fragment`;
- logging of payload hash, timestamp, and output mode.
