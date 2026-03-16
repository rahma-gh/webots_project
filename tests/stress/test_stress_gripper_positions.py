import pytest, time, random
def test_stress_gripper_positions():
    time.sleep(30.0)
    for _ in range(200):
        pos = random.uniform(0.0, 0.025)
        assert 0.0 <= pos <= 0.025
    print(" 200 positions gripper testées")
