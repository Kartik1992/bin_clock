#!/usr/bin/env python
import tkinter as tk
from tkinter import *
from clock import *
import time

# setting the default parameters
WIDTH = 300
HEIGHT = 300
bg_color = "black"
fg_color = "white"

# creating a widget (container)

widget = Tk()
widget.geometry('300x300+1000+50')
widget.config(bg=bg_color)
widget.overrideredirect(True)
widget.attributes('-alpha', 0.4)
widget._offset_x = 0
widget._offset_y = 0

# creating Close button
widget.close = tk.Button(widget, text='x', width=2, height=2, borderwidth=0,
                         bg=bg_color, fg=bg_color, border=0, command=lambda: widget.destroy())
widget.close.pack(anchor="ne")


def close_active():
    widget.close.config(bg=bg_color, fg=fg_color)


def close_inactive():
    widget.close.config(bg=bg_color, fg=bg_color)


widget.close.bind('<Enter>', close_active)
widget.close.bind('<Leave>', close_inactive)

# creating canvas

canvas = Canvas(widget, width=WIDTH, height=HEIGHT, bg=bg_color)
canvas.pack()

# creating a default list for objects locations

dot_list = [[x, y] for x in range(30, WIDTH - 30, 40) for y in range(50, HEIGHT - 100, 40)]


# converting current time in BCD and
def bcd_time():
    c_time = list((char for char in (time.strftime('%H%M%S'))))
    converted_list = []
    for number in c_time:
        octate = ("{0:04b}".format(int(number)))
        for x in octate:
            converted_list.append(int(x))
    return converted_list


# passing the canvas to the clock class by creating its objects(instances)
while True:
    bcd_list = bcd_time()
    final_list= [a+[x] for a, x in zip(dot_list, bcd_list)]
    for data in final_list:
        clock_dot = clock(canvas, data)
    widget.update()
    time.sleep(1)
