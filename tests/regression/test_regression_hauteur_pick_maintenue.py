import pytest, time, os, json
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def load():
    if not os.path.exists(RESULTS_PATH): pytest.skip("JSON absent")
    with open(RESULTS_PATH) as f: return json.load(f)
def test_regression_hauteur_pick_maintenue():
    time.sleep(0.5)
    assert load().get("max_box_height",0) > 0.25
    print(" Hauteur pick OK")
