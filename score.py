from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 18, 'normal')


class ScoreBoard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_wid=3)
        self.goto(position)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score : {self.score}", align=ALIGNMENT, move=False, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.write("GAME OVER", align=ALIGNMENT, move=False, font=FONT)

# class ScoreBoard(Turtle):
#
#     def __init__(self):
#         super().__init__()
#         self.penup()
#         self.hideturtle()
#         self.color("white")
#         self.speed("fastest")
#         self.shapesize(stretch_wid=3)
#         self.c_score = 0
#         self.u_score = 0
#         self.c_update_scoreboard()
#         self.u_update_scoreboard()
#
#     def c_update_scoreboard(self):
#         self.goto(-110, 260)
#         self.write(f"Score : {self.c_score}", align=ALIGNMENT, move=False, font=FONT)
#
#     def c_increase_score(self):
#         self.clear()
#         self.c_score += 1
#         self.c_update_scoreboard()
#
#     def u_update_scoreboard(self):
#         self.goto(100, 260)
#         self.write(f"Score : {self.u_score}", align=ALIGNMENT, move=False, font=FONT)
#
#     def u_increase_score(self):
#         self.clear()
#         self.u_score += 1
#         self.u_update_scoreboard()
#
#     def game_over(self):
#         self.goto(0, 0)
#         self.write("GAME OVER", align=ALIGNMENT, move=False, font=FONT)
