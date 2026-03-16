import pytest

TIMESTEP = 32
STEPS_MOVE_FORWARD = 520
STEPS_GRIPPER_CLOSE = 50
STEPS_LIFT_ARM = 200
STEPS_ROTATE = 690

def test_total_cycle_duration():
    total_steps = STEPS_MOVE_FORWARD + STEPS_GRIPPER_CLOSE + STEPS_LIFT_ARM + STEPS_ROTATE
    total_sec = (total_steps * TIMESTEP) / 1000
    assert total_sec < 60.0
    print(f" Durée cycle total : {total_sec:.2f}s")
