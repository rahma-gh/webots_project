import os, json, pytest
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def load_results():
    assert os.path.exists(RESULTS_PATH), "Fichier résultats non trouvé !"
    with open(RESULTS_PATH, 'r') as f:
        return json.load(f)
def test_robot_moved():
    results = load_results()
    assert results["robot_moved"], "Le robot n'a pas bougé !"
    print(" Le robot a bougé !")
