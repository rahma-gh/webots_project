import pytest, time, os
def test_integration_rapport_genere():
    time.sleep(0.4)
    assert any(os.path.exists(p) for p in ["reports/report.html","reports/report_failures.html"])
    print(" Rapport HTML généré")
