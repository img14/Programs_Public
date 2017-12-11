"""
1D Minimization
"""
import random
from random import *

def g(x):
		return (x-3)**2

'''def minimize(f,a,b,e):
		while b-a > e:
				#c = uniform(a, b)
				#d = uniform(c, b)
				print(a,b)
				c = (b-a)/3.0
				d = 2*(b-a)/3.0
				if f(c) < f(d):
						b = d
				else:
						a = c
		return a'''

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
		

print(minimize(g,-10.0, 10.0, 0.0000001))
