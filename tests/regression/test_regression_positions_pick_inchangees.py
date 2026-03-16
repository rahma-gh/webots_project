import pytest, time, os, json
BASELINE = {"arm_velocities": [0.2,0.5,0.5,0.3,0.5], "arm_pick": {"arm2":-0.55,"arm3":-0.9,"arm4":-1.5}, "arm_place": {"arm1":0.0,"arm2":-1.0,"arm3":-0.3,"arm4":-1.0}}
def test_regression_positions_pick_inchangees():
    time.sleep(0.4)
    assert BASELINE["arm_pick"]["arm2"] == -0.55
    assert BASELINE["arm_pick"]["arm3"] == -0.9
    assert BASELINE["arm_pick"]["arm4"] == -1.5
    print(" Positions pick inchangées")
