
# ❦ HexClusterMux

**Rule 30 cellular automaton on a 6-node hexagonal ring.**

## ❦ Overview

HexClusterMux is an experimental GenExpr audio algorithm developed within the HEX framework.

It combines cellular automaton state transitions, probabilistic mutation, six oscillator partials and envelope-based audio synthesis.

**Status:** Experimental / Not yet validated.

## ❦ Architecture

```text
          CLOCK INPUT
               │
               ▼
       Six-node ring state
               │
               ▼
          RULE 30
               │
               ▼
      Probabilistic mutation
               │
               ▼
        State transition
               │
        ┌──────┼──────┐
        ▼      ▼      ▼
       AUDIO  SINK   COUNT
```

## ❦ Input

| Input | Function |
|---|---|
| `in1` | Clock ramp. A negative transition triggers the next state update. |

The clock event is detected through:

`delta(in1) < -0.5`

## ❦ Parameters

| Parameter | Default | Minimum | Maximum |
|---|---:|---:|---:|
| `base` | 220 | 20 | 2000 |
| `decay` | 0.9993 | 0.9 | 0.99999 |
| `click` | 0.25 | 0 | 1 |
| `spread` | 0 | 0 | 1 |

## ❦ State Model

- Six cells arranged in a circular topology.
- Initial active cells: positions 0 and 3.
- Cellular transition: Rule 30.
- Optional probabilistic bit mutation.
- Automatic reseeding when the ring becomes inactive.

The transition rule is:

`new = left XOR (self OR right)`

## ❦ Frequency Relations

The six oscillators use these frequency ratios:

`1, 9/8, 5/4, 3/2, 5/3, 2`

Each oscillator maintains an individual phase and envelope.

## ❦ Outputs

| Output | Function |
|---|---|
| `out1` | Audio synthesis |
| `out2` | Global sink state |
| `out3` | Number of active cells |

## ❦ Implementation Environment

GenExpr / Cycling '74 Max / Gen.

The source is intended for a compatible Gen environment. A host patcher, input configuration and reproducible execution test are still required.

Documentation:
https://docs.cycling74.com/userguide/gen/gen_genexpr/

## ❦ Provenance

Original source:

`000-FLUX/03-Phenomena/1-Densos raros/Densos-raros.md.md`

Origin commit:

`7a6072b`

Extracted source integrity:

`SHA256: 6f7e08115c26c5df878c411de59185e701cc14e73a27fd7eaafe3f8cabffd63f`

The original FLUX document remains unchanged.

## ❦ Validation

This module has not yet been declared operationally validated.

Validation must include:

- GenExpr compilation.
- Clock input testing.
- Six-cell state transition testing.
- Audio output verification.
- Parameter range testing.
- Sink and reseeding behavior.

ᛝ HEX begins.
