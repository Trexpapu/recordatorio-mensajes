import tkinter as tk
from tkinter import ttk
import sqlite3 as sql
from datetime import datetime

def obtener_datos():
    # Obtener la fecha actual en formato YYYY-MM-DD
    fecha_actual = datetime.now().strftime("%d/%m/%Y")
    
    
    # Conectar a la base de datos y realizar la consulta
    conexion = sql.connect("USUARIOS_WP.db")
    cursor = conexion.cursor()
    cursor.execute("""SELECT M.MENSAJE_ID, U.NOMBRE, U.CELULAR, M.FECHA, M.MENSAJE
                      FROM USUARIOS U 
                      JOIN MENSAJES M ON U.USUARIO_ID = M.USUARIO_ID
                      WHERE M.FECHA = ?""", (fecha_actual,))
    datos = cursor.fetchall()
    
    conexion.close()
    return datos

    


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
    
    
    # Mostrar el Treeview en la root
    tree.pack(expand=True, fill="both")
    
    # Ejecutar la aplicación
    root.mainloop()


