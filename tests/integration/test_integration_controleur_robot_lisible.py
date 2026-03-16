import pytest, time, os
def test_integration_controleur_robot_lisible():
    time.sleep(0.4)
    with open("controllers/pick_and_place/pick_and_place.py") as f:
        c = f.read()
    assert "Robot()" in c
    assert "wheel" in c
    print(" Contrôleur robot valide")
