from turtle import Turtle

alignment="center"
Font=("Courier", 80, "normal")

class score(Turtle):
    def __init__(self):
        super().__init__()
        self.counter=0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.goto(-100,200)
        self.display()

    def display(self):
        self.clear()
        self.goto(-100,200)    
        self.write(self.l_score, align= alignment, font=Font)
        self.goto(100,200)
        self.write(self.r_score, align=alignment, font=Font)

    def game_over(self):
        self.write("Game Over", align=alignment, font=Font)

    def l_point(self):
        self.l_score+=1
        self.display()
    
    def r_point(self):
        self.r_score+=1
        self.display()

    