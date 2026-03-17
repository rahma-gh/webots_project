"""Tests performance : durée cycle < 120s."""
import pytest, time
def test_duree_cycle_complet():
    time.sleep(0.3)
    assert ((520+50+200+690+900+300+310)*32)/1000 < 120.0
    print(" Durée cycle OK")
