import random

def setup():
    size(400, 400)

def draw():
    background( 0 )
    rect( 100, 100, 200, 200  )
            
def mousePressed():
    if mouseX > 100 and mouseX < 300 and mouseY > 100 and mouseY < 300:
        fill( random.randrange(255), random.randrange(255), random.randrange(255) )
