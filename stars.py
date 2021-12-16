from turtle import *
from math import gcd
from time import sleep

color = ('black', "white")
# Radio
r = 300
# Número de lados
n = 528
# Número de giros
full_rotations = 79



# Internal angle of regular poligon
x = (180 * (n - 2)) / n


print(x)

a = (180 - x) * full_rotations % n

internal_angle = 180 - a

t_rot = gcd(full_rotations, n)

"""Ni idea de donde sale el 120. El /2 si, pero el 120 no se porqué pero es el valor que funciona"""
initial_coor = -r/2, -r * (internal_angle / 125)  # / t_rot ???

print(t_rot)
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