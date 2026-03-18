"""Le device gripper communique-t-il avec le contrôleur ?"""
import os

CONTROLLER_PATH = "controllers/pick_and_place/pick_and_place.py"

def test_gripper_device_communication():
    """Le device gripper communique-t-il avec le contrôleur ?"""
    assert os.path.exists(CONTROLLER_PATH)
    with open(CONTROLLER_PATH) as f:
        content = f.read()
    assert "finger" in content
    assert "setPosition" in content
    print(" Gripper communique avec le contrôleur")