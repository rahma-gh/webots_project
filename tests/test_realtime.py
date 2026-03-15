"""Tests temps réel — durées et steps de simulation."""
import pytest

# Paramètres temporels extraits du contrôleur
TIMESTEP = 32  # ms (valeur typique Webots)
STEPS_MOVE_FORWARD = 1500 #520
STEPS_GRIPPER_CLOSE = 50
STEPS_LIFT_ARM = 200
STEPS_ROTATE = 690

def test_move_forward_duration():
    """Le déplacement vers la boîte dure-t-il moins de 20 secondes ?"""
    duration_ms = STEPS_MOVE_FORWARD * TIMESTEP
    duration_sec = duration_ms / 1000
    assert duration_sec < 20.0
    print(f" Durée avancement : {duration_sec:.2f}s")

def test_gripper_close_duration():
    """La fermeture du gripper dure-t-elle moins de 5 secondes ?"""
    duration_ms = STEPS_GRIPPER_CLOSE * TIMESTEP
    duration_sec = duration_ms / 1000
    assert duration_sec < 5.0
    print(f" Durée fermeture gripper : {duration_sec:.2f}s")

def test_lift_arm_duration():
    """Le levage du bras dure-t-il moins de 10 secondes ?"""
    duration_ms = STEPS_LIFT_ARM * TIMESTEP
    duration_sec = duration_ms / 1000
    assert duration_sec < 10.0
    print(f" Durée levage bras : {duration_sec:.2f}s")

def test_total_cycle_duration():
    """Le cycle complet dure-t-il moins de 60 secondes ?"""
    total_steps = (STEPS_MOVE_FORWARD + STEPS_GRIPPER_CLOSE +
                   STEPS_LIFT_ARM + STEPS_ROTATE)
    total_sec = (total_steps * TIMESTEP) / 1000
    assert total_sec < 60.0
    print(f" Durée cycle total : {total_sec:.2f}s")