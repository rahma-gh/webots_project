import pytest

TIMESTEP = 32
STEPS_LIFT_ARM = 200

def test_lift_arm_duration():
    duration_sec = (STEPS_LIFT_ARM * TIMESTEP) / 1000
    assert duration_sec < 10.0
    print(f" Durée levage bras : {duration_sec:.2f}s")
