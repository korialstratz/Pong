from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 20
        self.y_move = 30
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def service(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def refresh_ball(self):
        self.move_speed = 0.1
        self.x_move *= -1
        self.goto(0, 0)
