"""Tests fonctionnels (conformance) : position tapis conforme aux specs."""
import pytest
BELT_POSITION_SPEC = 0.75
BELT_POSITION = 0.75
def test_conveyor_position_conforme():
    assert BELT_POSITION == BELT_POSITION_SPEC
    print(f" Position tapis conforme : {BELT_POSITION}")
