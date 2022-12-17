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

class ScorePong(Turtle):
    

    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0,210)
        
    def update(self):
        self.clear()
        self.write(f"{self.score1}               {self.score2}", align = 'center', font = ("arial",24))

    def score1_Up(self):
        global n
        self.score1 += 1
        self.update()
        if self.score1 >= 5:
            n = 1


    def score2_Up(self):
        global n
        self.score2 += 1
        self.update()
        if self.score2 >= 5:
            n = 2

        

   