"""Tests fonctionnels : gripper saisit la boîte."""
import pytest, os, json
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def load():
    if not os.path.exists(RESULTS_PATH): pytest.skip("JSON absent")
    with open(RESULTS_PATH) as f: return json.load(f)
def test_gripper_closes_on_box():
    assert load()["gripper_worked"], "Le gripper n'a pas fonctionné !"
    print(" Gripper s'est fermé sur la boîte")
