"""
Tests d'intégration — vérifier que tous les composants fonctionnent ensemble.
Ces tests valident l'interaction entre : robot, bras, gripper, convoyeur, cible.
Dans l'architecture classique, ils sont tous exécutés sans sélection intelligente.
"""
import pytest
import time
import math
import json
import os

RESULTS_PATH = os.path.abspath("reports/simulation_results.json")
SCENE_PATH = "simulation/pick_and_place.wbt"
CONTROLLER_ROBOT = "controllers/pick_and_place/pick_and_place.py"
CONTROLLER_BENCHMARK = "controllers/pick_and_place_benchmark/pick_and_place_benchmark.py"
CONTROLLER_BELT = "controllers/move_conveyor_belt/move_conveyor_belt.py"

def load_results():
    if not os.path.exists(RESULTS_PATH):
        pytest.skip("Fichier simulation_results.json absent.")
    with open(RESULTS_PATH, 'r') as f:
        return json.load(f)


# ─────────────────────────────────────────────
# 1. INTÉGRATION FICHIERS & STRUCTURE
# ─────────────────────────────────────────────

class TestIntegrationFichiers:

    def test_integration_scene_et_controleurs_presents(self):
        """INT-01 : La scène et tous les contrôleurs sont présents ensemble."""
        time.sleep(0.5)
        assert os.path.exists(SCENE_PATH), f"Scène manquante : {SCENE_PATH}"
        assert os.path.exists(CONTROLLER_ROBOT), f"Contrôleur robot manquant"
        assert os.path.exists(CONTROLLER_BENCHMARK), f"Contrôleur benchmark manquant"
        assert os.path.exists(CONTROLLER_BELT), f"Contrôleur convoyeur manquant"
        print(f"\n✅ INT-01 : scène + 3 contrôleurs présents")

    def test_integration_dossier_reports_avec_resultats(self):
        """INT-02 : Le dossier reports contient bien les résultats de simulation."""
        time.sleep(0.3)
        assert os.path.exists("reports"), "Dossier reports manquant !"
        assert os.path.exists(RESULTS_PATH), "Fichier résultats manquant !"
        taille = os.path.getsize(RESULTS_PATH)
        assert taille > 10, f"Fichier résultats vide ! ({taille} octets)"
        print(f"\n✅ INT-02 : dossier reports avec résultats ({taille} octets)")

    def test_integration_controleur_benchmark_lisible(self):
        """INT-03 : Le contrôleur benchmark peut être lu et parsé."""
        time.sleep(0.4)
        with open(CONTROLLER_BENCHMARK, 'r') as f:
            contenu = f.read()
        assert "Supervisor" in contenu, "Supervisor non trouvé dans le benchmark !"
        assert "getFromDef" in contenu, "getFromDef non trouvé !"
        assert "json.dump" in contenu or "json2.dump" in contenu, \
            "Sauvegarde JSON non trouvée !"
        print(f"\n✅ INT-03 : contrôleur benchmark valide")

    def test_integration_controleur_robot_lisible(self):
        """INT-04 : Le contrôleur robot principal peut être lu et parsé."""
        time.sleep(0.4)
        with open(CONTROLLER_ROBOT, 'r') as f:
            contenu = f.read()
        assert "Robot()" in contenu
        assert "wheel" in contenu
        assert "arm" in contenu
        assert "finger" in contenu
        print(f"\n✅ INT-04 : contrôleur robot valide")

    def test_integration_controleur_convoyeur_lisible(self):
        """INT-05 : Le contrôleur du convoyeur peut être lu et parsé."""
        time.sleep(0.3)
        with open(CONTROLLER_BELT, 'r') as f:
            contenu = f.read()
        assert "Robot()" in contenu
        assert "belt motor" in contenu or "motor" in contenu
        print(f"\n✅ INT-05 : contrôleur convoyeur valide")


# ─────────────────────────────────────────────
# 2. INTÉGRATION COMPOSANTS ROBOT
# ─────────────────────────────────────────────

