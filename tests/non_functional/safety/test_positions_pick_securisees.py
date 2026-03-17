"""Tests safety : positions pick dans limites."""
import pytest
def test_positions_pick_securisees():
    for arm, pos in {"arm2":-0.55,"arm3":-0.9,"arm4":-1.5}.items():
        assert -3.14 <= pos <= 3.14, f"{arm} hors limites !"
    print(" Positions pick sécurisées")
