'''
Se trata de crear una competencia de 10 bicicletas que 
avanzaran por turnos a un punto del plano cartesiano 
generado a traves del lanzamiento del dado.  Ganará la 
primer bici en alcanzar una distancia de 100, momento en
el cual la competencia debe terminar. 
'''
from Bicicleta import Bicicleta
from dado import Dado

lasBicis = [Bicicleta(" ") for i in range(10)]
for i in range(10):
    lasBicis[i].asignaPropietario(str(i))
miDado = Dado()
hayGanador = False
while (not hayGanador):
    for i in range(10):
        miDado.lanzar()
        x = miDado.consultar()
        miDado.lanzar()
        y = miDado.consultar()
        lasBicis[i].irHasta(x, y)
        lasBicis[i].mostrar()
        if lasBicis[i].distancia>=100:
            hayGanador=True
            print("LA BIBI GANADORA ES: ")
            lasBicis[i].mostrar()
            break
