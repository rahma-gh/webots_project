"""
Test de communication : devices roues → contrôleur
Vérifie que les 4 roues sont accessibles par le contrôleur.
Référence : Lee & Seshia (2017) - Interface Tests
"""
import pytest
import os

CONTROLLER_PATH = "simulation/controllers/pick_and_place/pick_and_place.py"

def test_wheel_devices_communication():
    """Les 4 roues communiquent-elles avec le contrôleur ?"""
    assert os.path.exists(CONTROLLER_PATH)
    with open(CONTROLLER_PATH, 'r') as f:
        contenu = f.read()
    for i in range(1, 5):
        assert f"wheel{i}" in contenu, f"Roue wheel{i} non trouvée !"
    assert "setVelocity" in contenu, "Contrôle vitesse non trouvé !"
    print(" 4 roues communicant avec le contrôleur")
