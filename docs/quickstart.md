# Ten-minute offline quickstart

This walkthrough uses the released `stellar-replay` v0.1.0 CLI and the core
repository's checked-in fixture. Run the commands from a
[`stellar-replay`](https://github.com/StellarReplay/stellar-replay) checkout, or
replace the path with a reviewed fixture of your own. It does not require a
wallet, credential, or live RPC endpoint.

## 1. Obtain the core

Download the archive for your supported platform from the [v0.1.0 release](https://github.com/StellarReplay/stellar-replay/releases/tag/v0.1.0)
and verify it with `SHA256SUMS` before placing `stellar-replay` on your `PATH`.

## 2. Validate and inspect a fixture

```text
stellar-replay validate --fixture fixtures/get-health.json
stellar-replay inspect --fixture fixtures/get-health.json
```

Validation checks schema, supported request semantics, and the integrity hash.
Inspection prints safe metadata without dumping the response payload.

## 3. Replay offline

```text
stellar-replay replay --fixture fixtures/get-health.json --method getHealth
stellar-replay serve --fixture fixtures/get-health.json --listen 127.0.0.1:8787
```

Replay and serve do not contact the recorded endpoint. The local server binds to
loopback by default and serves only validated fixture responses.

## 4. Record only when explicitly needed

`record` is the only network-dependent command. It requires an explicit HTTPS
endpoint and should be run only after reviewing the [capture contract](https://github.com/StellarReplay/stellar-replay/blob/main/docs/CAPTURE.md)
and sanitizing the resulting fixture.
