import pytest, time, os
RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
def test_integration_dossier_reports_avec_resultats():
    time.sleep(0.3)
    assert os.path.exists("reports")
    assert os.path.exists(RESULTS_PATH)
    assert os.path.getsize(RESULTS_PATH) > 10
    print(" Dossier reports avec résultats OK")
