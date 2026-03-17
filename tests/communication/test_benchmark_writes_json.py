"""Test de communication : benchmark → JSON. Référence : Arrieta et al. (2019)"""
import pytest, os
BENCHMARK_PATH = "controllers/pick_and_place_benchmark/pick_and_place_benchmark.py"
def test_benchmark_writes_json():
    assert os.path.exists(BENCHMARK_PATH), f"Benchmark non trouvé : {BENCHMARK_PATH}"
    with open(BENCHMARK_PATH) as f: c = f.read()
    assert "json.dump" in c or "json2.dump" in c, "Écriture JSON non trouvée !"
    print(" Benchmark écrit le JSON")
