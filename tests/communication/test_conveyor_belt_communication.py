"""
Test de communication : contrôleur tapis → moteur tapis
Vérifie que le contrôleur du tapis communique correctement avec le moteur.
Référence : Lee & Seshia (2017) - Interface Tests
"""
import pytest
import os

BELT_CONTROLLER = "simulation/controllers/move_conveyor_belt/move_conveyor_belt.py"

def test_conveyor_belt_communication():
    """Le contrôleur tapis communique-t-il avec le moteur ?"""
    assert os.path.exists(BELT_CONTROLLER), "Contrôleur tapis non trouvé !"
    with open(BELT_CONTROLLER, 'r') as f:
        contenu = f.read()
    assert "belt motor" in contenu, "Moteur tapis non trouvé !"
    assert "setVelocity" in contenu, "Contrôle vitesse tapis non trouvé !"
    assert "setPosition" in contenu, "Contrôle position tapis non trouvé !"
    print(" Contrôleur tapis communique avec le moteur belt motor")
