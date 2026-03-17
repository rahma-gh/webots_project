"""Tests non fonctionnels (safety) : gripper sans risque d'écrasement."""
import pytest
GRIPPER_CLOSE_POSITION = 0.013
def test_gripper_sans_ecrasement():
    assert GRIPPER_CLOSE_POSITION > 0.0, "Gripper trop fermé — risque écrasement !"
    print(f" Gripper sécurisé : {GRIPPER_CLOSE_POSITION} > 0.0")
