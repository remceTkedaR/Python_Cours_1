# Problem Solver Exercise
##########################
# By Ed Covert
##########################
# Write a function called area_of_circle that takes radius as input and returns the  # area of a circle. The area of a circle is equal to pi times the radius squared.
# (Use the math.pi in order to represent Pi.)
##########################

import math


def area_of_circle(r):
    """Funkcja obliczenia pola powierzchni koła pi * r2"""
    a = r**2 * math.pi
    return a


print(area_of_circle(2))  # wylicz pole powierzchni z ()