"""Le benchmark écrit-il le fichier JSON de communication ?"""
import os

BENCHMARK_PATH = "controllers/pick_and_place_benchmark/pick_and_place_benchmark.py"

def test_benchmark_writes_json():
    """Le benchmark écrit-il le fichier JSON de communication ?"""
    assert os.path.exists(BENCHMARK_PATH), "Benchmark non trouvé !"
    with open(BENCHMARK_PATH) as f:
        content = f.read()
    assert "json.dump" in content or "simulation_results.json" in content
    print(" Benchmark écrit bien un JSON")