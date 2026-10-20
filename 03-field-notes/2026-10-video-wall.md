# Field note . August to October 2026 . The video wall

Status. Field note, public and sanitized. The August image engine described in `2026-08-image-and-print-engine.md` is superseded by what follows.

## Two scenes per chapter

Every chapter has two short video scenes. The same model that writes the chapter proposes them, and a fixed visual grammar turns each proposal into a prompt, with no other model in between. Scene A is rendered in a visual style the work calls *normais*. Scene B is rendered in a style called *janelas*, and it is anchored to one sentence of the chapter, the sentence that is underlined on the printed page.

## The engine runs at home

The scenes are generated locally with **MiniMax-H3** in reference-to-video mode, with the Turbo LoRA by Larryvrh, in a version quantized by Felipe Sztutman. The model is larger than 130 GB and the cards are consumer cards of 24 GB, so the model is reassembled and loaded in blocks. A scene of five seconds takes about twelve minutes and close to 54 Wh. The precision moved from 4-bit to 8-bit in September and to bf16 on October 14.

The recipe, the measurements, and the traps are published as open code at <https://github.com/sztlink/h3-consumer-bench>.

The video follows the book. Rendering runs on the exhibition machine, on an RTX 3090, and a second card, an RTX 4090 in the studio, renders in parallel and redoes scenes. The energy of every scene is measured at the GPU and goes to the foot of the printed page (see `2026-10-lq-590-qr-and-declared-cost.md`).

## The wall program

The wall is projected by a laser projector that turns itself on and off with the hours of the house. The program that plays it is a fork of ONO-SENDAI, a real-time VJ instrument written in openFrameworks, adapted for the work in August 2026.

- It plays the generated takes and degrades and composes them live, through a chain of GLSL post-processing and modulators.
- The cadence of the needle replaces audio as the source of modulation. The printer drives the image.
- The wall captions, live, the sentence the printer head is typing at that moment.

It runs on a second GPU of the exhibition machine, separate from the card that renders.

## The second screen

A laptop in the room shows a public screen in kiosk mode, titled *O que Herética, a narradora sintética, não registrou*, what Herética, the synthetic narrator, did not record. It follows in real time what the needle is writing.

## On the site

Every scene is online, captioned with its chapter, at <https://heretica.xyz/videos.html>. The site plays them muted. The sound layer of the work is the printer.
