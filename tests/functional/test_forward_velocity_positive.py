import pytest

WHEEL_FORWARD_VELOCITY = 7.0

def test_forward_velocity_positive():
    assert WHEEL_FORWARD_VELOCITY > 0
    print(f" Vitesse d'avancement : {WHEEL_FORWARD_VELOCITY}")
