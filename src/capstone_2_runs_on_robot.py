"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and PUT_YOUR_NAME_HERE.
"""
# ------------------------------------------------------------------------------
# TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.  Then delete this TODO.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# TODO: 2. With your instructor, review the "big picture" of laptop-robot
# TODO:    communication, per the comment in mqtt_sender.py.
# TODO:    Once you understand the "big picture", delete this TODO.
# ------------------------------------------------------------------------------

import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3


def main():
    # --------------------------------------------------------------------------
    # TODO: 3. Construct a Snatch3rRobot.  Test.  When OK, delete this TODO.
    # --------------------------------------------------------------------------
    robot = rb.Snatch3rRobot()
    # --------------------------------------------------------------------------
    # TODO: 4. Add code that constructs a   com.MqttClient   that will
    # TODO:    be used to receive commands sent by the laptop.
    # TODO:    Connect it to this robot.  Test.  When OK, delete this TODO.
    # --------------------------------------------------------------------------
    rc = RemoteControlEtc(robot)
    mqtt_client = com.MqttClient(rc)
    mqtt_client.connect_to_pc()
    # --------------------------------------------------------------------------
    # TODO: 5. Add a class for your "delegate" object that will handle messages
    # TODO:    sent from the laptop.  Construct an instance of the class and
    # TODO:    pass it to the MqttClient constructor above.  Augment the class
    # TODO:    as needed for that, and also to handle the go_forward message.
    # TODO:    Test by PRINTING, then with robot.  When OK, delete this TODO.
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # TODO: 6. With your instructor, discuss why the following WHILE loop,
    # TODO:    that appears to do nothing, is necessary.
    # TODO:    When you understand this, delete this TODO.
    # --------------------------------------------------------------------------
    while True:
        # ----------------------------------------------------------------------
        # TODO: 7. Add code that makes the robot beep if the top-red button
        # TODO:    on the Beacon is pressed.  Add code that makes the robot
        # TODO:    speak "Hello. How are you?" if the top-blue button on the
        # TODO:    Beacon is pressed.  Test.  When done, delete this TODO.
        # ----------------------------------------------------------------------
        time.sleep(0.01)  # For the delegate to do its work


class RemoteControlEtc(object):
    def __init__(self, robot):
        """
        Stores the robot
            :type robot: rb.Snatch3rRobot
        """
        self.robot = robot

    def tone_c(self, degree):
        if degree == 0:
            ev3.Sound.speak('Please select an octave.')
        else:
            tone = 16.401 * (2.718 ** (0.6926 * degree))
            ev3.Sound.tone(tone, 200)

    def tone_csh(self, degree):
        if degree == 0:
            ev3.Sound.speak('Please select an octave.')
        else:
            tone = 17.406 * (2.718 ** (0.6922 * degree))
            ev3.Sound.tone(tone, 200)

    def tone_d(self, degree):
        if degree == 0:
            ev3.Sound.speak('Please select an octave.')
        else:
            tone = 18.403 * (2.718 ** (0.6926 * degree))
            ev3.Sound.tone(tone, 200)

    def tone_dsh(self, degree):
        if degree == 0:
            ev3.Sound.speak('Please select an octave.')
        else:
            tone = 19.445 * (2.718 ** (0.6926 * degree))
            ev3.Sound.tone(tone, 200)

    def tone_e(self, degree):
        if degree == 0:
            ev3.Sound.speak('Please select an octave.')
        else:
            tone = 20.602 * (2.718 ** (0.6926 * degree))
            ev3.Sound.tone(tone, 200)

    def tone_f(self, degree):
        if degree == 0:
            ev3.Sound.speak('Please select an octave.')
        else:
            tone = 21.827 * (2.718 ** (0.6926 * degree))
            ev3.Sound.tone(tone, 200)

    def tone_fsh(self, degree):
        if degree == 0:
            ev3.Sound.speak('Please select an octave.')
        else:
            tone = 23.125 * (2.718 ** (0.6926 * degree))
            ev3.Sound.tone(tone, 200)

    def tone_g(self, degree):
        if degree == 0:
            ev3.Sound.speak('Please select an octave.')
        else:
            tone = 24.500 * (2.718 ** (0.6926 * degree))
            ev3.Sound.tone(tone, 200)

    def tone_gsh(self, degree):
        if degree == 0:
            ev3.Sound.speak('Please select an octave.')
        else:
            tone = 25.957 * (2.718 ** (0.6926 * degree))
            ev3.Sound.tone(tone, 200)

    def tone_a(self, degree):
        if degree == 0:
            ev3.Sound.speak('Please select an octave.')
        else:
            tone = 27.500 * (2.718 ** (0.6926 * degree))
            ev3.Sound.tone(tone, 200)

    def tone_ash(self, degree):
        if degree == 0:
            ev3.Sound.speak('Please select an octave.')
        else:
            tone = 29.135 * (2.718 ** (0.6926 * degree))
            ev3.Sound.tone(tone, 200)

    def tone_b(self, degree):
        if degree == 0:
            ev3.Sound.speak('Please select an octave.')
        else:
            tone = 30.895 * (2.718 ** (0.6926 * degree))
            ev3.Sound.tone(tone, 200)

main()