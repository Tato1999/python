from turtle import Turtle
import random as r

class Food(Turtle):

    def __init__(self):
        super().__init__()
        rand_x = r.randint(-250,250)
        rand_y = r.randint(-250,250)
        self.penup()
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.speed(0)
        self.goto(rand_x,rand_y)
        self.color("blue")

    def refresh(self):
        rand_x = r.randint(-250,250)
        rand_y = r.randint(-250,250)
        self.goto(rand_x,rand_y)
        