"""
  Capstone Project.  Code written by Hanyu Yang.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import ev3dev.ev3 as ev3
import time


def main():
    """ Runs YOUR specific part of the project """
    run_tests()


def run_tests():
    # run_test_drive_system(20)
    # run_test_turning(90)
    # run_test_wait_color(rb.Color.RED.value)
    # run_test_moving_loop()
    # run_test_drive_polygon(9, 5)
    # run_test_arm_and_claw()
    run_test_infrared_sensor()
    # run_test_sounds()
    # run_test_camera()
    # run_test_beacon_sensor()


def run_test_drive_system(inches):
    print('test')
    robot = rb.Snatch3rRobot()
    print('test2')
    robot.drive_system.go_straight_inches(inches)
    time.sleep(1)
    print('test3')
    robot.drive_system.go_straight_inches(-inches)


def run_test_turning(angle):
    robot = rb.Snatch3rRobot()

    print("Testing the spinning methods.")
    print("The robot is turning.")

    robot.drive_system.spin_in_place_degrees(angle)
    time.sleep(1)
    robot.drive_system.spin_in_place_degrees(-angle)
    time.sleep(1)
    robot.drive_system.turn_degrees(angle)
    time.sleep(1)
    robot.drive_system.turn_degrees(-angle)


def run_test_drive_polygon(side, number_of_sides):
    robot = rb.Snatch3rRobot()

    print()
    print("Testing the  drive_system  of the robot.")
    print("The robot is drawing a polygon.")

    for k in range(number_of_sides):
        robot.drive_system.go_straight_inches(side, 50)
        time.sleep(0.3)
        robot.drive_system.spin_in_place_degrees(180-(((number_of_sides-2) * 180) / number_of_sides))
        time.sleep(0.3)


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
        robot.drive_system.start_moving(20, 20)
        print(robot.color_sensor.get_color())
        if robot.color_sensor.get_color() != rb.Color.BLACK.value:
            robot.drive_system.turn_degrees(-5)


def run_test_sounds():
    ev3.Sound.tone(440, 500)
    time.sleep(0.5)
    ev3.Sound.tone(500, 500)
    time.sleep(0.5)
    ev3.Sound.tone(560, 500)


'''def run_test_camera():
    robot = rb.Snatch3rRobot()
    print(robot.camera.get_biggest_blob())'''


def run_test_arm_and_claw():
    robot = rb.Snatch3rRobot()
    robot.arm.raise_arm_and_close_claw()
    robot.arm.move_arm_to_position(200)
    time.sleep(1)
    robot.arm.move_arm_to_position(350)
    time.sleep(1)
    robot.arm.move_arm_to_position(0)


def run_test_infrared_sensor():
    robot = rb.Snatch3rRobot()
    while True:
        if 15 < robot.proximity_sensor.get_distance_to_nearest_object_in_inches() < 50:
            run_test_sounds()
        elif robot.proximity_sensor.get_distance_to_nearest_object_in_inches() < 15:
            break


def run_test_beacon_sensor():
    robot = rb.Snatch3rRobot()
    while True:
        if robot.beacon_button_sensor.is_top_red_button_pressed():
            robot.drive_system.go_straight_inches(10)
        if robot.beacon_button_sensor.is_bottom_red_button_pressed():
            robot.drive_system.go_straight_inches(-10)
        if robot.beacon_button_sensor.is_top_blue_button_pressed():
            robot.drive_system.stop_moving()
            break
        time.sleep(0.01)



main()
