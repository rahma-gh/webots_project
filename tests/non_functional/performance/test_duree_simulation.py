"""Tests non fonctionnels (performance) : durée simulation."""
import pytest, os, json
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def test_duree_simulation():
    if not os.path.exists(RESULTS_PATH): pytest.skip("JSON absent")
    with open(RESULTS_PATH) as f: r = json.load(f)
    assert 5.0 < r.get("duration",0) < 120.0
    print(f" Durée simulation : {r.get('duration'):.1f}s")
