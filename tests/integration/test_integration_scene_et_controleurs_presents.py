import pytest, time, os
def test_integration_scene_et_controleurs_presents():
    time.sleep(0.5)
    assert os.path.exists("simulation/pick_and_place.wbt")
    assert os.path.exists("controllers/pick_and_place/pick_and_place.py")
    assert os.path.exists("controllers/pick_and_place_benchmark/pick_and_place_benchmark.py")
    assert os.path.exists("controllers/move_conveyor_belt/move_conveyor_belt.py")
    print(" Scène + 3 contrôleurs présents")
