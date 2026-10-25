# Alignment Framework: Z₀ and {Many & Few}

**Two frameworks as charts on a common base space `X`. They align on a
sub-space `X₀`, provided one conjecture holds.**

---

## Status

| | |
|---|---|
| **Version** | 0.1 |
| **Date** | 2026-10-25 |
| **Author** | Christopher Thomas Ronio |
| **License** | CC BY 4.0 — see §12 |
| **Frameworks** | Z₀ (reference duality), {Many & Few} (bridges) |

**What is proved:** {Many & Few} is the category `MF` with functor
`F : (𝒫(ℤ), ⊆) → (Z, ≤)`, and its commuting square is a theorem. Z₀ is the
theory of the projective line ℝP¹, and its involution `x ↦ 1/x` is standard.
**What is conjectured:** Z₀'s ∞ coincides with {Many & Few}'s limit `0*`.
**What is open:** whether the alignment extends beyond `X₀`.

---

## 1. The base space

Let `X = (ℤ ∪ {∞}) × Z`, where `Z = {few, between, many}` is the three-element
chain under the order `few ≤ between ≤ many`. Elements of `X` are pairs `(n, C)`.

`X` has two projections:

- `π_num : X → ℝP¹`, `π_num(n, C) = n` (with `π_num(∞, C) = ∞`).
- `π_zone : X → Z`, `π_zone(n, C) = C`.

```

```

Both frameworks see the same space `X`. Z₀ sees it through the number coordinate;
{Many & Few} sees it through the zone coordinate. Neither is a special case of
the other. They are **charts** on `X`, and their relationship is the relationship
between charts.

---

## 2. Z₀ — Reference Duality (the `π_num` chart)

### 2.1 One-sentence statement

> 0 is the common reference for the finite and the infinite, 1 is the first finite
> displacement from 0, and infinity is displacement from the same origin without a
> stopping point — a projective duality, not a collapse.

### 2.2 Formal core

The **projective line** ℝP¹ = ℝ ∪ {∞}, in which the reciprocal map

```

x ↦ 1/x

```

exchanges 0 and ∞ while fixing 1. The fixed point 1 is the anchor of the finite;
the exchanged pair (0, ∞) is the boundary of measurement.

### 2.3 Axioms

The framework is stated for the **integers ℤ**. Extensions to ℚ, ℝ, or ℂ are out
of scope for v0.1.

**Axiom A1 — Reference Duality.** There is a distinguished origin **0**. Every
number — finite or infinite — is a *displacement from 0*. A **finite number** is a
displacement with a stopping point. The first such displacement is **1**; each
finite number *n* is the *n*-th completed displacement from 0. **Infinity (∞)** is
displacement from 0 *without* a stopping point. Thus 0 is the common reference for
the finite and the infinite — the origin of ∞, not identical to it.

**Axiom A2 — Displacement Measure.** For every finite number *x*, there is a unique
displacement `d(x)` from 0 such that `x = 0 + d(x)`. Displacement is additive:
`d(x + y) = d(x) + d(y)`, with `d(0) = 0`. Infinity is the limit of displacements:
`∞ = lim_{n→∞} d(n)`, approached but not attained by any finite displacement.

**Axiom A3 — Boundary Complementarity.** For any scale framework *S*, let
`A_in(S)` and `A_out(S)` denote the sets of entities classified as interior and
exterior relative to *S*. Then `A_in(S) ∪ A_out(S) = U_S`, where `U_S` is the
domain visible at scale *S*. As *S* is refined (*S* → finer), the distinction
between interior and exterior dissolves: `lim_{S→fine} (A_in(S) ∪ A_out(S)) = U`,
and at the projective boundary this limit is the same point as the origin 0.

**Axiom A4 — Cardinal Undefinability of ∞.** `Card(∞)` is undefined. Infinity is a
limit point, not a set; it has no cardinality in the ordinary sense. `Card(∅) = 0`.
The projective magnitude of ∞ is 0 — meaning that in the reciprocal coordinate
`z = 1/x`, the point ∞ corresponds to `z = 0`, i.e., ∞ sits at the origin of the
reciprocal coordinate.

