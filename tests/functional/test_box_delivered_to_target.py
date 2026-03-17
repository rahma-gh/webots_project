"""Tests fonctionnels : boîte livrée à destination."""
import pytest, os, json
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def load():
    if not os.path.exists(RESULTS_PATH): pytest.skip("JSON absent")
    with open(RESULTS_PATH) as f: return json.load(f)
def test_box_delivered_to_target():
    r = load()
    assert r["box_delivered"], "Boîte non livrée !"
    assert r["final_distance"] < 0.05, f"Distance trop grande : {r['final_distance']:.4f}m"
    print(f" Boîte livrée à {r['final_distance']:.4f}m de la cible")
