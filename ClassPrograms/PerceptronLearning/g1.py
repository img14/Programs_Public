"""
Gradient Descent
"""
import numpy
from numpy import *
import random
from random import *

#f(x,y) = 4x^2 - 3xy + 2y^2 + 24x - 20y

def gradient(v):
	x,y = v[0], v[1]
	return array([(8*x - 3*y + 24),(-3*x + 4*y - 20)])

def magnitude(v):
	return sqrt(v[0]**2 + v[1]**2)

def gradient_descent():
	l = .2
	iterations = 0
	v = array([randrange(-10,10), randrange(-10,10)])
	while magnitude(gradient(v)) > .00000001:
		iterations += 1
		v = v - l*gradient(v)
	return v, iterations

print(gradient_descent())