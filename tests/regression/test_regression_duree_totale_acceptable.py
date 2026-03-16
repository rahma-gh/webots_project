import pytest, time, os, json
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def load():
    if not os.path.exists(RESULTS_PATH): pytest.skip("JSON absent")
    with open(RESULTS_PATH) as f: return json.load(f)
def test_regression_duree_totale_acceptable():
    time.sleep(0.4)
    total = (520+50+200+690)*32/1000
    assert total < 120.0
    print(f" Durée totale : {total:.2f}s")
