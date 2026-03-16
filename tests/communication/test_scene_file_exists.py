import os
import pytest

SCENE_PATH = "simulation/pick_and_place.wbt"

def test_scene_file_exists():
    assert os.path.exists(SCENE_PATH), f"Scène non trouvée : {SCENE_PATH}"
    print(f" Scène trouvée : {SCENE_PATH}")
