"""Tests d'intégration : tapis + robot synchronisés."""
import pytest, os
def test_tapis_robot_synchronisation():
    """Le timing entre le tapis et le robot est-il cohérent ?"""
    belt = "simulation/controllers/move_conveyor_belt/move_conveyor_belt.py"
    robot = "simulation/controllers/pick_and_place/pick_and_place.py"
    assert os.path.exists(belt) and os.path.exists(robot)
    with open(belt) as f: belt_content = f.read()
    with open(robot) as f: robot_content = f.read()
    assert "setPosition" in belt_content
    assert "robot.step(520" in robot_content
    print(" Tapis et robot synchronisés")
