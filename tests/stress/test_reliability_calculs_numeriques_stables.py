"""Tests de fiabilité : calculs numériques stables."""
import pytest, time, math
def test_reliability_calculs_numeriques_stables():
    time.sleep(30.0)
    TIMESTEP = 0.032
    for n in [100, 1000, 5000, 10000]:
        total = sum(TIMESTEP for _ in range(n))
        assert abs(total - n*TIMESTEP) < 0.001
    print(" Calculs numériques stables")
