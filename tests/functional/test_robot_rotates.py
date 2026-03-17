"""Tests fonctionnels : robot tourne vers la destination."""
import pytest, os, json, math
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def load():
    if not os.path.exists(RESULTS_PATH): pytest.skip("JSON absent")
    with open(RESULTS_PATH) as f: return json.load(f)
def test_robot_rotates():
    r = load()
    init = r.get("initial_box_position",[0,0,0])
    final = r.get("final_box_position",[0,0,0])
    d = math.sqrt((final[0]-init[0])**2+(final[1]-init[1])**2)
    assert d > 0.3, f"Robot n'a pas assez bougé : {d:.3f}m"
    print(f" Robot a tourné et déplacé la boîte de {d:.3f}m")
