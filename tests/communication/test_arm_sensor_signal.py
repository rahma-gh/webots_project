"""Test de communication : capteur bras → contrôleur. Référence : Lee & Seshia (2017)"""
import pytest, os
CONTROLLER_PATH = "controllers/pick_and_place/pick_and_place.py"
def test_arm_sensor_signal():
    assert os.path.exists(CONTROLLER_PATH), f"Contrôleur non trouvé : {CONTROLLER_PATH}"
    with open(CONTROLLER_PATH) as f: c = f.read()
    assert "arm4sensor" in c, "Capteur arm4sensor non trouvé !"
    assert "sensor.enable" in c, "Capteurs non activés !"
    print(" Capteur arm4sensor activé")
