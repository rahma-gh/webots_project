import pytest, time, os
def test_integration_conftest_charge():
    time.sleep(0.3)
    assert os.path.exists("conftest.py")
    with open("conftest.py") as f: c = f.read()
    assert "WEBOTS_HOME" in c
    print(" conftest.py valide")
