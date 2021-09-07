from turtle import Turtle


class Bars(Turtle): #1
    def __init__(self, position, len, wid):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=len, stretch_wid=wid)
        self.penup()
        self.goto(position)


    def up(self): #2
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self): #2
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)








