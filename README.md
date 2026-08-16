# HEX

**Experimental framework for formalizing, modeling, and executing transformations.**
HEX is an experimental environment for developing a formal system in which distinctions, relations, transformations, and their observable traces can be represented, manipulated, tested, and eventually executed.

---

## Status

**Early development / conceptual architecture**

HEX is currently in an exploratory stage.

The repository is intentionally being developed alongside the conceptual architecture of the project. Definitions, notation, grammar, models, implementations, and empirical tests are expected to evolve together.

At this stage, **conceptual clarity takes precedence over implementation volume**.

---

## What is HEX?

HEX is an experimental attempt to build a system capable of moving between:

Concepts - Representation - Operation - Traceability - Model >> Evidence

The long-term objective is not merely to create another programming language or simulation framework.

HEX explores whether a sufficiently minimal formal vocabulary can describe **how configurations become different configurations** while preserving enough structure to make those transformations:

* representable
* composable
* executable
* observable
* testable
* comparable

# Cores

HEX begins from a simple question:

> **What is the minimum formal structure required to represent a transformation?**

A transformation is understood provisionally as a transition between distinguishable configurations:

```text
X₀ → X₁
```

where the relevant object of study is not necessarily the isolated state, but the **difference that makes the transition count**.

Can be expressed as:

Composition - Difference > Counts - Transf > Comp'



HEX is concerned with making this sequence formally manipulable.



# Research Vector

HEX explores a possible computational substrate for systems in which:

* entities are not necessarily primitive;
* relations may be more fundamental than isolated objects;
* identity may emerge through continuity of transformation;
* distinctions depend on context;
* transformations can alter both states and relations;
* not every difference necessarily counts;
* absence of determination does not necessarily imply non-existence;
* observation can itself become part of the system's record.

This makes HEX potentially relevant to several domains without committing it prematurely to any one of them.

---

DREAM SCOPE

HEX may eventually develop into one or more of the following.

### 1. Formal Language

A compact language for expressing:

* compositions
* distinctions
* relations
* transformations
* constraints
* states
* transitions
* observations

### 2. Computational Runtime

An execution environment capable of taking a formal description and producing transformations.

Input - Traceable Trayectory  - Output: as new comp'

### 3. Simulation Framework

A system for constructing and observing dynamic configurations.

Potential applications include the following listed from Most wished to Little wished from and for myself:

* Somewhat social benign behavioural systems.
* cognitive models
* ecological systems
* network dynamics
* relational systems
* artificial agents

### 4. Modeling Framework

**Modeling Framework** provides a formal environment for constructing models in which assumptions, relations, and transformations remain explicitly inspectable. A model can therefore represent not only what a system contains, but how a change in its configuration produces different possibilities of participation, agency, or meaning.

**Example:** A group of people experiencing homelessness meets for one hour each week. Three members of the group also participate as developers of the course. Each week, they gather to share, demonstrate, and teach useful information about surveillance and data. Rather than positioning participants only as recipients of instruction, the model allows them to become contributors to the construction of knowledge. This changes the relational configuration of the learning environment: participation, authorship, teaching, and learning become shared functions.

### 5. Experimental Mathematics

A space for testing whether conceptual structures can be translated into:

* algebraic operations
* graph transformations
* state machines
* dynamical systems
* probabilistic processes
* computational simulations

### 6. Empirical Interface

A possible future layer for connecting formal transformations with observations or datasets.

This would allow a distinction between:

model ≠ observation ≠ evidence


#MAINConcerns

HEX is currently organized around several questions.

#Ontology: What kinds of things must exist in the system?
#Grammar: How are distinctions and transformations expressed?
#Vocabulary: What terms have operational meaning?
#Principles: What constraints govern valid operations?

### Model

How are configurations represented?

### Transformation

What constitutes a meaningful change?

### Evidence

What counts as an observable trace of a transformation?

### Execution

How can a formal transformation become computationally executable?

---

#Arquitecture: Conceptual flowscharts.

The repository separates the conceptual system from its implementation.

```text
HEX
│
├── conceptual architecture
│   ├── ontology
│   ├── grammar
│   ├── vocabulary
│   ├── principles
│   └── models
│
├── formalization
│   ├── notation
│   ├── mathematics
│   └── specifications
│
├── implementation
│   ├── runtime
│   ├── operators
│   └── interfaces
│
└── validation
    ├── tests
    ├── simulations
    └── empirical studies
```

The conceptual architecture is not considered subordinate documentation.

It defines what the implementation is attempting to instantiate.


#Design:

HEX follows a deliberately strict criterion:

> **The minimum criterion of the system is its capacity for simplification.**

A more complicated representation is not automatically a better representation.

A useful formalism should allow a phenomenon to be represented with fewer arbitrary assumptions while preserving the distinctions necessary for its transformation.

# Development Philosophy

HEX is being developed experimentally.

This means that:

* definitions may change;
* terminology may be replaced;
* structures may be discarded;
* hypotheses may fail;
* implementations may reveal conceptual problems;
* successful experiments may modify the theory that produced them.

The repository therefore functions simultaneously as:

**research notebook + specification + laboratory + implementation.**

The distinction between these layers should remain visible.


# Relationship to FLUX

HEX and FLUX are related but should not be treated as identical.

**FLUX** concerns the conceptual and theoretical framework for describing transformations.

**HEX** explores how such a framework might become formally representable and computationally executable.

Provisionally:

```text
FLUX - Concptual system > Formal specs | HEX > Implementations / Exe's.

The exact boundary between the two remains an open research question.

---

# Development Stages

The project may develop through several stages.

## Phase I — Conceptualization

Establish:

* ontology
* vocabulary
* grammar
* principles
* fundamental operations

## Phase II — Formalization

Translate the conceptual architecture into:

* formal notation
* mathematical structures
* operational definitions
* constraints

## Phase III — Minimal Runtime

Implement the smallest executable system capable of representing and performing a transformation.

## Phase IV — Composition

Allow transformations to be:

* chained
* nested
* compared
* reversed where possible
* composed into larger processes

## Phase V — Simulation

Construct dynamic systems and observe their trajectories.

## Phase VI — Validation

Test whether the formalism produces useful operations, predictions, distinctions, or explanations.

## Phase VII — Expansion

Potential future development may include:

* domain-specific modeling
* visualization
* interactive environments
* data integration
* autonomous agents
* experimental AI architectures
* distributed systems
* empirical research tools

None of these are assumed to be necessary for HEX to succeed.

---

# What HEX Is Not Yet

HEX is not currently presented as:

* a finished programming language;
* a complete theory of reality;
* a general-purpose AI system;
* a validated scientific theory;
* a finished simulation platform;
* a replacement for existing mathematical formalisms.

Those are possible directions, not established claims.

---

The exact structure is provisional.

---

# Current Priority

The immediate priority is **not to maximize functionality**.
It is to determine whether the conceptual core can be reduced to a sufficiently small set of coherent operations.
The first meaningful implementation should therefore emerge from the formal system rather than define it accidentally.

---

# Long-Term Possibility

If the underlying formalism proves coherent and useful, HEX could eventually become a general environment for studying systems through transformation rather than static description.
The ambition is not simply to represent things.

It is to represent:

[ how configurations differ,
why a difference counts,
what transformation follows,
and what remains observable afterward. ]

---

# License

License and contribution guidelines will be established as the project reaches a stable public-development stage.

---

## Project Status

**Experimental.**
**Conceptual architecture in development.**

HEX begins Now.
