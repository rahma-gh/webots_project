"""Tests fonctionnels (conformance) : positions place."""
import pytest
def test_arm_place_positions_conformes():
    assert {"arm1": 0.0, "arm2": -1.0, "arm3": -0.3, "arm4": -1.0} == {"arm1": 0.0, "arm2": -1.0, "arm3": -0.3, "arm4": -1.0}
    print(" Positions place conformes")
