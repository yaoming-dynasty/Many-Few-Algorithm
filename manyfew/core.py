"""
Minimal Many-Few framework primitives used by the falsification test-suite.
This module provides small, self-contained implementations of:
- TypedZero: typed zero sentinel
- classify_measurement: Many/Few/Boundary classification
- detect_dynamics: heuristic dynamics classifier (fixed point, cycle, expansion, contraction, unresolved)
- perturb_and_flip_rate: measurement perturbation harness

These are intentionally small and numeric so the test-suite can exercise
falsification hypotheses quickly. The code is deterministic given the RNG seed.
"""
from __future__ import annotations

import math
from typing import Any, Callable, List, Tuple

import numpy as np


class TypedZero:
    """A typed zero. Two typed zeros with different tags are considered distinct.

    It's a lightweight wrapper so tests can place typed zeros in structured states.
    """

    def __init__(self, tag: str):
        self.tag = tag

    def __repr__(self) -> str:  # pragma: no cover - trivial
        return f"TypedZero({self.tag!r})"


def classify_measurement(m: float, b1: float, b2: float) -> str:
    """Classify a scalar measurement m relative to frozen boundaries b1 < b2.

    Returns 'Few', 'Boundary', or 'Many'.
    """
    if m < b1:
        return "Few"
    if m > b2:
        return "Many"
    return "Boundary"


def detect_dynamics(
    T: Callable[[float], float],
    x0: float,
    steps: int = 1000,
    tol: float = 1e-10,
    cycle_check_len: int = 50,
) -> str:
    """Heuristic dynamics classifier.

    Runs x_{n+1} = T(x_n) for `steps` steps from x0 and examines the tail to
    detect: fixed point, short cycle, expansion, contraction, or unresolved.

    This is not a formal proof; it's a numeric probe intended for falsification.
    """
    seq: List[float] = [x0]
    for i in range(steps):
        seq.append(T(seq[-1]))

    tail = np.array(seq[-(cycle_check_len * 3) :])

    # Fixed point: tail values nearly equal
    maxdiff = float(np.max(np.abs(np.diff(tail))))
    if maxdiff < tol:
        return "fixed_point"

    # Cycle detection (naive): look for short repeated patterns in the last window
    # Compare pairwise distances to find near-equality repeating values
    window = tail[-cycle_check_len:]
    for p in range(1, min(20, cycle_check_len)):
        if np.all(np.isclose(window[:-p], window[p:], atol=1e-9, rtol=1e-9)):
            return f"cycle_length_{p}"

    # Expansion / contraction heuristic: look at distances between successive iterates
    diffs = np.abs(np.diff(tail))
    # Compare early and late diffs
    half = len(diffs) // 2
    if half > 0:
        early = np.mean(diffs[:half])
        late = np.mean(diffs[half:])
        if late > 10 * (early + 1e-20):
            return "expansion"
        if late * 10 < (early + 1e-20):
            return "contraction"

    return "unresolved"


def perturb_and_flip_rate(
    state: float,
    mu: Callable[[float], float],
    b1: float,
    b2: float,
    noise_sigma: float = 1e-6,
    trials: int = 1000,
    rng: np.random.Generator | None = None,
) -> Tuple[float, List[float]]:
    """Perturb the scalar `state` with gaussian noise and compute the fraction of
    trials where the classification (Many/Few/Boundary) differs from the
    unperturbed classification.

    Returns (flip_rate, margins) where margins are distances of mu(state_noisy) to
    the closest boundary.
    """
    rng = rng or np.random.default_rng()
    baseline = classify_measurement(mu(state), b1, b2)
    flips = 0
    margins: List[float] = []
    for _ in range(trials):
        noisy = state + rng.normal(0.0, noise_sigma)
        m = mu(noisy)
        cl = classify_measurement(m, b1, b2)
        if cl != baseline:
            flips += 1
        # margin: distance to nearest boundary
        margins.append(float(min(abs(m - b1), abs(m - b2))))
    return flips / trials, margins


def projection_mu_factory(index: int = 0) -> Callable[[Any], float]:
    """Return a simple measurement map for structured states.

    For numeric states it's identity; for sequences it returns the element at
    `index`.
    """

    def mu(s: Any) -> float:
        if isinstance(s, (list, tuple, np.ndarray)):
            return float(s[index])
        if isinstance(s, TypedZero):
            # typed zero treated as 0.0 but typed
            return 0.0
        return float(s)

    return mu
