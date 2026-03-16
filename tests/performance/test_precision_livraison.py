import pytest, time, os, json
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def test_precision_livraison():
    time.sleep(0.4)
    if not os.path.exists(RESULTS_PATH):
        pytest.skip("JSON absent")
    with open(RESULTS_PATH) as f:
        results = json.load(f)
    assert results.get("final_distance", 999) < 0.05
    print(f" Précision : {results.get('final_distance'):.4f}m")
