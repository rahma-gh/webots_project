import pytest

TIMESTEP = 32
STEPS_MOVE_FORWARD = 520

def test_move_forward_duration():
    duration_sec = (STEPS_MOVE_FORWARD * TIMESTEP) / 1000
    assert duration_sec < 20.0
    print(f" Durée avancement : {duration_sec:.2f}s")
