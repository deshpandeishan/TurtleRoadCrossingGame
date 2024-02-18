import turtle
from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.display_level()

    def display_level(self):
        turtle.clear()
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(-280, 250)
        turtle.write(f"Level: {self.level}", font=FONT)

    def increase_level(self):
        self.level += 1
        self.display_level()
