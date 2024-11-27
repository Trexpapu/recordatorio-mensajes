import sqlite3 as sql
from datetime import datetime
from tkinter import messagebox
def LimpiarDatos():
    conexion = sql.connect("USUARIOS_WP.db")
    try:
    # Obtener la fecha actual en formato YYYY-MM-DD
        fecha_actual = datetime.now().strftime("%d/%m/%Y")
        
        
        # Conectar a la base de datos y realizar la consulta
        
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM MENSAJES WHERE FECHA = ?", (fecha_actual,))
        conexion.commit()
        
        messagebox.showinfo("Mensaje", "Éxito: Datos borrados correctamente")
    except Exception as e:
        messagebox.showinfo("Mensaje", "Error: No se pudieron borrar los datos")
    finally:
        conexion.close()
    