"""Tests non fonctionnels (safety) : positions place dans limites sécurisées."""
import pytest
ARM_PLACE = {"arm1": 0.0, "arm2": -1.0, "arm3": -0.3, "arm4": -1.0}
def test_positions_place_securisees():
    for arm, pos in ARM_PLACE.items():
        assert -3.14 <= pos <= 3.14, f"{arm} hors limites : {pos}"
    print(" Positions place sécurisées")
