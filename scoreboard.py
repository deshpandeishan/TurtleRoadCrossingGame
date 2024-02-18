import turtle
from turtle import Turtle
FONT = ("Courier", 30, "normal")


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

    def display_game_over(self):
        self.hideturtle()
        self.write("Game Over! 💀", align="center", font=FONT)
