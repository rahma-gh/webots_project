import pytest

ARM_PICK_POSITIONS = {"arm2": -0.55, "arm3": -0.9, "arm4": -1.5}

def test_arm_pick_positions_in_range():
    for arm, pos in ARM_PICK_POSITIONS.items():
        assert -3.14 <= pos <= 3.14, f"{arm} hors limites : {pos}"
    print(" Positions de saisie sécurisées")
