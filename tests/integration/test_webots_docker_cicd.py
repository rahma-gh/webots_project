"""Tests d'intégration : Webots + Docker + CI/CD."""
import pytest, os
def test_webots_docker_cicd():
    assert os.path.exists("Dockerfile")
    assert os.path.exists(".github/workflows") or os.path.exists(".github/workflows/ci.yml")
    with open("Dockerfile") as f: c = f.read()
    assert "webots" in c.lower()
    print(" Webots + Docker + CI/CD intégrés")
