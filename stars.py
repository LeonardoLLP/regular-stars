from turtle import *
from math import gcd
from time import sleep


# Radio
r = 200
# Número de lados
n = 528
# Número de giros
full_rotations = 79



#! CALCULATIONS
# Internal angle of regular poligon
x = (180 * (n - 2)) / n

# External angle of star
a = (180 - x) * (full_rotations % n)

# Internal angle of star
internal_angle = 180 - a




# Cálculo de coordenadas iniciales
initial_coor = -r/2, -r * (internal_angle / 125)  # / t_rot ???


#! INITIAL SETUP
color = ('black', "white")
up()
speed(2)
goto(initial_coor)
print(abs(pos()))
down()

#! DRAWING THE STAR
begin_fill()
speed(0)

rep = 1
while True:
    forward(r)
    left(a)

    # print(rep)
    # rep += 1

    if abs(initial_coor[0] - xcor()) < 0.5 and abs(initial_coor[1] - ycor()) < 0.5 :
        break

done()