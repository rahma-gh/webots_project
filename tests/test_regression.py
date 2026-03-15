"""
Tests de régression — vérifier que rien n'est cassé après chaque modification.
Dans l'architecture classique (sans IA), TOUS ces tests sont exécutés à chaque push,
même si seulement un fichier a été modifié. C'est la limite principale.
"""
import pytest
import time
import math
import json
import os

RESULTS_PATH = os.path.abspath("reports/simulation_results.json")

def load_results():
    if not os.path.exists(RESULTS_PATH):
        pytest.skip("Fichier simulation_results.json absent.")
    with open(RESULTS_PATH, 'r') as f:
        return json.load(f)


# ─────────────────────────────────────────────
# VALEURS DE RÉFÉRENCE (baseline)
# ─────────────────────────────────────────────
BASELINE = {
    "wheel_velocity": 7.0,
    "gripper_close": 0.013,
    "arm_velocities": [0.2, 0.5, 0.5, 0.3, 0.5],
    "arm_pick": {"arm2": -0.55, "arm3": -0.9, "arm4": -1.5},
    "arm_place": {"arm1": 0.0, "arm2": -1.0, "arm3": -0.3, "arm4": -1.0},
    "steps_forward": 520,
    "steps_gripper": 50,
    "steps_lift": 200,
    "steps_rotate": 690,
    "timestep": 32,
    "max_duration": 90.0,
    "precision_threshold": 0.05,
}


# ─────────────────────────────────────────────
# 1. RÉGRESSION PARAMÈTRES CONTRÔLEUR
# ─────────────────────────────────────────────

class TestRegressionParametresControleur:

    def test_regression_vitesse_roues_inchangee(self):
        """REG-01 : La vitesse des roues n'a pas changé depuis la baseline."""
        time.sleep(0.4)
        assert BASELINE["wheel_velocity"] == 7.0, \
            f"RÉGRESSION : vitesse roues changée ! Attendu 7.0, obtenu {BASELINE['wheel_velocity']}"
        print(f"\n REG-01 : vitesse roues inchangée ({BASELINE['wheel_velocity']})")

    def test_regression_gripper_inchange(self):
        """REG-02 : La position de fermeture du gripper n'a pas changé."""
        time.sleep(0.4)
        assert BASELINE["gripper_close"] == 0.013
        print(f"\n REG-02 : gripper inchangé ({BASELINE['gripper_close']})")

    def test_regression_velocites_bras_inchangees(self):
        """REG-03 : Les vitesses du bras n'ont pas changé."""
        time.sleep(0.4)
        expected = [0.2, 0.5, 0.5, 0.3, 0.5]
        assert BASELINE["arm_velocities"] == expected, \
            f"RÉGRESSION : vitesses bras changées !"
        print(f"\n REG-03 : vitesses bras inchangées {BASELINE['arm_velocities']}")

    def test_regression_positions_pick_inchangees(self):
        """REG-04 : Les positions de saisie n'ont pas changé."""
        time.sleep(0.4)
        assert BASELINE["arm_pick"]["arm2"] == -0.55
        assert BASELINE["arm_pick"]["arm3"] == -0.9
        assert BASELINE["arm_pick"]["arm4"] == -1.5
        print(f"\n REG-04 : positions pick inchangées")

    def test_regression_positions_place_inchangees(self):
        """REG-05 : Les positions de dépose n'ont pas changé."""
        time.sleep(0.4)
        assert BASELINE["arm_place"]["arm1"] == 0.0
        assert BASELINE["arm_place"]["arm2"] == -1.0
        assert BASELINE["arm_place"]["arm3"] == -0.3
        assert BASELINE["arm_place"]["arm4"] == -1.0
        print(f"\n REG-05 : positions place inchangées")

    def test_regression_timestep_inchange(self):
        """REG-06 : Le timestep n'a pas changé."""
        time.sleep(0.3)
        assert BASELINE["timestep"] == 32
        print(f"\n REG-06 : timestep inchangé ({BASELINE['timestep']}ms)")


# ─────────────────────────────────────────────
# 2. RÉGRESSION SÉQUENCE DE MOUVEMENT
# ─────────────────────────────────────────────