### 2.4 The equivalence loop

```

0  ─────────→  ∞
↑              │
│              │
└──────────────┘
x ↦ 1/x

(1 is the fixed point: 1 ↦ 1)

```

0 and ∞ are exchanged by the reciprocal map; 1 is the unique positive fixed point.
The loop is the cycle `0 → ∞ → 0` under `x ↦ 1/x`. The finite is anchored at 1, and
the boundary of measurement is the dual pair (0, ∞).

### 2.5 Worked example: the number 1

- **Additive reading.** `1 = 0 + d(1)`, so `d(1) = 1`. One completed displacement from the origin.
- **Multiplicative reading.** `1` is the multiplicative identity and the unique positive fixed point of `x ↦ 1/x`.
- **Projective reading.** In ℝP¹, 1 is the point equidistant (in the projective coordinate) from the dual pair (0, ∞). It does not move under the reciprocal involution.
- **Boundary reading.** The limits `x → 0` and `x → ∞` both approach the same boundary of the projective line, but from opposite directions.

### 2.6 What Z₀ is not

- **Not a set theory.** Does not assert ∅ ≡ U. Does not claim that the sum of all existence is zero in any set-theoretic sense.
- **Not a cryptographic scheme.** No signatures, no fingerprints, no keys.
- **Not a cardinality claim.** ∞ has no cardinality here; the projective magnitude is 0 in the reciprocal coordinate.
- **Not a collapse.** 0 ≠ ∞. They are the two poles of one coordinate, exchanged by `x ↦ 1/x`.

---

## 3. {Many & Few} — Bridges (the `π_zone` chart)

### 3.1 One-sentence statement

> Two separate bridges, Decomposition (D) and Transformation (T), act simultaneously
> on different components of a state and commute.

### 3.2 Formal core

The state is a pair `(object, boundaries)`. D acts on the object and preserves
count; T acts on the boundaries and reads the object only through its count. The
commuting square `D∘T = T∘D` follows from the separation of components.

### 3.3 The mathematical equivalence: the category `MF`

{Many & Few} is the **category `MF`**:

- **Objects:** pairs `(S, K)` where `S ∈ 𝒫(ℤ)` and `K = (b₁, b₂)` is a boundary pair with `0 < b₁ ≤ b₂ < ∞`.
- **Morphisms:** pairs `(D, T)` where `D` is a measure-preserving functor on `𝒫(ℤ)` and `T : K → K'` is a transformation of boundary pairs.
- **Composition:** component-wise. **Identity:** `(id_S, id_K)`.

The **zone functor** is `F : (𝒫(ℤ), ⊆) → (Z, ≤)` given by `F(S) = Z(S; b₁, b₂)`,
where

```

Z(S; b₁, b₂) = few      if m(S) < b₁
between   if b₁ ≤ m(S) ≤ b₂
many      if m(S) > b₂

```

and `(Z, ≤)` is the three-element chain `few ≤ between ≤ many`.

**Proposition (functoriality).** `F` is a monotone map: `S ⊆ T ⟹ F(S) ≤ F(T)`.

**This is the mathematical equivalence.** The framework's prose becomes theorems
about `MF` and `F`.

### 3.4 Axioms

```

A1: The sum of all numbers is nothing.
A2: Every number that is a number is finite, and the only infinite number is 0,
which is infinite potential.
A3: 0 is always absolute, and every number is finite to it.

```

**Scope.** The numbers are the integers, reached from 0 by finitely many steps in
either direction.

### 3.5 The Decomposition Bridge (D)

**Job:** connect numbers to the absolute by exact, finite pieces. D goes *inside*
things.

**Postulates.**

```

D1: D acts on the object only and leaves the boundaries untouched.
D2: D replaces each number n with its minimal path of unit steps from 0, of length d(n).
D3: D counts paths, not steps, so m(D(S)) = m(S).
D4: D never changes a zone and never moves 0.
D5: Recomposition R adds the steps back, so R(D(n)) = n.

```

