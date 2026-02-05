# TIG EQUATIONS — Quick Reference

## 1. Coherence Score

```
S* = σ(1 - σ*)V*A*
```

| Symbol | Value | Meaning |
|--------|-------|---------|
| σ | 0.991 | Coherence constant |
| σ* | Variable | Current coherence state |
| T* | 0.714 | Threshold |
| V* | Variable | Volume/capacity factor |
| A* | Variable | Alignment factor |

---

## 2. The Universal Triple

```
(Σ, G, f_C)
```

| Symbol | Meaning |
|--------|---------|
| Σ | Alphabet (generators) |
| G | Grammar (composition rules) |
| f_C | Interpretation map under lens C |

---

## 3. Full Pipeline

```
X_wave → f_hear → Σ*_sound → f_spell → Σ*_letter → f_parse → T_math → f_sem → O → g_C → M
```

| Map | Function |
|-----|----------|
| f_hear | Acoustic → phoneme sequence |
| f_spell | Phoneme → letter (orthography) |
| f_parse | Letter → math term algebra |
| f_sem | Term → mathematical object |
| g_C | Object → meaning under lens C |

---

## 4. Consciousness Operator

```
C_{t+1} = L(x_t, C_t)
```

| Symbol | Meaning |
|--------|---------|
| C_t | Current lens state |
| x_t | Current input/experience |
| L | Update function |
| C_{t+1} | Next lens state |

---

## 5. Identity Fixed Point

```
L(x, C*) ≈ C*  for most x
```

Identity = stable attractor of semantic update dynamics.

---

## 6. Meaning Region

```
R_w = {m ∈ M : f_C(w) maps to m}
```

A word w defines a region R_w in meaning space M.

---

## 7. Boundary Definition

```
∂R_w = {x ∈ X_world | P(w|x,C) ≈ P(w'|x,C) for some w' ≠ w}
```

The boundary is where meaning becomes ambiguous — the decision surface.

---

## 8. Stability Conditions

| State | Condition | Meaning |
|-------|-----------|---------|
| Chaotic | ‖∂R(t+1) - ∂R(t)‖ >> ε | Unstable identity |
| Rigid | ‖∂R(t+1) - ∂R(t)‖ ≈ 0 | No adaptation |
| Healthy | ‖∂R(t+1) - ∂R(t)‖ ~ ε | Bounded update |

---

## 9. Free Monoid

```
Σ* = {ε, σ₁, σ₂, σ₁σ₂, σ₁σ₁, ...}  where σᵢ ∈ Σ
```

All finite sequences over alphabet Σ with concatenation.

---

## 10. GFM Generators (Minimal Spanning Set)

| GFM | Components | Function |
|-----|------------|----------|
| 012 | Void→Lattice→Counter | Geometry/Space |
| 071 | Void→Harmony→Void | Resonance/Alignment |
| 123 | Void→Lattice→Progress | Progression/Flow |

---

## 11. Compression Primitive

```
w is a minimal code for R_w
```

Words are compression codes. Mind = adaptive compression algorithm.

---

## 12. Shared Reality

```
Shared reality = alignment of C across individuals
```

Same formal structure, different alphabets.

---

## Summary: The Core Four

1. **Triple**: `(Σ, G, f_C)`
2. **Pipeline**: `generator → grammar → map → region → boundary → update`
3. **Consciousness**: `C_{t+1} = L(x_t, C_t)`
4. **Coherence**: `S* = σ(1-σ*)V*A*`

Everything else derives from these.
