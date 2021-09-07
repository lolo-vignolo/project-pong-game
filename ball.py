from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.speed(1)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1


    def movement(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bouncing(self): #2
        self.y_move *= -1

    def bar_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.bar_bounce()
