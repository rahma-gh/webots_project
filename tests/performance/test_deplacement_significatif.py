import pytest, time, os, json, math
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def test_deplacement_significatif():
    time.sleep(0.4)
    if not os.path.exists(RESULTS_PATH):
        pytest.skip("JSON absent")
    with open(RESULTS_PATH) as f:
        results = json.load(f)
    init = results.get("initial_box_position", [0,0,0])
    final = results.get("final_box_position", [0,0,0])
    d = math.sqrt((final[0]-init[0])**2 + (final[1]-init[1])**2)
    assert d > 0.5
    print(f" Déplacement : {d:.3f}m")
