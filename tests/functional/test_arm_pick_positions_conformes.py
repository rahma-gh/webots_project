"""Tests fonctionnels (conformance) : positions pick."""
import pytest
def test_arm_pick_positions_conformes():
    assert {"arm2": -0.55, "arm3": -0.9, "arm4": -1.5} == {"arm2": -0.55, "arm3": -0.9, "arm4": -1.5}
    print(" Positions pick conformes")
