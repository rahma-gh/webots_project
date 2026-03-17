"""Tests d'intégration : tapis + robot synchronisés."""
import pytest, os
def test_tapis_robot_synchronisation():
    belt = "controllers/move_conveyor_belt/move_conveyor_belt.py"
    robot = "controllers/pick_and_place/pick_and_place.py"
    assert os.path.exists(belt) and os.path.exists(robot)
    with open(belt) as f: bc = f.read()
    with open(robot) as f: rc = f.read()
    assert "setPosition" in bc
    assert "robot.step(520" in rc
    print(" Tapis et robot synchronisés")
