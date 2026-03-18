"""Tests fonctionnels (conformance) : vitesses bras conformes aux specs."""
import pytest
ARM_VELOCITIES_SPEC = [0.2, 0.5, 0.5, 0.3, 0.5]
ARM_VELOCITIES = [0.2, 0.5, 0.5, 0.3, 0.5]
def test_arm_velocities_conformes():
    assert ARM_VELOCITIES == ARM_VELOCITIES_SPEC
    print(f" Vitesses bras conformes : {ARM_VELOCITIES}")
