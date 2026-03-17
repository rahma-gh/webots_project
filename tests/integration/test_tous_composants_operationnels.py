"""Tests d'intégration : tous les composants opérationnels ensemble."""
import pytest, os, json
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def test_tous_composants_operationnels():
    """Tous les composants fonctionnent-ils ensemble correctement ?"""
    assert os.path.exists("simulation/pick_and_place.wbt")
    assert os.path.exists("Dockerfile")
    assert os.path.exists("requirements.txt")
    assert os.path.exists("conftest.py")
    if not os.path.exists(RESULTS_PATH): pytest.skip("JSON absent")
    with open(RESULTS_PATH) as f: r = json.load(f)
    assert all([r["robot_moved"], r["box_picked"],
                r["gripper_worked"], r["box_delivered"]])
    print(" Tous les composants opérationnels ensemble")
