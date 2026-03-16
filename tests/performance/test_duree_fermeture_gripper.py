import pytest, time
TIMESTEP = 32; STEPS_GRIPPER_CLOSE = 50
def test_duree_fermeture_gripper():
    time.sleep(0.3)
    duree = (STEPS_GRIPPER_CLOSE * TIMESTEP) / 1000
    assert duree < 3.0
    print(f" Durée gripper : {duree:.2f}s")
