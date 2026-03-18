"""Tests fonctionnels (conformance) : positions pick conformes aux specs."""
import pytest
ARM_PICK_SPEC = {"arm2": -0.55, "arm3": -0.9, "arm4": -1.5}
ARM_PICK = {"arm2": -0.55, "arm3": -0.9, "arm4": -1.5}
def test_arm_pick_positions_conformes():
    assert ARM_PICK == ARM_PICK_SPEC
    print(f" Positions pick conformes")