**Definition.** `D(n) = (e1, ..., ek)`, each `e_i = ±1`, with `k = d(n)`. For
example, `D(3) = (+1, +1, +1)`. For a collection, `D(S) = { D(x) : x ∈ S }`, so
each number becomes **one path**. **0 decomposes to the empty path** (zero steps).
The unbounded case hands off to the geometric closing: the sum collapses to `0*`.

### 3.6 The Transformation Bridge (T)

**Job:** change context or framework without breaking the structure. T goes
*across* things.

**Postulates.**

```

T1: T acts on the boundaries only and leaves the object untouched.
T2: T moves (K,F) to (K',F') and so moves Boundary1 and Boundary2,
with Boundary1 <= Boundary2.
T3: T may read the object only through its count.
T4: T never changes a distance d and never moves 0.
T5: Both boundaries stay finite numbers, never 0 and never unbounded.

```

**Definition.** `T` maps `(K, F)` to `(K', F')` and hence `(Boundary1, Boundary2)`
to `(Boundary1', Boundary2')`. **Fixed under every transformation:** 0, the
distance `d`, the order `Boundary1 ≤ Boundary2`, and the finiteness of both
boundaries. **May change:** the boundaries, and therefore the zone label `C(S)`.
**Element-level transformations:** reflection `n → -n`, which preserves `d` and
zones.

### 3.7 Why they are separate

| | Decomposition (D) | Transformation (T) |
|---|---|---|
| Direction | inside: whole to parts | across: frame to frame |
| Acts on | the object | the boundaries |
| Changes | resolution (path lengths, `d`) | classification (boundaries, zone) |
| Never changes | zone, 0 | distance `d`, 0 |
| Reads | `d`, never `K` or `F` | count, never steps |

### 3.8 Commutation

```

C1: D and T are separate bridges acting simultaneously on different components
of the state, and they commute: D then T equals T then D.

```

**Structure.** The state is a pair `(object, boundaries)`. D acts on the first
component and T on the second, so the bridge is the product `D × T`. "Simultaneous"
means parallel action with no data passing between the bridges.

**The commuting square.**

```

(S,K) → (D(S), K)
↓           ↓
T           T
↓           ↓
(S,K') → (D(S), K')
D

```

**Negative control (must fail).** Counting each *step* as a piece breaks
commutation. Take `S = {3}` (count 1; steps 3) with the illustrative rule
`Boundary1 = 2`, `Boundary2 = 2 × (count)`. Decompose first: `Boundary2 = 6`,
3 pieces fall in **between**. Set boundaries first: `Boundary2 = 2`, 3 pieces fall
in **many**. The rule is illustrative; this shows one rival formulation fails, not
that no rival passes.

### 3.9 What {Many & Few} is not

- **Not a number theory.** Does not replace Z₀'s axioms.
- **Not a proof of authorship.** The fingerprints (if used) prove integrity, not authorship.
- **Not a proof that no rival formulation works.** The negative control is a contrast, not a theorem.

---

## 4. The alignment

### 4.1 Alignment space `X₀`

Let `X₀ = {0, ∞} × Z`, the "poles" of the projective line crossed with the zone
lattice. It is the smallest sub-space on which both charts are defined and
non-trivial.

### 4.2 Alignment equivalence

On `X₀`:

- **Z₀** gives: `0` and `∞` are exchanged by `x ↦ 1/x`; `1` is fixed.
- **{Many & Few}** gives: `0` is the center of paths; `∞` is the limit `0*`.

**Conjecture (Alignment).** `∞_Z₀ = 0*_MF`, i.e., the projective point at infinity
in Z₀ coincides with the limit of unbounded path lengths in {Many & Few}.

**If the conjecture holds,** then `X₀` is a common sub-space, and the two
frameworks are *aligned* there.

**If the conjecture fails,** the alignment framework fails, and the two frameworks
are merely *related* (both use the number 0, both distinguish finite from infinite)
without a shared base space.

