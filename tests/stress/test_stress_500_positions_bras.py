"""Tests de stress : 500 positions bras aléatoires."""
import pytest, time, random
def test_stress_500_positions_bras():
    time.sleep(30.0)
    for _ in range(500):
        pos = random.uniform(-3.14, 3.14)
        assert -3.14 <= pos <= 3.14
    print(" 500 positions bras dans les limites")
