import pytest, time
GRIPPER_CLOSE_POSITION = 0.013
def test_gripper_position_efficace():
    time.sleep(0.3)
    assert 0.005 < GRIPPER_CLOSE_POSITION < 0.05
    print(f" Position gripper efficace : {GRIPPER_CLOSE_POSITION}")
