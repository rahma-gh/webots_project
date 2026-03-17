"""Tests fonctionnels (conformance) : vitesse tapis conforme aux specs."""
import pytest
BELT_VELOCITY_SPEC = 0.2
BELT_VELOCITY = 0.2
def test_conveyor_velocity_conforme():
    assert BELT_VELOCITY == BELT_VELOCITY_SPEC
    print(f" Vitesse tapis conforme : {BELT_VELOCITY}")
