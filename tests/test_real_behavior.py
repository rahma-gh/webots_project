"""Tests comportementaux — vérifie le vrai comportement du robot."""
import os
import json
import pytest
import subprocess
import time

# Chemin Webots selon le système
if os.name == 'nt':  # Windows
    WEBOTS_PATH = "C:/Program Files/Webots/msys64/mingw64/bin/webots.exe"
else:  # Linux / Docker
    WEBOTS_PATH = "webots"

WORLD_PATH = os.path.abspath("simulation/pick_and_place.wbt")
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")


@pytest.fixture(scope="module", autouse=True)
def run_simulation():
    """Lance la simulation seulement si le JSON n'existe pas déjà."""

    # Sur Linux/Docker : Webots a déjà tourné, JSON déjà créé → on skip
    if os.name != 'nt' and os.path.exists(RESULTS_PATH):
        print(f"\n JSON déjà présent (Docker), simulation ignorée.")
        return

    # Sur Windows (ou si JSON absent) : lancer Webots
    if os.path.exists(RESULTS_PATH):
        os.remove(RESULTS_PATH)

    print(f"\n🚀 Lancement simulation Webots...")
    cmd = [WEBOTS_PATH, "--mode=fast", "--batch", "--no-rendering", WORLD_PATH]

    start = time.time()
    try:
        subprocess.run(cmd, capture_output=True, text=True, timeout=90)
    except subprocess.TimeoutExpired:
        pass

    elapsed = round(time.time() - start, 1)
    print(f"  Simulation terminée en {elapsed}s")


def load_results():
    """Charger les résultats de la simulation."""
    assert os.path.exists(RESULTS_PATH), \
        " Fichier résultats non trouvé — la simulation n'a pas écrit les résultats !"
    with open(RESULTS_PATH, 'r') as f:
        return json.load(f)


def test_robot_moved():
    """Est-ce que le robot a vraiment bougé ?"""
    results = load_results()
    init_pos = results.get("initial_box_position", [0, 0, 0])
    final_pos = results.get("final_box_position", [0, 0, 0])
    print(f"\n Position initiale : {init_pos}")
    print(f" Position finale   : {final_pos}")
    assert results["robot_moved"], " Le robot n'a pas bougé !"
    print(" Le robot a bougé !")


def test_box_picked():
    """Est-ce que la boîte a été saisie ?"""
    results = load_results()
    max_height = round(results.get("max_box_height", 0), 3)
    print(f"\n📦 Hauteur max boîte : {max_height}m")
    assert results["box_picked"], \
        f" La boîte n'a pas été saisie ! Hauteur max : {max_height}m"
    print(f" La boîte a été saisie ! Hauteur max : {max_height}m")


def test_gripper_worked():
    """Est-ce que le gripper a bien fonctionné ?"""
    results = load_results()
    assert results["gripper_worked"], "❌ Le gripper n'a pas fonctionné !"
    print(" Le gripper a bien fonctionné !")


def test_box_delivered():
    """Est-ce que la boîte est arrivée à destination ?"""
    results = load_results()
    distance = round(results.get("final_distance", 999), 4)
    print(f"\n Distance finale boîte→cible : {distance}m")
    assert results["box_delivered"], \
        f" La boîte n'est pas arrivée à destination ! Distance : {distance}m"
    print(f" La boîte est arrivée à destination !")


def test_simulation_duration():
    """La simulation s'est-elle terminée dans un temps raisonnable ?"""
    results = load_results()
    duration = round(results.get("duration", 0), 1)
    print(f"\n  Durée simulation : {duration}s")
    assert 0 < duration < 120, \
        f" Durée anormale : {duration}s"
    print(f" Durée correcte : {duration}s")

@pytest.mark.slow  # ← pour pouvoir l'exclure facilement en local si besoin
@pytest.mark.parametrize("num_runs", [1, 3, 5])  # ← lance 1, puis 3, puis 5 simulations
def test_multiple_full_simulations(num_runs):
    """
    Démo : plusieurs exécutions complètes de la simulation pick-and-place.
    Dans un vrai projet, on pourrait avoir 10–20 scénarios / variantes à tester.
    """
    print(f"\n=== Lancement de {num_runs} simulations complètes ===")
    
    for run in range(1, num_runs + 1):
        print(f"Run {run}/{num_runs} en cours...")
        
        # Supprime l'ancien JSON pour forcer une nouvelle simu
        if os.path.exists(RESULTS_PATH):
            os.remove(RESULTS_PATH)
        
        # Relance exactement la même fixture que pour les autres tests
        run_simulation()  # ← ta fixture qui lance Webots
        
        # Charge et vérifie rapidement (optionnel)
        results = load_results()
        assert results["box_delivered"], f"Échec au run {run}"
        print(f"  → Run {run} OK (durée simu : {results.get('duration', 'N/A')}s)")

    print("Toutes les simulations terminées.")
