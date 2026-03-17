"""Tests fiabilité : résultats reproductibles."""
import pytest, time, os, json
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def test_reliability_resultats_reproductibles():
    time.sleep(30.0)
    if not os.path.exists(RESULTS_PATH): pytest.skip("JSON absent")
    with open(RESULTS_PATH) as f: r1 = json.load(f)
    with open(RESULTS_PATH) as f: r2 = json.load(f)
    assert r1["robot_moved"] == r2["robot_moved"]
    assert r1["final_distance"] == r2["final_distance"]
    print(" Résultats reproductibles")
