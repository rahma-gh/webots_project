import pytest, time
TIMESTEP = 32; STEPS_LIFT_ARM = 200
def test_duree_levage_bras():
    time.sleep(0.3)
    duree = (STEPS_LIFT_ARM * TIMESTEP) / 1000
    assert duree < 8.0
    print(f" Durée levage : {duree:.2f}s")
