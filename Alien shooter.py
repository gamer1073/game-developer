import pgzrun
from random import randint

width = 400
height = 400
TITLE = "Alien shooter"
alien = Actor("alien image")

alien.pos = 200,80

def draw():
    screen.clear()
    screen.fill(color = ("blue"))
    alien.draw()

pgzrun.go()