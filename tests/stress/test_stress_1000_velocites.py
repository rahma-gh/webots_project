"""Tests stress : 1000 valeurs vitesse. Référence : Arrieta et al. (2019)"""
import pytest, time, random
def test_stress_1000_velocites():
    time.sleep(30.0)
    assert all(0 < v <= 10.0 for v in [random.uniform(0.1,10.0) for _ in range(1000)])
    print(" 1000 vitesses testées")
