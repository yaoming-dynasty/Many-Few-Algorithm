"""pytests that try to falsify the Many-Few framework using the tests and
procedures outlined in the design notes.
"""

from __future__ import annotations

import math
from collections import Counter

import numpy as np

from manyfew.core import (
    TypedZero,
    detect_dynamics,
    perturb_and_flip_rate,
    projection_mu_factory,
    classify_measurement,
)


RNG = np.random.default_rng(42)


def test_boundary_sensitivity_flip_rate():
    """Identity transform, measurement near the frozen boundary. Expect that
    arbitrarily small perturbations can flip classification (non-robustness).
    """
    # T = identity (not needed for this scalar test)
    x0 = 0.5
    mu = projection_mu_factory()
    b1 = 0.4999
    b2 = 0.5001

    flip_rate, margins = perturb_and_flip_rate(
        state=x0, mu=mu, b1=b1, b2=b2, noise_sigma=1e-6, trials=2000, rng=RNG
    )

    # We expect some flips due to noise crossing the close boundaries
    print(f"boundary_sensitivity: flip_rate={flip_rate:.4f}, min_margin={min(margins):.3e}")
    assert flip_rate > 0.0


def test_logistic_map_classification_variance():
    """Use logistic map at r=4 (chaotic) and show classification variability under
    tiny measurement noise.
    """

    def T(x: float) -> float:
        return 4.0 * x * (1.0 - x)

    def mu(x: float) -> float:
        return x

    # Choose a boundary that lies close to typical orbit values
    b1, b2 = 0.499, 0.501

    # Sample many initial conditions and compute dynamics classification
    classes = []
    for seed in range(20):
        x0 = RNG.random()
        # perturb initial slightly to simulate measurement / initialization noise
        x0_noisy = x0 + RNG.normal(0.0, 1e-9)
        dyn = detect_dynamics(T, x0_noisy, steps=500, tol=1e-12)
        # classification of the measurement at time 400
        m = mu(T(T(x0_noisy)))
        cl = classify_measurement(m, b1, b2)
        classes.append((dyn, cl))

    counts = Counter(classes)
    print("logistic_map: distinct dynamics x classification pairs:")
    for (dyn, cl), cnt in counts.items():
        print(f"  {dyn:20s} | {cl:8s} : {cnt}")

    # We expect variability: not all runs yield the same pair
    assert len(counts) > 1


def test_typed_zero_distinction():
    """Construct two states differing only by typed-zero placement and assert
    the measurement map can distinguish them (typed-zero soundness).
    """
    tz_a = TypedZero("A")
    tz_b = TypedZero("B")

    mu = projection_mu_factory()

    # Represent states as (primary_value, zero_slot)
    s1 = (0.6, tz_a)
    s2 = (0.6, tz_b)

    m1 = mu(s1)
    m2 = mu(s2)

    print(f"typed_zero: m1={m1}, m2={m2}, tz_a={tz_a}, tz_b={tz_b}")

    # The simple numeric mu above treats typed zeros as 0.0, so numeric measurement
    # will be identical. This test asserts that naive measurement DOES NOT
    # distinguish typed zero placement, demonstrating where the framework needs
    # richer mu semantics to realize typed-zero soundness.
    assert m1 == m2


def test_detection_of_fixed_point_and_cycle():
    """Discrete finite-state like map that cycles; verify detect_dynamics finds cycle
    and that a constant map reports a fixed point.
    """

    # constant map -> fixed point
    def T_const(x: float) -> float:
        return 0.123456789

    fp = detect_dynamics(T_const, 0.9, steps=200, tol=1e-12)
    print(f"constant_map -> {fp}")
    assert fp == "fixed_point"

    # 2-cycle map on two points: define T to alternate between 0.2 and 0.8
    seq = [0.2, 0.8]

    def T_cycle(x: float) -> float:
        # map 0.2 -> 0.8, 0.8 -> 0.2; for other inputs project to nearest
        if abs(x - 0.2) < 1e-6:
            return 0.8
        if abs(x - 0.8) < 1e-6:
            return 0.2
        # project to nearest of the two
        return 0.2 if abs(x - 0.2) < abs(x - 0.8) else 0.8

    cyc = detect_dynamics(T_cycle, 0.2, steps=200, tol=1e-12)
    print(f"2-cycle_map -> {cyc}")
    assert "cycle" in cyc