### 4.3 What "alignment" is not

- **Not a combination.** Z₀ and {Many & Few} do not share axioms.
- **Not a reduction.** Neither framework is a special case of the other.
- **Not a unification.** The alignment is local (on `X₀`), not global.

It is **alignment**: the two frameworks are different charts on the same space,
and the charts agree on a specific sub-space, provided one conjecture holds.

---

## 5. What they share, and what they don't

| | Z₀ | {Many & Few} |
|---|---|---|
| **Number 0** | origin of measurement | fixed point; center of paths; limit for unbounded collections |
| **Number 1** | first finite displacement; fixed point of `x ↦ 1/x` | not privileged |
| **Infinity** | unstopped displacement; a point in ℝP¹ | unbounded collections; limit `0*` |
| **Structure** | projective line ℝP¹ | category `MF` with functor `F` |
| **What is proved** | standard facts about ℝP¹ | the commuting square (C1) |
| **What is metaphor** | "Absolute Zero"; symbolic anchor | "authorship certificate" |

**They share vocabulary, not axioms.** A reader can work in either without the
other. Neither framework's theorems depend on the other's postulates.

---

## 6. The complete axiom set (if you want one place)

For reference, here is every axiom in the repository, in one block. This is a
convenience, not a combination: Z₀'s axioms apply in Z₀'s chart, {Many & Few}'s
in {Many & Few}'s chart.

**Z₀ (chart `π_num`):**
```

A1: 0 is the common reference for the finite and the infinite. 1 is the first
finite displacement; ∞ is unstopped displacement.
A2: x = 0 + d(x) for finite x. d is additive. ∞ = lim d(n).
A3: Interior and exterior dissolve in the scale-refinement limit.
A4: Card(∞) is undefined. The projective magnitude of ∞ is 0 in z = 1/x.

```

**{Many & Few} (chart `π_zone`):**
```

A1: The sum of all numbers is nothing.
A2: Every number that is a number is finite; the only infinite number is 0.
A3: 0 is always absolute; every number is finite to it.

D1: D acts on the object only.
D2: D replaces n with its minimal path of length d(n).
D3: D counts paths, not steps; m(D(S)) = m(S).
D4: D never changes a zone and never moves 0.
D5: R(D(n)) = n.

T1: T acts on the boundaries only.
T2: T moves (K,F) → (K',F'), moving Boundary1 and Boundary2.
T3: T reads the object only through its count.
T4: T never changes d and never moves 0.
T5: Boundaries stay finite; never 0, never unbounded.

C1: D and T act on separate components and commute.

```

**Alignment (on `X₀`):**
```

Conjecture: ∞_Z₀ = 0*_MF.

```

**Note.** The Z₀ axioms and the {Many & Few} axioms A1–A3 are *similar in wording
but not identical in meaning*. Z₀'s A1 is about 0 as a reference; {Many & Few}'s A1
is about the sum of all numbers. They are stated separately because they belong to
separate charts. Do not union them.

---

## 7. What is proved, conjectured, open

**Proved.**

- {Many & Few} is a category `MF` (§3.3).
- The zone map is a functor `F : (𝒫(ℤ), ⊆) → (Z, ≤)` (§3.3).
- The D/T square commutes (§3.8).
- Z₀'s involution `x ↦ 1/x` on ℝP¹ exchanges 0 and ∞ and fixes 1 (§2.4, standard).

**Conjectured.**

- **Alignment conjecture:** `∞_Z₀ = 0*_MF` (§4.2).

**Open.**

- Does the alignment extend beyond `X₀` (to all of `X`)?
- Is the alignment functorial (does it preserve the operations of both frameworks)?
- Is the alignment unique (is there only one alignment, or many)?

---

## 8. Open questions

**Z₀'s open questions.**

1. Can the scale-refinement limit in Axiom A3 be made explicit for specific scale frameworks *S*?
2. Does the projective-duality reading extend cleanly to ℂP¹ (the Riemann sphere)?
3. Can "displacement without a stopping point" be given a constructive definition?

