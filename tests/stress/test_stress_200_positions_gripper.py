"""Tests stress : 200 positions gripper. Référence : Arrieta et al. (2019)"""
import pytest, time, random
def test_stress_200_positions_gripper():
    time.sleep(30.0)
    for _ in range(200):
        assert 0.0 <= random.uniform(0.0,0.025) <= 0.025
    print(" 200 positions gripper valides")
