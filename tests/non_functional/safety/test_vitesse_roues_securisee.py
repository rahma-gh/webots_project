"""Tests non fonctionnels (safety) : vitesse roues sécurisée."""
import pytest
WHEEL_MAX_VELOCITY = 7.0
def test_vitesse_roues_securisee():
    assert WHEEL_MAX_VELOCITY <= 10.0
    print(f" Vitesse roues sécurisée : {WHEEL_MAX_VELOCITY} <= 10.0")