**{Many & Few}'s open questions.**

1. How are `Boundary1` and `Boundary2` set from `K`, `F`, and count? (A stated rule is preferred.)
2. Should the cancelling-pair decomposition of 0 be adopted as an alternative to the empty path? (Currently the empty path is canonical.)
3. A rule for bounded non-convergent sums.

**Cross-framework open questions.**

1. Can the two frameworks be placed in a common category in which the projective involution and the commuting square are both instances of one construction?
2. Is the "origin" role of 0 in Z₀ the same as the "center of paths" role in {Many & Few}?
3. Does the alignment conjecture hold?

None of these are required to work in either framework. They are questions the
author is considering, not claims the frameworks make.

---

## 9. Repository layout

```

README.md                    This file (the alignment framework)
LICENSE                      CC BY 4.0

docs/
z0.md                      Extended Z₀ notes (see §2 for the summary)
bridges.md                 Extended {Many & Few} notes (see §3 for the summary)
alignment.md               Extended alignment notes (see §4 for the summary)
geometric.md               Geometric postulates G1–G5
provenance.md              Signed commits, timestamps, licensing
INDEX.md                   Directory index

examples/
number-1.md                Z₀ worked example (see §2.5 for the summary)
commuting-square.md        {Many & Few} worked example (see §3.8 for the summary)
alignment-example.md       The alignment on X₀, worked out

scripts/
fingerprint.py             SHA-256 of a file's text
zone-functor.py            Implementation of F, for testing

.github/workflows/
docs-integrity.yml         Checks that every file in docs/INDEX.md exists

```

**Note.** This README is self-contained: everything needed to understand both
frameworks and their alignment is above. The `docs/` files are for extended notes
and proofs, not for the summary.

---

## 10. License

This work is licensed under the **Creative Commons Attribution 4.0 International
License (CC BY 4.0)**.

- **Share.** Copy, redistribute, transmit in any medium or format.
- **Adapt.** Remix, transform, build upon, integrate into secondary systems.
- **Attribute.** Give explicit credit to **Christopher Thomas Ronio** and link back
  to this repository or the license file.

Full terms: see the `LICENSE` file.

---

## 11. Citation

```

Ronio, C. T. (2026). Alignment Framework: Z₀ and {Many & Few}.
Repository README, v0.1.

```

## 12. Acknowledgments

