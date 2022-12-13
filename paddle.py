from turtle import Turtle,Screen




class Paddle(Turtle):

    def __init__(self,Position):
        super().__init__()

        self.cord = Position
        self.create_Paddle()



    def create_Paddle(self):
        
        self.penup()
        self.shape("square")
        self.shapesize(5,1)
        self.goto(self.cord)
        print(self.position)

    def moveUpFirst(self):
        if self.xcor() == -325:
            x = self.xcor()
            y = self.ycor() + 15

            self.goto(x,y)

    def moveDownFirst(self):
        if self.xcor() == -325:
            x = self.xcor()
            y = self.ycor() - 15

            self.goto(x,y)

    def moveUpSecond(self):
        if self.xcor() == 325:
            x = self.xcor()
            y = self.ycor() + 15

            self.goto(x,y)

    def moveDownSecond(self):
        if self.xcor() == 325:
            x = self.xcor()
            y = self.ycor() - 15

            self.goto(x,y)
            
    def paddle_x(self):
        return self.xcor()

    def paddle_y(self):
        return self.ycor()