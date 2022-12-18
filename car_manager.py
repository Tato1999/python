COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
RANDOM_NUM_FOR_CAR_COUNT = 5

from turtle import Turtle
import random

class CarManager():

    def __init__(self):
        self.all_car = []
        
        


    def create_car(self):
        if random.randint(0,RANDOM_NUM_FOR_CAR_COUNT) == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(1,2)
            new_car.color(COLORS[random.randint(0,len(COLORS)-1)])
            new_car.goto(300,random.randint(-300,300))
            self.all_car.append(new_car)

    def move(self):
        for car in self.all_car:
            car.backward(STARTING_MOVE_DISTANCE)

    def speed_up(self):
        global STARTING_MOVE_DISTANCE, RANDOM_NUM_FOR_CAR_COUNT
        RANDOM_NUM_FOR_CAR_COUNT = random.randint(0,5)
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
        
    