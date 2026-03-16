import pytest, time
WHEEL_VELOCITY = 7.0
def test_vitesse_roues_optimale():
    time.sleep(0.3)
    assert 5.0 <= WHEEL_VELOCITY <= 10.0
    print(f" Vitesse roues : {WHEEL_VELOCITY}")
