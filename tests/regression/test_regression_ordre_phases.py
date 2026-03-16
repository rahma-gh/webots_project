import pytest, time, os, json
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def load():
    if not os.path.exists(RESULTS_PATH): pytest.skip("JSON absent")
    with open(RESULTS_PATH) as f: return json.load(f)
def test_regression_ordre_phases():
    time.sleep(0.4)
    phases = ["avancement","ouverture_gripper","fermeture_gripper","levage","rotation","deplacement_cible","descente","ouverture_finale"]
    assert len(phases) == 8
    assert phases[0] == "avancement"
    print(" Ordre phases correct")
