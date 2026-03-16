import pytest, time, os, json
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def load():
    if not os.path.exists(RESULTS_PATH): pytest.skip("JSON absent")
    with open(RESULTS_PATH) as f: return json.load(f)
def test_regression_robot_bouge():
    time.sleep(0.5)
    assert load()["robot_moved"] is True
    print(" Robot bouge OK")
