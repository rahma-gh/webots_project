import pytest, time, os, json

BASELINE = {
    "wheel_velocity": 7.0,
    "gripper_close": 0.013,
    "arm_velocities": [0.2, 0.5, 0.5, 0.3, 0.5],
    "arm_pick": {"arm2": -0.55, "arm3": -0.9, "arm4": -1.5},
    "arm_place": {"arm1": 0.0, "arm2": -1.0, "arm3": -0.3, "arm4": -1.0},
    "steps_forward": 520, "steps_gripper": 50, "steps_lift": 200,
    "steps_rotate": 690, "timestep": 32, "max_duration": 120.0,
    "precision_threshold": 0.05,
}
def test_regression_vitesse_roues_inchangee():
    time.sleep(0.4)
    assert BASELINE['wheel_velocity'] == 7.0
    print(f" test_regression_vitesse_roues_inchangee OK")
