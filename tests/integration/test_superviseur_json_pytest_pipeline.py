"""Tests d'intégration : pipeline superviseur → JSON → pytest."""
import pytest, os, json
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def test_superviseur_json_pytest_pipeline():
    """Le pipeline superviseur → JSON → pytest fonctionne-t-il ?"""
    if not os.path.exists(RESULTS_PATH): pytest.skip("JSON absent")
    with open(RESULTS_PATH) as f: r = json.load(f)
    assert isinstance(r, dict)
    assert len(r) >= 9
    print(" Pipeline superviseur → JSON → pytest opérationnel")
