from turtle import Turtle

class paddle(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.paddle_creation(pos)
    
    def paddle_creation(self, pos):
        # for pos in positions:
        self.shape("square")
        self.color("green")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup() 
        self.speed("fastest")       
        self.goto(pos)

    def goup(self):
        self.goto(self.xcor(),self.ycor()+20)
    
    def godown(self):
        self.goto(self.xcor(),self.ycor()-20)
    
    def lgoup(self):
        self.goto(self.xcor(),self.ycor()+20)
    
    def lgodown(self):
        self.goto(self.xcor(),self.ycor()-20)