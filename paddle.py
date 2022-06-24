from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.speed(1.5)
        self.shape("square")
        self.penup()
        self.setheading(90)
        self.color("white")
        self.shapesize(stretch_wid=0.5, stretch_len=5)
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 20
        x = self.xcor()
        self.goto(x, new_y)

    def down(self):
        new_y = self.ycor() - 20
        x = self.xcor()
        self.goto(x, new_y)
