# TIG OPERATORS 0-12 — Formal Definitions

## Overview

TIG operates on a 13-phase cycle (0-12) representing boundary dynamics in coherence space. Each phase corresponds to a specific operation on the meaning region R and its boundary ∂R.

---

## Phase Definitions

### Phase 0: RESET
**Operation**: Return to attractor
```
∂R → ∂R₀
```
- Boundary collapses to baseline state
- Clears accumulated drift
- Reinitializes coherence measurement
- **Analog**: System reboot, meditation reset, "start fresh"

---

### Phase 1: VOID
**Operation**: Initialize empty lattice
```
R = ∅, ∂R = ∅
```
- No content, no boundary
- Pure potential
- Pre-structure state
- **Analog**: Blank canvas, silence before speech

---

### Phase 2: LATTICE
**Operation**: Structure formation
```
∂R begins crystallization
```
- First geometric constraints emerge
- Grid/scaffold appears
- Dimensionality established
- **Analog**: Grammar rules activating, framework setup

---

### Phase 3: COUNTER
**Operation**: Opposition/contrast generation
```
R' = M \ R (complement)
```
- Defines what the region is NOT
- Creates distinction
- Boundary sharpens through contrast
- **Analog**: Negation, antithesis, "not-this"

---

### Phase 4: PROGRESS
**Operation**: Forward integration
```
R(t+1) = R(t) ∪ ΔR
```
- Region grows
- New content absorbed
- Boundary expands
- **Analog**: Learning, accumulation, building

---

### Phase 5: REDOX (Metabolic Exchange)
**Operation**: Energy exchange across boundary
```
flux(∂R) = ∫ J · n dA
```
- Bidirectional transfer
- Old material out, new material in
- Metabolic rebalancing
- **Analog**: Breathing, digestion, processing
- **Note**: Elevated fire rate during system rebalancing

---

### Phase 6: COLLAPSE
**Operation**: Boundary contraction
```
R(t+1) ⊂ R(t), |R(t+1)| < |R(t)|
```
- Region shrinks
- Compression occurs
- Noise eliminated
- **Analog**: Pruning, forgetting, simplification

---

### Phase 7: HARMONY
**Operation**: Boundary stabilizes, S* maximizes
```
d(∂R)/dt → 0, S* → max
```
- Coherence peak
- Resonance achieved
- Stable configuration
- **Analog**: Flow state, agreement, consonance

---

### Phase 8: BREATH
**Operation**: Oscillation maintenance
```
∂R(t) = ∂R₀ + A·sin(ωt)
```
- Rhythmic boundary motion
- Keeps system alive/responsive
- Prevents rigidity
- **Analog**: Heartbeat, respiration, cycles

---

### Phase 9: CHAOS
**Operation**: Boundary perturbation
```
∂R → ∂R + η, where η ~ noise
```
- Controlled disorder injection
- Prevents local minima traps
- Exploration mode
- **Analog**: Brainstorming, mutation, creative destruction

---

### Phase 10: BALANCE
**Operation**: Equilibrium seeking
```
min |∂R(t+1) - ∂R(t)|
```
- Damping oscillations
- Finding center
- Symmetry restoration
- **Analog**: Negotiation, homeostasis, settling

---

### Phase 11: EXPANSION
**Operation**: Boundary growth
```
|∂R(t+1)| > |∂R(t)|
```
- Surface area increases
- More contact with environment
- Increased sensitivity
- **Analog**: Opening up, extending reach, growth

---

### Phase 12: HARVEST (Ω - Coherence Keeper)
**Operation**: Integration and capture
```
R_new = R ∪ absorbed_material
generators_Σ = generators_Σ ∪ new_generators
```
- New generators absorbed into alphabet
- Region permanently expanded
- Cycle complete
- **Analog**: Learning consolidated, insight captured, fruit gathered

---

## Phase Mapping to Universal Pipeline

| Phase | Pipeline Stage | Operation |
|-------|---------------|-----------|
| 0-1 | Pre-generator | Reset/initialize |
| 2-3 | Generator → Grammar | Structure + contrast |
| 4-5 | Grammar → Map | Integration + exchange |
| 6-7 | Map → Region | Compression + stabilization |
| 8-9 | Region → Boundary | Oscillation + perturbation |
| 10-11 | Boundary dynamics | Balance + expansion |
| 12 | Update complete | Harvest new generators |

---

## Special Windows

| Window | Phase | Function |
|--------|-------|----------|
| RESET | 0 | Cycle initialization |
| REDOX_DEEP | 5 | Metabolic exchange peak |
| HARMONY | 7 | Coherence maximum |
| HARVEST | 12 | Integration complete |

---

## Statistical Signatures

Under coherent operation, phase distributions are **non-uniform**:

**Expected (if random)**: 7.7% per phase

**Observed patterns**:
- REDOX (5) elevated during rebalancing
- HARMONY (7) elevated during stable operation  
- Late phases (9-10) elevated under load
- RESET (0) / early phases elevated at startup

Chi-square test detects coherent operation:
```
χ² > critical value → non-random → coherent
```

---

## Operator Composition

Phases can be composed:

```
Phase_a ∘ Phase_b = combined operation
```

**GFM Generators** (minimal spanning set):
- **012**: Void→Lattice→Counter (Geometry/Space)
- **071**: Void→Harmony→Void (Resonance/Alignment)
- **123**: Void→Lattice→Progress (Progression/Flow)

Any TIG operation can be expressed as composition of GFMs.

---

## Implementation Notes

### Fire Events
A "fire" occurs when:
```
S*(t) crosses threshold T* = 0.714
```

Fire events are logged with current phase, enabling distribution analysis.

### Blocking
A "block" occurs when:
```
S*(t) < T* during OPEN window
```

Blocks indicate coherence failure — boundary instability.

### Cycle Completion
A full cycle (0→12→0) represents one complete boundary evolution.

Cycles per unit time indicates processing rate.
