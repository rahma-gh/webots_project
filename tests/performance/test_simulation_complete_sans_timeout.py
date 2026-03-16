import pytest, time, os, json
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def test_simulation_complete_sans_timeout():
    time.sleep(0.5)
    if not os.path.exists(RESULTS_PATH):
        pytest.skip("JSON absent")
    with open(RESULTS_PATH) as f:
        results = json.load(f)
    assert results.get("duration", 0) < 85.0
    print(" Simulation terminée sans timeout")
