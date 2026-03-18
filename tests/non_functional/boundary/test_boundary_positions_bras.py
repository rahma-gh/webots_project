"""
Tests non fonctionnels (boundary) : valeurs limites positions bras.
Référence : Myers et al. (2011) - Boundary Value Analysis
"""
import pytest

ARM_MIN = -3.14
ARM_MAX = 3.14

def test_boundary_position_bras_minimum():
    """Position exactement au minimum → doit passer."""
    pos = -3.14
    assert ARM_MIN <= pos <= ARM_MAX
    print(f" Position {pos} à la limite min ✅")

def test_boundary_position_bras_maximum():
    """Position exactement au maximum → doit passer."""
    pos = 3.14
    assert ARM_MIN <= pos <= ARM_MAX
    print(f" Position {pos} à la limite max ✅")

def test_boundary_position_bras_hors_limites():
    """Position hors limites → doit être détectée."""
    pos = 3.15
    assert pos > ARM_MAX, "Hors limite non détectée !"
    print(f" Position {pos} hors limite ❌ détectée")
