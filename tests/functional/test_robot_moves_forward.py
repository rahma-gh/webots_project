"""Tests fonctionnels : robot avance vers la boîte."""
import pytest, os, json
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def load():
    if not os.path.exists(RESULTS_PATH): pytest.skip("JSON absent")
    with open(RESULTS_PATH) as f: return json.load(f)
def test_robot_moves_forward():
    assert load()["robot_moved"], "Le robot n'a pas avancé !"
    print(" Robot a avancé vers la boîte")
