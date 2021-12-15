from turtle import *
color = ('black', "white")

# Radio
r = 200
# Número de lados
n = 5
# Número de giros
full_rotations = 2

"""Proceso a seguir
En teoría, podemos usar la fórmula de los polígonos regulares para calcular las rotaciones necesarias para realizar la estrella. La fórmula de los ángulos de un polígono regular es
a = (180 * (n - 2)) / n.

Nosotros, al menos por ahora, usaremos:
a = (180 * (n - 2) + 360 * (full_rotations - 1)) / n
"""

x = (180 * (n - 2) + 360 * (full_rotations - 1)) / n

a = 180 - x


begin_fill()
while True:
    forward(r)
    left(a)
    if abs(pos()) < 1:
        break
done()