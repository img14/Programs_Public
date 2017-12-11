"""
Perceptron Learn of 14/16 functions for 2 inputs
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
	w = array([0,0,0])
	for n in range(epoch):
		for x,y in train:
			f = a(dot(x,w))
			w = w + (rate*y-f)*x
	s = 0.0
	for x,y in train:
		s += abs(y - a(dot(x,w)))
	accuracy = 1-s/len(train)
	return w, accuracy

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