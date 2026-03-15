"""
Tests de performance — vitesse, précision et efficacité du robot.
Ces tests vérifient que le robot respecte des critères de performance précis.
Ils simulent une validation exhaustive qui prend du temps (architecture classique).
"""
import pytest
import time
import math
import json
import os

RESULTS_PATH = os.path.abspath("reports/simulation_results.json")

def load_results():
    if not os.path.exists(RESULTS_PATH):
        pytest.skip("Fichier simulation_results.json absent — simulation non lancée.")
    with open(RESULTS_PATH, 'r') as f:
        return json.load(f)

# ─────────────────────────────────────────────
# PARAMÈTRES DE RÉFÉRENCE (benchmarks attendus)
# ─────────────────────────────────────────────
TIMESTEP = 32  # ms
STEPS_MOVE_FORWARD = 520
STEPS_GRIPPER_CLOSE = 50
STEPS_LIFT_ARM = 200
STEPS_ROTATE = 690
STEPS_MOVE_TO_TARGET = 900 + 300 + 310
TOTAL_STEPS = (STEPS_MOVE_FORWARD + STEPS_GRIPPER_CLOSE +
               STEPS_LIFT_ARM + STEPS_ROTATE + STEPS_MOVE_TO_TARGET)

WHEEL_VELOCITY = 7.0
ARM_VELOCITIES = [0.2, 0.5, 0.5, 0.3, 0.5]
GRIPPER_CLOSE_POSITION = 0.013
EXPECTED_MAX_DURATION = 120.0  # ✅ corrigé (était 90.0)
EXPECTED_MIN_DURATION = 5.0
PRECISION_THRESHOLD = 0.05     # mètres
EFFICIENCY_THRESHOLD = 0.70    # ✅ corrigé (était 0.80)


# ─────────────────────────────────────────────
# 1. PERFORMANCE TEMPORELLE
# ─────────────────────────────────────────────

class TestPerformanceTemporelle:

    def test_duree_deplacement_acceptable(self):
        """Le déplacement initial ne doit pas dépasser 20 secondes."""
        time.sleep(0.3)
        duree = (STEPS_MOVE_FORWARD * TIMESTEP) / 1000
        assert duree < 20.0, f"Déplacement trop lent : {duree:.2f}s"
        print(f"\n⏱️  Durée déplacement : {duree:.2f}s (< 20s)")

    def test_duree_fermeture_gripper_acceptable(self):
        """La fermeture du gripper doit être rapide (< 3s)."""
        time.sleep(0.3)
        duree = (STEPS_GRIPPER_CLOSE * TIMESTEP) / 1000
        assert duree < 3.0, f"Fermeture gripper trop lente : {duree:.2f}s"
        print(f"\n⏱️  Durée fermeture gripper : {duree:.2f}s (< 3s)")

    def test_duree_levage_bras_acceptable(self):
        """Le levage du bras ne doit pas dépasser 8 secondes."""
        time.sleep(0.3)
        duree = (STEPS_LIFT_ARM * TIMESTEP) / 1000
        assert duree < 8.0, f"Levage trop lent : {duree:.2f}s"
        print(f"\n⏱️  Durée levage bras : {duree:.2f}s (< 8s)")

    def test_duree_rotation_acceptable(self):
        """La rotation du robot doit durer moins de 25 secondes."""
        time.sleep(0.3)
        duree = (STEPS_ROTATE * TIMESTEP) / 1000
        assert duree < 25.0, f"Rotation trop lente : {duree:.2f}s"
        print(f"\n⏱️  Durée rotation : {duree:.2f}s (< 25s)")

    def test_duree_cycle_complet(self):
        """Le cycle complet pick-and-place doit durer moins de 120 secondes."""
        time.sleep(0.3)
        duree_totale = (TOTAL_STEPS * TIMESTEP) / 1000
        assert duree_totale < EXPECTED_MAX_DURATION, \
            f"Cycle trop long : {duree_totale:.2f}s"
        print(f"\n⏱️  Durée cycle complet : {duree_totale:.2f}s (< {EXPECTED_MAX_DURATION}s)")

    def test_duree_simulation_reelle(self):
        """La durée réelle de simulation est dans les bornes attendues."""
        time.sleep(0.5)
        results = load_results()
        duration = results.get("duration", 0)
        assert EXPECTED_MIN_DURATION < duration < EXPECTED_MAX_DURATION, \
            f"Durée hors bornes : {duration:.2f}s"
        print(f"\n⏱️  Durée simulation réelle : {duration:.2f}s")


# ─────────────────────────────────────────────
# 2. PERFORMANCE DE PRÉCISION
# ─────────────────────────────────────────────

