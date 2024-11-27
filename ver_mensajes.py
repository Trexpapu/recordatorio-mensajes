import tkinter as tk
from tkinter import ttk
import sqlite3 as sql
import elementos as ele
import fuente_color as ft
from tkinter import messagebox

from datetime import datetime
def obtener_datos():
    # Conectar a la base de datos y realizar la consulta
    conexion = sql.connect("USUARIOS_WP.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT M.MENSAJE_ID, U.NOMBRE, U.CELULAR, M.FECHA, M.MENSAJE FROM USUARIOS U JOIN MENSAJES M ON U.USUARIO_ID = M.USUARIO_ID")
    datos = cursor.fetchall()
    conexion.close()
    return datos

def regresar(ventana):
    ventana.destroy()
    mostrar_datos()
    
def borrar_datos(MensajeID):
    conexion = sql.connect("USUARIOS_WP.db")
    try:
        
        cursor = conexion.cursor()

        cursor.execute("DELETE FROM MENSAJES WHERE MENSAJE_ID = ?", (MensajeID[0],))

        conexion.commit()
        
        messagebox.showinfo("Mensaje", "Éxito: Mensaje borrado correctamente")
    except Exception as e:
        
        messagebox.showinfo("Mensaje", "Error: No se pudo borrar el mensaje")

    finally:
        conexion.close()

def actualizar_datos(datos):
    conexion = sql.connect("USUARIOS_WP.db")
    try:
        mensajeID = datos[0]
        fecha = datos[1]
        mensaje = datos[2]
        datetime.strptime(fecha, "%d/%m/%Y")  # Verifica formato día/mes/año
        
        cursor = conexion.cursor()

        cursor.execute("UPDATE MENSAJES SET FECHA = ?, MENSAJE = ? WHERE MENSAJE_ID = ?", (fecha, mensaje, mensajeID,))

        conexion.commit()
        
        messagebox.showinfo("Mensaje", "Éxito: Mensaje actualizado correctamente")
    except Exception as e:
        
        messagebox.showinfo("Mensaje", "Error: No se pudo actualizar el mensaje")

    finally:
        conexion.close() 



