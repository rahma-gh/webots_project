import os
import pytest

CONTROLLER_PATH = "controllers/pick_and_place/pick_and_place.py"

def test_controller_file_exists():
    assert os.path.exists(CONTROLLER_PATH), f"Contrôleur non trouvé : {CONTROLLER_PATH}"
    print(f" Contrôleur trouvé : {CONTROLLER_PATH}")
