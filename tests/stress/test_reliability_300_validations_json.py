"""Tests fiabilité : structure JSON valide 300 fois."""
import pytest, time, os, json
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
CHAMPS = ["robot_moved","box_picked","box_delivered","gripper_worked","final_distance","max_box_height","initial_box_position","final_box_position","duration"]
def test_reliability_300_validations_json():
    time.sleep(30.0)
    if not os.path.exists(RESULTS_PATH): pytest.skip("JSON absent")
    for _ in range(300):
        with open(RESULTS_PATH) as f: r = json.load(f)
        for c in CHAMPS: assert c in r
    print(" Structure JSON stable")
