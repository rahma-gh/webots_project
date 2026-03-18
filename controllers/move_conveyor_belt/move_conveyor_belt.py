"""Move the conveyor belt until the cube reaches the desired position."""

from controller import Robot

robot = Robot()

motor = robot.getDevice("belt motor")
motor.setVelocity(0.9)#0.2
motor.setPosition(0.75)
