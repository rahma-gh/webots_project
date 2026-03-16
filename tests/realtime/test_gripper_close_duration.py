import pytest

TIMESTEP = 32
STEPS_GRIPPER_CLOSE = 50

def test_gripper_close_duration():
    duration_sec = (STEPS_GRIPPER_CLOSE * TIMESTEP) / 1000
    assert duration_sec < 5.0
    print(f" Durée fermeture gripper : {duration_sec:.2f}s")
