"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    # run_test_wait_color(rb.Color.RED.value)
    run_test_moving_loop()


def run_test_wait_color(color):
    robot = rb.Snatch3rRobot()

    print("Testing the color sensor.")
    print("The robot will stop until it detects", color)

    robot.drive_system.start_moving(50, 50)
    robot.color_sensor.wait_until_color_is(color)
    robot.drive_system.stop_moving()


def run_test_moving_loop():
    robot = rb.Snatch3rRobot()

    print("Testing the  color_sensor  of the robot.")
    print("Repeatedly move the robot to different surfaces.")
    print("Press Control-C when you are ready to stop testing.")

    while True:
        robot.drive_system.start_moving(50, 50)
        if robot.color_sensor.get_color() != rb.Color.BLACK.value:
            robot.drive_system.turn_degrees(-3)

main()
