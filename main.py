from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=500, height=550)
screen.bgcolor("black")
screen.title("PING PONG")
screen.tracer(0)

left_paddle = Paddle((-350,0))
right_paddle = Paddle((350,0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(right_paddle.go_up,"Up")
screen.onkey(right_paddle.go_down,"Down")
screen.onkey(left_paddle.go_up,"w")
screen.onkey(left_paddle.go_down,"s")

game_is_on = True
while game_is_on:
  time.sleep(ball.move_speed)
  screen.update()
  ball.move()

  #bouce the ball if collide with wall
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()

  #bounce the ball if collide with the paddle
  if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or  ball.distance(left_paddle) < 50 and ball.xcor() < -320:
    ball.bounce_x()

  #if ball misses the left paddle
  if ball.xcor() > 380:
    ball.reset_position()
    score.right_point()

  #if ball misses the right paddle
  if ball.xcor() < -380:
    ball.reset_position()
    score.left_point()



  

  





