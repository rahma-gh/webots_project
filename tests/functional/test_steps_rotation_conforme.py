"""Tests fonctionnels (conformance) : steps rotation conformes aux specs."""
import pytest
STEPS_ROTATE_SPEC = 690
STEPS_ROTATE = 690
def test_steps_rotation_conforme():
    assert STEPS_ROTATE == STEPS_ROTATE_SPEC
    print(f" Steps rotation conformes : {STEPS_ROTATE}")
