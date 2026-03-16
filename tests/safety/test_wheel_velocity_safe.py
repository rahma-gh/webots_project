import pytest

WHEEL_MAX_VELOCITY = 15.0 #7.0

def test_wheel_velocity_safe():
    assert WHEEL_MAX_VELOCITY <= 10.0
    print(f" Vitesse roues sécurisée : {WHEEL_MAX_VELOCITY}")
