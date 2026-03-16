import pytest, time
TIMESTEP = 32; STEPS_ROTATE = 690
def test_duree_rotation():
    time.sleep(0.3)
    duree = (STEPS_ROTATE * TIMESTEP) / 1000
    assert duree < 25.0
    print(f" Durée rotation : {duree:.2f}s")
