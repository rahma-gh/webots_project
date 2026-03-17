"""Tests non fonctionnels (performance) : déplacement total boîte."""
import pytest, os, json, math
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def test_deplacement_total():
    if not os.path.exists(RESULTS_PATH): pytest.skip("JSON absent")
    with open(RESULTS_PATH) as f: r = json.load(f)
    init = r.get("initial_box_position",[0,0,0])
    final = r.get("final_box_position",[0,0,0])
    d = math.sqrt((final[0]-init[0])**2+(final[1]-init[1])**2)
    assert d > 0.5
    print(f" Déplacement total : {d:.3f}m")
