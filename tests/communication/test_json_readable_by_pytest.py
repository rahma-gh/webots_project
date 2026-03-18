"""
Test de communication : fichier JSON → pytest
Vérifie que pytest peut lire et interpréter le JSON produit par Webots.
Référence : Arrieta et al. (2019) - CPS Communication Testing
"""
import pytest
import os
import json

RESULTS_PATH = os.path.abspath("reports/simulation_results.json")

def test_json_readable_by_pytest():
    """Le JSON est-il lisible et valide pour pytest ?"""
    if not os.path.exists(RESULTS_PATH):
        pytest.skip("JSON absent — simulation non lancée")
    with open(RESULTS_PATH, 'r') as f:
        results = json.load(f)
    champs_requis = [
        "robot_moved", "box_picked", "box_delivered",
        "gripper_worked", "final_distance", "duration"
    ]
    for champ in champs_requis:
        assert champ in results, f"Champ manquant dans JSON : {champ}"
    print(" JSON lisible et valide par pytest")
