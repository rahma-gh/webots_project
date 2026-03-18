"""Tests d'intégration : requirements + Dockerfile intégrés."""
import pytest, os
def test_requirements_dockerfile_integres():
    """Les dépendances Python sont-elles intégrées dans le Dockerfile ?"""
    assert os.path.exists("requirements.txt")
    assert os.path.exists("Dockerfile")
    with open("requirements.txt") as f: req = f.read()
    with open("Dockerfile") as f: dock = f.read()
    assert "pytest" in req
    assert "pip" in dock.lower()
    print(" requirements.txt intégré dans Dockerfile")
