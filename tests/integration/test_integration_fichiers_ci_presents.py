import pytest, time, os
def test_integration_fichiers_ci_presents():
    time.sleep(0.4)
    assert os.path.exists(".github/workflows") or os.path.exists(".github/workflows/ci.yml")
    print(" CI/CD présent")
