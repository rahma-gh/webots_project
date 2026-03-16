import pytest, time, os, json
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def test_stress_lecture_json_repetee():
    time.sleep(30.0)
    if not os.path.exists(RESULTS_PATH):
        pytest.skip("JSON absent")
    for _ in range(100):
        with open(RESULTS_PATH) as f:
            r = json.load(f)
        assert "robot_moved" in r
    print(" 100 lectures JSON réussies")
