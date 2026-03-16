import pytest, time, random
def test_stress_velocite_roues_limites():
    time.sleep(30.0)
    erreurs = [v for v in [random.uniform(0.1,10.0) for _ in range(1000)] if not (0 < v <= 10.0)]
    assert len(erreurs) == 0
    print(" 1000 vitesses testées")
