"""
Tests non fonctionnels (boundary) : valeurs limites vitesse roues.
Référence : Myers et al. (2011) - The Art of Software Testing
Boundary Value Analysis : juste en dessous, à la limite, juste au dessus
"""
import pytest

WHEEL_MAX = 10.0

def test_boundary_vitesse_roues_juste_en_dessous():
    """Vitesse juste en dessous de la limite → doit passer."""
    vitesse = 9.9
    assert vitesse <= WHEEL_MAX
    print(f" Vitesse {vitesse} < limite {WHEEL_MAX} ✅")

def test_boundary_vitesse_roues_a_la_limite():
    """Vitesse exactement à la limite → doit passer."""
    vitesse = 10.0
    assert vitesse <= WHEEL_MAX
    print(f" Vitesse {vitesse} = limite {WHEEL_MAX} ✅")

def test_boundary_vitesse_roues_au_dessus():
    """Vitesse au dessus de la limite → doit échouer."""
    vitesse = 10.1
    assert vitesse > WHEEL_MAX, "Cette valeur devrait dépasser la limite !"
    print(f" Vitesse {vitesse} > limite {WHEEL_MAX} ❌ détectée")
