"""Test de communication : JSON → pytest. Référence : Arrieta et al. (2019)"""
import pytest, os, json
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def test_json_readable_by_pytest():
    if not os.path.exists(RESULTS_PATH): pytest.skip("JSON absent")
    with open(RESULTS_PATH) as f: r = json.load(f)
    for c in ["robot_moved","box_picked","box_delivered","gripper_worked","final_distance","duration"]:
        assert c in r, f"Champ manquant : {c}"
    print(" JSON lisible et valide par pytest")
