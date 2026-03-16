import pytest, time, os, json
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def test_position_initiale_connue():
    time.sleep(0.3)
    if not os.path.exists(RESULTS_PATH):
        pytest.skip("JSON absent")
    with open(RESULTS_PATH) as f:
        results = json.load(f)
    init_pos = results.get("initial_box_position")
    assert init_pos is not None and len(init_pos) == 3
    print(f" Position initiale : {init_pos}")