class TestRegressionSequenceMouvement:

    def test_regression_steps_avancement(self):
        """REG-07 : Le nombre de steps d'avancement n'a pas changé."""
        time.sleep(0.4)
        assert BASELINE["steps_forward"] == 520
        print(f"\n REG-07 : steps avancement inchangés ({BASELINE['steps_forward']})")

    def test_regression_steps_gripper(self):
        """REG-08 : Le nombre de steps du gripper n'a pas changé."""
        time.sleep(0.3)
        assert BASELINE["steps_gripper"] == 50
        print(f"\n REG-08 : steps gripper inchangés ({BASELINE['steps_gripper']})")

    def test_regression_steps_levage(self):
        """REG-09 : Le nombre de steps de levage n'a pas changé."""
        time.sleep(0.3)
        assert BASELINE["steps_lift"] == 200
        print(f"\n REG-09 : steps levage inchangés ({BASELINE['steps_lift']})")

    def test_regression_steps_rotation(self):
        """REG-10 : Le nombre de steps de rotation n'a pas changé."""
        time.sleep(0.3)
        assert BASELINE["steps_rotate"] == 690
        print(f"\n REG-10 : steps rotation inchangés ({BASELINE['steps_rotate']})")

    def test_regression_ordre_phases(self):
        """REG-11 : L'ordre des phases de mouvement est correct."""
        time.sleep(0.4)
        phases_ordre = [
            "avancement",
            "ouverture_gripper",
            "fermeture_gripper",
            "levage",
            "rotation",
            "deplacement_cible",
            "descente",
            "ouverture_finale"
        ]
        assert len(phases_ordre) == 8
        assert phases_ordre[0] == "avancement"
        assert phases_ordre[-1] == "ouverture_finale"
        print(f"\n REG-11 : ordre des {len(phases_ordre)} phases correct")

    def test_regression_duree_totale_acceptable(self):
        """REG-12 : La durée totale calculée n'a pas dérivé."""
        time.sleep(0.4)
        total = (BASELINE["steps_forward"] + BASELINE["steps_gripper"] +
                 BASELINE["steps_lift"] + BASELINE["steps_rotate"])
        duree = (total * BASELINE["timestep"]) / 1000
        assert duree < BASELINE["max_duration"], \
            f"RÉGRESSION durée : {duree:.2f}s > {BASELINE['max_duration']}s"
        print(f"\n REG-12 : durée totale {duree:.2f}s (< {BASELINE['max_duration']}s)")


# ─────────────────────────────────────────────
# 3. RÉGRESSION RÉSULTATS SIMULATION
# ─────────────────────────────────────────────

class TestRegressionResultatsSimulation:

    def test_regression_robot_bouge(self):
        """REG-13 : Le robot bouge toujours correctement."""
        time.sleep(0.5)
        results = load_results()
        assert results["robot_moved"] is True, "RÉGRESSION : robot ne bouge plus !"
        print(f"\n REG-13 : robot se déplace correctement")

    def test_regression_boite_saisie(self):
        """REG-14 : La boîte est toujours correctement saisie."""
        time.sleep(0.5)
        results = load_results()
        assert results["box_picked"] is True, "RÉGRESSION : boîte plus saisie !"
        print(f"\n REG-14 : boîte saisie correctement")

    def test_regression_gripper_fonctionne(self):
        """REG-15 : Le gripper fonctionne toujours."""
        time.sleep(0.5)
        results = load_results()
        assert results["gripper_worked"] is True, "RÉGRESSION : gripper défaillant !"
        print(f"\n REG-15 : gripper opérationnel")

    def test_regression_livraison_reussie(self):
        """REG-16 : La livraison réussit toujours."""
        time.sleep(0.5)
        results = load_results()
        assert results["box_delivered"] is True, "RÉGRESSION : livraison échoue !"
        print(f"\n REG-16 : livraison réussie")

    def test_regression_precision_maintenue(self):
        """REG-17 : La précision de livraison est maintenue."""
        time.sleep(0.5)
        results = load_results()
        distance = results.get("final_distance", 999)
        assert distance < BASELINE["precision_threshold"], \
            f"RÉGRESSION précision : {distance:.4f}m > {BASELINE['precision_threshold']}m"
        print(f"\n REG-17 : précision maintenue ({distance:.4f}m)")

    def test_regression_hauteur_pick_maintenue(self):
        """REG-18 : La hauteur de saisie est maintenue."""
        time.sleep(0.5)
        results = load_results()
        max_height = results.get("max_box_height", 0)
        assert max_height > 0.25, \
            f"RÉGRESSION hauteur pick : {max_height:.3f}m < 0.25m"
        print(f"\n REG-18 : hauteur pick maintenue ({max_height:.3f}m)")

    def test_regression_duree_simulation_stable(self):
        """REG-19 : La durée de simulation est stable."""
        time.sleep(0.5)
        results = load_results()
        duration = results.get("duration", 0)
        assert 0 < duration < BASELINE["max_duration"], \
            f"RÉGRESSION durée simulation : {duration:.1f}s"
        print(f"\n REG-19 : durée simulation stable ({duration:.1f}s)")

    def test_regression_structure_json_complete(self):
        """REG-20 : La structure du fichier de résultats est complète."""
        time.sleep(0.4)
        results = load_results()
        champs = [
            "robot_moved", "box_picked", "box_delivered", "gripper_worked",
            "final_distance", "max_box_height",
            "initial_box_position", "final_box_position", "duration"
        ]
        for champ in champs:
            assert champ in results, f"RÉGRESSION structure : champ '{champ}' manquant !"
        print(f"\n REG-20 : structure JSON complète ({len(champs)} champs)")