#!/usr/bin/env python
from tkinter import *
from clock import *
import time

# creating a widget (container)
widget = Tk()

# setting the default parameters
WIDTH = 300
HEIGHT = 300
# creating a default list for objects locations
dot_list = [[x, y] for x in range(30, WIDTH - 30, 40) for y in range(50, HEIGHT - 100, 40)]
# creating canvas
canvas = Canvas(widget, width=WIDTH, height=HEIGHT)
canvas.pack()
# passing the canvas to the clock class by creating its objects(instances)
for data in dot_list:
    clock_dot = clock(canvas, data)

widget.mainloop()
