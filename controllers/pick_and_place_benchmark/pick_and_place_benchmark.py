"""Controller program to manage the benchmark."""
from controller import Supervisor
import math
import os
import json

robot = Supervisor()
timestep = int(robot.getBasicTimeStep())

targetNode = robot.getFromDef("TARGET")
targetPosition = targetNode.getPosition()
targetPosition[2] = 0.0350

boxNode = robot.getFromDef("PRODUCT")

results = {
    "robot_moved": False,
    "box_picked": False,
    "box_delivered": False,
    "gripper_worked": False,
    "final_distance": 999,
    "max_box_height": 0,
    "initial_box_position": None,
    "final_box_position": None,
    "duration": 0
}

initial_pos = boxNode.getPosition()
results["initial_box_position"] = list(initial_pos)

boxPicked = False
notMovingStepCount = 0
previousDistance = 999

# ─────────────────────────────────────────────
# Chemin de sortie du JSON
# ─────────────────────────────────────────────
if os.name == 'nt':  # Windows
    output_path = os.path.normpath(
        os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "../../reports/simulation_results.json")
    )
else:  # Linux / Docker
    output_path = os.path.normpath(
        os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "../../reports/simulation_results.json")
    )

os.makedirs(os.path.dirname(output_path), exist_ok=True)

def save_results():
    """Sauvegarder les résultats à tout moment."""
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)

# Sauvegarder le JSON dès le début (valeurs initiales)
save_results()
print(f"JSON initialisé : {output_path}")

# ─────────────────────────────────────────────
# Boucle principale de surveillance
# ─────────────────────────────────────────────
while robot.step(timestep) != -1:
    position = boxNode.getPosition()
    time = robot.getTime()

    # Mettre à jour la hauteur maximale
    if position[2] > results["max_box_height"]:
        results["max_box_height"] = position[2]

    # La boîte est suffisamment haute → saisie !
    if position[2] > 0.25:
        results["box_picked"] = True
        results["gripper_worked"] = True

    # Calculer la distance boîte → cible
    distance = round(math.sqrt(
        math.pow(targetPosition[0] - position[0], 2) +
        math.pow(targetPosition[1] - position[1], 2)
    ), 4)

    results["final_distance"] = distance
    results["final_box_position"] = list(position)
    results["duration"] = time

    # Vérifier si la boîte est livrée
    if boxPicked and distance < 0.036 and position[2] < 0.156:
        results["box_delivered"] = True
        if distance == previousDistance:
            notMovingStepCount += 1
            if notMovingStepCount > 10:
                # Sauvegarder et terminer
                save_results()
                break
        else:
            notMovingStepCount = 0
        previousDistance = distance
    elif not boxPicked and position[2] > 0.21:
        boxPicked = True

    # ── Sauvegarder le JSON toutes les 100 steps ──
    # Comme ça même si la simulation s'arrête brutalement,
    # le JSON existe toujours avec les dernières valeurs
    if int(time * 1000) % (100 * timestep) == 0:
        save_results()

# ─────────────────────────────────────────────
# Vérifier si le robot a bougé
# ─────────────────────────────────────────────
final_pos = boxNode.getPosition()
dist_moved = math.sqrt(
    math.pow(final_pos[0] - initial_pos[0], 2) +
    math.pow(final_pos[1] - initial_pos[1], 2)
)
results["robot_moved"] = dist_moved > 0.1

# Sauvegarde finale
save_results()
print("Results saved!")
print(f"   Robot bougé     : {results['robot_moved']}")
print(f"   Boîte saisie    : {results['box_picked']}")
print(f"   Boîte livrée    : {results['box_delivered']}")
print(f"   Distance finale : {results['final_distance']:.4f}m")
print(f"   Durée           : {results['duration']:.1f}s")

robot.simulationSetMode(Supervisor.SIMULATION_MODE_PAUSE)