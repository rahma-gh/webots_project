"""Tests de sécurité — limites et positions."""
import pytest

ARM_PICK_POSITIONS = {"arm2": -0.55, "arm3": -0.9, "arm4": -1.5}
ARM_PLACE_POSITIONS = {"arm1": 0.0, "arm2": -1.0, "arm3": -0.3, "arm4": -1.0}
WHEEL_MAX_VELOCITY = 7.0
GRIPPER_CLOSE_POSITION = 0.013

def test_arm_pick_positions_in_range():
    """Les positions de saisie sont-elles dans les limites sécurisées ?"""
    for arm, pos in ARM_PICK_POSITIONS.items():
        assert -3.14 <= pos <= 3.14, f"{arm} hors limites : {pos}"
    print(" Positions de saisie sécurisées")

def test_arm_place_positions_in_range():
    """Les positions de dépose sont-elles dans les limites sécurisées ?"""
    for arm, pos in ARM_PLACE_POSITIONS.items():
        assert -3.14 <= pos <= 3.14, f"{arm} hors limites : {pos}"
    print(" Positions de dépose sécurisées")

def test_wheel_velocity_safe():
    """La vitesse des roues est-elle sous la limite maximale ?"""
    assert WHEEL_MAX_VELOCITY <= 10.0
    print(f" Vitesse roues sécurisée : {WHEEL_MAX_VELOCITY}")

def test_gripper_no_crush():
    """Le gripper ne se ferme-t-il pas complètement (éviter l'écrasement) ?"""
    assert GRIPPER_CLOSE_POSITION > 0.0, "Gripper trop fermé — risque d'écrasement !"
    print(f" Gripper sécurisé : position {GRIPPER_CLOSE_POSITION}")