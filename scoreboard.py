from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.update()
        

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}", align = 'center', font = ("arial",24))
       

    def scoreUp(self):
        self.score+=1   
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align='center', font=('arial',24))