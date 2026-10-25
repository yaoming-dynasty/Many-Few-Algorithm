# Alignment Framework: Z₀ and {Many & Few}

**Two frameworks as charts on a common base space `X`. They align on a
sub-space `X₀`, provided one conjecture holds.**

---

## Status

| | |
|---|---|
| **Version** | 0.1 (alignment draft) |
| **Date** | 2026-10-25 |
| **Author** | Christopher Thomas Ronio |
| **License** | CC BY 4.0 — see `LICENSE` |
| **Frameworks** | Z₀ (reference duality), {Many & Few} (bridges) |
| **Alignment** | Theorem with one open conjecture |

**What is proved:** {Many & Few} is the functor `F : (𝒫(ℤ), ⊆) → (Z, ≤)`,
and its commuting square is a theorem about this functor.
**What is conjectured:** Z₀'s ∞ coincides with {Many & Few}'s limit `0*`.
**What is open:** whether the alignment extends beyond `X₀`.

---

## 1. The base space

Let `X = (ℤ ∪ {∞}) × Z`, where `Z = {few, between, many}` is the three-element
chain. Elements of `X` are pairs `(n, C)`.

`X` has two projections:

- `π_num : X → ℝP¹`, `π_num(n, C) = n` (with `π_num(∞, C) = ∞`).
- `π_zone : X → Z`, `π_zone(n, C) = C`.

---

## 2. The two charts

### Z₀ as the `π_num` chart

Z₀ is the theory of the projective line ℝP¹:

- The involution `x ↦ 1/x` exchanges 0 and ∞, fixes 1.
- The axioms A1–A4 (Reference Duality, Displacement Measure, Boundary
  Complementarity, Cardinal Undefinability of ∞).

**Full documentation:** [`docs/z0.md`](docs/z0.md)

### {Many & Few} as the `π_zone` chart

{Many & Few} is the theory of the zone functor `F : (𝒫(ℤ), ⊆) → (Z, ≤)`:

- The zone map `F(S) = Z(S; b₁, b₂)`.
- The D/T separation (object vs. boundaries).
- The commuting square (C1).

**Full documentation:** [`docs/bridges.md`](docs/bridges.md)

---

## 3. The alignment

### Alignment space `X₀`

Let `X₀ = {0, ∞} × Z`, the "poles" of the projective line crossed with the zone
lattice. It is the smallest sub-space on which both charts are defined and
non-trivial.

### Alignment equivalence (proposed)

On `X₀`:

- **Z₀** gives: `0` and `∞` are exchanged by `x ↦ 1/x`; `1` is fixed.
- **{Many & Few}** gives: `0` is the center of paths; `∞` is the limit `0*`.

**Conjecture (Alignment).** `∞_Z₀ = 0*_MF`, i.e., the projective point at infinity
in Z₀ coincides with the limit of unbounded path lengths in {Many & Few}.

**If the conjecture holds,** then `X₀` is a common sub-space, and the two
frameworks are *aligned* there.

**If the conjecture fails,** the alignment framework fails, and the two
frameworks are merely *related* (both use the number 0, both distinguish finite
from infinite) without a shared base space.

### What "alignment" is not

- It is **not** a combination. Z₀ and {Many & Few} do not share axioms.
- It is **not** a reduction. Neither framework is a special case of the other.
- It is **not** a unification. The alignment is local (on `X₀`), not global.

It is **alignment**: the two frameworks are different charts on the same space,
and the charts agree on a specific sub-space, provided one conjecture holds.

---

## 4. The {Many & Few} equivalence, in detail

The mathematical equivalence for {Many & Few} is:

> **{Many & Few} is the category `MF` whose objects are pairs `(S, K)` and
> whose morphisms are pairs `(D, T)` acting on `S` and `K` respectively, together
> with the functor `F : (𝒫(ℤ), ⊆) → (Z, ≤)` that assigns a zone to each subset.**

The framework's claims become theorems:

| Claim | Mathematical statement |
|---|---|
| D preserves count | `m(D(S)) = m(S)` (D is a measure-preserving functor) |
| T preserves the object | `π_S(T(S, K)) = S` (T acts only on the second component) |
| D and T commute | The square `(S, K) → (D(S), K) → (D(S), K') → (S, K')` commutes |
| Zones are monotone | `F` is a monotone map of posets |
| The zone is `F(S)` | `F(S) = Z(S; b₁, b₂)` |

**This is the mathematical content of {Many & Few}.** The prose was a description of
this category; the category is the framework.

---

## 5. Repository layout
```

README.md                    This file (the alignment map)
LICENSE                      CC BY 4.0

docs/
z0.md                      Z₀ in full: axioms, equivalence loop, worked example
bridges.md                 {Many & Few} in full: category MF, functor F, D/T
alignment.md               The alignment theorem, the conjecture, the proof obligation
geometric.md               Geometric postulates G1–G5 (companion to both)
provenance.md              Signed commits, timestamps, licensing
INDEX.md                   Directory index

examples/
number-1.md                Z₀ worked example
commuting-square.md        {Many & Few} worked example
alignment-example.md       The alignment on X₀, worked out

scripts/
fingerprint.py             SHA-256 of a file's text
zone-functor.py            Implementation of F, for testing

.github/workflows/
docs-integrity.yml         Checks that every file in docs/INDEX.md exists

---

## 6. What is proved, conjectured, open

**Proved.**

- {Many & Few} is a category MF (Definition 6).
- The zone map is a functor (Proposition, Definition 4).
- The D/T square commutes (Proposition, Definition 6).

**Conjectured.**

- **Alignment conjecture:** `∞_Z₀ = 0*_MF`.

**Open.**

- Does the alignment extend beyond `X₀` (to all of `X`)?
- Is the alignment functorial (does it preserve the operations of both frameworks)?
- Is the alignment unique (is there only one alignment, or many)?

---

## 7. License

CC BY 4.0. See `LICENSE`.

## 8. Citation

```
