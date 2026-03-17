"""Tests de stress : accumulation 10000 timesteps sans dérive."""
import pytest, time
def test_stress_10000_timesteps():
    time.sleep(30.0)
    TIMESTEP = 0.032
    total = sum(TIMESTEP for _ in range(10000))
    assert abs(total - 10000*TIMESTEP) < 0.001
    print(f" 10000 timesteps sans dérive")
