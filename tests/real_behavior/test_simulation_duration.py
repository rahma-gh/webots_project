import os, json, pytest
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def load_results():
    assert os.path.exists(RESULTS_PATH), "Fichier résultats non trouvé !"
    with open(RESULTS_PATH, 'r') as f:
        return json.load(f)
def test_simulation_duration():
    results = load_results()
    duration = round(results.get("duration", 0), 1)
    assert 0 < duration < 120, f"Durée anormale : {duration}s"
    print(f" Durée correcte : {duration}s")
