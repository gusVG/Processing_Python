from random import *

dx = dy = up = down = left = right = 0
x = y = 10
adelante = True
abajo = True

def setup():
    global y, dx,dy
    y = randrange(10,390,1)
    dx = randrange(5,11,1)
    dy = randrange(5,11,1)
    background(0)
    size(600,400)

def draw():
    global x, y, adelante, abajo, dx, dy
    global up, down, left, right
    background(0)
    fill(0,0,255)
    ellipse(x, y, 20, 20)
    textSize(32)
    #PARTE SUPERIOR
    fill(255,0,0)
    text(up, width / 2, 30)
    #PARTE DERECHA
    fill(0,255,0)
    text(right, width - 40, height / 2)
    #PARTE INFERIOR
    fill(0,255,255)
    text(down, width / 2, height - 10)
    #PARTE IZQUIERDA
    fill(255,255,255)
    text(left, 2, height / 2)
    
    if adelante:
        x += dx
        if(x >= 590):
            adelante = False
            dx = randrange(5,11,1)
            right += 1
    else:
        x -= dx
        if(x <= 10):
            adelante = True
            dx = randrange(5,11,1)
            left += 1
            
    if abajo:
        y += dy
        if(y >= 390):
            abajo = False
            dy = randrange(5,11,1)
            down += 1
    else:
        y -= dy
        if(y <= 10):
            abajo = True
            dy = randrange(5,11,1)
            up += 1
