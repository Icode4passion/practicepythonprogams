#Write a Python program which accepts the radius of a circle from the user and compute the area.

import math

radius = float(raw_input("Enter the radius of the Circle"))
# area = math.pi * radius * radius
# print area

def square(num):
	return num * num 

def area(rad):
	return math.pi * square(rad)

print area(radius)