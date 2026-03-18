"""Tests d'intégration : capteurs bras + contrôleur intégrés."""
import pytest, os
def test_capteurs_controleur_integres():
    """Les capteurs sont-ils bien intégrés dans le contrôleur ?"""
    with open("simulation/controllers/pick_and_place/pick_and_place.py") as f:
        c = f.read()
    assert "armPositionSensors" in c
    assert "sensor.enable" in c
    assert "getValue" in c
    print(" Capteurs intégrés dans le contrôleur")
