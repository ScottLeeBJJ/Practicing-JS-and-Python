# connect 4 game

import turtle
import time

# window or screen
screen = turtle.Screen()
screen.setup(800,800)
screen.title("Connect 4 Game with Python!")
turtle.speed(0)
turtle.hideturtle()
screen.tracer(0,0)
score = turtle.Turtle()
score.up()
score.hideturtle()

# connect 4 board
ROWS = 6
COLS = 7
STARTX = -450
STARTY = -450*ROWS/COLS
WIDTH = 2*STARTX
HEIGHT = -2*STARTY

def draw_rectangle(x,y,w,h,color):
    turtle.up()
    turtle.goto(x,y)
    turtle.set(0)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.fd(w)
    turtle.left(90)
    turtle.fd(h)
    turtle.left(90)
    

# player pieces


# AI pieces


# you win


# you lose


# close the game






# citation
# https://pythonturtle.academy/connect-4-with-python-turtle-source-code-included/