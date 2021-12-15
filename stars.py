from turtle import *
color = ('black', "white")

# Radio
r = 300
# Número de lados
n = 528
# Número de giros
full_rotations = 79

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

# TODO: Full_rotations no funciona
x = ((180 * (n - 2)) / n)

a = (180 - x) * full_rotations

up()
speed(2)
goto(-r/2, -r/2)
down()
begin_fill()
speed(0)
rep = 1
while True:
    forward(r)
    left(a)
    if abs(pos()) < 1:
        break

    print(rep)
    rep += 1

done()