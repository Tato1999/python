STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.create_player()


    def create_player(self):
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def is_finish_true(self):
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(0,-280)
            return True
        else:
            return False
    
