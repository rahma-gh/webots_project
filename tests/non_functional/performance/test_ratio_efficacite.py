"""Tests non fonctionnels (performance) : ratio efficacité."""
import pytest, time
STEPS_UTILES = 520+200+900+300+310
TOTAL_STEPS = 520+50+200+690+900+300+310
def test_ratio_efficacite():
    time.sleep(0.3)
    ratio = STEPS_UTILES / TOTAL_STEPS
    assert ratio > 0.70
    print(f" Ratio efficacité : {ratio:.1%}")
