import pgzrun
from random import randint 

screenwidth = 300
screenheight = 300


def draw():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    startx = 50
    starty = 80
    endx = screenwidth - 50
    endy = starty
    for i in range(5):
        screen.draw.line((startx,starty),(endx,endy),(r,g,b))
        starty += 30
        endy += 30


    startx1 = 340
    starty1 = screenheight - 50
    endx1 = 340
    endy1 = startx1
    for i in range (5):
        screen.draw.line((startx1,starty1),(endx1,endy1),(r,g,b))
        startx1 +=50
        endx1 +=50



    
pgzrun.go()




        









