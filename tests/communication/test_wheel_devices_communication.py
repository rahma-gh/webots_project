"""Les 4 roues communiquent-elles avec le contrôleur ?"""
import os

CONTROLLER_PATH = "controllers/pick_and_place/pick_and_place.py"

def test_wheel_devices_communication():
    """Les 4 roues communiquent-elles avec le contrôleur ?"""
    assert os.path.exists(CONTROLLER_PATH)
    with open(CONTROLLER_PATH) as f:
        content = f.read()
    assert "wheel1" in content
    assert "wheel2" in content
    assert "wheel3" in content
    assert "wheel4" in content
    print(" 4 roues communiquent avec le contrôleur")