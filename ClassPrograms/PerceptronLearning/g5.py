"""
Gradient Descent with minimized lambda
"""
import numpy
from numpy import *
import random
from random import *

def f(v):
	x,y = v[0], v[1]
	return 4*(x**2) - 3*x*y + 2*(y**2) + 24*x - 20*y

def minimize(z,a,b,e):
	while b-a > e:
		print(b,a)
		c = a + (b-a)/3.0
		d = a + 2*(b-a)/3.0
		if z(c) < z(d):
			b = d
		else:
			a = c
	return a

def gradient(v):
	x,y = v[0], v[1]
	return array([(8*x - 3*y + 24),(-3*x + 4*y - 20)])

def magnitude(v):
	return sqrt(v[0]**2 + v[1]**2)

def gradient_descent():
	count = 0
	v = array([randrange(-10,10), randrange(-10,10)])
	while magnitude(gradient(v)) > .00000001:
		l = minimize(lambda a: f(v-a*gradient(v)), 0,1,.0001)
		v = v - l*gradient(v)
		count += 1
	return v, l, count

print(gradient_descent())

