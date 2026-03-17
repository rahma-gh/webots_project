"""Tests fonctionnels : la boîte est livrée à destination."""
import pytest, os, json
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def load():
    if not os.path.exists(RESULTS_PATH): pytest.skip("JSON absent")
    with open(RESULTS_PATH) as f: return json.load(f)
def test_box_delivered_to_target():
    """La boîte est-elle livrée à la destination correcte ?"""
    r = load()
    assert r["box_delivered"], "Boîte non livrée !"
    assert r["final_distance"] < 0.05, \
        f"Boîte pas assez proche de la cible : {r['final_distance']:.4f}m"
    print(f" Boîte livrée à {r['final_distance']:.4f}m de la cible")
