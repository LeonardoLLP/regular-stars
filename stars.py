from turtle import *

pencolor("black")

# Radio
r = 200
# Número de lados
n = 6
# Número de giros
full_rotations = 1

"""Proceso a seguir
En teoría, podemos usar la fórmula de los polígonos regulares para calcular las rotaciones necesarias para realizar la estrella. La fórmula de los ángulos de un polígono regular es
a = (180 * (n - 2)) / n.

Nosotros, al menos por ahora, usaremos:
a = ((180 * (n - 2) + 360 * (full_rotations - 1)) / n
"""