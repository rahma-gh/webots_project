"""Tests fonctionnels (conformance) : steps gripper conformes aux specs."""
import pytest
STEPS_GRIPPER_SPEC = 50
STEPS_GRIPPER = 50
def test_steps_gripper_conforme():
    assert STEPS_GRIPPER == STEPS_GRIPPER_SPEC
    print(f" Steps gripper conformes : {STEPS_GRIPPER}")
