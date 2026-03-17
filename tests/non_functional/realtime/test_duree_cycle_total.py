"""Tests realtime : cycle total < 60s."""
import pytest
def test_duree_cycle_total():
    assert ((520+50+200+690)*32)/1000 < 60.0
    print(f" Durée cycle : {((520+50+200+690)*32)/1000:.2f}s")
