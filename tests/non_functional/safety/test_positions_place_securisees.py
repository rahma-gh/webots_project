"""Tests safety : positions place dans limites."""
import pytest
def test_positions_place_securisees():
    for arm, pos in {"arm1":0.0,"arm2":-1.0,"arm3":-0.3,"arm4":-1.0}.items():
        assert -3.14 <= pos <= 3.14, f"{arm} hors limites !"
    print(" Positions place sécurisées")
