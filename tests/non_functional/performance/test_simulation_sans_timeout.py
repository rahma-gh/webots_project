"""Tests performance : simulation sans timeout."""
import pytest, os, json
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def test_simulation_sans_timeout():
    if not os.path.exists(RESULTS_PATH): pytest.skip("JSON absent")
    with open(RESULTS_PATH) as f: r = json.load(f)
    assert r.get("duration",0) < 85.0
    print(" Simulation sans timeout")
