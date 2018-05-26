"juan esteban triviño"
import time
from tkinter import *
flag=True
def arriba():
    lienzo.move(1,0,-60)
    Tk.update(ventana)
def abajo():
    lienzo.move(1,0,60)
    Tk.update(ventana)
def izq():
    lienzo.move(1,-60,0)
    Tk.update(ventana)
def der():
    lienzo.move(1,60,0)
    Tk.update(ventana)
def salir():
    global flag
    flag=False


ventana=Tk()
btn1=Button(ventana,text="arriba",command=arriba)
btn2=Button(ventana,text="abajo",command=abajo)
btn3=Button(ventana,text="izquierda",command=izq)
btn4=Button(ventana,text="derecha",command=der)
btn5=Button(ventana,text="salir",command=salir)

lienzo=Canvas(ventana,width=999,height=500)
lienzo.pack()
lienzo.create_rectangle(190,190,210,210,fill='blue')

Tk.update(ventana)
time.sleep(2)


Tk.update(ventana)
btn1.pack(side="top")
btn2.pack(side="bottom")
btn3.pack(side="left")
btn4.pack(side="right")
btn5.pack()

while(flag):
    Tk.update(ventana)
  if   