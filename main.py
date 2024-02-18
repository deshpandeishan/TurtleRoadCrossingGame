import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

p_turtle = Player()
car = CarManager()

screen.listen()
screen.onkey(p_turtle.move_turtle, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.set_car()
    car.move_car()

    for vehicle in car.cars:
        if vehicle.distance(p_turtle) < 20:
            game_is_on = False

    if p_turtle.finish_line():
        p_turtle.send_turtle()
        car.increase_speed()

# screen.exitonclick()
