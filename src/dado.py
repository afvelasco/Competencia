'''
Representa un dado, que identifica el valor en su cara
superior, que se puede lanzar y también consultar
'''
from random import randint
class Dado:
    def __init__(self):
        self.caraSuperior = 6

    def lanzar(self):
        self.caraSuperior = randint(1,6)

    def consultar(self):
        return self.caraSuperior
