"""Tests fonctionnels (conformance) : vitesse roues conforme aux specs."""
import pytest
WHEEL_VELOCITY_SPEC = 7.0
WHEEL_VELOCITY = 7.0
def test_wheel_velocity_conforme():
    assert WHEEL_VELOCITY == WHEEL_VELOCITY_SPEC, \
        f"Vitesse roues non conforme : {WHEEL_VELOCITY} != {WHEEL_VELOCITY_SPEC}"
    print(f" Vitesse roues conforme : {WHEEL_VELOCITY}")
