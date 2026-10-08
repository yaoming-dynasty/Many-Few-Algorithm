# {Many & Few}: Bridges

**Two separate bridges, Decomposition and Transformation, that act simultaneously and commute.**

> Status: working draft (v0.1) · Date: 2026-10-08
> Author: **Christopher T Ronio**
> © 2026 Christopher T Ronio. License: *not yet chosen, add a `LICENSE` file.*
> Companions: `README.md` (axioms, framework, algebra) and `Geometric.md` (geometry).

---

## 1. Authorship certificate

The framework's own algorithm is

```
{Many & Few}(S) = (S, C(S))
```

where `C(S)` is the zone a collection falls into: **few**, **between**, or **many**, decided by comparing the measure `m(S)` with two adaptive boundaries, `Boundary1 <= Boundary2`.

### 1.1 The object

| Item | Value |
|---|---|
| Context `K` | authorship attribution |
| `S` | the set of authors = { Christopher T Ronio } |
| Encoding | authors are indexed by order of attribution, so Christopher T Ronio = 1 |
| `m(S)` | count of elements = 1 |
| Boundaries (declared by the author) | `Boundary1 = 2`, `Boundary2 = 4` |
| `C(S)` | **few** (1 < Boundary1) |

### 1.2 Certification by alternating crossing

Each bridge is applied to its own component of the state `(object, boundaries)`:

- **D** (Decomposition) replaces the author's number with its path: `D(1) = (+1)`. The count stays 1.
- **T** (Transformation) moves the context from `K` = authorship to `K'` = verification, with boundaries declared as `(2, 4) -> (3, 6)`.

The four states of the crossing:

| State | Object | Boundaries | Zone |
|---|---|---|---|
| `s00` | `S` = { Christopher T Ronio } | (2, 4) | few |
| `s10` | `D(S)` = { (+1) } | (2, 4) | few |
| `s01` | `S` | (3, 6) | few |
| `s11` | `D(S)` | (3, 6) | few |

```
          D
 s00 ------------> s10
  |                 |
  | T               | T
  v                 v
 s01 ------------> s11
          D
```

The two routes cross at the center and meet at `s11`:

- **Route 1 (D first):** `s00 -> s10 -> s11`
- **Route 2 (T first):** `s00 -> s01 -> s11`

Alternating the bridges repeatedly gives the same endpoint:

- **D, T, D, T:** `s00 -> s10 -> s11 -> s11 -> s11`
- **T, D, T, D:** `s00 -> s01 -> s11 -> s11 -> s11`

(Repeating a bridge with the same target does nothing further; see section 5.)

**Certificate.** The authorship statement survives every route and every alternation:

```
{Many & Few}(S) = ({Christopher T Ronio}, few)
```

### 1.3 Fingerprints (SHA-256)

The documents carry four fingerprints. Each is reproducible from the exact text shown, with the command beside it.

**Axioms** (identical to `README.md` and `Geometric.md`):

```
6e97c9160408cf86510bf919ddf55074ef68236f60f3ae1887f63dc1e6e4bd26
```

```bash
printf '%s\n' \
"A1: The sum of all numbers is nothing." \
"A2: Every number that is a number is finite, and the only infinite number is 0, which is infinite potential." \
"A3: 0 is always absolute, and every number is finite to it." \
| sha256sum
```

**Decomposition Bridge postulates** (section 3):

```
8f09e1d31ba5fe8bd9ef5bcd82bb15f9f49950448d83ca877271d64b2c2c6d81
```

```bash
printf '%s\n' \
"D1: D acts on the object only and leaves the boundaries untouched." \
"D2: D replaces each number n with its minimal path of unit steps from 0, of length d(n)." \
"D3: D counts paths, not steps, so m(D(S)) = m(S)." \
"D4: D never changes a zone and never moves 0." \
"D5: Recomposition R adds the steps back, so R(D(n)) = n." \
| sha256sum
```

**Transformation Bridge postulates** (section 4):

```
a4d191794d5addc7dcedfd054f0d6293cc3b7bf531edaaa3b8afd041a3ba4b7c
```

```bash
printf '%s\n' \
"T1: T acts on the boundaries only and leaves the object untouched." \
"T2: T moves (K,F) to (K',F') and so moves Boundary1 and Boundary2, with Boundary1 <= Boundary2." \
"T3: T may read the object only through its count." \
"T4: T never changes a distance d and never moves 0." \
"T5: Both boundaries stay finite numbers, never 0 and never unbounded." \
| sha256sum
```

**Crossed fingerprint.** The two postulate lists interleaved alternately (D1, T1, D2, T2, and so on), followed by the commutation postulate. This binds the two bridges to each other, so altering either list, or the order of the crossing, changes it:

```
963640db64743ed4f275654289a290dfce20ccee9fd6771c8bb6f3d9fd3ddd14
```

