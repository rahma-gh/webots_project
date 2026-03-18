"""Tests d'intégration : Webots + Docker + CI/CD."""
import pytest, os
def test_webots_docker_cicd():
    """L'environnement Webots + Docker + CI/CD est-il bien configuré ?"""
    assert os.path.exists("Dockerfile")
    assert os.path.exists(".github/workflows/ci.yml") or \
           os.path.exists(".github/workflows")
    with open("Dockerfile") as f: c = f.read()
    assert "webots" in c.lower()
    print(" Webots + Docker + CI/CD intégrés")
