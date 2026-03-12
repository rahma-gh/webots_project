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

final_pos = boxNode.getPosition()
dist_moved = math.sqrt(
    math.pow(final_pos[0] - initial_pos[0], 2) +
    math.pow(final_pos[1] - initial_pos[1], 2)
)
results["robot_moved"] = dist_moved > 0.1

if os.name == 'nt':  # Windows
    output_path = r"C:\Users\User\pfe-simulation\reports\simulation_results.json"
else:  # Linux / Docker
    output_path = os.path.normpath(
        os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "../../../reports/simulation_results.json")
    )
with open(output_path, "w") as f:
    import json as json2
    json2.dump(results, f, indent=2)

print("Results saved!")
robot.simulationSetMode(Supervisor.SIMULATION_MODE_PAUSE)
