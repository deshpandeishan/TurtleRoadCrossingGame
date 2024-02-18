from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.send_turtle()

    def send_turtle(self):
        self.goto(STARTING_POSITION)

    def move_turtle(self):
        self.fd(MOVE_DISTANCE)

    def finish_line(self):
        y_cor = self.ycor()
        if y_cor > FINISH_LINE_Y:
            print("Turtle has reached to the other side of the screen.")
            return True
        else:
            return False
