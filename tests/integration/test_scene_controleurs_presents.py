"""Tests d'intégration : scène + contrôleurs présents."""
import pytest, os
def test_scene_controleurs_presents():
    for f in [
        "simulation/pick_and_place.wbt",
        "controllers/pick_and_place/pick_and_place.py",
        "controllers/pick_and_place_benchmark/pick_and_place_benchmark.py",
        "controllers/move_conveyor_belt/move_conveyor_belt.py"
    ]:
        assert os.path.exists(f), f"Fichier manquant : {f}"
    print(" Scène + 3 contrôleurs présents")
