"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

This module runs on your LAPTOP.
It uses MQTT to SEND information to a program running on the ROBOT.

Authors:  David Mutchler, his colleagues, and Hanyu Yang.
"""
# ------------------------------------------------------------------------------
# DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.  Then delete this TODO.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# TODO: 2. With your instructor, discuss the "big picture" of laptop-robot
# TODO:    communication:
# TODO:      - One program runs on your LAPTOP.  It displays a GUI.  When the
# TODO:        user presses a button intended to make something happen on the
# TODO:        ROBOT, the LAPTOP program sends a message to its MQTT client
# TODO:        indicating what it wants the ROBOT to do, and the MQTT client
# TODO:        SENDS that message TO a program running on the ROBOT.
# TODO:
# TODO:      - Another program runs on the ROBOT. It stays in a loop, responding
# TODO:        to events on the ROBOT (like pressing buttons on the IR Beacon).
# TODO:        It also, in the background, listens for messages TO the ROBOT
# TODO:        FROM the program running on the LAPTOP.  When it hears such a
# TODO:        message, it calls the method in the DELAGATE object's class
# TODO:        that the message indicates, sending arguments per the message.
# TODO:
# TODO:  Once you understand the "big picture", delete this TODO (if you wish).
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# TODO: 3. One team member: change the following in mqtt_remote_method_calls.py:
#                LEGO_NUMBER = 99
# TODO:    to use YOUR robot's number instead of 99.
# TODO:    Commit and push the change, then other team members Update Project.
# TODO:    Then delete this TODO.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# TODO: 4. Run this module.
# TODO:    Study its code until you understand how the GUI is set up.
# TODO:    Then delete this TODO.
# ------------------------------------------------------------------------------

import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com


def main():
    """ Constructs and runs a GUI for this program. """
    root = tkinter.Tk()

    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    setup_gui(root, mqtt_client)

    root.mainloop()
    # --------------------------------------------------------------------------
    # TODO: 5. Add code above that constructs a   com.MqttClient   that will
    # TODO:    be used to send commands to the robot.  Connect it to this pc.
    # TODO:    Test.  When OK, delete this TODO.
    # --------------------------------------------------------------------------


def setup_gui(root_window, mqtt_client):
    """ Constructs and sets up widgets on the given window. """
    frame = ttk.Frame(root_window, padding=10)
    frame.grid()

    tone_entry_box = ttk.Entry(frame)
    c_button = ttk.Button(frame, text="C")
    csh_button = ttk.Button(frame, text="C#")
    d_button = ttk.Button(frame, text="D")
    dsh_button = ttk.Button(frame, text="D#")
    e_button = ttk.Button(frame, text="E")
    f_button = ttk.Button(frame, text="F")
    fsh_button = ttk.Button(frame, text="F#")
    g_button = ttk.Button(frame, text="G")
    gsh_button = ttk.Button(frame, text="G#")
    a_button = ttk.Button(frame, text="A")
    ash_button = ttk.Button(frame, text="A#")
    b_button = ttk.Button(frame, text="B")

    tone_entry_box.grid()
    c_button.grid()
    csh_button.grid()
    d_button.grid()
    dsh_button.grid()
    e_button.grid()
    f_button.grid()
    fsh_button.grid()
    g_button.grid()
    gsh_button.grid()
    a_button.grid()
    ash_button.grid()
    b_button.grid()

    c_button['command'] = lambda: play_c(tone_entry_box, mqtt_client)
    csh_button['command'] = lambda: play_csh(tone_entry_box, mqtt_client)
    d_button['command'] = lambda: play_d(tone_entry_box, mqtt_client)
    dsh_button['command'] = lambda: play_dsh(tone_entry_box, mqtt_client)
    e_button['command'] = lambda: play_e(tone_entry_box, mqtt_client)
    f_button['command'] = lambda: play_f(tone_entry_box, mqtt_client)
    fsh_button['command'] = lambda: play_fsh(tone_entry_box, mqtt_client)
    g_button['command'] = lambda: play_g(tone_entry_box, mqtt_client)
    gsh_button['command'] = lambda: play_gsh(tone_entry_box, mqtt_client)
    a_button['command'] = lambda: play_a(tone_entry_box, mqtt_client)
    ash_button['command'] = lambda: play_ash(tone_entry_box, mqtt_client)
    b_button['command'] = lambda: play_b(tone_entry_box, mqtt_client)


def play_c(entry_box, mqtt_client):
    degree = int(entry_box.get())
    mqtt_client.send_message('tone_c', [degree])


def play_csh(entry_box, mqtt_client):
    degree = int(entry_box.get())
    mqtt_client.send_message('tone_csh', [degree])


def play_d(entry_box, mqtt_client):
    degree = int(entry_box.get())
    mqtt_client.send_message('tone_d', [degree])


def play_dsh(entry_box, mqtt_client):
    degree = int(entry_box.get())
    mqtt_client.send_message('tone_dsh', [degree])


def play_e(entry_box, mqtt_client):
    degree = int(entry_box.get())
    mqtt_client.send_message('tone_e', [degree])


def play_f(entry_box, mqtt_client):
    degree = int(entry_box.get())
    mqtt_client.send_message('tone_f', [degree])


def play_fsh(entry_box, mqtt_client):
    degree = int(entry_box.get())
    mqtt_client.send_message('tone_fsh', [degree])


def play_g(entry_box, mqtt_client):
    degree = int(entry_box.get())
    mqtt_client.send_message('tone_g', [degree])


def play_gsh(entry_box, mqtt_client):
    degree = int(entry_box.get())
    mqtt_client.send_message('tone_gsh', [degree])


def play_a(entry_box, mqtt_client):
    degree = int(entry_box.get())
    mqtt_client.send_message('tone_a', [degree])


def play_ash(entry_box, mqtt_client):
    degree = int(entry_box.get())
    mqtt_client.send_message('tone_ash', [degree])


def play_b(entry_box, mqtt_client):
    degree = int(entry_box.get())
    mqtt_client.send_message('tone_b', [degree])


main()
