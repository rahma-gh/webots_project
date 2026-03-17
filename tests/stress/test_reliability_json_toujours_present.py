"""Tests de fiabilité : JSON toujours présent après simulation."""
import pytest, time, os
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def test_reliability_json_toujours_present():
    time.sleep(0.5)
    assert os.path.exists(RESULTS_PATH), \
        "JSON non présent — simulation n'a pas écrit les résultats !"
    assert os.path.getsize(RESULTS_PATH) > 10, "JSON vide !"
    print(" JSON toujours présent et non vide")
