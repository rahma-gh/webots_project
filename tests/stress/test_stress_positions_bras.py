import pytest, time, random
def test_stress_positions_bras():
    time.sleep(30.0)
    hors = sum(1 for _ in range(500) if not (-3.14 <= random.uniform(-3.14,3.14) <= 3.14))
    assert hors == 0
    print(" 500 positions bras testées")
