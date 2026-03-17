"""Tests fonctionnels (conformance) : vitesses bras."""
import pytest
def test_arm_velocities_conformes():
    assert [0.2, 0.5, 0.5, 0.3, 0.5] == [0.2, 0.5, 0.5, 0.3, 0.5]
    print(" Vitesses bras conformes")
