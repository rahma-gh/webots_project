import pytest, time, os, json
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def test_integration_sequence_pick_place_complete():
    time.sleep(0.5)
    if not os.path.exists(RESULTS_PATH): pytest.skip("JSON absent")
    with open(RESULTS_PATH) as f: r = json.load(f)
    assert r["robot_moved"] and r["box_picked"] and r["gripper_worked"] and r["box_delivered"]
    print(" Séquence complète OK")
