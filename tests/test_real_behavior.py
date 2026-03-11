"""Vrais tests comportementaux — pick and place Webots."""
import subprocess
import time
import os
import json
import pytest

WEBOTS_PATH = "C:/Program Files/Webots/msys64/mingw64/bin/webots.exe"
WORLD_PATH = os.path.abspath("simulation/pick_and_place.wbt")
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")

@pytest.fixture(scope="module", autouse=True)
def run_simulation():
    """Lance la simulation une seule fois pour tous les tests."""
    
    # Supprimer les anciens résultats
    if os.path.exists(RESULTS_PATH):
        os.remove(RESULTS_PATH)

    print(f"\n🚀 Lancement simulation Webots...")
    
    cmd = [WEBOTS_PATH, "--mode=fast", "--batch", "--no-rendering", WORLD_PATH]
    
    start = time.time()
    try:
        subprocess.run(cmd, capture_output=True, text=True, timeout=90)
    except subprocess.TimeoutExpired as e:
        if hasattr(e, 'process'):
            e.process.kill()
    
    duration = time.time() - start
    print(f"⏱️  Simulation terminée en {duration:.1f}s")
    
    # Attendre que le fichier JSON soit écrit
    time.sleep(2)
    
    yield
    
def load_results():
    """Charger les résultats de la simulation."""
    assert os.path.exists(RESULTS_PATH), \
        "❌ Fichier résultats non trouvé — la simulation n'a pas écrit les résultats !"
    with open(RESULTS_PATH, 'r') as f:
        return json.load(f)

def test_robot_moved():
    """Est-ce que le robot a vraiment bougé ?"""
    results = load_results()
    print(f"\n📍 Position initiale : {results['initial_box_position']}")
    print(f"📍 Position finale   : {results['final_box_position']}")
    assert results["robot_moved"], "❌ Le robot n'a pas bougé !"
    print("✅ Le robot a bougé !")

def test_box_picked():
    """Est-ce que la boîte a été saisie ?"""
    results = load_results()
    print(f"\n📦 Hauteur max boîte : {results['max_box_height']:.3f}m")
    assert results["box_picked"], \
        f"❌ La boîte n'a pas été saisie ! Hauteur max : {results['max_box_height']:.3f}m"
    print(f"✅ La boîte a été saisie ! Hauteur max : {results['max_box_height']:.3f}m")

def test_gripper_worked():
    """Est-ce que le gripper a bien fonctionné ?"""
    results = load_results()
    assert results["gripper_worked"], "❌ Le gripper n'a pas fonctionné !"
    print("✅ Le gripper a bien fonctionné !")

def test_box_delivered():
    """Est-ce que la boîte est arrivée à destination ?"""
    results = load_results()
    print(f"\n📏 Distance finale boîte→cible : {results['final_distance']:.4f}m")
    assert results["box_delivered"], \
        f"❌ La boîte n'est pas arrivée ! Distance : {results['final_distance']:.4f}m"
    print(f"✅ La boîte est arrivée à destination !")

def test_simulation_duration():
    """La simulation s'est-elle terminée dans un temps raisonnable ?"""
    results = load_results()
    print(f"\n⏱️  Durée simulation : {results['duration']:.1f}s")
    assert results["duration"] > 5, "❌ Simulation trop courte !"
    assert results["duration"] < 300, "❌ Simulation trop longue !"
    print(f"✅ Durée correcte : {results['duration']:.1f}s")