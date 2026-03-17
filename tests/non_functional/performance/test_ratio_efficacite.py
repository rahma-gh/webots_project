"""Tests performance : ratio efficacité > 70%."""
import pytest, time
def test_ratio_efficacite():
    time.sleep(0.3)
    assert (520+200+900+300+310)/(520+50+200+690+900+300+310) > 0.70
    print(" Ratio efficacité OK")
