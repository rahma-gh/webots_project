"""Tests d'intégration : scène + tous les contrôleurs présents ensemble."""
import pytest, os
def test_scene_controleurs_presents():
    """La scène et tous les contrôleurs sont-ils présents ensemble ?"""
    fichiers = [
        "simulation/pick_and_place.wbt",
        "simulation/controllers/pick_and_place/pick_and_place.py",
        "simulation/controllers/pick_and_place_benchmark/pick_and_place_benchmark.py",
        "simulation/controllers/move_conveyor_belt/move_conveyor_belt.py",
    ]
    for f in fichiers:
        assert os.path.exists(f), f"Fichier manquant : {f}"
    print(" Scène + 3 contrôleurs présents ensemble")
