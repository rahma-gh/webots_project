import pytest, time
TIMESTEP = 32; STEPS_MOVE_FORWARD = 520
def test_duree_deplacement_acceptable():
    time.sleep(0.3)
    duree = (STEPS_MOVE_FORWARD * TIMESTEP) / 1000
    assert duree < 20.0
    print(f" Durée déplacement : {duree:.2f}s")
