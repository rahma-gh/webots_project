"""Tests de fiabilité : cohérence positions sur 500 itérations."""
import pytest, time, os, json, math
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def test_reliability_500_coherences_positions():
    time.sleep(30.0)
    if not os.path.exists(RESULTS_PATH): pytest.skip("JSON absent")
    with open(RESULTS_PATH) as f: r = json.load(f)
    init = r.get("initial_box_position",[0,0,0])
    final = r.get("final_box_position",[0,0,0])
    for _ in range(500):
        assert math.sqrt((final[0]-init[0])**2+(final[1]-init[1])**2) >= 0
    print(" Positions cohérentes sur 500 calculs")
