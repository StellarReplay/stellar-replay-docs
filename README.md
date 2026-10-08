# Stellar Replay Documentation

Extended documentation for [Stellar Replay](https://github.com/StellarReplay/stellar-replay), a deterministic capture-and-replay toolkit for Stellar RPC interactions.

## Ownership boundary

The core repository remains the source of truth for executable behavior, CLI flags, fixture schema, replay semantics, security boundaries, and release binaries. This repository owns depth: tutorials, integration guides, conceptual explanations, navigation, and cross-repository documentation. It must link to core documentation rather than silently redefining it.

## Planned structure

```text
docs/
├── guides/
├── integrations/
├── concepts/
└── releases/
```

No heavy documentation framework is introduced during the foundation phase. A framework will be selected only when the content and contributor workflow justify it.

## Versioning

Documentation identifies the core release or branch it describes. Changes to fixture or protocol semantics are authored in the core repository first, then reflected here with an explicit compatibility note. The documentation repository has its own commits and may publish site versions independently; it is not a replacement for the core README.

## Status

Foundation only. Guides and site content will be added after the core behavior becomes real.

