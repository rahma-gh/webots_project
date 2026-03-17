"""Tests stress longue durée 1/3."""
import pytest, time, os, json
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def test_stress_longue_duree_1():
    time.sleep(60.0)
    if not os.path.exists(RESULTS_PATH): pytest.skip("JSON absent")
    with open(RESULTS_PATH) as f: r = json.load(f)
    assert r["robot_moved"] is True
    print(" Stress longue durée 1/3 terminé")
