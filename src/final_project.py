"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import ev3dev.ev3 as ev3
import time


def main():
    """ Runs YOUR specific part of the project """
    # gun_shots()
    grab_things()


def grab_things():
    robot = rb.Snatch3rRobot()
    robot.drive_system.go_straight_inches(5)
    robot.arm.move_arm_to_position(300)
    robot.drive_system.go_straight_inches(20)


def gun_shots():
    for k in range(3):

        ev3.Sound.play('ak47-1.wav')
        time.sleep(1.3)

    ev3.Sound.play('ak47_clipout.wav')
    time.sleep(0.8)
    ev3.Sound.play('ak47_clipin.wav')

main()
