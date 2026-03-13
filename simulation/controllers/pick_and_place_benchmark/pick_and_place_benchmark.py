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

# Données à collecter
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

while robot.step(timestep) != -1:
    position = boxNode.getPosition()
    time = robot.getTime()

    if position[2] > results["max_box_height"]:
        results["max_box_height"] = position[2]

    if position[2] > 0.25:
        results["box_picked"] = True
        results["gripper_worked"] = True

    distance = round(math.sqrt(
        math.pow(targetPosition[0] - position[0], 2) +
        math.pow(targetPosition[1] - position[1], 2)
    ), 4)

    results["final_distance"] = distance
    results["final_box_position"] = list(position)
    results["duration"] = time

    if boxPicked and distance < 0.036 and position[2] < 0.156:
        results["box_delivered"] = True
        if distance == previousDistance:
            notMovingStepCount += 1
            if notMovingStepCount > 10:
                break
        else:
            notMovingStepCount = 0
        previousDistance = distance
    elif not boxPicked and position[2] > 0.21:
        boxPicked = True

# Vérifier si le robot a bougé
final_pos = boxNode.getPosition()
dist_moved = math.sqrt(
    math.pow(final_pos[0] - initial_pos[0], 2) +
    math.pow(final_pos[1] - initial_pos[1], 2)
)
results["robot_moved"] = dist_moved > 0.1

# Sauvegarder JSON
output_path = r"C:\Users\User\pfe-simulation\reports\simulation_results.json"

with open(output_path, 'w') as f:
    json.dump(results, f, indent=2)

print(f"✅ Résultats sauvegardés !")
print(f"   Robot bougé     : {results['robot_moved']}")
print(f"   Boîte saisie    : {results['box_picked']}")
print(f"   Boîte livrée    : {results['box_delivered']}")
print(f"   Distance finale : {results['final_distance']:.4f}m")

robot.simulationSetMode(Supervisor.SIMULATION_MODE_PAUSE)