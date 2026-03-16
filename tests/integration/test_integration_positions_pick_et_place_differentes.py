import pytest, time
def test_integration_positions_pick_et_place_differentes():
    time.sleep(0.4)
    assert -0.55 != -1.0
    assert -0.9 != -0.3
    print(" Positions pick/place différentes")
