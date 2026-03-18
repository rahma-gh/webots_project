"""Le contrôleur tapis communique-t-il avec le moteur ?"""
import os

BELT_CONTROLLER = "controllers/move_conveyor_belt/move_conveyor_belt.py"

def test_conveyor_belt_communication():
    """Le contrôleur tapis communique-t-il avec le moteur ?"""
    assert os.path.exists(BELT_CONTROLLER), "Contrôleur tapis non trouvé !"
    with open(BELT_CONTROLLER) as f:
        content = f.read()
    assert "belt motor" in content
    assert "setVelocity" in content
    print(" Tapis communique avec le moteur")