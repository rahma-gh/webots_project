import pytest, time, os, json
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def load():
    if not os.path.exists(RESULTS_PATH): pytest.skip("JSON absent")
    with open(RESULTS_PATH) as f: return json.load(f)
def test_regression_structure_json_complete():
    time.sleep(0.4)
    r = load()
    for c in ["robot_moved","box_picked","box_delivered","gripper_worked","final_distance","max_box_height","initial_box_position","final_box_position","duration"]:
        assert c in r
    print(" Structure JSON complète")
