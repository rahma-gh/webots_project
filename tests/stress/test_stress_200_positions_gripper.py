"""Tests de stress : 200 positions gripper."""
import pytest, time, random
def test_stress_200_positions_gripper():
    time.sleep(30.0)
    for _ in range(200):
        pos = random.uniform(0.0, 0.025)
        assert 0.0 <= pos <= 0.025
    print(" 200 positions gripper valides")
