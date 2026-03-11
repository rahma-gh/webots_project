"""Tests de communication — fichiers et structure."""
import pytest
import os

WEBOTS_HOME = "C:/Program Files/Webots"
SCENE_PATH = "simulation/pick_and_place.wbt"
CONTROLLER_PATH = "simulation/controllers/pick_and_place/pick_and_place.py"

def test_webots_installed():
    """Webots est-il installé sur le système ?"""
    assert os.path.exists(WEBOTS_HOME), "Webots non trouvé !"
    print(f"✅ Webots trouvé : {WEBOTS_HOME}")

def test_scene_file_exists():
    """Le fichier de scène pick_and_place.wbt existe-t-il ?"""
    assert os.path.exists(SCENE_PATH), f"Scène non trouvée : {SCENE_PATH}"
    print(f"✅ Scène trouvée : {SCENE_PATH}")

def test_controller_file_exists():
    """Le fichier contrôleur existe-t-il ?"""
    assert os.path.exists(CONTROLLER_PATH), \
        f"Contrôleur non trouvé : {CONTROLLER_PATH}"
    print(f"✅ Contrôleur trouvé : {CONTROLLER_PATH}")

def test_webots_controller_library_exists():
    """La librairie controller de Webots est-elle accessible ?"""
    lib_path = f"{WEBOTS_HOME}/lib/controller/python"
    assert os.path.exists(lib_path), f"Librairie non trouvée : {lib_path}"
    print(f"✅ Librairie controller trouvée")

def test_reports_directory_exists():
    """Le dossier reports existe-t-il ?"""
    assert os.path.exists("reports"), "Dossier reports manquant !"
    print("✅ Dossier reports présent")