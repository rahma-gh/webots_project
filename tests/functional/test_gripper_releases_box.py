"""Tests fonctionnels : le gripper dépose la boîte."""
import pytest, os, json
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def load():
    if not os.path.exists(RESULTS_PATH): pytest.skip("JSON absent")
    with open(RESULTS_PATH) as f: return json.load(f)
def test_gripper_releases_box():
    """Le gripper dépose-t-il la boîte à destination ?"""
    r = load()
    assert r["box_delivered"], "La boîte n'a pas été déposée !"
    print(" Gripper a déposé la boîte à destination")
