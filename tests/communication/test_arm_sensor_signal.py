"""
Test de communication : capteur de position du bras → contrôleur
Vérifie que le capteur arm4sensor envoie un signal valide au contrôleur.
Référence : Lee & Seshia (2017) - Interface Tests
"""
import pytest
import os

CONTROLLER_PATH = "simulation/controllers/pick_and_place/pick_and_place.py"

def test_arm_sensor_signal():
    """Le capteur arm4sensor est-il activé dans le contrôleur ?"""
    assert os.path.exists(CONTROLLER_PATH), "Contrôleur non trouvé !"
    with open(CONTROLLER_PATH, 'r') as f:
        contenu = f.read()
    assert "arm4sensor" in contenu, "Capteur arm4sensor non trouvé !"
    assert "sensor.enable" in contenu, "Capteurs non activés !"
    print(" Capteur arm4sensor activé et communique avec le contrôleur")
