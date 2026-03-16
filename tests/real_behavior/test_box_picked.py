import os, json, pytest
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def load_results():
    assert os.path.exists(RESULTS_PATH), "Fichier résultats non trouvé !"
    with open(RESULTS_PATH, 'r') as f:
        return json.load(f)
def test_box_picked():
    results = load_results()
    max_height = round(results.get("max_box_height", 0), 3)
    assert results["box_picked"], f"La boîte n'a pas été saisie ! Hauteur max : {max_height}m"
    print(f" La boîte a été saisie ! Hauteur max : {max_height}m")
