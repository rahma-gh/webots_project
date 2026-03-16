import os, json, pytest
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def load_results():
    assert os.path.exists(RESULTS_PATH), "Fichier résultats non trouvé !"
    with open(RESULTS_PATH, 'r') as f:
        return json.load(f)
def test_box_delivered():
    results = load_results()
    distance = round(results.get("final_distance", 999), 4)
    assert results["box_delivered"], f"La boîte n'est pas arrivée à destination ! Distance : {distance}m"
    print(f" La boîte est arrivée à destination !")
