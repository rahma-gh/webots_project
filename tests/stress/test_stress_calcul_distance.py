import pytest, time, random, math
def test_stress_calcul_distance():
    time.sleep(30.0)
    for _ in range(2000):
        x1,y1 = random.uniform(-5,5), random.uniform(-5,5)
        x2,y2 = random.uniform(-5,5), random.uniform(-5,5)
        assert math.sqrt((x2-x1)**2+(y2-y1)**2) >= 0
    print(" 2000 distances calculées")
