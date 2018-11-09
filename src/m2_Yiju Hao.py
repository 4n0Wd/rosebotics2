"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import ev3dev.ev3 as ev3
import time


def main():
    """ Runs YOUR specific part of the project """

    # run_test_touch_sensor()
    # run_test_touch_sensor_10()
    # run_test_beacon_sensor()
    run_test_arm_and_claw()


def run_test_touch_sensor():

    robot = rb.Snatch3rRobot()

    print()
    time.sleep(1)
    count = 1
    while True:
        print(count, ".Touch sensor value is: ", robot.touch_sensor.get_value())
        time.sleep(0.5)
        count = count + 1


# def run_test_touch_sensor_10():

#    robot = rb.Snatch3rRobot()

#    print()
#    print("Testing the  touch_sensor  of the robot.")
#    print("Repeatedly press and release the touch sensor.")
#    print("Press Control-C when you are ready to stop testing.")
#   time.sleep(1)
#    count = 0
#   while True:
#       print("{:4}.".format(count),
#           "times ", count)
#
#       n = robot.touch_sensor.get_value()
#       time.sleep(0.5)
#        if n - run_test_touch_sensor() == 1:
#           count = count + 1
#        if count == 10:
#           break


def run_test_beacon_sensor():
    robot = rb.Snatch3rRobot()
    while True:

        if robot.beacon_button_sensor.is_top_red_button_pressed():
            robot.drive_system.go_straight_inches(10)
        if robot.beacon_button_sensor.is_bottom_red_button_pressed():
            robot.drive_system.go_straight_inches(-10)

        time.sleep(0.01)


def run_test_arm_and_claw():
    robot = rb.Snatch3rRobot()
    robot.arm.raise_arm_and_close_claw()
    robot.arm.move_arm_to_position(200)
    time.sleep(1)
    robot.arm.move_arm_to_position(350)
    time.sleep(1)
    robot.arm.move_arm_to_position(0)


main()
