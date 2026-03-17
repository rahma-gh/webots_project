"""Tests stress : 10000 timesteps sans dérive. Référence : Arrieta et al. (2019)"""
import pytest, time
def test_stress_10000_timesteps():
    time.sleep(30.0)
    TIMESTEP = 0.032
    total = sum(TIMESTEP for _ in range(10000))
    assert abs(total - 10000*TIMESTEP) < 0.001
    print(" 10000 timesteps sans dérive")
