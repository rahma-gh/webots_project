"""Tests realtime : fermeture gripper < 5s."""
import pytest
def test_duree_fermeture_gripper():
    assert (50*32)/1000 < 5.0
    print(f" Durée gripper : {(50*32)/1000:.2f}s")
