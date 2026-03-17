"""Tests performance : précision livraison < 5cm."""
import pytest, os, json
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def test_precision_livraison():
    if not os.path.exists(RESULTS_PATH): pytest.skip("JSON absent")
    with open(RESULTS_PATH) as f: r = json.load(f)
    assert r.get("final_distance",999) < 0.05
    print(f" Précision : {r.get('final_distance'):.4f}m")
