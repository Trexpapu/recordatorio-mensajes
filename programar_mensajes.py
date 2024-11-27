import elementos as ele
import fuente_color as ft
import tkinter as tk
from tkinter import messagebox
import sqlite3 as sql
from datetime import datetime

def regresar(ventana):
    ventana.destroy()

def procesar_datos(datos):
    usuarioID = datos[0]
    fecha = datos[1]
    mensaje = datos[2]
    if not fecha and mensaje:
        messagebox.showinfo("Mensaje","Error: Faltan campos por llenar")
        return
    conexion = sql.connect("USUARIOS_WP.db")
    try:
        # Validar formato de fecha
        datetime.strptime(fecha, "%d/%m/%Y")  # Verifica formato día/mes/año
        
        # Conectar a la base de datos
        
        cursor = conexion.cursor()
        
        # Insertar datos en la tabla MENSAJES
        cursor.execute("INSERT INTO MENSAJES (USUARIO_ID, FECHA, MENSAJE) VALUES (?, ?, ?)", (usuarioID, fecha, mensaje))
        conexion.commit()

        messagebox.showinfo("Mensaje", "Éxito: Datos cargados correctamente")
    except Exception:
        messagebox.showinfo("Mensaje", "Error: No se pudo subir la información")
    
    finally:
        conexion.close()

    
def main(datos):
    root = ele.Elementos("Programar mensaje", ft.negro)
    ancho_pantalla = root.winfo_screenwidth()
    alto_pantalla = root.winfo_screenheight()
    mitad_pantalla = ancho_pantalla / 2
    pos_en_y = alto_pantalla - alto_pantalla
    pos_en_x = ancho_pantalla - ancho_pantalla
    ancho_local = 25
    usuarioID = tk.StringVar()
    fecha = tk.StringVar()
    mensaje = tk.StringVar()
    usuarioID.set(datos[0])

    root.BotonAccion(
        texto="Regresar",      # Texto del Label
        fuente=ft.FUENTE,               # Fuente
        ancho=ft.ancho,                    # Ancho del Label
        altura=ft.altura,                    # Altura del Label
        color=ft.morado,             # Color de fondo
        posx=pos_en_x + 20,                    # Posición en X
        posy=pos_en_y + 25 ,               #Posición en Y
        funcion = regresar ,
        entrada = root                 
    )

    root.Label(texto = f"Nombre: {datos[1]}", 
               fuente = ft.FUENTE, 
               ancho = ancho_local, 
               altura=ft.altura, 
               color=ft.azul, 
               relieve=ft.relieve,
               borde= ft.borde, 
               posx=pos_en_x + 300, 
               posy= pos_en_y + 100)
    
    

    root.Label(texto = f"Celular: {datos[2]}", 
               fuente = ft.FUENTE, 
               ancho = ancho_local, 
               altura=ft.altura, 
               color=ft.azul, 
               relieve=ft.relieve,
               borde= ft.borde, 
               posx=pos_en_x + 300, 
               posy= pos_en_y + 200)
    
    root.Label(texto = "Fecha de mensaje (dia/mes/año)", 
               fuente = ft.FUENTE, 
               ancho = ancho_local, 
               altura=ft.altura, 
               color=ft.azul, 
               relieve=ft.relieve,
               borde= ft.borde, 
               posx=pos_en_x + 300, 
               posy= pos_en_y + 400)
    
    root.Entrada(
        fuente = ft.FUENTE,
        color = ft.gris,
        justificacion = tk.LEFT,
        relieve = ft.relieve,
        posx=pos_en_x + 600,
        posy=pos_en_y + 400,
        ancho= ft.anchoEntry,
        altura= ft.altoEntry,
        variable = fecha
    )

    root.Label(texto = "Mensaje", 
               fuente = ft.FUENTE, 
               ancho = ancho_local, 
               altura=ft.altura, 
               color=ft.azul, 
               relieve=ft.relieve,
               borde= ft.borde, 
               posx=pos_en_x + 300, 
               posy= pos_en_y + 600)
    
    root.Entrada(
        fuente = ft.FUENTE,
        color = ft.gris,
        justificacion = tk.LEFT,
        relieve = ft.relieve,
        posx=pos_en_x + 600,
        posy=pos_en_y + 600,
        ancho= ft.anchoEntry,
        altura= ft.altoEntry,
        variable = mensaje
    )
    



    root.BotonEnvio(
        texto = "Subir datos",      # Texto del Label
        fuente = ft.FUENTE,
        ancho= ft.ancho,
        altura= ft.altura,
        color= ft.verde,
        posx=pos_en_x + 20,                    # Posición en X
        posy=pos_en_y + 300 ,
        funcion= procesar_datos,
        entradas= [usuarioID, fecha, mensaje]

    )
    
    

    root.mainloop()