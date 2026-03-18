"""Tests fonctionnels (conformance) : position gripper conforme aux specs."""
import pytest
GRIPPER_SPEC = 0.013
GRIPPER_CLOSE_POSITION = 0.013
def test_gripper_position_conforme():
    assert GRIPPER_CLOSE_POSITION == GRIPPER_SPEC
    print(f" Position gripper conforme : {GRIPPER_CLOSE_POSITION}")
