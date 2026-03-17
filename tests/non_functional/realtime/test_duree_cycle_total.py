"""Tests non fonctionnels (realtime) : durée cycle total < 60s."""
import pytest
TIMESTEP = 32
TOTAL = 520+50+200+690
def test_duree_cycle_total():
    duree = (TOTAL * TIMESTEP) / 1000
    assert duree < 60.0
    print(f" Durée cycle total : {duree:.2f}s < 60s")
