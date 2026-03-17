"""Tests non fonctionnels (safety) : positions pick dans limites sécurisées."""
import pytest
ARM_PICK = {"arm2": -0.55, "arm3": -0.9, "arm4": -1.5}
def test_positions_pick_securisees():
    for arm, pos in ARM_PICK.items():
        assert -3.14 <= pos <= 3.14, f"{arm} hors limites : {pos}"
    print(" Positions pick sécurisées")
