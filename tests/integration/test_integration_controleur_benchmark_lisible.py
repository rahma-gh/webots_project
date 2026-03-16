import pytest, time, os
def test_integration_controleur_benchmark_lisible():
    time.sleep(0.4)
    with open("controllers/pick_and_place_benchmark/pick_and_place_benchmark.py") as f:
        c = f.read()
    assert "Supervisor" in c
    assert "getFromDef" in c
    print(" Contrôleur benchmark valide")
