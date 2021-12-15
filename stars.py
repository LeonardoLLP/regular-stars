from turtle import *
from math import gcd
from time import sleep

color = ('black', "white")
# Radio
r = 300
# Número de lados
n = 528
# Número de giros
full_rotations = 263

"""Proceso a seguir
En teoría, podemos usar la fórmula de los polígonos regulares para calcular las rotaciones necesarias para realizar la estrella. La fórmula de los ángulos de un polígono regular es
a = (180 * (n - 2)) / n.

Nosotros, al menos por ahora, usaremos:
x = (180 * (n - 2) + 360 * (full_rotations - 1)) / n

Esto nos dá el ángulo interior. Para pasarlo al ángulo exterior,

a = 180 - x

Multiplicamos el ángulo interior por full_rotations. Esto hace que se cierre más cuantas más rotaciones hallamos especificado. Tiene que estar entre 1 y n

Estaba pensando en dividir para cerrar en ángulo. Sin embargo, más grande a, más cerrado el ángulo interior (a determina rotación exterior)
"""


x = ((180 * (n - 2)) / n)

a = (180 - x) * full_rotations


# TODO: Error found. Need to adjust y to circle containing the figure
initial_coor = -r/2, -r

print(gcd(n, full_rotations))
sleep(2)

up()
speed(2)
goto(initial_coor)
print(abs(pos()))
down()
begin_fill()
speed(0)
rep = 1
while True:
    forward(r)
    left(a)

    print(rep)
    rep += 1

    if abs(initial_coor[0] - xcor()) < 0.5 and abs(initial_coor[1] - ycor()) < 0.5 :
        break

done()