"""Tests fonctionnels : robot se déplace vers la cible."""
import pytest, os, json
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def load():
    if not os.path.exists(RESULTS_PATH): pytest.skip("JSON absent")
    with open(RESULTS_PATH) as f: return json.load(f)
def test_robot_moves_to_target():
    r = load()
    assert r["final_distance"] < 0.5, f"Robot n'a pas atteint la cible !"
    print(" Robot s'est déplacé vers la cible")
