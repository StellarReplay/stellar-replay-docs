# GitHub Action integration

The companion [`stellar-replay-action`](https://github.com/StellarReplay/stellar-replay-action)
repository provides an untagged Action integration for the released core CLI.
It downloads a pinned core release, verifies `SHA256SUMS`, and runs offline
fixture validation or replay.

```yaml
name: deterministic-rpc-test
on: [push, pull_request]
jobs:
  replay:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v5
      - uses: StellarReplay/stellar-replay-action@main
        with:
          fixture: fixtures/get-health.json
          command: validate
          core-version: 0.1.0
```

The Action does not sign transactions, use wallet credentials, or contact a live
RPC endpoint. It currently has no release tag; pinning `main` is therefore a
development integration choice, not a stable marketplace compatibility promise.
The core repository remains authoritative for fixture semantics and CLI behavior.
