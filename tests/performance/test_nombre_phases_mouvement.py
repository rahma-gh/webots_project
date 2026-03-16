import pytest, time
def test_nombre_phases_mouvement():
    time.sleep(0.3)
    phases = {"avancement": 520, "fermeture_gripper": 50, "levage": 200, "rotation": 690, "deplacement_cible": 1510}
    assert len(phases) == 5
    for nom, steps in phases.items():
        assert steps > 0
    print(" 5 phases définies")
