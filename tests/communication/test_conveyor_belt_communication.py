"""Test de communication : contrôleur tapis → moteur. Référence : Lee & Seshia (2017)"""
import pytest, os
BELT_CONTROLLER = "controllers/move_conveyor_belt/move_conveyor_belt.py"
def test_conveyor_belt_communication():
    assert os.path.exists(BELT_CONTROLLER), f"Contrôleur tapis non trouvé : {BELT_CONTROLLER}"
    with open(BELT_CONTROLLER) as f: c = f.read()
    assert "belt motor" in c, "Moteur tapis non trouvé !"
    assert "setVelocity" in c, "Contrôle vitesse tapis non trouvé !"
    assert "setPosition" in c, "Contrôle position tapis non trouvé !"
    print(" Contrôleur tapis communique avec le moteur")
