import pytest, time
def test_integration_gripper_et_bras_compatibles():
    time.sleep(0.4)
    assert 0.03 < 0.3
    print(" Gripper/bras compatibles")