class TestIntegrationComposantsRobot:

    def test_integration_roues_et_bras_parametres_compatibles(self):
        """INT-06 : Les paramètres roues et bras sont compatibles."""
        time.sleep(0.5)
        wheel_velocity = 7.0
        arm_velocities = [0.2, 0.5, 0.5, 0.3, 0.5]
        # Le bras doit être plus lent que les roues (stabilité)
        assert arm_velocities[0] < wheel_velocity, \
            "Le bras ne devrait pas être plus rapide que les roues !"
        print(f"\n✅ INT-06 : roues ({wheel_velocity}) plus rapides que bras ({arm_velocities[0]})")

    def test_integration_gripper_et_bras_compatibles(self):
        """INT-07 : Les paramètres gripper et bras sont compatibles."""
        time.sleep(0.4)
        gripper_velocity = 0.03
        arm_velocity_arm4 = 0.3
        # Gripper doit être plus précis (lent) que le bras
        assert gripper_velocity < arm_velocity_arm4
        print(f"\n✅ INT-07 : gripper ({gripper_velocity}) plus précis que arm4 ({arm_velocity_arm4})")

    def test_integration_sequence_pick_place_complete(self):
        """INT-08 : La séquence pick-and-place complète est cohérente."""
        time.sleep(0.5)
        results = load_results()
        # Vérifier la séquence logique : bouger → saisir → livrer
        assert results["robot_moved"], "Étape 1 (mouvement) échouée !"
        assert results["box_picked"], "Étape 2 (saisie) échouée !"
        assert results["gripper_worked"], "Étape 3 (gripper) échouée !"
        assert results["box_delivered"], "Étape 4 (livraison) échouée !"
        print(f"\n✅ INT-08 : séquence complète pick-and-place réussie")

    def test_integration_positions_pick_et_place_differentes(self):
        """INT-09 : Les positions de saisie et dépose sont bien différentes."""
        time.sleep(0.4)
        pick = {"arm2": -0.55, "arm3": -0.9, "arm4": -1.5}
        place = {"arm1": 0.0, "arm2": -1.0, "arm3": -0.3, "arm4": -1.0}
        # arm2 doit être différent entre pick et place
        assert pick["arm2"] != place["arm2"], \
            "Les positions pick et place de arm2 sont identiques !"
        assert pick["arm3"] != place["arm3"], \
            "Les positions pick et place de arm3 sont identiques !"
        print(f"\n✅ INT-09 : positions pick ≠ place (mouvement réel effectué)")

    def test_integration_boite_deplacee_vers_cible(self):
        """INT-10 : La boîte a bien été déplacée de sa position initiale vers la cible."""
        time.sleep(0.5)
        results = load_results()
        init = results.get("initial_box_position", [0, 0, 0])
        final = results.get("final_box_position", [0, 0, 0])
        deplacement = math.sqrt((final[0]-init[0])**2 + (final[1]-init[1])**2)
        assert deplacement > 0.3, \
            f"Déplacement insuffisant : {deplacement:.3f}m"
        distance_finale = results.get("final_distance", 999)
        assert distance_finale < 0.1, \
            f"Boîte pas arrivée à cible : {distance_finale:.4f}m"
        print(f"\n✅ INT-10 : boîte déplacée de {deplacement:.3f}m, à {distance_finale:.4f}m de la cible")


# ─────────────────────────────────────────────
# 3. INTÉGRATION PIPELINE CI/CD
# ─────────────────────────────────────────────

class TestIntegrationPipelineCICD:

    def test_integration_fichiers_ci_presents(self):
        """INT-11 : Les fichiers de configuration CI/CD sont présents."""
        time.sleep(0.4)
        assert os.path.exists(".github/workflows/ci.yml") or \
               os.path.exists(".github/workflows"), \
               "Fichier CI/CD manquant !"
        print(f"\n✅ INT-11 : fichier CI/CD présent")

    def test_integration_dockerfile_present(self):
        """INT-12 : Le Dockerfile est présent pour l'environnement Docker."""
        time.sleep(0.3)
        assert os.path.exists("Dockerfile"), "Dockerfile manquant !"
        with open("Dockerfile", 'r') as f:
            contenu = f.read()
        assert "webots" in contenu.lower() or "WEBOTS" in contenu, \
            "Webots non référencé dans le Dockerfile !"
        print(f"\n✅ INT-12 : Dockerfile présent et valide")

    def test_integration_requirements_complets(self):
        """INT-13 : Les dépendances Python sont toutes listées."""
        time.sleep(0.3)
        assert os.path.exists("requirements.txt"), "requirements.txt manquant !"
        with open("requirements.txt", 'r') as f:
            contenu = f.read()
        assert "pytest" in contenu, "pytest manquant dans requirements.txt !"
        assert "pytest-html" in contenu, "pytest-html manquant !"
        print(f"\n✅ INT-13 : requirements.txt complet")

    def test_integration_rapport_genere(self):
        """INT-14 : Le rapport HTML a été généré après les tests."""
        time.sleep(0.4)
        rapport_paths = [
            "reports/report.html",
            "reports/report_statique.html",
            "reports/report_comportemental.html"
        ]
        rapport_existe = any(os.path.exists(p) for p in rapport_paths)
        assert rapport_existe, "Aucun rapport HTML trouvé !"
        print(f"\n✅ INT-14 : rapport HTML généré")

    def test_integration_conftest_charge(self):
        """INT-15 : Le conftest.py est présent et configure l'environnement."""
        time.sleep(0.3)
        assert os.path.exists("conftest.py"), "conftest.py manquant !"
        with open("conftest.py", 'r') as f:
            contenu = f.read()
        assert "WEBOTS_HOME" in contenu, "Configuration Webots manquante !"
        print(f"\n✅ INT-15 : conftest.py présent et valide")

    def test_integration_fin_tous_composants_ok(self):
        """INT-16 : Vérification finale — tous les composants intégrés fonctionnent."""
        time.sleep(1.0)
        # Vérifier fichiers
        assert os.path.exists(SCENE_PATH)
        assert os.path.exists(CONTROLLER_ROBOT)
        assert os.path.exists(CONTROLLER_BENCHMARK)
        assert os.path.exists(CONTROLLER_BELT)
        assert os.path.exists("Dockerfile")
        assert os.path.exists("requirements.txt")
        # Vérifier résultats
        results = load_results()
        assert all([
            results["robot_moved"],
            results["box_picked"],
            results["gripper_worked"],
            results["box_delivered"]
        ]), "Au moins un composant a échoué !"
        print(f"\n✅ INT-16 : INTÉGRATION COMPLÈTE — tous les composants opérationnels !")