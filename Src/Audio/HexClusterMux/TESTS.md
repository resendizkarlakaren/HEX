
# ❦ HexClusterMux — Validation Protocol

**Status:** Pending execution.

This document defines the initial validation protocol for HexClusterMux.

No test is considered passed until its result has been observed and recorded in a compatible Gen environment.

## ❦ 01 — Compilation

- [ ] Load the source in a compatible Gen environment.
- [ ] Confirm that the GenExpr code compiles.
- [ ] Record the Max / Gen version.
- [ ] Record any compilation warnings or errors.

## ❦ 02 — Initialization

Expected initial configuration:

- Six cells.
- Active positions: 0 and 3.
- Remaining positions: 1, 2, 4 and 5 inactive.

- [ ] Verify initialization.
- [ ] Verify frequency-ratio initialization.
- [ ] Verify that initialization occurs only once.

## ❦ 03 — Clock Input

Input: `in1`

The transition detector is:

`delta(in1) < -0.5`

- [ ] Test a ramp with a downward wrap.
- [ ] Verify one state update per detected event.
- [ ] Verify behavior without a clock event.

## ❦ 04 — Cellular Automaton

Transition rule:

`new = left XOR (self OR right)`

Topology: six-node circular ring.

- [ ] Verify neighbor wrapping.
- [ ] Verify state transitions.
- [ ] Verify that all six nodes are updated.
- [ ] Compare observed results against a reference calculation.

## ❦ 05 — Mutation

Parameter: `spread`

- [ ] Test `spread = 0`.
- [ ] Test an intermediate value.
- [ ] Test `spread = 1`.
- [ ] Record the observed mutation frequency over repeated trials.

Note: mutation is probabilistic, so individual trials are not expected to produce identical sequences.

## ❦ 06 — Sink and Reseeding

- [ ] Verify global sink output.
- [ ] Verify behavior when all cells become inactive.
- [ ] Verify automatic reseeding.
- [ ] Confirm that the system continues evolving.

## ❦ 07 — Audio Generation

- [ ] Verify all six oscillator phases.
- [ ] Verify the six frequency ratios.
- [ ] Verify envelope decay.
- [ ] Verify impulse behavior.
- [ ] Check output stability and audible artifacts.

## ❦ 08 — Outputs

| Output | Expected meaning |
|---|---|
| `out1` | Audio signal |
| `out2` | Global sink state |
| `out3` | Number of active nodes |

- [ ] Verify audio output.
- [ ] Verify sink output remains binary.
- [ ] Verify active-node count stays between 0 and 6.

## ❦ 09 — Validation Record

| Field | Result |
|---|---|
| Execution environment | Pending |
| Max / Gen version | Pending |
| Compilation | Not tested |
| Functional tests | Not tested |
| Audio verification | Not tested |
| Validation date | Pending |

## ❦ Validation Policy

A successful compilation does not establish full functional validation.

HexClusterMux must pass the relevant functional and audio tests before being described as a validated implementation.

ᛝ HEX begins.
