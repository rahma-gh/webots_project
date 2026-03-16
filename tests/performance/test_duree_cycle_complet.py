import pytest, time
TIMESTEP = 32
TOTAL_STEPS = 520 + 50 + 200 + 690 + 900 + 300 + 310
def test_duree_cycle_complet():
    time.sleep(0.3)
    duree = (TOTAL_STEPS * TIMESTEP) / 1000
    assert duree < 120.0
    print(f" Durée cycle : {duree:.2f}s")
