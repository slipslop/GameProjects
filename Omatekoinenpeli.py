import turtle
import math
import random


wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Simple Object Motion Template")

class Player(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("white")
        self.shape("triangle")
        self.penup()
        self.speed(0)
        self.thrust = 1
        self.friction = 0.99
        self.dx = 0
        self.dy = 0

    def move(self):
        self.dx *= self.friction
        self.dy *= self.friction
        self.goto(self.xcor()+self.dx, self.ycor()+self.dy)


        # boundary detection
        if self.xcor() > 350:
            self.setx(350)
           # self.rt(60)
        if self.xcor() < -350:
            self.setx(-350)
           # self.rt(60)
        if self.ycor() > 350:
            self.sety(350)
           # self.rt(60)
        if self.ycor() < -350:
            self.sety(-350)
           # self.rt(60)

    def turnleft(self):
        self.left(45)
    def turnright(self):
        self.right(45)
    def accelerate(self):
        h = self.heading()
        self.dx += math.cos(h*math.pi/180)*self.thrust
        self.dy += math.sin(h*math.pi/180)*self.thrust


class Food(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("red")
        self.speed(0)
        self.shape("square")
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.penup()
        self.goto(random.randint(0,300), random.randint(0,300))
        food = []
        for i in range(4):
            food.append(Food)








class Game():
    def __init__(self):
        self.pen = turtle.Turtle()

    def draw_border(self):
        # draw border
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-350, 350)
        self.pen.pendown()
        for side in range(4):
           self.pen.fd(700)
           self.pen.rt(90)
        self.pen.penup()
        self.pen.ht()
        self.pen.pendown()

def is_collision(food, player):
    if (food.xcor() >= (player.xcor() - 20)) and \
    (food.xcor() <= (player.xcor() + 20)) and \
    (food.ycor() >= (player.ycor() - 20)) and \
    (food.ycor() <= (player.ycor() + 20)):
        return True
    else:
        return False



player = Player()
game = Game()
game.draw_border()

food = Food()


turtle.listen()
turtle.onkey(player.turnleft, "Left")
turtle.onkey(player.turnright, "Right")
turtle.onkey(player.accelerate, "Up")

# wn.tracer(0)

while True:
    wn.update()
    player.move()

    # collision checking between player and food
    if is_collision(food, player):
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        food.goto(x, y)








