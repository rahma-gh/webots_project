"""Tests d'intégration : séquence complète pick-and-place."""
import pytest, os, json
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def test_sequence_complete_pick_and_place():
    """La séquence complète pick-and-place fonctionne-t-elle ?"""
    if not os.path.exists(RESULTS_PATH): pytest.skip("JSON absent")
    with open(RESULTS_PATH) as f: r = json.load(f)
    assert r["robot_moved"], "Étape 1 échouée : robot n'a pas bougé"
    assert r["box_picked"], "Étape 2 échouée : boîte non saisie"
    assert r["gripper_worked"], "Étape 3 échouée : gripper défaillant"
    assert r["box_delivered"], "Étape 4 échouée : boîte non livrée"
    print(" Séquence complète pick-and-place réussie")
