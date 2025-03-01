from turtle import Screen
from create_paddle import paddle
from ball import Ball
from scoreboard import score
import time


screen=Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_pos=(380,0)
l_pos=(-380,0)
r_paddle=paddle(r_pos)
l_paddle=paddle(l_pos)
game_ball=Ball()
game_score=score()

screen.listen()
screen.onkeypress(key="Up", fun=r_paddle.goup)
screen.onkeypress(key="Down", fun=r_paddle.godown)
screen.onkeypress(key="a", fun=l_paddle.lgoup)
screen.onkeypress(key="z", fun=l_paddle.lgodown)

game_is_on=True
while game_is_on:
    time.sleep(game_ball.move_speed)
    screen.update()
    game_ball.move()

    # detect collision with walls
    if game_ball.ycor()>=280 or game_ball.ycor()<=-280:
        game_ball.bounce_y()
    
    # detect collision with paddle
    if game_ball.distance(r_paddle)<50 and game_ball.xcor()>340 or game_ball.distance(l_paddle)<50 and game_ball.xcor()<-340:
        game_ball.bounce_x()
    
    # detect rpaddle misses
    if game_ball.xcor()>380:
        game_ball.reset_position()
        game_score.l_point()
    
    # detect lpaddle misses
    if game_ball.xcor()<-380:
        game_ball.reset_position()
        game_score.r_point()


screen.exitonclick()