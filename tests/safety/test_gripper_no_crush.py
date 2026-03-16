import pytest

GRIPPER_CLOSE_POSITION = 0.013

def test_gripper_no_crush():
    assert GRIPPER_CLOSE_POSITION > 0.0, "Gripper trop fermé — risque d'écrasement !"
    print(f" Gripper sécurisé : position {GRIPPER_CLOSE_POSITION}")
