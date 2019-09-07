import random

def setup():
    size(400, 400)
    stroke(255)
      
def draw():
    line(150, 25, mouseX, mouseY)
     
def mousePressed():
    background( random.randrange(255), random.randrange(255), random.randrange(255) )
