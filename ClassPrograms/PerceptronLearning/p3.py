"""
4 variables
Break out of for loop if accuracy is equal to 1.0
"""
import numpy
from numpy import *
import random
from random import *

def a(num):
	if num > 0:
		return 1
	return 0

epoch = 500
rate = 1

def perceptron_learn(train):
	w = array([randrange(-1,1), randrange(-1,1), randrange(-1,1), randrange(-1,1), randrange(-1,1)])
	for n in range(epoch):
		for x,y in train:
			f = a(dot(x,w))
			w = w + (rate*y-f)*x
		s = 0.0
		for x,y in train:
			s += abs(y - a(dot(x,w)))
		accuracy = 1-s/len(train)
		if accuracy == 1.0:
			return w, accuracy
	return w, accuracy

right = 0
for q in range(65536):
	t = list()
	s = format(q, '016b')
	for i in range(16):
		d = format(i, '04b')
		t.append((array([int(d[0]),int(d[1]),int(d[2]),int(d[3]),1]),int(s[i])))
	weight, ac = perceptron_learn(t)
	print(weight, ac)
	if ac == 1.0:
		right = right + 1
print(right/65536.0)