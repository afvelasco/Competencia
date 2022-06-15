'''
Se trata de una clase que representa una bibicleta que
conoce su propietario, su ubicación en el plano
cartesiano y que acumula la distancia recorrida
'''
from math import sqrt

class Bicicleta:
    def __init__(self, pro):
        self.propietario = pro
        self.posX = 0
        self.posY = 0
        self.distancia = 0
    def irHasta(self, x, y):
        tramo = sqrt((self.posX-x)**2 + (self.posY-y)**2)
        self.posX = x
        self.posY = y
        self.distancia += tramo
    def mostrar(self):
        print(f"Bicicleta de: {self.propietario}")
        print(f"Ubicacion x = {self.posX}, y = {self.posY}")
        print(f"Distancia recorrida: {self.distancia}")
    def asignaPropietario(self, prop):
        self.propietario = prop

