from turtle import Screen
from bars import Bars
from ball import Ball
import time
from score import Score


window = Screen()
window.setup(width=800, height=600)
window.bgcolor("black")
window.title("PONG")
window.tracer(0)

r_bar = Bars((350, 0), 1, 5)
l_bar = Bars((-350, 0), 1, 5)
middle_bar = Bars((0,0), 0.1, 30)

ball = Ball()
score = Score()


window.listen()
window.onkey(key="Up", fun=r_bar.up)
window.onkey(key="Down", fun=r_bar.down)
window.onkey(key="w", fun=l_bar.up)
window.onkey(key="s", fun=l_bar.down)


game_is_on = True
while game_is_on:
    window.update()
    time.sleep(ball.move_speed)
    ball.movement()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bouncing()

    if ball.distance(r_bar) < 40 and ball.xcor() > 330 \
            or l_bar.distance(ball) < 40 and ball.xcor() < -330:
        ball.bar_bounce()

    if ball.xcor() == -400:
        score.r_score()
        ball.reset_position()

    if ball.xcor() == 400:
        score.l_score()
        ball.reset_position()


window.exitonclick()
