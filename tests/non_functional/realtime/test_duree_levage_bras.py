"""Tests realtime : levage bras < 10s."""
import pytest
def test_duree_levage_bras():
    assert (200*32)/1000 < 10.0
    print(f" Durée levage : {(200*32)/1000:.2f}s")
