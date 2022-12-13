from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create_ball()
        self.y_move = 2
        self.x_move = 2
        self.x_cor = self.xcor()
        self.y_cor = self.ycor()



    def create_ball(self):
        self.shape("circle")
        self.penup()
        self.shapesize(1)
        self.color("black")
        self.setpos(random.randint(-250,250),random.randint(-250,250))
        #self.set_head()


    def set_head(self):
        x = self.xcor()
        y = self.ycor()

        if x > 0 and y > 0:
            self.setheading(225)
        elif x < 0 and y > 0:
            self.setheading(315)
        elif x > 0 and y < 0:
            self.setheading(135)
        elif x < 0 and y < 0:
            self.setheading(45)

    def move_ball(self):
        #self.forward(1)
        y = self.ycor() + self.y_move
        x = self.xcor() + self.x_move

        self.goto(x,y)


    def detect_wall(self):
        x = self.xcor()
        y = self.ycor()

        if y >= 230 or y <= -230:

            self.y_move *= -1
            # if self.heading() == 45:
            #     self.setheading(315)
            # elif self.heading() == 135:
            #     self.setheading(225)
            # elif self.heading() == 225:
            #     self.setheading(315)
            # elif self.heading() == 315:
            #     self.setheading(45)

    def ball_x(self):
        return self.xcor()

    def ball_y(self):
        return self.ycor()
