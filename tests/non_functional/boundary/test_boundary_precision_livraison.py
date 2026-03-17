"""Tests boundary : valeurs limites précision. Référence : Myers et al. (2011)"""
import pytest
PRECISION_LIMIT = 0.05
def test_boundary_precision_juste_dans_limite():
    assert 0.049 < PRECISION_LIMIT
    print(" Distance 0.049m < limite 0.05m ✅")
def test_boundary_precision_a_la_limite():
    assert 0.050 <= PRECISION_LIMIT
    print(" Distance 0.050m = limite 0.05m ✅")
def test_boundary_precision_hors_limite():
    assert 0.051 > PRECISION_LIMIT
    print(" Distance 0.051m > limite 0.05m ❌ détectée")