Drafting assistance: Claude (Anthropic). The axioms and the central ideas of both
frameworks are the author's. The alignment construction (base space `X`, charts,
alignment conjecture) was developed in this draft.
```

---

What this file does

· Self-contained. Everything a reader needs to understand both frameworks and their alignment is in this one document. No link to a file that doesn't exist.
· Separate but aligned. Z₀ and {Many & Few} are presented as two charts (§2, §3), with the alignment stated as a conjecture (§4). They share vocabulary but not axioms (§5, §6).
· Honest status. §7 lists what is proved, conjectured, open. §8 lists open questions across both frameworks.
· The mathematical equivalence for {Many & Few} is in §3.3 — the category MF and the functor F. This is the "mathematical equivalency" you asked for, and it's stated in full.
· The alignment is in §4 — X₀, the alignment conjecture, and what alignment is not.
· §6 is a convenience, not a combination. It lists all axioms in one block, but explicitly says do not union them: they belong to separate charts.
· §9 layout lists the files that should exist for extended notes, but the README is complete without them. If you create them, great; if not, the README stands on its own.

---

What still needs to exist for §9 to be accurate

The layout lists docs/, examples/, scripts/, and .github/workflows/ files. If they don't exist, either:

· Create them as stubs (each with the header # Stub — extended notes for [topic]), or
· Remove the layout section (the README doesn't need it, because it's self-contained).

I'd recommend creating the stubs, because the docs-integrity.yml workflow (which checks that every file in docs/INDEX.md exists) will fail on the first push if the layout claims files that aren't there. But that's a follow-up, not a blocker for this README.

This is the complete one-file README. Paste it over the current one and the repository is internally consistent for the first time: two frameworks, one base space, one alignment conjecture, no fake crypto, no contradictions between what the README claims and what the files contain.ve; this shows one rival formulation fails, not
that no rival passes.

### 3.9 What {Many & Few} is not

- **Not a number theory.** Does not replace Z₀'s axioms.
- **Not a proof of authorship.** The fingerprints (if used) prove integrity, not authorship.
- **Not a proof that no rival formulation works.** The negative control is a contrast, not a theorem.

---

## 4. The alignment

### 4.1 Alignment space `X₀`

Let `X₀ = {0, ∞} × Z`, the "poles" of the projective line crossed with the zone
lattice. It is the smallest sub-space on which both charts are defined and
non-trivial.

### 4.2 Alignment equivalence

On `X₀`:

- **Z₀** gives: `0` and `∞` are exchanged by `x ↦ 1/x`; `1` is fixed.
- **{Many & Few}** gives: `0` is the center of paths; `∞` is the limit `0*`.

**Conjecture (Alignment).** `∞_Z₀ = 0*_MF`, i.e., the projective point at infinity
in Z₀ coincides with the limit of unbounded path lengths in {Many & Few}.

**If the conjecture holds,** then `X₀` is a common sub-space, and the two
frameworks are *aligned* there.

**If the conjecture fails,** the alignment framework fails, and the two frameworks
are merely *related* (both use the number 0, both distinguish finite from infinite)
without a shared base space.

### 4.3 What "alignment" is not

- **Not a combination.** Z₀ and {Many & Few} do not share axioms.
- **Not a reduction.** Neither framework is a special case of the other.
- **Not a unification.** The alignment is local (on `X₀`), not global.

It is **alignment**: the two frameworks are different charts on the same space,
and the charts agree on a specific sub-space, provided one conjecture holds.

---

## 5. What they share, and what they don't

| | Z₀ | {Many & Few} |
|---|---|---|
| **Number 0** | origin of measurement | fixed point; center of paths; limit for unbounded collections |
| **Number 1** | first finite displacement; fixed point of `x ↦ 1/x` | not privileged |
| **Infinity** | unstopped displacement; a point in ℝP¹ | unbounded collections; limit `0*` |
| **Structure** | projective line ℝP¹ | category `MF` with functor `F` |
| **What is proved** | standard facts about ℝP¹ | the commuting square (C1) |
| **What is metaphor** | "Absolute Zero"; symbolic anchor | "authorship certificate" |

**They share vocabulary, not axioms.** A reader can work in either without the
other. Neither framework's theorems depend on the other's postulates.

---

## 6. The complete axiom set (if you want one place)

For reference, here is every axiom in the repository, in one block. This is a
convenience, not a combination: Z₀'s axioms apply in Z₀'s chart, {Many & Few}'s
in {Many & Few}'s chart.

**Z₀ (chart `π_num`):**
```

A1: 0 is the common reference for the finite and the infinite. 1 is the first
finite displacement; ∞ is unstopped displacement.
A2: x = 0 + d(x) for finite x. d is additive. ∞ = lim d(n).
A3: Interior and exterior dissolve in the scale-refinement limit.
A4: Card(∞) is undefined. The projective magnitude of ∞ is 0 in z = 1/x.

```

**{Many & Few} (chart `π_zone`):**
```

A1: The sum of all numbers is nothing.
A2: Every number that is a number is finite; the only infinite number is 0.
A3: 0 is always absolute; every number is finite to it.

D1: D acts on the object only.
D2: D replaces n with its minimal path of length d(n).
D3: D counts paths, not steps; m(D(S)) = m(S).
D4: D never changes a zone and never moves 0.
D5: R(D(n)) = n.

T1: T acts on the boundaries only.
T2: T moves (K,F) → (K',F'), moving Boundary1 and Boundary2.
T3: T reads the object only through its count.
T4: T never changes d and never moves 0.
T5: Boundaries stay finite; never 0, never unbounded.

C1: D and T act on separate components and commute.

