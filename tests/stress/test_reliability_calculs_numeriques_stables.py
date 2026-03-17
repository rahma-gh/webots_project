"""Tests fiabilité : calculs numériques stables."""
import pytest, time
def test_reliability_calculs_numeriques_stables():
    time.sleep(30.0)
    TIMESTEP = 0.032
    for n in [100,1000,5000,10000]:
        assert abs(sum(TIMESTEP for _ in range(n)) - n*TIMESTEP) < 0.001
    print(" Calculs numériques stables")
