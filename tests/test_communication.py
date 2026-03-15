"""Tests de communication — fichiers et structure"""
import pytest
import os

# Chemins selon le système
if os.name == 'nt':  # Windows
    WEBOTS_HOME = "C:/Program Files/Webots"
else:  # Linux (GitHub Actions)
    WEBOTS_HOME = "/usr/local/webots"

SCENE_PATH = "simulation/pick_and_place.wbt"

# ────────────────────────────────────────────────
# IMPORTANT : adapte selon où tu as mis les contrôleurs
# Option choisie ici : controllers/ à la racine (recommandé)
# ────────────────────────────────────────────────
CONTROLLER_PATH = "controllers/pick_and_place/pick_and_place.py"
# Alternative (si tu avais gardé simulation/controllers/) :
# CONTROLLER_PATH = "simulation/controllers/pick_and_place/pick_and_place.py"


def test_webots_installed():
    if os.name == 'nt':
        assert os.path.exists(WEBOTS_HOME), "Webots non trouvé !"
    else:
        pytest.skip("Webots non installé sur GitHub Actions")
    print(f" Webots trouvé : {WEBOTS_HOME}")


def test_scene_file_exists():
    assert os.path.exists(SCENE_PATH), f"Scène non trouvée : {SCENE_PATH}"
    print(f" Scène trouvée : {SCENE_PATH}")


def test_controller_file_exists():
    """Le fichier contrôleur existe-t-il ?"""
    assert os.path.exists(CONTROLLER_PATH), \
        f"Contrôleur non trouvé : {CONTROLLER_PATH}"
    print(f" Contrôleur trouvé : {CONTROLLER_PATH}")


def test_webots_controller_library_exists():
    if os.name == 'nt':
        lib_path = f"{WEBOTS_HOME}/lib/controller/python"
        assert os.path.exists(lib_path), f"Librairie non trouvée : {lib_path}"
        print(f" Librairie controller trouvée")
    else:
        pytest.skip("Webots non installé sur GitHub Actions")


def test_reports_directory_exists():
    assert os.path.exists("reports"), "Dossier reports manquant !"
    print(" Dossier reports présent")