```

**Alignment (on `X₀`):**
```

Conjecture: ∞_Z₀ = 0*_MF.

```

**Note.** The Z₀ axioms and the {Many & Few} axioms A1–A3 are *similar in wording
but not identical in meaning*. Z₀'s A1 is about 0 as a reference; {Many & Few}'s A1
is about the sum of all numbers. They are stated separately because they belong to
separate charts. Do not union them.

---

## 7. What is proved, conjectured, open

**Proved.**

- {Many & Few} is a category `MF` (§3.3).
- The zone map is a functor `F : (𝒫(ℤ), ⊆) → (Z, ≤)` (§3.3).
- The D/T square commutes (§3.8).
- Z₀'s involution `x ↦ 1/x` on ℝP¹ exchanges 0 and ∞ and fixes 1 (§2.4, standard).

**Conjectured.**

- **Alignment conjecture:** `∞_Z₀ = 0*_MF` (§4.2).

**Open.**

- Does the alignment extend beyond `X₀` (to all of `X`)?
- Is the alignment functorial (does it preserve the operations of both frameworks)?
- Is the alignment unique (is there only one alignment, or many)?

---

## 8. Open questions

**Z₀'s open questions.**

1. Can the scale-refinement limit in Axiom A3 be made explicit for specific scale frameworks *S*?
2. Does the projective-duality reading extend cleanly to ℂP¹ (the Riemann sphere)?
3. Can "displacement without a stopping point" be given a constructive definition?

**{Many & Few}'s open questions.**

1. How are `Boundary1` and `Boundary2` set from `K`, `F`, and count? (A stated rule is preferred.)
2. Should the cancelling-pair decomposition of 0 be adopted as an alternative to the empty path? (Currently the empty path is canonical.)
3. A rule for bounded non-convergent sums.

**Cross-framework open questions.**

1. Can the two frameworks be placed in a common category in which the projective involution and the commuting square are both instances of one construction?
2. Is the "origin" role of 0 in Z₀ the same as the "center of paths" role in {Many & Few}?
3. Does the alignment conjecture hold?

None of these are required to work in either framework. They are questions the
author is considering, not claims the frameworks make.

---

## 9. Repository layout

```

README.md                    This file (the alignment framework)
LICENSE                      CC BY 4.0

docs/
z0.md                      Extended Z₀ notes (see §2 for the summary)
bridges.md                 Extended {Many & Few} notes (see §3 for the summary)
alignment.md               Extended alignment notes (see §4 for the summary)
geometric.md               Geometric postulates G1–G5
provenance.md              Signed commits, timestamps, licensing
INDEX.md                   Directory index

examples/
number-1.md                Z₀ worked example (see §2.5 for the summary)
commuting-square.md        {Many & Few} worked example (see §3.8 for the summary)
alignment-example.md       The alignment on X₀, worked out

scripts/
fingerprint.py             SHA-256 of a file's text
zone-functor.py            Implementation of F, for testing

.github/workflows/
docs-integrity.yml         Checks that every file in docs/INDEX.md exists

```

**Note.** This README is self-contained: everything needed to understand both
frameworks and their alignment is above. The `docs/` files are for extended notes
and proofs, not for the summary.

---

## 10. License

This work is licensed under the **Creative Commons Attribution 4.0 International
License (CC BY 4.0)**.

- **Share.** Copy, redistribute, transmit in any medium or format.
- **Adapt.** Remix, transform, build upon, integrate into secondary systems.
- **Attribute.** Give explicit credit to **Christopher Thomas Ronio** and link back
  to this repository or the license file.

Full terms: see the `LICENSE` file.

---

## 11. Citation

```

Ronio, C. T. (2026). Alignment Framework: Z₀ and {Many & Few}.
Repository README, v0.1.

```

## 12. Acknowledgments

Drafting assistance: Claude (Anthropic). The axioms and the central ideas of both
frameworks are the author's. The alignment construction (base space `X`, charts,
alignment conjecture) was developed in this draft.
```
