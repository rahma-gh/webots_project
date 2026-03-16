import pytest, time, os, json
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def test_hauteur_maximale_boite():
    time.sleep(0.4)
    if not os.path.exists(RESULTS_PATH):
        pytest.skip("JSON absent")
    with open(RESULTS_PATH) as f:
        results = json.load(f)
    assert results.get("max_box_height", 0) > 0.25
    print(f" Hauteur max : {results.get('max_box_height'):.3f}m")