def mostrar_un_mensaje(ventana, datos):
    ventana.destroy()
    
    global root_mostrar_mensaje
    root_mostrar_mensaje = ele.Elementos("Configurar mensajes", ft.negro)
    ancho_pantalla = root_mostrar_mensaje.winfo_screenwidth()
    alto_pantalla = root_mostrar_mensaje.winfo_screenheight()
    mitad_pantalla = ancho_pantalla / 2
    pos_en_y = alto_pantalla - alto_pantalla
    pos_en_x = ancho_pantalla - ancho_pantalla
    ancho_local = 25

    MensajeID = tk.StringVar()
    
    
    Fecha = tk.StringVar()
    Mensaje = tk.StringVar()
    MensajeID.set(datos[0])
    
    
    Fecha.set(datos[3])
    Mensaje.set(datos[4])
    

    root_mostrar_mensaje.BotonAccion(
        texto="Regresar",      # Texto del Label
        fuente=ft.FUENTE,               # Fuente
        ancho=ft.ancho,                    # Ancho del Label
        altura=ft.altura,                    # Altura del Label
        color=ft.morado,             # Color de fondo
        posx=pos_en_x + 20,                    # Posición en X
        posy=pos_en_y + 25 ,               #Posición en Y
        funcion = regresar ,
        entrada = root_mostrar_mensaje                 
    )

    root_mostrar_mensaje.Label(texto = f"Nombre: {datos[1]}", 
               fuente = ft.FUENTE, 
               ancho = ancho_local, 
               altura=ft.altura, 
               color=ft.azul, 
               relieve=ft.relieve,
               borde= ft.borde, 
               posx=pos_en_x + 300, 
               posy= pos_en_y + 100)
    
    

    root_mostrar_mensaje.Label(texto = f"Celular: {datos[2]}", 
               fuente = ft.FUENTE, 
               ancho = ancho_local, 
               altura=ft.altura, 
               color=ft.azul, 
               relieve=ft.relieve,
               borde= ft.borde, 
               posx=pos_en_x + 300, 
               posy= pos_en_y + 200)
    
    root_mostrar_mensaje.Label(texto = f"Fecha(dia/mes/año)", 
               fuente = ft.FUENTE, 
               ancho = ancho_local, 
               altura=ft.altura, 
               color=ft.azul, 
               relieve=ft.relieve,
               borde= ft.borde, 
               posx=pos_en_x + 300, 
               posy= pos_en_y + 300)
    
    root_mostrar_mensaje.Entrada(
        fuente = ft.FUENTE,
        color = ft.gris,
        justificacion = tk.LEFT,
        relieve = ft.relieve,
        posx=pos_en_x + 600,
        posy=pos_en_y + 300,
        ancho= ft.anchoEntry,
        altura= ft.altoEntry,
        variable = Fecha
    )

    root_mostrar_mensaje.Label(texto = f"Mensaje", 
               fuente = ft.FUENTE, 
               ancho = ancho_local, 
               altura=ft.altura, 
               color=ft.azul, 
               relieve=ft.relieve,
               borde= ft.borde, 
               posx=pos_en_x + 300, 
               posy= pos_en_y + 400)
    
    root_mostrar_mensaje.Entrada(
        fuente = ft.FUENTE,
        color = ft.gris,
        justificacion = tk.LEFT,
        relieve = ft.relieve,
        posx=pos_en_x + 600,
        posy=pos_en_y + 400,
        ancho= ft.anchoEntry,
        altura= ft.altoEntry,
        variable = Mensaje
    )
    
    
    root_mostrar_mensaje.BotonEnvio(
        texto = "Borrar datos",      # Texto del Label
        fuente = ft.FUENTE,
        ancho= ft.ancho,
        altura= ft.altura,
        color= ft.rojo,
        posx=pos_en_x + 20,                    # Posición en X
        posy=pos_en_y + 200 ,
        funcion= borrar_datos,
        entradas= [MensajeID]
    )

    root_mostrar_mensaje.BotonEnvio(
        texto = "Actualizar datos",      # Texto del Label
        fuente = ft.FUENTE,
        ancho= ft.ancho,
        altura= ft.altura,
        color= ft.verde,
        posx=pos_en_x + 20,                    # Posición en X
        posy=pos_en_y + 400 ,
        funcion= actualizar_datos,
        entradas= [MensajeID, Fecha, Mensaje]
    )

    

    root_mostrar_mensaje.mainloop()

    


def mostrar_datos():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Tabla de Mensajes")
    root.state("zoomed")
    
    # Crear el Treeview
    tree = ttk.Treeview(root, columns=("MENSAJE_ID", "NOMBRE", "CELULAR", "FECHA", "MENSAJE"), show="headings")
    
    # Configurar encabezados
    tree.heading("MENSAJE_ID", text="MENSAJE_ID")
    tree.heading("NOMBRE", text="Nombre")
    tree.heading("CELULAR", text="Celular")
    tree.heading("FECHA", text="FECHA")
    tree.heading("MENSAJE", text="MENSAJE")
    
    # Ajustar tamaño de las columnas
    tree.column("MENSAJE_ID", width=50, anchor="center")
    tree.column("NOMBRE", width=200, anchor="center")
    tree.column("CELULAR", width=150, anchor="center")
    tree.column("FECHA", width=150, anchor="center")
    tree.column("MENSAJE", width=150, anchor="center")
    
    # Insertar datos en el Treeview
    for fila in obtener_datos():
        tree.insert("", "end", values=fila)
    
    # Agregar un evento para capturar el clic en una fila
    def obtener_fila_seleccionada(event):
        item = tree.selection()[0]  # Obtener el identificador del elemento seleccionado
        valores = tree.item(item, "values")  # Obtener los valores de la fila
        mostrar_un_mensaje(root, valores)
    
    # Vincular el evento de clic
    tree.bind("<<TreeviewSelect>>", obtener_fila_seleccionada)
    
    # Mostrar el Treeview en la root
    tree.pack(expand=True, fill="both")
    
    # Ejecutar la aplicación
    root.mainloop()


