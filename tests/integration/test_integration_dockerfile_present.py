import pytest, time, os
def test_integration_dockerfile_present():
    time.sleep(0.3)
    assert os.path.exists("Dockerfile")
    with open("Dockerfile") as f: c = f.read()
    assert "webots" in c.lower() or "WEBOTS" in c
    print(" Dockerfile valide")
