# Epson FX-2190 calibration notes

> **Historical note (October 2026).** Written during the research and rehearsal phase of the work, then called *Projeto 2047 / Arquivo Terra Viva*, and kept as process. Some of it no longer describes the work as it runs. For the current apparatus see `../../03-field-notes/2026-10-lq-590-qr-and-declared-cost.md`, `../../03-field-notes/2026-10-video-wall.md`, and `../../03-field-notes/2026-10-opening-at-casa-firjan.md`.

These notes summarize previous internal calibration sessions in a public, sanitized form.

The current physical prototype is an **Epson FX-2190** installed at AYA Studio. It is connected to a Raspberry Pi print server through USB and exposed through CUPS.

## Known prototype stack

```txt
szt.link / local workstation
  -> CUPS / IPP print server
  -> Epson FX-2190
  -> continuous fanfold paper
```

Internal addresses, usernames, passwords, serial numbers, and operational details are intentionally omitted.

## Recovered operational modes

### DOC mode

Working target:

```txt
80 columns @ 10 cpi
```

Use:

- diagnostics;
- readable text;
- administrative tests;
- calibration receipts.

### ASCII / WIDE mode

Working target from earlier tests:

```txt
100 columns @ 12 cpi
condensed off
no form feed by default
```

Use:

- ASCII art;
- wide text fields;
- visual output;
- continuous archive strips.

Required ESC/P idea:

```txt
reset printer
turn condensed mode off
select 12 cpi
send payload
avoid forced form feed when printing as continuous artwork
```

In ESC/P terms, previous tests used the equivalent of:

```txt
ESC @   reset
DC2     condensed off
ESC M   12 cpi
```

## Calibration history

### First stable path

Early testing confirmed that the print server and CUPS spool path were functional. Minimal text jobs reached the printer, and raw text output was possible after physical paper alignment and local printer state were corrected.

### ASCII width fix

A first ASCII output appeared too narrow. The cause was traced to printer state: condensed mode needed to be explicitly disabled. Once the preamble forced reset, condensed-off, and 12 cpi, the wide ASCII preset became usable.

### Compact art mode

For artwork, avoiding automatic form feed became important. Continuous output should not waste paper or force each fragment into a document-like page. Manual tear-off or future auto tear-off calibration remains preferable.

## Critical unresolved issue: width

Later diagnostics found a persistent width limit around **149 mm** under some configurations, even after attempting ESC/P mode, raw CUPS output, CPI changes, double-width commands, and margin commands.

This creates an important unresolved contradiction:

- earlier calibration suggested a useful wide 100-column mode;
- later diagnostics suggested a fixed printable width around 149 mm.

Current interpretation:

```txt
The FX-2190 is a valid prototype for the apparatus, but not yet validated as final exhibition hardware.
```

The next physical test should measure:

- visible character count at 10 cpi;
- visible character count at 12 cpi;
- actual printed width in mm;
- behavior after front-panel reset/default settings;
- behavior with raw ESC/P payloads;
- behavior with and without condensed mode;
- paper position and tractor alignment.

## Test line

A simple width test should include repeated visible characters:

```txt
000000000111111111122222222223333333333444444444455555555556666666666777777777788888888889999999999
```

A second line should mark every ten columns:

```txt
|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|
```

## Current decision

Use the FX-2190 for the next prototype block, but do not assume it is the final exhibition printer until the width issue is retested physically.
