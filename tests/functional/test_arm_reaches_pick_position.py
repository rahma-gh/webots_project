"""Tests fonctionnels : bras atteint position de saisie."""
import pytest, os, json
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def load():
    if not os.path.exists(RESULTS_PATH): pytest.skip("JSON absent")
    with open(RESULTS_PATH) as f: return json.load(f)
def test_arm_reaches_pick_position():
    r = load()
    assert r["max_box_height"] > 0.1, f"Bras n'a pas atteint la boîte !"
    print(" Bras a atteint la position de saisie")
