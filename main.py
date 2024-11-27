import elementos as ele
import fuente_color as ft
import agregar_contacto
import ver_contactos
import ver_mensajes
import mensajes_de_hoy
import limpiar_mensajes
def nuevo_contacto(ventana):
    ventana.destroy()
    agregar_contacto.main()
    main()

def mostrar_contactos(ventana):
    ventana.destroy()
    ver_contactos.mostrar_datos()
    main()
def mostrar_mensajes(ventana):
    ventana.destroy()
    ver_mensajes.mostrar_datos()
    main()

def ver_mensajes_hoy(ventana):
    ventana.destroy()
    mensajes_de_hoy.mostrar_datos()
    main()
def limpiar_datos(ventana):
    limpiar_mensajes.LimpiarDatos()

def main():
    # Crear la ventana principal con título y color de fondo
    root = ele.Elementos("Menú principal", ft.negro)
    ancho_pantalla = root.winfo_screenwidth()
    alto_pantalla = root.winfo_screenheight()
    mitad_pantalla = ancho_pantalla / 2
    pos_altura = alto_pantalla - alto_pantalla
    
    # Agregar un Label con todos los parámetros definidos
    root.BotonAccion(
        texto = "Añadir contacto",      # Texto del Label
        fuente = ft.FUENTE,               # Fuente
        ancho = ft.ancho,                    # Ancho del Label
        altura = ft.altura,                    # Altura del Label
        color = ft.azul,             # Color de fondo
        posx = mitad_pantalla,                    # Posición en X
        posy = pos_altura + 25 ,               #Posición en Y
        funcion = nuevo_contacto ,
        entrada = root                 
    )

    root.BotonAccion(
        texto = "Ver contactos",      # Texto del Label
        fuente = ft.FUENTE,               # Fuente
        ancho = ft.ancho,                    # Ancho del Label
        altura = ft.altura,                    # Altura del Label
        color = ft.azul,             # Color de fondo
        posx = mitad_pantalla,                    # Posición en X
        posy = pos_altura + 145 ,               #Posición en Y
        funcion = mostrar_contactos ,
        entrada = root                 
    )

    root.BotonAccion(
        texto = "Ver mensajes",      # Texto del Label
        fuente = ft.FUENTE,               # Fuente
        ancho = ft.ancho,                    # Ancho del Label
        altura = ft.altura,                    # Altura del Label
        color = ft.azul,             # Color de fondo
        posx = mitad_pantalla,                    # Posición en X
        posy = pos_altura + 265 ,               #Posición en Y
        funcion = mostrar_mensajes ,
        entrada = root                 
    )

    root.BotonAccion(
        texto = "Mensajes de hoy",      # Texto del Label
        fuente = ft.FUENTE,               # Fuente
        ancho = ft.ancho ,                    # Ancho del Label
        altura = ft.altura,                    # Altura del Label
        color = ft.azul,             # Color de fondo
        posx = mitad_pantalla,                    # Posición en X
        posy = pos_altura + 385 ,               #Posición en Y
        funcion = ver_mensajes_hoy ,
        entrada = root                 
    )

    root.BotonAccion(
        texto = "Limpiar",      # Texto del Label
        fuente = ft.FUENTE,               # Fuente
        ancho = ft.ancho ,                    # Ancho del Label
        altura = ft.altura,                    # Altura del Label
        color = ft.azul,             # Color de fondo
        posx = mitad_pantalla,                    # Posición en X
        posy = pos_altura + 525 ,               #Posición en Y
        funcion = limpiar_datos ,
        entrada = root                 
    )

    
    
    # Iniciar el bucle principal
    root.mainloop()

main()
