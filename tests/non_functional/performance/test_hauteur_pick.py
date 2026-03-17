"""Tests non fonctionnels (performance) : hauteur de saisie."""
import pytest, os, json
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def test_hauteur_pick():
    if not os.path.exists(RESULTS_PATH): pytest.skip("JSON absent")
    with open(RESULTS_PATH) as f: r = json.load(f)
    assert r.get("max_box_height",0) > 0.25
    print(f" Hauteur pick : {r.get('max_box_height'):.3f}m")
