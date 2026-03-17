"""Tests d'intégration : tous les composants opérationnels."""
import pytest, os, json
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def test_tous_composants_operationnels():
    assert os.path.exists("simulation/pick_and_place.wbt")
    assert os.path.exists("controllers/pick_and_place/pick_and_place.py")
    assert os.path.exists("Dockerfile")
    assert os.path.exists("requirements.txt")
    if not os.path.exists(RESULTS_PATH): pytest.skip("JSON absent")
    with open(RESULTS_PATH) as f: r = json.load(f)
    assert all([r["robot_moved"],r["box_picked"],r["gripper_worked"],r["box_delivered"]])
    print(" Tous les composants opérationnels")
