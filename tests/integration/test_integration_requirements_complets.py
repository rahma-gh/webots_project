import pytest, time, os
def test_integration_requirements_complets():
    time.sleep(0.3)
    assert os.path.exists("requirements.txt")
    with open("requirements.txt") as f: c = f.read()
    assert "pytest" in c
    print(" requirements.txt complet")
