"""Le capteur arm4sensor est-il activé dans le contrôleur ?"""
import os
 
CONTROLLER_PATH = "controllers/pick_and_place/pick_and_place.py"
 
def test_arm_sensor_signal():
    """Le capteur arm4sensor est-il activé dans le contrôleur ?"""
    assert os.path.exists(CONTROLLER_PATH), "Contrôleur non trouvé !"
    with open(CONTROLLER_PATH) as f:
        content = f.read()
    assert "arm4sensor" in content or "armPositionSensors" in content
    assert "sensor.enable" in content
    print(" arm4sensor activé dans le contrôleur")
 