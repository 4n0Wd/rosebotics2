"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import ev3dev.ev3 as ev3
import time
import math

def main():
    """ Runs YOUR specific part of the project """
    # gun_shots()
    # grab_things()
    follow_me()


def grab_things():
    robot = rb.Snatch3rRobot()
    robot.drive_system.go_straight_inches(5)
    robot.arm.move_arm_to_position(300)
    robot.drive_system.go_straight_inches(20)
    robot.arm.calibrate()


def gun_shots():
    for k in range(3):
        ev3.Sound.play('ak47-1.wav')
        time.sleep(1.3)
    ev3.Sound.play('ak47_clipout.wav')
    time.sleep(0.8)
    ev3.Sound.play('ak47_clipin.wav')


def follow_me():
    robot = rb.Snatch3rRobot()
    while True:
        print(robot.beacon_sensor.get_heading_and_distance_to_beacon())
        if robot.beacon_sensor.get_distance_to_beacon() > 20:
            if robot.beacon_sensor.get_heading_to_beacon() != 0:
                sign = abs(robot.beacon_sensor.get_heading_to_beacon())/robot.beacon_sensor.get_heading_to_beacon()
            else:
                sign = 0
            x = abs(robot.beacon_sensor.get_heading_to_beacon())
            y = robot.beacon_sensor.get_distance_to_beacon()
            if y != 0:
                angle = sign * math.atan(x/y)
            else:
                angle = 0
            robot.drive_system.go_straight_inches(5)
            robot.drive_system.spin_in_place_degrees(angle * 180 / 3.1415926)


main()
