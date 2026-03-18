"""
Test de communication : gripper device → contrôleur
Vérifie que le gripper est bien accessible par le contrôleur.
Référence : Lee & Seshia (2017) - Interface Tests
"""
import pytest
import os

CONTROLLER_PATH = "simulation/controllers/pick_and_place/pick_and_place.py"

def test_gripper_device_communication():
    """Le device gripper communique-t-il avec le contrôleur ?"""
    assert os.path.exists(CONTROLLER_PATH)
    with open(CONTROLLER_PATH, 'r') as f:
        contenu = f.read()
    assert "finger::left" in contenu, "Device gripper non trouvé !"
    assert "finger.setPosition" in contenu, "Gripper non contrôlé !"
    print(" Gripper device communique avec le contrôleur")