```bash
printf '%s\n' \
"D1: D acts on the object only and leaves the boundaries untouched." \
"T1: T acts on the boundaries only and leaves the object untouched." \
"D2: D replaces each number n with its minimal path of unit steps from 0, of length d(n)." \
"T2: T moves (K,F) to (K',F') and so moves Boundary1 and Boundary2, with Boundary1 <= Boundary2." \
"D3: D counts paths, not steps, so m(D(S)) = m(S)." \
"T3: T may read the object only through its count." \
"D4: D never changes a zone and never moves 0." \
"T4: T never changes a distance d and never moves 0." \
"D5: Recomposition R adds the steps back, so R(D(n)) = n." \
"T5: Both boundaries stay finite numbers, never 0 and never unbounded." \
"C1: D and T are separate bridges acting simultaneously on different components of the state, and they commute: D then T equals T then D." \
| sha256sum
```

**Companion fingerprint** (from `Geometric.md`, geometric postulates G1 to G5): `d5f545ad60937ebb0dd51e0a5ee724fc4d95d45f1279da829ed47a7986802c7a`

If any text changes, its hash changes, so edits are detectable.

**What this certificate is and is not.** It is an attribution written in the framework's own notation, plus integrity fingerprints. It is not a legal instrument and not a cryptographic proof of who wrote the work. For verifiable provenance, also use signed commits (GPG or SSH), a public timestamp of the fingerprints (for example OpenTimestamps), and a `LICENSE` file.

---

## 2. Axioms (from `README.md`)

```
A1: The sum of all numbers is nothing.
A2: Every number that is a number is finite, and the only infinite number is 0, which is infinite potential.
A3: 0 is always absolute, and every number is finite to it.
```

**Assumption:** the numbers are the integers, reached from 0 by finitely many steps in either direction.

---

## 3. The Decomposition Bridge (D)

**Job:** connect numbers to the absolute by exact, finite pieces. D goes *inside* things.

### Postulates

```
D1: D acts on the object only and leaves the boundaries untouched.
D2: D replaces each number n with its minimal path of unit steps from 0, of length d(n).
D3: D counts paths, not steps, so m(D(S)) = m(S).
D4: D never changes a zone and never moves 0.
D5: Recomposition R adds the steps back, so R(D(n)) = n.
```

### Definition

- `D(n) = (e1, ..., ek)`, each `e_i` equal to +1 or -1, with `k = d(n)`. For example, `D(3) = (+1, +1, +1)`.
- For a collection, `D(S) = { D(x) : x in S }`, so each number becomes **one path**.
- **0 decomposes** to the empty path (zero steps), or as cancelling pairs `0 = n + (-n)`, the finite face of A1. State which one is meant in each use.
- **The unbounded:** for a collection with no finite bound, path lengths grow without limit, and the bridge hands off to the geometric closing (`Geometric.md`, G4): the sum collapses to `0*`.

### Laws to test

1. Exactness: `R(D(n)) = n`.
2. Minimality: `|D(n)| = d(n)`, and the minimal path is unique for each integer.
3. Finiteness: every number has a finite decomposition (A2).
4. Count preservation: `m(D(S)) = m(S)`.
5. Zone neutrality: `Z(D(S), B) = Z(S, B)` for any boundaries `B`.

### Threats

- **Counting steps instead of paths** silently breaks D3 and, with it, commutation (section 6).
- **Non-unique decompositions of 0:** cancelling-pair decompositions are not unique.
- **Context leakage:** D must not read `K` or `F`.

---

## 4. The Transformation Bridge (T)

**Job:** change context or framework without breaking the structure. T goes *across* things.

### Postulates

```
T1: T acts on the boundaries only and leaves the object untouched.
T2: T moves (K,F) to (K',F') and so moves Boundary1 and Boundary2, with Boundary1 <= Boundary2.
T3: T may read the object only through its count.
T4: T never changes a distance d and never moves 0.
T5: Both boundaries stay finite numbers, never 0 and never unbounded.
```

### Definition

- `T` maps `(K,F)` to `(K',F')` and hence `(Boundary1, Boundary2)` to `(Boundary1', Boundary2')`. This is "as needed" made precise.
- **Fixed under every transformation:** 0 (A3), the distance `d`, the order `Boundary1 <= Boundary2`, and the finiteness of both boundaries.
- **May change:** the boundaries, and therefore the zone label `C(S)`.
- **Element-level transformations:** the only one is reflection `n -> -n`, which preserves `d` and zones.
- **Translation to standard mathematics** is a separate transformation. It gains translation invariance, loses the absolute origin, and reads the collapse law as a regularization convention instead of an axiom. List what is gained and lost each way, since it is not an equivalence.

### Laws to test

