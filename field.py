from turtle import Turtle


class Field:

    def __init__(self):
        self.line_list = []
        self.make_field()

    def make_line(self, x, y):
        line = Turtle()
        line.speed("fastest")
        line.shape("square")
        line.penup()
        line.setheading(90)
        line.color("white")
        line.shapesize(stretch_wid=0.5, stretch_len=2)
        line.goto(x, y)
        self.line_list.append(line)

    def make_field(self):
        cor_x = 0
        cor_y = 280
        for i in range(12):
            self.make_line(cor_x, cor_y)
            cor_y -= 50
