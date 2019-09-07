NEGRO = 0 # Escala de grises que va de 0 a 255
BLANCO = 255 # Donde 0 es Negro y 255 es Blanco
ANCHO_LIENZO = ALTO_LIENZO = 400 #Variables globales

# Funcion que inicializa el frame de trabajo. Solo se ejecuta una vez
def setup():
    '''
    Para todas aquellas funciones que acepten color como argumento,
    se puede utilizar solo uno (escala de grises) o
    se pueden utilizar tres: RGB
    ''' 
    background(NEGRO) # Pasar el fondo a color Negro, si no es declarado, da un tono de gris
    size(ANCHO_LIENZO, ALTO_LIENZO) # Función que determina tamaño del lienzo

# Funcion que se ejecuta de manera indefinida hasta que detengamos el programa
# Se parece a un ciclo que inicia tantas veces como se deje activo
def draw():
    strokeWeight(1) # Grosor de linea/contorno/ancho de punto, en pixeles
    stroke(BLANCO) # Color de contorno, si no es declarado, inicia en negro.
    # Las palabras reservadas (para Processing) 'mouseX' y 'mouseX' nos dan la posicion X y Y del mouse, respectivamente
    point(mouseX, mouseY) # Dibuja un punto en la posicion dada ( x, y )
    line(5, 5, ANCHO_LIENZO - 5, ALTO_LIENZO - 5) # Dibuja una linea de un punto inicial(x1, y1) al punto final (x2, y2)
    noStroke() # Sin contorno para las siguientes lineas
    fill(255,0,0) # Funcion que define el color de relleno para las formas
    # Las palabras reservadas (para Processing) 'width' y 'height' nos dan el ancho y alto del lienzo, respectivamente
    rect(50, 50, width-100, height-100) # Dibuja un rectangulo que recibe X y Y inicial y despues ancho y alto
    fill(0,255,0) # Se puede utilizar la forma RGB(Red, Green, Blue) para colores
    ellipse(50, 150, 50, 50) # Dibuja una elipse que recibe X y Y inicial y despues ancho y alto
    fill(0,0,255) # RGB utiliza la escala 0-255, donde 0 es ausencia y 255 presencia
    triangle(10,50,25,10,50,50) # Dibuja un triangulo (x1, y1, x2, y2, x3, y3)
    stroke(248,24,148) # Se activa nuevamente el contorno para las siguientes lineas
    strokeWeight(5) # Grosor de linea/contorno/ancho de punto, en pixeles
    fill(255,255,0) # Cambio de relleno de forma a una combinacion de rojo con verde
    quad(100, 15, 150, 15, 200, 50, 150, 88) # Dibuja un cuadrilatero (x1, y1, x2, y2, x3, y3, x4, y4)
    fill(125,64,10) # Combinacion de colores que da un tono de cafe
    textSize(32) # Tamanio de texto. En pixeles
    text("Hola mundo", 150, 380) # Dibuja texto que recibe la cadena, X y Y inicial
