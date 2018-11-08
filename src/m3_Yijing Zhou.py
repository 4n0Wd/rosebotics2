"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    run_test_wait_color(rb.Color.RED.value)


def run_test_wait_color(color):
    robot = rb.Snatch3rRobot()

    print("Testing the color sensor.")
    print("The robot will stop until it detects", color)

    robot.drive_system.start_moving(50)
    robot.color_sensor.wait_until_color_is(color)
    robot.drive_system.stop_moving()

main()
