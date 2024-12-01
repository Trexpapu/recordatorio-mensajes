import pywhatkit
import sqlite3 as sql
from datetime import datetime
from tkinter import messagebox
import time

def obtener_datos():
    # Obtener la fecha actual en formato YYYY-MM-DD
    fecha_actual = datetime.now().strftime("%d/%m/%Y")
    
    
    # Conectar a la base de datos y realizar la consulta
    conexion = sql.connect("USUARIOS_WP.db")
    cursor = conexion.cursor()
    cursor.execute("""SELECT U.CELULAR, M.MENSAJE
                      FROM USUARIOS U 
                      JOIN MENSAJES M ON U.USUARIO_ID = M.USUARIO_ID
                      WHERE M.FECHA = ?""", (fecha_actual,))
    datos = cursor.fetchall()
    
    conexion.close()
    return datos

    
    
def enviar_automaticamente():
    datos = obtener_datos()
    for valor in datos:
        celular = valor[0]
        mensaje = valor[1]
        pywhatkit.sendwhatmsg_instantly(celular, mensaje)
        time.sleep(2)
    messagebox.showinfo("Mensaje", "Éxito: Mensajes enviados")