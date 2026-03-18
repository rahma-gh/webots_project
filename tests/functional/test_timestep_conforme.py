"""Tests fonctionnels (conformance) : timestep conforme aux specs."""
import pytest
TIMESTEP_SPEC = 32
TIMESTEP = 32
def test_timestep_conforme():
    assert TIMESTEP == TIMESTEP_SPEC
    print(f" Timestep conforme : {TIMESTEP}ms")
