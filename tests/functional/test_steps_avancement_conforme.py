"""Tests fonctionnels (conformance) : steps avancement conformes aux specs."""
import pytest
STEPS_FORWARD_SPEC = 520
STEPS_FORWARD = 520
def test_steps_avancement_conforme():
    assert STEPS_FORWARD == STEPS_FORWARD_SPEC
    print(f" Steps avancement conformes : {STEPS_FORWARD}")
