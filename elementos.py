from tkinter import ttk
import tkinter as tk
class Elementos(tk.Tk):
    def __init__(self, titulo, color):#funcion inicial que recibe parametros titulo y color de ventana
        super().__init__()#heredamos las funciones de tkinter
        self.title(titulo)#agregamos titulo
        self.state('zoomed')  # Maximiza la ventana
        self.configure(bg=color)  # Puedes usar cualquier color válido
        
    def Label(self, texto, fuente, ancho, altura, color, relieve, borde, posx, posy):
        self.label = tk.Label(text=texto, font=fuente, width=ancho, height=altura, bg=color, relief=relieve, bd=borde)
        self.label.place(x=posx, y=posy)

    def Entrada(self,fuente, color, justificacion, relieve, posx, posy, ancho, altura, variable):
        self.entry = tk.Entry(self, font = fuente, bg=color, fg="#212121", justify=justificacion, relief=relieve, textvariable=variable)
        self.entry.place(x=posx,y=posy,width=ancho,height=altura)

    def BotonEnvio(self, texto, fuente, ancho, altura, color, posx, posy, funcion, entradas):
        self.boton = tk.Button(
            self,
            text=texto,
            font=fuente,
            width=ancho,
            height=altura,
            bg=color,
            cursor="hand2",
            command=lambda: funcion([entry.get() for entry in entradas])  
        )
        self.boton.place(x=posx, y=posy)
    
    def BotonAccion(self, texto, fuente, ancho, altura, color, posx, posy, funcion, entrada):
        self.boton = tk.Button(
            self,
            text=texto,
            font=fuente,
            width=ancho,
            height=altura,
            bg=color,
            cursor= "hand2",
            command= lambda: funcion(entrada)
        )
        self.boton.place(x=posx, y=posy)