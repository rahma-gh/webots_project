import os, json, pytest
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def load_results():
    assert os.path.exists(RESULTS_PATH), "Fichier résultats non trouvé !"
    with open(RESULTS_PATH, 'r') as f:
        return json.load(f)
def test_gripper_worked():
    results = load_results()
    assert results["gripper_worked"], "Le gripper n'a pas fonctionné !"
    print(" Le gripper a bien fonctionné !")
