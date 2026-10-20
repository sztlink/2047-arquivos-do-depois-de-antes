# Local controller

> **Historical note (October 2026).** Written during the research and rehearsal phase of the work, then called *Projeto 2047 / Arquivo Terra Viva*, and kept as process. Some of it no longer describes the work as it runs. For the current apparatus see `../03-field-notes/2026-10-lq-590-qr-and-declared-cost.md`, `../03-field-notes/2026-10-video-wall.md`, and `../03-field-notes/2026-10-opening-at-casa-firjan.md`.

The local controller is the physical machine that keeps the apparatus alive in the exhibition space.

It does not need to be the same machine that runs the model.

## Role

The controller can:

- collect public signals;
- call a local or remote model;
- maintain local memory and ledgers;
- calibrate sonic score through szt.link;
- format stories for the dot-matrix printer;
- send print jobs;
- log printing, silence, refusal, and failure;
- recover after network or printer interruption.

## Controller versus model host

The controller and the model host are separate roles.

```txt
local controller
  -> source collection
  -> memory and state
  -> score calibration
  -> printer control
  -> logs and fallback

model host
  -> text generation
  -> optional fine-tuned model
  -> local, cloud, or hybrid inference
```

A long-duration exhibition installation may use a physical controller connected to the printer while sending requests to a hosted fine-tuned model. The exact exhibition duration remains to be confirmed from the institutional schedule.

## Why a physical controller matters

The controller keeps the work tied to the room.

Even if model inference happens remotely, the local machine remains responsible for paper, timing, silence, failure, and recovery. It is the conductor of the physical apparatus.

## Old server as material body

Using an old professional server or recovered computer may be conceptually stronger than using a new mini PC.

It connects the work to:

- electronic waste;
- discarded enterprise infrastructure;
- maintenance culture;
- heat, fans, noise, weight, dust;
- the afterlife of computational systems.

The old server should not be chosen only for theatrical effect. It must still be stable enough to run the installation.

## Minimum functional requirements

The controller needs:

- stable power;
- stable network;
- local storage;
- printer connection;
- process supervision;
- logs;
- safe restart behavior;
- ability to stop printing immediately;
- local fallback mode.

It does not need a powerful GPU if generation is remote.

## Printer connection

For the current Epson FX-2190 prototype, the preferred practical connection is USB.

### USB

Use for the first working path.

Advantages:

- simple;
- available on the FX-2190;
- compatible with modern machines;
- easier CUPS integration;
- avoids unreliable adapter chains.

### Parallel

The parallel port belongs to the printer's original historical context. It may be interesting as media archaeology, but it is not the preferred automation path.

Risks:

- adapters can be unreliable;
- modern machines rarely include native parallel ports;
- debugging adds friction without clear benefit.

### Serial

The FX-2190 does not require serial for the current path. Some old servers may include serial ports, but the printer does not make that useful unless a specific optional serial interface is installed and validated.

## Long-duration posture

For a full exhibition run, the controller must be treated as runtime infrastructure:

- monitored;
- restartable;
- replaceable;
- logged;
- physically accessible;
- able to fail without destroying the archive.

## Public boundary

This file does not publish internal IP addresses, credentials, serial numbers, or production-specific configuration.
