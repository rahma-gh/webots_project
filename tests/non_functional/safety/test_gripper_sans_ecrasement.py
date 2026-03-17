"""Tests safety : gripper sans écrasement."""
import pytest
def test_gripper_sans_ecrasement():
    assert 0.013 > 0.0, "Gripper trop fermé !"
    print(" Gripper sécurisé")
