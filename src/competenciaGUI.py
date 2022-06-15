'''
Se trata de crear una competencia de 10 bicicletas que 
avanzaran por turnos a un punto del plano cartesiano 
generado a traves del lanzamiento del dado.  Ganará la 
primer bici en alcanzar una distancia de 100, momento en
el cual la competencia debe terminar. 
'''
from tkinter import *
from bicicleta import Bicicleta
from dado import Dado

def turno():
    for i in range(10):
        miDado.lanzar()
        x = miDado.consultar()
        miDado.lanzar()
        y = miDado.consultar()
        lasBicis[i].irHasta(x, y)
        botones[i].place(x=20+10*lasBicis[i].distancia, y=20+35*i)
        if lasBicis[i].distancia >= 100:
            lbMensaje["text"]=f"Gana: la bici {i}"
            btAvanzar["state"]=DISABLED
            btReiniciar["state"]=NORMAL
            break
def reiniciar():
    for i in range(10):
        lasBicis[i].distancia=0
        botones[i].place(x=20, y=20+35*i)
    btAvanzar["state"]=NORMAL
    btReiniciar["state"]=DISABLED

ventanita = Tk()
ventanita.geometry("1200x500")
ventanita.title("Competencia de bicis")
btAvanzar = Button(text="Avanzar", command=turno)
btAvanzar.place(x=540, y=460)
btReiniciar = Button(text="Reiniciar", command=reiniciar)
btReiniciar.place(x=630, y=460)
btReiniciar["state"]=DISABLED
lasBicis = [Bicicleta("") for x in range(10)]
miDado = Dado()
botones = [Button() for x in range(10)]
for i in range(10):
    botones[i]["text"] = str(i)
    botones[i].place(x=20, y=20+35*i)
lbMensaje = Label(text="")
lbMensaje.place(x=550, y=420)
meta = Canvas(width=5, height=360, bg="black")
meta.create_line(3,0,3,360)
meta.place(x=1020, y=15) 
ventanita.mainloop()