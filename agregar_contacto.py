import elementos as ele
import fuente_color as ft
import tkinter as tk  # Asegúrate de importar tkinter
import sqlite3 as sql
from tkinter import messagebox

def regresar(ventana):
    ventana.destroy()

def SubirDatos(Datos):
    # Extraer los datos de la lista
    Nombre = Datos[0]
    Celular = Datos[1]
    Celular = Celular.replace(" ", "")
    subidos = 0


    if not (Nombre and Celular):
        return -1

    try:
        # Abrir conexión a la base de datos
        conexion = sql.connect("USUARIOS_WP.db")  # Asegúrate de usar una extensión como .db
        cursor = conexion.cursor()

        # Insertar datos en la tabla USUARIOS
        cursor.execute("""
        INSERT INTO USUARIOS (NOMBRE, CELULAR)
        VALUES (?, ?)
        """, (Nombre, Celular))  # Usar parámetros para evitar inyecciones SQL

        # Confirmar los cambios
        conexion.commit()
        subidos = 1
        
    
    except sql.Error as e:
        subidos = 0
    
    finally:
        # Cerrar la conexión
        conexion.close()

    return subidos

def procesar_datos(entradas):
    resultado = SubirDatos(entradas)

    mensaje_label = ""

    if resultado == -1:
        mensaje_label = "Error: Faltan campos por llenar"
    elif resultado == 0:
        mensaje_label= "Error: No se pudo subir la información"
    elif resultado == 1:
        mensaje_label = "Éxito: Datos subidos correctamente"

    messagebox.showinfo("Mensaje", mensaje_label)


def main():
    global root
    global mitad_pantalla
    global pos_en_y
    root = ele.Elementos("Agregar contácto", ft.negro)
    ancho_pantalla = root.winfo_screenwidth()
    alto_pantalla = root.winfo_screenheight()
    mitad_pantalla = ancho_pantalla / 2
    pos_en_y = alto_pantalla - alto_pantalla
    pos_en_x = ancho_pantalla - ancho_pantalla
    Nombre = tk.StringVar()
    Celular = tk.StringVar()


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

    root.Label(texto = "Nombre", 
               fuente = ft.FUENTE, 
               ancho = ft.ancho, 
               altura=ft.altura, 
               color=ft.azul, 
               relieve=ft.relieve,
               borde= ft.borde, 
               posx=pos_en_x + 300, 
               posy= pos_en_y + 100)
    
    root.Entrada(
        fuente = ft.FUENTE,
        color = ft.gris,
        justificacion = tk.LEFT,
        relieve = ft.relieve,
        posx=pos_en_x + 500,
        posy=pos_en_y + 100,
        ancho= ft.anchoEntry,
        altura= ft.altoEntry,
        variable = Nombre
    )

    root.Label(texto = "Celular", 
               fuente = ft.FUENTE, 
               ancho = ft.ancho, 
               altura=ft.altura, 
               color=ft.azul, 
               relieve=ft.relieve,
               borde= ft.borde, 
               posx=pos_en_x + 300, 
               posy= pos_en_y + 200)
    
    root.Entrada(
        fuente = ft.FUENTE,
        color = ft.gris,
        justificacion = tk.LEFT,
        relieve = ft.relieve,
        posx=pos_en_x + 500,
        posy=pos_en_y + 200,
        ancho= ft.anchoEntry,
        altura= ft.altoEntry,
        variable = Celular
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
        entradas= [Nombre, Celular]

    )


    root.mainloop()


