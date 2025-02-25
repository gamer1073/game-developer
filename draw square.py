import pgzrun
from random import randint
from pygame import Rect
height = 400
width = 400
def draw():
    red = 255
    green = randint(100,255)
    blue =  0
    width1 = width - 200
    height1 = height - 200

    for i in range (20):
        rect = Rect((0,0),(width1,height1))
        rect.center = 200,200
        screen.draw.rect(rect,(red,green,blue))
        red -= 10
        blue += 10
        width1 -= 10
        height1 -= 10

pgzrun.go()
