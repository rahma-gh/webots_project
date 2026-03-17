"""Tests stress : 3000 calculs trigonométriques. Référence : Arrieta et al. (2019)"""
import pytest, time, random, math
def test_stress_3000_calculs_trigo():
    time.sleep(30.0)
    for _ in range(3000):
        a = random.uniform(-math.pi, math.pi)
        assert abs(math.sqrt(math.cos(a)**2+math.sin(a)**2)-1.0) < 1e-9
    print(" 3000 calculs trigo cohérents")
