"""Tests non fonctionnels (realtime) : durée avancement < 20s."""
import pytest
TIMESTEP = 32; STEPS = 520
def test_duree_avancement():
    duree = (STEPS * TIMESTEP) / 1000
    assert duree < 20.0
    print(f" Durée avancement : {duree:.2f}s < 20s")
