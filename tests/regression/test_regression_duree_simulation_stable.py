import pytest, time, os, json
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def load():
    if not os.path.exists(RESULTS_PATH): pytest.skip("JSON absent")
    with open(RESULTS_PATH) as f: return json.load(f)
def test_regression_duree_simulation_stable():
    time.sleep(0.5)
    d = load().get("duration",0)
    assert 0 < d < 120.0
    print(f" Durée stable : {d:.1f}s")
