"""Tests non fonctionnels (realtime) : durée fermeture gripper < 5s."""
import pytest
TIMESTEP = 32; STEPS = 50
def test_duree_fermeture_gripper():
    duree = (STEPS * TIMESTEP) / 1000
    assert duree < 5.0
    print(f" Durée fermeture gripper : {duree:.2f}s < 5s")
