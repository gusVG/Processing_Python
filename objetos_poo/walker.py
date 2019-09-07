import random

"""Clase caminante aleatorio"""
class Walker:
    """Metodo Constructor"""
    def __init__(self, posx, posy, rgb):
        self.x = posx
        self.y = posy
        self.colorRGB = rgb
        self.tamanio = 5
        
    """Metodo mostrar el punto"""
    def display(self):
        noStroke()
        fill( self.colorRGB[0], self.colorRGB[1], self.colorRGB[2], random.randrange( 255 ))
        ellipse(self.x, self.y, self.tamanio, self.tamanio)
    
    """Metodo de movimiento aleatorio"""
    def walk(self):
        choice = random.randrange( 4 )
        if choice == 0:
            self.x = self.x + self.tamanio
        elif choice == 1:
            self.x = self.x - self.tamanio
        elif choice == 2:
            self.y = self.y + self.tamanio
        elif choice == 3:
            self.y = self.y - self.tamanio
