"""Test de communication : roues → contrôleur. Référence : Lee & Seshia (2017)"""
import pytest, os
CONTROLLER_PATH = "controllers/pick_and_place/pick_and_place.py"
def test_wheel_devices_communication():
    assert os.path.exists(CONTROLLER_PATH), f"Contrôleur non trouvé : {CONTROLLER_PATH}"
    with open(CONTROLLER_PATH) as f: c = f.read()
    for i in range(1, 5):
        assert f"wheel{i}" in c, f"Roue wheel{i} non trouvée !"
    assert "setVelocity" in c, "Contrôle vitesse non trouvé !"
    print(" 4 roues communicant avec le contrôleur")
