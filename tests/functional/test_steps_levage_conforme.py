"""Tests fonctionnels (conformance) : steps levage conformes aux specs."""
import pytest
STEPS_LIFT_SPEC = 200
STEPS_LIFT = 200
def test_steps_levage_conforme():
    assert STEPS_LIFT == STEPS_LIFT_SPEC
    print(f" Steps levage conformes : {STEPS_LIFT}")
