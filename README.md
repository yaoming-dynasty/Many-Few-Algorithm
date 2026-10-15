# Falsification test-suite for Many-Few framework

This test-suite implements the experimental harness described in the design notes.
It includes reproducible experiments for boundary sensitivity, chaotic dynamics,
and typed-zero distinction.

Run with:

    pip install -r requirements.txt  # numpy pytest
    pytest -q

The tests are written as experiments that document falsification evidence; they
assert conditions that indicate fragility or nontrivial behavior rather than
"passing" a correctness property.
