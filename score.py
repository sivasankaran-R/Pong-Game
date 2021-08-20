from turtle import Turtle

class Score(Turtle):
  def __init__(self):
    super().__init__()
    self.left_score = 0
    self.right_score = 0
    self.color("white")
    self.hideturtle()
    self.penup()
    self.update_score()

  def update_score(self):
    self.clear()
    self.goto(-100,200)
    self.write(self.left_score,align="center",font=("courier",80,"normal"))
    self.goto(100,200)
    self.write(self.right_score,align="center",font=("courier",80,"normal"))

  def left_point(self):
    self.left_score +=1
    self.update_score()
  
  def right_point(self):
    self.right_score +=1
    self.update_score()

  