i = a = 0
def setup():
    size(768, 400)
    colorMode(RGB, 255, 255, 255, 1 )
    background(255)

def draw():
    global i, a
    a %= 256
    noStroke()
    if i < 256:
        for x in range(200):            
            fill( 255, a, 0, 1 - 0.005 * x )
            rect( i, x, 1, 1 )
            fill( 0, 255 - a, 255, 0.005 * x )
            rect( i, 200 + x, 1, 1 )
    elif 256 <= i < 512 :
        for x in range(200):
            fill( 255 - a, 255, 0, 1 - 0.005 * x )
            rect( i, x, 1, 1 )
            fill( a, 0, 255, 0.005 * x )
            rect( i, 200 + x, 1, 1 )
    else:
        for x in range(200):
            fill( 0, 255, a, 1 - 0.005 * x )
            rect( i, x, 1, 1 )
            fill( 255, 0, 255 - a, 0.005 * x )
            rect( i, 200 + x, 1, 1 )
    i += 1
    a += 1
