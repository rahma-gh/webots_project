import pytest, time
ARM_VELOCITIES = [0.2, 0.5, 0.5, 0.3, 0.5]
def test_velocites_bras_progressives():
    time.sleep(0.3)
    assert ARM_VELOCITIES[0] < ARM_VELOCITIES[1]
    assert ARM_VELOCITIES[1] == ARM_VELOCITIES[2]
    print(f" Vitesses bras : {ARM_VELOCITIES}")
