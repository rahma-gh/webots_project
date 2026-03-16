import pytest

GRIPPER_CLOSE_POSITION = 0.013

def test_gripper_close_position_valid():
    assert GRIPPER_CLOSE_POSITION > 0
    assert GRIPPER_CLOSE_POSITION < 1.0
    print(f" Position gripper : {GRIPPER_CLOSE_POSITION}")
