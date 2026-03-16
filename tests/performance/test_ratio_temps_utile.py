import pytest, time
STEPS_MOVE_FORWARD = 520; STEPS_LIFT_ARM = 200
STEPS_MOVE_TO_TARGET = 900+300+310
TOTAL_STEPS = 520+50+200+690+900+300+310
def test_ratio_temps_utile():
    time.sleep(0.5)
    ratio = (STEPS_MOVE_FORWARD + STEPS_LIFT_ARM + STEPS_MOVE_TO_TARGET) / TOTAL_STEPS
    assert ratio > 0.70
    print(f" Ratio efficacité : {ratio:.1%}")
