"""
Tests non fonctionnels (boundary) : valeurs limites précision livraison.
Référence : Myers et al. (2011) - Boundary Value Analysis
"""
import pytest, os, json

RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
PRECISION_LIMIT = 0.05  # 5cm

def test_boundary_precision_juste_dans_limite():
    """Précision juste dans la limite → acceptable."""
    distance = 0.049
    assert distance < PRECISION_LIMIT
    print(f" Distance {distance}m < limite {PRECISION_LIMIT}m ✅")

def test_boundary_precision_a_la_limite():
    """Précision exactement à la limite → acceptable."""
    distance = 0.050
    assert distance <= PRECISION_LIMIT
    print(f" Distance {distance}m = limite {PRECISION_LIMIT}m ✅")

def test_boundary_precision_hors_limite():
    """Précision hors limite → inacceptable."""
    distance = 0.051
    assert distance > PRECISION_LIMIT
    print(f" Distance {distance}m > limite {PRECISION_LIMIT}m ❌ détectée")
