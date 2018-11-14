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
from tkinter import *
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
    frame = ttk.Frame(root_window, padding=20)
    frame.grid()

    oct = IntVar()
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
    three = ttk.Radiobutton(frame, text='Octave: 3', variable=oct, value=3)
    four = ttk.Radiobutton(frame, text='Octave: 4', variable=oct, value=4)
    five = ttk.Radiobutton(frame, text='Octave: 5', variable=oct, value=5)
    six = ttk.Radiobutton(frame, text='Octave: 6', variable=oct, value=6)
    seven = ttk.Radiobutton(frame, text='Octave: 7', variable=oct, value=7)
    eight = ttk.Radiobutton(frame, text='Octave: 8', variable=oct, value=8)
    go_button = ttk.Button(frame, text="↑")
    back_button = ttk.Button(frame, text="↓")
    stop_button = ttk.Button(frame, text="-")

    three.grid(row=0, column=0, sticky=W)
    four.grid(row=0, column=1, sticky=W)
    five.grid(row=1, column=0, sticky=W)
    six.grid(row=1, column=1, sticky=W)
    seven.grid(row=2, column=0, sticky=W)
    eight.grid(row=2, column=1, sticky=W)
    c_button.grid(row=3)
    csh_button.grid(row=4)
    d_button.grid(row=5)
    dsh_button.grid(row=6)
    e_button.grid(row=7)
    f_button.grid(row=8)
    fsh_button.grid(row=9)
    g_button.grid(row=10)
    gsh_button.grid(row=11)
    a_button.grid(row=12)
    ash_button.grid(row=13)
    b_button.grid(row=14)
    go_button.grid(row=7, column=1)
    stop_button.grid(row=8, column=1)
    back_button.grid(row=9, column=1)

    c_button['command'] = lambda: play_c(oct, mqtt_client)
    csh_button['command'] = lambda: play_csh(oct, mqtt_client)
    d_button['command'] = lambda: play_d(oct, mqtt_client)
    dsh_button['command'] = lambda: play_dsh(oct, mqtt_client)
    e_button['command'] = lambda: play_e(oct, mqtt_client)
    f_button['command'] = lambda: play_f(oct, mqtt_client)
    fsh_button['command'] = lambda: play_fsh(oct, mqtt_client)
    g_button['command'] = lambda: play_g(oct, mqtt_client)
    gsh_button['command'] = lambda: play_gsh(oct, mqtt_client)
    a_button['command'] = lambda: play_a(oct, mqtt_client)
    ash_button['command'] = lambda: play_ash(oct, mqtt_client)
    b_button['command'] = lambda: play_b(oct, mqtt_client)
    go_button['command'] = lambda: go_forward(mqtt_client)


def play_c(oct, mqtt_client):
    octave = oct.get()
    mqtt_client.send_message('tone_c', [octave])


def play_csh(oct, mqtt_client):
    octave = oct.get()
    mqtt_client.send_message('tone_csh', [octave])


def play_d(oct, mqtt_client):
    octave = oct.get()
    mqtt_client.send_message('tone_d', [octave])


def play_dsh(oct, mqtt_client):
    octave = oct.get()
    mqtt_client.send_message('tone_dsh', [octave])


def play_e(oct, mqtt_client):
    octave = oct.get()
    mqtt_client.send_message('tone_e', [octave])


def play_f(oct, mqtt_client):
    octave = oct.get()
    mqtt_client.send_message('tone_f', [octave])


def play_fsh(oct, mqtt_client):
    octave = oct.get()
    mqtt_client.send_message('tone_fsh', [octave])


def play_g(oct, mqtt_client):
    octave = oct.get()
    mqtt_client.send_message('tone_g', [octave])


def play_gsh(oct, mqtt_client):
    octave = oct.get()
    mqtt_client.send_message('tone_gsh', [octave])


def play_a(oct, mqtt_client):
    octave = oct.get()
    mqtt_client.send_message('tone_a', [octave])


def play_ash(oct, mqtt_client):
    octave = oct.get()
    mqtt_client.send_message('tone_ash', [octave])


def play_b(oct, mqtt_client):
    octave = oct.get()
    mqtt_client.send_message('tone_b', [octave])


def go_forward(mqtt_client):
    mqtt_client.send_message('go_forward')


main()
