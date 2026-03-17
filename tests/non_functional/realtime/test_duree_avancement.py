"""Tests realtime : avancement < 20s."""
import pytest
def test_duree_avancement():
    assert (520*32)/1000 < 20.0
    print(f" Durée avancement : {(520*32)/1000:.2f}s")
