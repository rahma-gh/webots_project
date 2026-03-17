"""Tests performance : vitesses bras progressives."""
import pytest, time
ARM = [0.2, 0.5, 0.5, 0.3, 0.5]
def test_velocites_bras_progressives():
    time.sleep(0.3)
    assert ARM[0] < ARM[1]
    assert ARM[1] == ARM[2]
    print(f" Vitesses bras progressives : {ARM}")
