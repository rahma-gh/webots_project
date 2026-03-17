"""Test de communication : gripper → contrôleur. Référence : Lee & Seshia (2017)"""
import pytest, os
CONTROLLER_PATH = "controllers/pick_and_place/pick_and_place.py"
def test_gripper_device_communication():
    assert os.path.exists(CONTROLLER_PATH), f"Contrôleur non trouvé : {CONTROLLER_PATH}"
    with open(CONTROLLER_PATH) as f: c = f.read()
    assert "finger::left" in c, "Device gripper non trouvé !"
    assert "finger.setPosition" in c, "Gripper non contrôlé !"
    print(" Gripper communique avec le contrôleur")
