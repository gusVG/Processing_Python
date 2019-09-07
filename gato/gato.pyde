cat = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ] #Almacena las tiradas
movimiento = False # Turno por participante

ganaTermina = False # Variable que termina juego
ganador = 0 # Variabl

# Funcion de logica de gane 
def haGanado( gato ):
    print( gato )
    contaJ1 = contaJ2 = contaFin = 0
    # FILAS
    for i in range(3):
        for j in range(3):
            if gato[i][j] == 1:
                contaJ1 += 1
            elif gato[i][j] == 2:
                contaJ2 += 1
            if contaJ1 == 3:
                return True, 1
            elif contaJ2 == 3:
                return True, 2
        contaJ1 = contaJ2 = 0
    
    # COLUMNAS
    for i in range(3):
        for j in range(3):
            if gato[j][i] == 1:
                contaJ1 += 1
            elif gato[j][i] == 2:
                contaJ2 += 1
            if contaJ1 == 3:
                return True, 1
            elif contaJ2 == 3:
                return True, 2
        contaJ1 = contaJ2 = 0
    
    # DIAGONALES
    if gato[0][0] == 1 and gato[1][1] == 1 and gato[2][2] == 1:
        return True, 1
    elif gato[2][0] == 1 and gato[1][1] == 1 and gato[0][2] == 1:
        return True, 1
    elif gato[0][0] == 2 and gato[1][1] == 2 and gato[2][2] == 2:
        return True, 2
    elif gato[2][0] == 2 and gato[1][1] == 2 and gato[0][2] == 2:
        return True, 2
    
    # FIN DE JUEGO
    for i in range(3):
        for j in range(3):
            if gato[i][j] > 0:
                contaFin += 1    
    
    if contaFin == 9:
        return True, 0
    else:
        return False, 0

def setup():
    background(0)
    size(400,400)

def draw():
    global cat, ganaTermina, ganador
    
    stroke(255)    
    for i in range(2): # Dibuja Gato
        line(50, 150 + 100 * i, 350, 150 + 100 * i) # HORIZONTALES
        line(150 + 100 * i, 50, 150 + 100 * i, 350) # VERTICALES
    
    if (ganaTermina == True ):
        textSize(32)
        fill(0, 255, 0)
        if (ganador > 0 ):
            text("Ganador: Jugador {}".format( ganador ), 50, 380)
        else:
            text("Juego termina s/ganador", 5, 380)

    else:
        noFill()
        for fila in range(3):
            for columna in range(3):
                if cat[fila][columna] == 1:
                    dibujaCirculo( columna , fila )
                elif cat[fila][columna] == 2:
                    dibujaTache( columna , fila )
    ganaTermina, ganador = haGanado( cat )

# Pinta un circulo de acuerdo a posicion dada    
def dibujaCirculo(x, y):
    stroke(255, 0, 0)
    ellipse(100 + 100 * x, 100 + 100 * y, 80, 80)

# Pinta un tache de acuerdo a posicion dada    
def dibujaTache(x, y):
    stroke(0, 0, 255)
    line(60 + 100 * x, 60 + 100 * y, 140 + 100 * x, 140 + 100 * y)
    line(140 + 100 * x, 60 + 100 * y, 60 + 100 * x, 140 + 100 * y)

# Funcion propia de Processing que cacha cada vez que se produce un evento de click
def mousePressed():
    global cat, movimiento
    valor = 0
    
    if( movimiento ):
        valor = 2
    else:
        valor = 1
    
    # Escritura de tirada en posicion correspondiente
    # Solo se escribe si esta en 0 y "ganaTermina" es igual a falso
    # PRIMER FILA
    if mouseX > 50 and mouseX < 150 and mouseY > 50 and mouseY < 150:
        if( cat[0][0] == 0 and ganaTermina == False ):
            cat[0][0] = valor
            movimiento = not movimiento
    elif mouseX > 150 and mouseX < 250 and mouseY > 50 and mouseY < 150:
        if( cat[0][1] == 0 and ganaTermina == False ):
            cat[0][1] = valor
            movimiento = not movimiento
    elif mouseX > 250 and mouseX < 350 and mouseY > 50 and mouseY < 150:
        if( cat[0][2] == 0 and ganaTermina == False ):
            cat[0][2] = valor
            movimiento = not movimiento
    # SEGUNDA FILA
    elif mouseX > 50 and mouseX < 150 and mouseY > 150 and mouseY < 250:
        if( cat[1][0] == 0 and ganaTermina == False ):
            cat[1][0] = valor
            movimiento = not movimiento
    elif mouseX > 150 and mouseX < 250 and mouseY > 150 and mouseY < 250:
        if( cat[1][1] == 0 and ganaTermina == False ):
            cat[1][1] = valor
            movimiento = not movimiento
    elif mouseX > 250 and mouseX < 350 and mouseY > 150 and mouseY < 250:
        if( cat[1][2] == 0 and ganaTermina == False ):
            cat[1][2] = valor
            movimiento = not movimiento
    # TERCERA FILA
    elif mouseX > 50 and mouseX < 150 and mouseY > 250 and mouseY < 350:
        if( cat[2][0] == 0 and ganaTermina == False ):
            cat[2][0] = valor
            movimiento = not movimiento
    elif mouseX > 150 and mouseX < 250 and mouseY > 250 and mouseY < 350:
        if( cat[2][1] == 0 and ganaTermina == False ):
            cat[2][1] = valor
            movimiento = not movimiento
    elif mouseX > 250 and mouseX < 350 and mouseY > 250 and mouseY < 350:
        if( cat[2][2] == 0 and ganaTermina == False ):
            cat[2][2] = valor
            movimiento = not movimiento

