from turtle import *
from math import gcd, sin, pi
from time import sleep
import time


# Ditancia de lado
d = 200  # TODO: hacer que se escale automáticamente para ocupar máximo posible (que se vea bien) de pantalla.

# Número de lados
# while True:
#     try:
#         n = int(input("Please choose number of sides: "))
#         break
#     except:
#         print("That's not a valid number.")
n = 19

# Número de giros
# while True:
#     try:
#         full_rotations = int(input("Choose rotation number (seed): "))
#         break
#     except:
#         print("That's not a valid number.")
full_rotations = 5


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

diameter = max(y_list)

center_y /= rn
print(center_y)
print(angle_list)
print(y_list)


print("Time: {:4}".format(time.time() - start_time))
print("Done")
# sleep(2)

# Cálculo de coordenadas iniciales
initial_coor = -d/2, -center_y

print(d)
print(center_y)
# sleep(2)


#! CANVAS SETUP
# Getting screen size: https://stackoverflow.com/questions/3949844/how-can-i-get-the-screen-size-in-tkinter/3949983#3949983
from tkinter import Tk
root = Tk()
screen_width = root.winfo_screenwidth() - 10
screen_height = root.winfo_screenheight() - 10
root.destroy()  # Don't want tinker window to open

print(screen_width)
print(screen_height)

screen = Screen()
screen.setup(width=screen_width, height=screen_height, startx=None, starty=None)


#! TURTLE SETUP
color = ('black', "white")
up()
speed(1)
goto(initial_coor)
print(abs(pos()))
down()

#! DRAWING THE STAR
begin_fill()
speed(0)

rep = 1
while True:
    forward(d)
    left(a)

    # print(rep)
    # rep += 1

    if abs(initial_coor[0] - xcor()) < 0.5 and abs(initial_coor[1] - ycor()) < 0.5 :
        break

done()