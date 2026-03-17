"""Tests fonctionnels : bras lève la boîte."""
import pytest, os, json
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def load():
    if not os.path.exists(RESULTS_PATH): pytest.skip("JSON absent")
    with open(RESULTS_PATH) as f: return json.load(f)
def test_arm_lifts_box():
    r = load()
    assert r["box_picked"], "La boîte n'a pas été levée !"
    assert r["max_box_height"] > 0.25, f"Hauteur insuffisante : {r['max_box_height']:.3f}m"
    print(f" Bras a levé la boîte à {r['max_box_height']:.3f}m")
