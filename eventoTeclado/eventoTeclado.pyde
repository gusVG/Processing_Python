# USAR 'D' o 'd' para mover a la derecha
# USAR 'A' o 'a' para mover a la izquierda
# USAR 'W' o 'w' para mover hacia arriba
# USAR 'S' o 's' para mover hacia abajo

W_LIENZO = H_LIENZO = 400
cuadro = { 'posX': W_LIENZO / 2 - 25, 'posY': H_LIENZO / 2 - 25, 'ancho': 50, 'alto': 50 }

VELOCIDAD = 10

def setup():
    size( W_LIENZO, H_LIENZO )

def draw():
    background( 0 )
    fill( 255 )
    rect( cuadro['posX'], cuadro['posY'], 50, 50 )
            
def keyPressed():
    global cuadro
    print(key)
    
    if key == "d" or key == "D":
        if cuadro['posX'] >= 401:
            cuadro['posX'] = -49
        else:
            cuadro['posX'] += VELOCIDAD            
    elif key == "a" or key == "A":
        if cuadro['posX'] <= -51:
            cuadro['posX'] = 401
        else:
            cuadro['posX'] -= VELOCIDAD
    elif key == "s" or key == "S":
        if cuadro['posY'] >= 401:
            cuadro['posY'] = -49
        else:
            cuadro['posY'] += VELOCIDAD
    elif key == "w" or key == "W":
        if cuadro['posY'] <= -51:
            cuadro['posY'] = 401
        else:
            cuadro['posY'] -= VELOCIDAD
