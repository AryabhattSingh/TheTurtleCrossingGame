from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-280, 260)
        self.level = 1
        self.hideturtle()
        self.write_level()

    def update_level(self):
        self.level += 1
        self.clear()
        self.write_level()

    def write_level(self):
        self.write(f"Level : {self.level}", align="left", font=FONT)

    def game_over(self):
        turtle_obj = Turtle()
        turtle_obj.penup()
        turtle_obj.goto(-60,0)
        turtle_obj.write("GAME OVER", font=FONT)
