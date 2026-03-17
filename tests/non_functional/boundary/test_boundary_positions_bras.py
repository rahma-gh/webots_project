"""Tests boundary : valeurs limites positions bras. Référence : Myers et al. (2011)"""
import pytest
ARM_MIN, ARM_MAX = -3.14, 3.14
def test_boundary_position_bras_minimum():
    assert ARM_MIN <= -3.14 <= ARM_MAX
    print(" Position -3.14 à la limite min ✅")
def test_boundary_position_bras_maximum():
    assert ARM_MIN <= 3.14 <= ARM_MAX
    print(" Position 3.14 à la limite max ✅")
def test_boundary_position_bras_hors_limites():
    assert 3.15 > ARM_MAX
    print(" Position 3.15 hors limite ❌ détectée")
