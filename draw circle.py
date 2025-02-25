import pgzrun
from random import randint

screenwidth = 300
screenheight = 300

def draw():
    screen.fill(color = ("blue"))
    width = screenwidth - 100
    height = screenheight - 100
    radius = screenheight // 2
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)

    for i in range(10):
        center = (150,150)
        screen.draw.circle(center,radius,(r,g,b))
        width -=10
        height -=10
        radius -=5

pgzrun.go()




