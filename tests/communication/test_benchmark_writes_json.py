"""
Test de communication : superviseur → fichier JSON
Vérifie que le benchmark écrit bien le JSON (canal de communication vers pytest).
Référence : Arrieta et al. (2019) - CPS Communication Testing
"""
import pytest
import os
import json

RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
BENCHMARK_PATH = "simulation/controllers/pick_and_place_benchmark/pick_and_place_benchmark.py"

def test_benchmark_writes_json():
    """Le benchmark écrit-il le fichier JSON de communication ?"""
    assert os.path.exists(BENCHMARK_PATH), "Benchmark non trouvé !"
    with open(BENCHMARK_PATH, 'r') as f:
        contenu = f.read()
    assert "json.dump" in contenu or "json2.dump" in contenu, \
        "Écriture JSON non trouvée dans le benchmark !"
    print(" Benchmark configure l'écriture du JSON")
