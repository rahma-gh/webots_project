import pytest

ARM_PLACE_POSITIONS = {"arm1": 0.0, "arm2": -1.0, "arm3": -0.3, "arm4": -1.0}

def test_arm_place_positions_in_range():
    for arm, pos in ARM_PLACE_POSITIONS.items():
        assert -3.14 <= pos <= 3.14, f"{arm} hors limites : {pos}"
    print(" Positions de dépose sécurisées")
