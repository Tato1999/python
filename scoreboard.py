from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("snake_high_score.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.update()
        

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}", align = 'right', font = ("arial",15))
        self.penup()
        self.check_hight_score()
       

    def scoreUp(self):
        self.score+=1   
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align='center', font=('arial',24))

    def check_hight_score(self):
            self.write(f"High Score: {self.high_score}", align = 'left', font = ("arial",15))

            if self.high_score < self.score:
                high = open("snake_high_score.txt", mode='w')
                high.write(str(self.score))
                high.close()
                self.clear()
                self.write(f"High Score: {self.high_score}", align = 'left', font = ("arial",15))

    def reset_point(self):
        self.score = 0

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

        
FONT = ("Courier", 24, "normal")

lvl = Turtle()

class ScoreCar():
    def __init__(self):
        self.level = 0

    def create_level(self):
        global lvl
        lvl.penup()
        lvl.goto(-285,270)
        lvl.write(f"{self.level}",move=True, align = "left", font = ("arial",24))
        lvl.hideturtle()
    
    def level_up_counter(self):
        self.level += 1

    def clear_old(self):
        global lvl
        lvl.clear()

    def game_over(self):
        over = Turtle()
        over.hideturtle()
        over.write(f"Game Over", align = "center", font = ("arial",30))
