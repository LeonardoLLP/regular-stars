# Regular stars
[Dirección del repositorio]
## Proceso a seguir
En teoría, podemos usar la fórmula de los polígonos regulares para calcular las rotaciones necesarias para realizar la estrella. La fórmula de los ángulos de un polígono regular es
a = (180 * (n - 2)) / n.

Sin embargo, si queremos que realize rotaciones extra (para que forme estrellas), tendremos que hacer que gire más veces. Es decir, reducir el ángulo en 360 / n hace que realize una rotación más. Sin embargo, podemos simplificar los cálculos realizando esta operación con el ángulo exterior.

Como la tortuga se mueve desde uno extremo del segmento, necesita el ángulo exterior a girar. La fórmula en cuestión es

a = 180 - x * full_rotations % n

Multiplicamos el ángulo externo por full_rotations. Esto hace que se cierre más cuantas más rotaciones hallamos especificado. Tiene que estar entre 1 y n (mayor que n es lo mismo que volver a 1 hasta n)

Antes de imprimir, desplazamos la tortuga para ver la figura en el centro. La x es fácil, pero la y puede ser muy complicada de hallar, ya que el radio total de la circunferencia más pequeña que contiene a la figura puede variar mucho. La fórmula hallada fue a base de provar con factores que creía que afectaban a las dimensiones de la figura multiplicados por coeficientes también obtenidos mediante pruebas.


Diagrama de flujo:

![flowchart](https://github.com/LeonardoLLP/regular-stars/blob/main/stars.drawio.png)

Código:

```python
from turtle import *
from math import gcd, sin, pi
from time import sleep
import time

t_speed = int(input("Please choose the speed of the turtle (1 slowest / 11 fastest): "))

if t_speed < 1:
    t_speed = 1
elif t_speed > 10:
    t_speed = 0

# Ditancia de lado
d = 200  # TODO: hacer que se escale automáticamente para ocupar máximo posible (que se vea bien) de pantalla.

# Número de lados
while True:
    try:
        n = int(input("Please choose number of sides: "))
        break
    except:
        print("That's not a valid number.")
# n = 19

# Número de giros
while True:
    try:
        full_rotations = int(input("Choose rotation number (seed): "))
        break
    except:
        print("That's not a valid number.")
# full_rotations = 5


# Real n (for calculations)
rn = n // gcd(full_rotations, n)



#! CALCULATIONS
# Internal angle of regular poligon
x = (180 * (n - 2)) / n

# External angle of star
a = (180 - x) * (full_rotations % n)
a_radians = (a / 180) * pi

# Internal angle of star
internal_angle = 180 - a

# Calculate where the center of the figure lands and use it to move the starting_coor
# Time calculation for performance check: https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
angle = 0
y_pos = 0
y_list = []
angle_list = []  # TODO: Unnecesary variable. Just to check. Remove
start_time = time.time()
for _ in range(rn):
    y_pos += d * sin(angle)
    y_list.append(y_pos)
    angle += a_radians
    angle_list.append(angle)

center_y = 0
for coor in y_list:
    center_y += coor

diameter = max(y_list) - min(y_list)

center_y /= rn
print(center_y)
print(angle_list)
print(y_list)


print("Time: {:4}".format(time.time() - start_time))
print("Done")
# sleep(2)


print(d)
print(center_y)
# sleep(2)


#! CANVAS SETUP
# Getting screen size: https://stackoverflow.com/questions/3949844/how-can-i-get-the-screen-size-in-tkinter/3949983#3949983
from tkinter import Tk
root = Tk()
screen_width = root.winfo_screenwidth() - 0
screen_height = root.winfo_screenheight() - 50
root.destroy()  # Don't want tinker window to open

screen = Screen()
screen.setup(width=screen_width, height=screen_height, startx=None, starty=5)


#! TURTLE SETUP

# Update d
d *= (screen_height - 50) / diameter
center_y *= (screen_height - 50) / diameter
# Cálculo de coordenadas iniciales
initial_coor = -d/2, -center_y

color = ('black', "white")
up()
speed(1)
goto(initial_coor)
down()


print(d)

#! DRAWING THE STAR
begin_fill()
speed(t_speed)

rep = 1
while True:
    forward(d)
    left(a)

    # print(rep)
    # rep += 1

    if abs(initial_coor[0] - xcor()) < 0.5 and abs(initial_coor[1] - ycor()) < 0.5 :
        break

done()
```