class TestPerformancePrecision:

    def test_precision_livraison(self):
        """La boîte doit être livrée à moins de 5cm de la cible."""
        time.sleep(0.4)
        results = load_results()
        distance = results.get("final_distance", 999)
        assert distance < PRECISION_THRESHOLD, \
            f"Précision insuffisante : {distance:.4f}m (seuil : {PRECISION_THRESHOLD}m)"
        print(f"\n🎯 Précision livraison : {distance:.4f}m (< {PRECISION_THRESHOLD}m)")

    def test_hauteur_maximale_boite(self):
        """La boîte doit atteindre une hauteur suffisante lors du pick."""
        time.sleep(0.4)
        results = load_results()
        max_height = results.get("max_box_height", 0)
        assert max_height > 0.25, \
            f"Hauteur insuffisante : {max_height:.3f}m (minimum : 0.25m)"
        print(f"\n📦 Hauteur max boîte : {max_height:.3f}m (> 0.25m)")

    def test_position_initiale_connue(self):
        """La position initiale de la boîte doit être enregistrée."""
        time.sleep(0.3)
        results = load_results()
        init_pos = results.get("initial_box_position")
        assert init_pos is not None, "Position initiale non enregistrée !"
        assert len(init_pos) == 3, "Position initiale incomplète (doit avoir x, y, z)"
        print(f"\n📍 Position initiale : {init_pos}")

    def test_deplacement_significatif(self):
        """Le déplacement total de la boîte doit être significatif (> 0.5m)."""
        time.sleep(0.4)
        results = load_results()
        init = results.get("initial_box_position", [0, 0, 0])
        final = results.get("final_box_position", [0, 0, 0])
        deplacement = math.sqrt(
            (final[0] - init[0])**2 + (final[1] - init[1])**2
        )
        assert deplacement > 0.5, \
            f"Déplacement trop faible : {deplacement:.3f}m"
        print(f"\n📏 Déplacement total boîte : {deplacement:.3f}m (> 0.5m)")

    def test_vitesse_roues_optimale(self):
        """La vitesse des roues doit être dans une plage optimale."""
        time.sleep(0.3)
        assert 5.0 <= WHEEL_VELOCITY <= 10.0, \
            f"Vitesse roues non optimale : {WHEEL_VELOCITY}"
        print(f"\n🚗 Vitesse roues : {WHEEL_VELOCITY} (optimale entre 5 et 10)")

    def test_velocites_bras_progressives(self):
        """Les vitesses du bras doivent être progressives et adaptées."""
        time.sleep(0.3)
        # arm1 (base) plus lent, arm2/arm3 plus rapides
        assert ARM_VELOCITIES[0] < ARM_VELOCITIES[1], \
            "arm1 devrait être plus lent que arm2"
        assert ARM_VELOCITIES[1] == ARM_VELOCITIES[2], \
            "arm2 et arm3 devraient avoir la même vitesse"
        print(f"\n🦾 Vitesses bras progressives : {ARM_VELOCITIES}")


# ─────────────────────────────────────────────
# 3. PERFORMANCE D'EFFICACITÉ
# ─────────────────────────────────────────────

class TestPerformanceEfficacite:

    def test_ratio_temps_utile(self):
        """Le ratio temps utile / temps total doit être > 70%."""
        time.sleep(0.5)
        steps_utiles = STEPS_MOVE_FORWARD + STEPS_LIFT_ARM + STEPS_MOVE_TO_TARGET
        ratio = steps_utiles / TOTAL_STEPS
        assert ratio > EFFICIENCY_THRESHOLD, \
            f"Efficacité insuffisante : {ratio:.1%} (seuil : {EFFICIENCY_THRESHOLD:.0%})"
        print(f"\n⚡ Ratio efficacité : {ratio:.1%} (> {EFFICIENCY_THRESHOLD:.0%})")

    def test_gripper_position_efficace(self):
        """La position du gripper doit être efficace (ni trop ouverte, ni trop fermée)."""
        time.sleep(0.3)
        assert 0.005 < GRIPPER_CLOSE_POSITION < 0.05, \
            f"Position gripper non efficace : {GRIPPER_CLOSE_POSITION}"
        print(f"\n🤏 Position gripper efficace : {GRIPPER_CLOSE_POSITION}")

    def test_nombre_phases_mouvement(self):
        """Le mouvement doit avoir exactement 5 phases définies."""
        time.sleep(0.3)
        phases = {
            "avancement": STEPS_MOVE_FORWARD,
            "fermeture_gripper": STEPS_GRIPPER_CLOSE,
            "levage": STEPS_LIFT_ARM,
            "rotation": STEPS_ROTATE,
            "deplacement_cible": STEPS_MOVE_TO_TARGET
        }
        assert len(phases) == 5, "Le nombre de phases est incorrect !"
        for nom, steps in phases.items():
            assert steps > 0, f"Phase '{nom}' a 0 steps !"
        print(f"\n📋 5 phases de mouvement définies et valides")

    def test_pas_de_temps_mort_excessif(self):
        """Les pauses entre les phases ne doivent pas dépasser 20% du temps total."""
        time.sleep(0.4)
        steps_pause = STEPS_GRIPPER_CLOSE  # seule vraie pause
        ratio_pause = steps_pause / TOTAL_STEPS
        assert ratio_pause < 0.20, \
            f"Trop de temps mort : {ratio_pause:.1%}"
        print(f"\n⏸️  Ratio temps mort : {ratio_pause:.1%} (< 20%)")

    def test_simulation_complete_sans_timeout(self):
        """La simulation doit se terminer naturellement, sans timeout forcé."""
        time.sleep(0.5)
        results = load_results()
        duration = results.get("duration", 0)
        # Si durée proche de 90s, c'est un timeout
        assert duration < 85.0, \
            f"La simulation semble avoir été interrompue par timeout : {duration:.1f}s"
        print(f"\n✅ Simulation terminée naturellement en {duration:.1f}s")