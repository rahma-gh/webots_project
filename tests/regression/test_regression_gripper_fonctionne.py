import pytest, time, os, json
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def load():
    if not os.path.exists(RESULTS_PATH): pytest.skip("JSON absent")
    with open(RESULTS_PATH) as f: return json.load(f)
def test_regression_gripper_fonctionne():
    time.sleep(0.5)
    assert load()["gripper_worked"] is True
    print(" Gripper OK")
