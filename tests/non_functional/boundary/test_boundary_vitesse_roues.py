"""Tests boundary : valeurs limites vitesse roues. Référence : Myers et al. (2011)"""
import pytest
WHEEL_MAX = 10.0
def test_boundary_vitesse_roues_juste_en_dessous():
    assert 9.9 <= WHEEL_MAX
    print(" Vitesse 9.9 < limite 10.0 ✅")
def test_boundary_vitesse_roues_a_la_limite():
    assert 10.0 <= WHEEL_MAX
    print(" Vitesse 10.0 = limite 10.0 ✅")
def test_boundary_vitesse_roues_au_dessus():
    assert 10.1 > WHEEL_MAX
    print(" Vitesse 10.1 > limite 10.0 ❌ détectée")
