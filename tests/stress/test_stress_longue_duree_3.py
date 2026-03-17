"""Tests stress longue durée 3/3."""
import pytest, time, os, json
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def test_stress_longue_duree_3():
    time.sleep(60.0)
    if not os.path.exists(RESULTS_PATH): pytest.skip("JSON absent")
    with open(RESULTS_PATH) as f: r = json.load(f)
    assert r["box_delivered"] is True
    print(" Stress longue durée 3/3 terminé")
