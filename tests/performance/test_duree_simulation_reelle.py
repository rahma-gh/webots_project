import pytest, time, os, json
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def test_duree_simulation_reelle():
    time.sleep(0.5)
    if not os.path.exists(RESULTS_PATH):
        pytest.skip("JSON absent")
    with open(RESULTS_PATH) as f:
        results = json.load(f)
    duration = results.get("duration", 0)
    assert 5.0 < duration < 120.0
    print(f" Durée simulation : {duration:.2f}s")
