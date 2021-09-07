from turtle import Turtle, Screen

ALIGNMENT = "center"
FONT = ("Courier", 45, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(0, 240)
        self.current_score_r = 0
        self.current_score_l = 0
        self.write(arg=f"{self.current_score_l}  {self.current_score_r}", move=False, align=ALIGNMENT, font=FONT)

    def r_score(self):
        self.clear()
        self.current_score_r += 1
        self.write(arg=f"{self.current_score_l}  {self.current_score_r}", move=False, align=ALIGNMENT, font=FONT)

    def l_score(self):
        self.clear()
        self.current_score_l += 1
        self.write(arg=f"{self.current_score_l}  {self.current_score_r}", move=False, align=ALIGNMENT, font=FONT)

