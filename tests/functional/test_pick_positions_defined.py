import pytest

ARM_PICK_POSITIONS = {"arm2": -0.55, "arm3": -0.9, "arm4": -1.5}

def test_pick_positions_defined():
    assert "arm2" in ARM_PICK_POSITIONS
    assert "arm3" in ARM_PICK_POSITIONS
    assert "arm4" in ARM_PICK_POSITIONS
    print(" Positions de pick définies")
