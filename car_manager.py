from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]  # Colors of the moving cars
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []

    def set_car(self):
        random_time = randint(1, 6)
        if random_time == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(choice(COLORS))
            x, y = 250, randint(-200, 200)
            new_car.goto(x, y)
            self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            car.bk(STARTING_MOVE_DISTANCE)
