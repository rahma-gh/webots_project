import pytest, time, os
def test_integration_controleur_convoyeur_lisible():
    time.sleep(0.3)
    with open("controllers/move_conveyor_belt/move_conveyor_belt.py") as f:
        c = f.read()
    assert "Robot()" in c
    print(" Contrôleur convoyeur valide")
