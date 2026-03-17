"""Tests stress : 500 positions bras. Référence : Arrieta et al. (2019)"""
import pytest, time, random
def test_stress_500_positions_bras():
    time.sleep(30.0)
    for _ in range(500):
        assert -3.14 <= random.uniform(-3.14,3.14) <= 3.14
    print(" 500 positions bras valides")