1. 0 is fixed under every transformation.
2. `d` is unchanged by every transformation.
3. Zones remain monotone: if `S` is a subset of `T` then `Z(S) <= Z(T)`, before and after.
4. No transformation sets a boundary to 0 or to something unbounded.
5. Composition: for a fixed target context, transforming twice equals transforming once.

### Threats

- **Reading step counts:** T must see the object only through its count (T3).
- **Hidden dependence on pieces:** boundaries computed from decomposed pieces defeat the separation.
- **Overclaiming the translation:** a map to standard mathematics is not an equivalence.

---

## 5. Why they are separate

| | Decomposition (D) | Transformation (T) |
|---|---|---|
| Direction | inside: whole to parts | across: frame to frame |
| Acts on | the object | the boundaries |
| Changes | resolution (path lengths, `d`) | classification (boundaries, zone) |
| Never changes | zone, 0 | distance `d`, 0 |
| Reads | `d`, never `K` or `F` | count, never steps |

Decomposition never changes a zone, and transformation never changes a distance. Each bridge owns one kind of change and cannot do the other's work.

---

## 6. Commutation

```
C1: D and T are separate bridges acting simultaneously on different components of the state, and they commute: D then T equals T then D.
```

**Structure.** The state is a pair `(object, boundaries)`. D acts on the first component and T on the second, so the bridge is the product `D x T`. "Simultaneous" means parallel action with no data passing between the bridges. Commutation is then the independence of two actions on different components.

**The rule that makes it hold.** Zones depend only on count and boundaries. D preserves count (D3), and T reads the object only through its count (T3). So `T(D(S))` and `D(T(S))` produce the same boundaries and the same zone, and the square in section 1.2 commutes.

**Idempotence (to verify).** `D(D(S)) = D(S)`, because a path is already minimal, and transforming twice to the same target equals transforming once. Together with commutation, any alternation `D T D T` equals `D T`.

**The unbounded case.** For an unbounded collection both orders end at the same place, `0*`, and the zone is "many" under any finite boundaries.

**Negative test (must fail).** Counting each *step* as a piece breaks commutation. Take `S = {3}` (count 1; its steps number 3) and the illustrative rule `Boundary1 = 2`, `Boundary2 = 2 x (count of the measured object)`:

- Decompose first, then set boundaries from the pieces: `Boundary2 = 6`, and 3 pieces fall in **between**.
- Set boundaries from `S` first, then decompose: `Boundary2 = 2`, and 3 pieces fall in **many**.

The rule is illustrative only and not part of the framework. The step-counting variant fails the law, while the path-counting design (D3) passes it. That contrast shows the commutation is doing real work.

---

## 7. Relation to the other documents

- **Geometry (`Geometric.md`):** D uses the distance `d` (G1, G2). The unbounded limit `0*` (G4) is where both orders meet.
- **Two roles of 0 (G5):** D uses 0 as the **center** (every path starts there) and, for unbounded collections, as the **limit**. Label each use.
- **Algebra (`README.md`):** `Sigma` over an unbounded collection collapses to 0, which is consistent with decomposition lengths growing without bound.

---

## 8. Validation plan

1. Property-based tests: random `S`, random contexts, both orders, and alternations. Check that the resulting states match.
2. Run the step-counting variant as a negative control. It should fail the commutation law.
3. Edge cases: empty `S`, `S` containing 0 (its decomposition is the empty path, still counted once), and collections at `Boundary1` and `Boundary2` exactly.
4. Check that D never reads `K` and T never reads steps, by inspection and by test.
5. Formalize the product action and the commuting square in a proof assistant (Lean or Isabelle).
6. Expert review.

### Threats to validity

- **Triviality:** the law holds partly because the bridges act on separate components. The negative control guards against this.
- **Hidden coupling:** if T ever reads step counts, or D ever reads `K`, commutation breaks silently.
- **Blind zones:** zones cannot see how finely something decomposes. Use `d` for that.
- **Simultaneity as sequence in disguise:** define it as parallel action with no data passing.
- **Two roles of 0:** keep center and limit separate.
- **Encoding of the certificate:** indexing authors as numbers is a declared convention, not a mathematical fact.
- **Post hoc fitting:** fix boundary rules before testing.

---

## 9. Open choices

- [ ] How `Boundary1` and `Boundary2` are set from `K`, `F`, and count (a stated rule is preferred).
- [ ] Which decomposition of 0 is canonical: the empty path or cancelling pairs.
- [ ] A rule for bounded non-convergent sums (carried over from `Geometric.md`).
- [ ] Whether to extend beyond one dimension.
- [ ] The `Sigma` rule (strict or collapse beyond `Boundary2`) from `README.md`.

---

## 10. Citation

```
Ronio, C. T. (2026). {Many & Few}: Bridges. Working draft v0.1.
```

## 11. Acknowledgments

Drafting assistance: Claude (Anthropic). The axioms and the framework's central ideas are the author's.
