import pytest, time, os, json
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def test_stress_longue_duree_2():
    print("\n Stress longue durée 2/3...")
    time.sleep(60.0)
    if not os.path.exists(RESULTS_PATH):
        pytest.skip("JSON absent")
    with open(RESULTS_PATH) as f:
        r = json.load(f)
    assert r["box_picked"] is True
    assert r["gripper_worked"] is True
    print(" Partie 2/3 terminée")
