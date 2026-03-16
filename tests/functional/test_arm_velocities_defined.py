import pytest

ARM_VELOCITIES = [0.2, 0.5, 0.5, 0.3, 0.5]

def test_arm_velocities_defined():
    assert len(ARM_VELOCITIES) == 5
    for vel in ARM_VELOCITIES:
        assert vel > 0
    print(" 5 vitesses de moteurs définies")
