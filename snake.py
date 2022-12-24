from turtle import Turtle

LENGHT = 3
POSITION = [(0,0),(20,0),(30,0)]
class Snake:

    def __init__(self):
        self.count = []
        self.create_snake()
        self.head = self.count[0]
        


    def create_snake(self):
        '''Function To create snake'''
        for i in POSITION:
            self.add(i)

    def add(self, position):
        obj = Turtle()
        obj.penup()
        obj.shape('square')
        obj.color('white')
        obj.setposition(position)
        self.count.append(obj)

    def extend(self):
        self.add(self.count[-1].position())

    def move(self):
        '''Function To move Snake'''
        for i in range(len(self.count)-1,0,-1):
        
            x = self.count[i-1].xcor()
            y = self.count[i-1].ycor()
            self.count[i].goto(x,y)
        self.count[0].forward(10)

    def up(self):
        '''Function To turn Up'''
        if self.head.heading() != 270.0:
            self.count[0].setheading(90)
    
    def right(self):
        '''Function To turn Right'''
        if self.head.heading() != 180.0:
            self.count[0].setheading(0)
    
    def down(self):
        '''Function To turn down'''
        if self.head.heading() != 90.0:
            self.count[0].setheading(270)
    
    def left(self):
        '''Function To turn left'''
        if self.head.heading() != 0.0:
            self.count[0].setheading(180)

    def reset(self):
        for i in self.count:
            i.setpos(1000,1000)
        self.count.clear()
        self.create_snake()
        self.head = self.count[0]
    
