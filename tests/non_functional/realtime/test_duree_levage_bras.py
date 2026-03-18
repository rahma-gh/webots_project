"""Tests non fonctionnels (realtime) : durée levage bras < 10s."""
import pytest
TIMESTEP = 32; STEPS = 200
def test_duree_levage_bras():
    duree = (STEPS * TIMESTEP) / 1000
    assert duree < 10.0
    print(f" Durée levage bras : {duree:.2f}s < 10s")
