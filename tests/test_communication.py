
import pytest
import os

if os.name == 'nt':  # Windows
    WEBOTS_HOME = "C:/Program Files/Webots"
else:  # Linux (GitHub Actions)
    WEBOTS_HOME = "/usr/local/webots"

SCENE_PATH = "simulation/pick_and_place.wbt"

CONTROLLER_PATH = "controllers/pick_and_place/pick_and_place.py"

def test_scene_file_exists():
    assert os.path.exists(SCENE_PATH), f"Scène non trouvée : {SCENE_PATH}"
    print(f" Scène trouvée : {SCENE_PATH}")


def test_controller_file_exists():
    """Le fichier contrôleur existe-t-il ?"""
    assert os.path.exists(CONTROLLER_PATH), \
        f"Contrôleur non trouvé : {CONTROLLER_PATH}"
    print(f" Contrôleur trouvé : {CONTROLLER_PATH}")


def test_reports_directory_exists():
    assert os.path.exists("reports"), "Dossier reports manquant !"
    print(" Dossier reports présent")