"""
perceptron_learn finds a line with weights (a,b,c). The line separates data into true or false. It does this for each of the 16 possible functions f(x)
that take two binary variables and perform some boolean operation (and, or, xor, not) on them. 
In order to find the line, it uses the dot product. If the dot product is positive, that data is on the correct side of the line. 

Added:
perceptron learn function
structure to deal with multiple lengths
checks the accuracy of the 16 functions for two variables

Notes: #t = [(array([0,0,1]),int(s[0])),(array([0,1,1]),int(s[1])),(array([1,0,1]),int(s[2])),(array([1,1,1]),int(s[3]))]
"""
import numpy
from numpy import *
import random
from random import *

def a(num):
	if num > 0:
		return 1
	return 0

epoch = 1000
rate = 1
def perceptron_learn(train):
	w = array([randrange(-5,5), randrange(-5,5), randrange(-5,5)])
	for n in range(epoch):
		for x,y in train:
			f = a(dot(x,w))
			w = w + (rate*y-f)*x
	s = 0.0
	for x,y in train:
		s += abs(y - a(dot(x,w)))
	accuracy = 1-s/len(train)
	return w, accuracy

#2^(2^n)
#2^n
#2^n
#n
right = 0
for q in range(16):
	t = list()
	s = format(q, '04b')
	for i in range(4):
		d = format(i, '02b')
		t.append((array([int(d[0]),int(d[1]),1]),int(s[i])))
	weight, ac = perceptron_learn(t)
	print(weight, ac)
	if ac == 1.0:
		right = right + 1
print(right/16.0)