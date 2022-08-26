import turtle
import numpy as np
import time






class Dipole():
    """custom Turtle class to create dipoles """

    def __init__(self, x_cor = None, y_cor = None , wid_stretch = None, len_stretch = None, color = "black", state = 0, shape = "square" ):
        self.dipole = turtle.Turtle()
        self.shape = self.dipole.shape(shape)
        self.color = self.dipole.color(color)
        self.shapesize = self.dipole.shapesize(stretch_wid = wid_stretch , stretch_len = len_stretch)
        self.state = state
        self.dipole.penup()
        self.dipole.goto(x_cor, y_cor)


    def clear(self):
        self.dipole.clear()

    def xcor(self):
        return self.dipole.xcor()  

    def ycor(self):
        return self.dipole.ycor() 
    def set_color(self, state):
        if state == -1:
            self.dipole.color("white")
        elif state == 1:
            self.dipole.color("black")
        else:
            print("state must be either +1 or -1") 
