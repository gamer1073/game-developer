import pgzrun
from random import randint 

WIDTH = 400
HEIGHT = 400
def draw ():
    red = 255
    green = randint(100,255)
    blue =  0
    width = WIDTH
    height = HEIGHT - 300

    for i in range (20):
        rect = Rect((0,0),(width,height))
        rect.center = 200,200
        screen.draw.rect(rect,(red,green,blue))
        red -= 10
        blue += 10
        width -= 10
        height += 10

pgzrun.go()









