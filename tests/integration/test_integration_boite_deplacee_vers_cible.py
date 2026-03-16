import pytest, time, os, json, math
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def test_integration_boite_deplacee_vers_cible():
    time.sleep(0.5)
    if not os.path.exists(RESULTS_PATH): pytest.skip("JSON absent")
    with open(RESULTS_PATH) as f: r = json.load(f)
    init = r.get("initial_box_position",[0,0,0])
    final = r.get("final_box_position",[0,0,0])
    d = math.sqrt((final[0]-init[0])**2+(final[1]-init[1])**2)
    assert d > 0.3 and r.get("final_distance",999) < 0.1
    print(f" Boîte déplacée de {d:.3f}m")
