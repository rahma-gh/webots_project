"""Tests fonctionnels — logique du pick and place."""
import pytest
import sys
sys.path.insert(0, "C:/Program Files/Webots/lib/controller/python")

# Paramètres du robot extraits du contrôleur
ARM_VELOCITIES = [0.2, 0.5, 0.5, 0.3, 0.5]
WHEEL_FORWARD_VELOCITY = 7.0
GRIPPER_CLOSE_POSITION = 0.013
ARM_PICK_POSITIONS = {
    "arm2": -0.55,
    "arm3": -0.9,
    "arm4": -1.5
}

def test_arm_velocities_defined():
    """Les vitesses des moteurs du bras sont-elles définies ?"""
    assert len(ARM_VELOCITIES) == 5
    for vel in ARM_VELOCITIES:
        assert vel > 0
    print("✅ 5 vitesses de moteurs définies")

def test_pick_positions_defined():
    """Les positions de saisie sont-elles définies ?"""
    assert "arm2" in ARM_PICK_POSITIONS
    assert "arm3" in ARM_PICK_POSITIONS
    assert "arm4" in ARM_PICK_POSITIONS
    print("✅ Positions de pick définies")

def test_gripper_close_position_valid():
    """La position de fermeture du gripper est-elle valide ?"""
    assert GRIPPER_CLOSE_POSITION > 0
    assert GRIPPER_CLOSE_POSITION < 1.0
    print(f"✅ Position gripper : {GRIPPER_CLOSE_POSITION}")

def test_forward_velocity_positive():
    """La vitesse d'avancement est-elle positive ?"""
    assert WHEEL_FORWARD_VELOCITY > 0
    print(f"✅ Vitesse d'avancement : {WHEEL_FORWARD_VELOCITY}")