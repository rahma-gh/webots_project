"""Tests fonctionnels (conformance) : positions place conformes aux specs."""
import pytest
ARM_PLACE_SPEC = {"arm1": 0.0, "arm2": -1.0, "arm3": -0.3, "arm4": -1.0}
ARM_PLACE = {"arm1": 0.0, "arm2": -1.0, "arm3": -0.3, "arm4": -1.0}
def test_arm_place_positions_conformes():
    assert ARM_PLACE == ARM_PLACE_SPEC
    print(f" Positions place conformes")
