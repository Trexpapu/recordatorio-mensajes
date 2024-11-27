import tkinter as tk
from tkinter import ttk
import sqlite3 as sql
import elementos as ele
import fuente_color as ft
from tkinter import messagebox
import programar_mensajes as pm
def obtener_datos():
    # Conectar a la base de datos y realizar la consulta
    conexion = sql.connect("USUARIOS_WP.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT USUARIO_ID, NOMBRE, CELULAR FROM USUARIOS")
    datos = cursor.fetchall()
    conexion.close()
    return datos
def regresar(ventana):
    ventana.destroy()
    mostrar_datos()

def borrar_datos(usuarioID):
    conexion = sql.connect("USUARIOS_WP.db")
    try:
        
        cursor = conexion.cursor()

        cursor.execute("DELETE FROM USUARIOS WHERE USUARIO_ID = ?", (usuarioID[0],))
        cursor.execute("DELETE FROM MENSAJES WHERE USUARIO_ID = ?", (usuarioID[0],))

        conexion.commit()
        
        messagebox.showinfo("Mensaje", "Éxito: Usuario borrado correctamente")
    except Exception as e:
        
        messagebox.showinfo("Mensaje", "Error: No se pudo borrar el usuario")

    finally:
        conexion.close()

def actualizar_datos(datos):
    conexion = sql.connect("USUARIOS_WP.db")
    try:
        usuarioID = datos[0]
        Nombre = datos[1]
        celular = datos[2]
        celular = celular.replace(" ", "")
        
        cursor = conexion.cursor()

        cursor.execute("UPDATE USUARIOS SET NOMBRE = ?, CELULAR = ? WHERE USUARIO_ID = ?", (Nombre, celular, usuarioID))

        conexion.commit()
        
        messagebox.showinfo("Mensaje", "Éxito: Usuario actualizado correctamente")
    except Exception as e:
        
        messagebox.showinfo("Mensaje", "Error: No se pudo actualizar el usuario")

    finally:
        conexion.close() 

def llamar_main_programar_mensaje(datos):
    root_mostrar_usuario.destroy()
    pm.main(datos)

def mostrar_un_usuario(ventana, datos):
    ventana.destroy()
    global root_mostrar_usuario
    root_mostrar_usuario = ele.Elementos("Configurar usuarios", ft.negro)
    ancho_pantalla = root_mostrar_usuario.winfo_screenwidth()
    alto_pantalla = root_mostrar_usuario.winfo_screenheight()
    mitad_pantalla = ancho_pantalla / 2
    pos_en_y = alto_pantalla - alto_pantalla
    pos_en_x = ancho_pantalla - ancho_pantalla
    Nombre = tk.StringVar()
    Celular = tk.StringVar()
    usuarioID_var = tk.StringVar()  # Variable para el usuarioID
    usuarioID_var.set(datos[0])  # Establecer el valor en la variable
    Nombre.set(datos[1])
    Celular.set(datos[2])
    

    root_mostrar_usuario.BotonAccion(
        texto="Regresar",      # Texto del Label
        fuente=ft.FUENTE,               # Fuente
        ancho=ft.ancho,                    # Ancho del Label
        altura=ft.altura,                    # Altura del Label
        color=ft.morado,             # Color de fondo
        posx=pos_en_x + 20,                    # Posición en X
        posy=pos_en_y + 25 ,               #Posición en Y
        funcion = regresar ,
        entrada = root_mostrar_usuario                 
    )

    root_mostrar_usuario.Label(texto = "Nombre", 
               fuente = ft.FUENTE, 
               ancho = ft.ancho, 
               altura=ft.altura, 
               color=ft.azul, 
               relieve=ft.relieve,
               borde= ft.borde, 
               posx=pos_en_x + 300, 
               posy= pos_en_y + 100)
    
    root_mostrar_usuario.Entrada(
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

    root_mostrar_usuario.Label(texto = "Celular", 
               fuente = ft.FUENTE, 
               ancho = ft.ancho, 
               altura=ft.altura, 
               color=ft.azul, 
               relieve=ft.relieve,
               borde= ft.borde, 
               posx=pos_en_x + 300, 
               posy= pos_en_y + 200)
    
    root_mostrar_usuario.Entrada(
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
    root_mostrar_usuario.BotonEnvio(
        texto = "Borrar datos",      # Texto del Label
        fuente = ft.FUENTE,
        ancho= ft.ancho,
        altura= ft.altura,
        color= ft.rojo,
        posx=pos_en_x + 20,                    # Posición en X
        posy=pos_en_y + 200 ,
        funcion= borrar_datos,
        entradas= [usuarioID_var]
    )

    root_mostrar_usuario.BotonEnvio(
        texto = "Actualizar datos",      # Texto del Label
        fuente = ft.FUENTE,
        ancho= ft.ancho,
        altura= ft.altura,
        color= ft.verde,
        posx=pos_en_x + 20,                    # Posición en X
        posy=pos_en_y + 400 ,
        funcion= actualizar_datos,
        entradas= [usuarioID_var, Nombre, Celular]
    )

    

    root_mostrar_usuario.BotonEnvio(
        texto = "Programar mensaje",      # Texto del Label
        fuente = ft.FUENTE,
        ancho= ft.ancho,
        altura= ft.altura,
        color= ft.naranja,
        posx=pos_en_x + 20,                    # Posición en X
        posy=pos_en_y + 600 ,
        funcion= llamar_main_programar_mensaje,
        entradas= [usuarioID_var, Nombre, Celular]
    )

    root_mostrar_usuario.mainloop()

    


def mostrar_datos():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Tabla de Usuarios")
    root.state("zoomed")
    
    # Crear el Treeview
    tree = ttk.Treeview(root, columns=("USUARIO_ID", "NOMBRE", "CELULAR"), show="headings")
    
    # Configurar encabezados
    tree.heading("USUARIO_ID", text="USUARIO_ID")
    tree.heading("NOMBRE", text="Nombre")
    tree.heading("CELULAR", text="Celular")
    
    # Ajustar tamaño de las columnas
    tree.column("USUARIO_ID", width=50, anchor="center")
    tree.column("NOMBRE", width=200, anchor="center")
    tree.column("CELULAR", width=150, anchor="center")
    
    # Insertar datos en el Treeview
    for fila in obtener_datos():
        tree.insert("", "end", values=fila)
    
    # Agregar un evento para capturar el clic en una fila
    def obtener_fila_seleccionada(event):
        item = tree.selection()[0]  # Obtener el identificador del elemento seleccionado
        valores = tree.item(item, "values")  # Obtener los valores de la fila
        mostrar_un_usuario(root, valores)
    
    # Vincular el evento de clic
    tree.bind("<<TreeviewSelect>>", obtener_fila_seleccionada)
    
    # Mostrar el Treeview en la root
    tree.pack(expand=True, fill="both")
    
    # Ejecutar la aplicación
    root.mainloop()


