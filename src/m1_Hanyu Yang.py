"""
  Capstone Project.  Code written by Hanyu Yang.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    run_tests()


def run_tests():
    run_test_drive_polygon(10, 4)
    # run_test_color()


def run_test_drive_polygon(side, number_of_sides):
    robot = rb.Snatch3rRobot()

    print()
    print("Testing the  drive_system  of the robot.")
    print("The robot is drawing a polygon.")

    for k in range(number_of_sides):
        robot.drive_system.go_straight_inches(side, 50)
        time.sleep(1)
        robot.drive_system.turn_degrees(((number_of_sides-2) * 180) / number_of_sides)
        time.sleep(1)


def run_test_color():
    robot = rb.Snatch3rRobot()

    print("Testing the  color_sensor  of the robot.")
    print("Repeatedly move the robot to different surfaces.")
    print("Press Control-C when you are ready to stop testing.")

    time.sleep(1)
    while True:
        robot.drive_system.start_moving(20, 20)
        if robot.color_sensor.get_color() != rb.Color.BLACK.value:
            robot.drive_system.turn_degrees(3, 50)


main()
