"""
All functions that can work as XOR
"""

import numpy
from numpy import *
import random
from random import *

class Perceptron():
	def __init__(self, w, th):
		self.weights = w
		self.threshold = th

	def step(self, num):
		if num > self.threshold:
			return 1
		else:
			return 0

	def eval(self):
		ins = []
		for i in self.inputs:
			ins.append(i.eval())
		x = array(ins)
		w = array(self.weights)
		return self.step(dot(x,w))

	def set_inputs(self, ins):
		self.inputs = ins

class Input(Perceptron):
	def __init__(self, num = 0):
		self.val = num
	def set_val(self, num):
		self.val = num
	def eval(self):
		return self.val

def a(num):
	if num > 0:
		return 1
	return 0

def perceptron_learn(train):
	w = array([0, 0, 0])
	for n in range(500):
		for x,y in train:
			f = a(dot(x,w))
			w = w + (y-f)*x
		s = 0.0
		for x,y in train:
			s += abs(y - a(dot(x,w)))
		accuracy = 1-s/len(train)
		if accuracy == 1.0:
			return w, accuracy
	return w, accuracy

funcs = list([])

for q in range(16):
	t = list()
	s = format(q, '04b')
	for i in range(4):
		d = format(i, '02b')
		t.append((array([int(d[0]),int(d[1]),1]),int(s[i])))
	weight, ac = perceptron_learn(t)
	funcs.append(weight)	

print(funcs)	

x1 = Input()
x2 = Input()

count = 0
for i in range(len(funcs)):
	for j in range(len(funcs)):
		for k in range(len(funcs)):
			p1 = Perceptron([funcs[i][0], funcs[i][1]], -1*funcs[i][2])
			p2 = Perceptron([funcs[j][0], funcs[j][1]], -1*funcs[j][2])
			p3 = Perceptron([funcs[k][0], funcs[k][1]], -1*funcs[k][2])

			p1.set_inputs([x1,x2])
			p2.set_inputs([x1,x2])
			p3.set_inputs([p1,p2])

			xor = p3

			outs = ""
			for ii in range(4):
				x = format(ii, '02b')
				x1.set_val(int(x[0]))
				x2.set_val(int(x[1]))
				outs = outs + str(xor.eval())
			if outs == '0110':
				count += 1
				print(i,j,k)
print(count)

"""
OUTPUT
1 7 4
1 8 8
2 4 7
2 11 11
4 2 7
4 13 11
7 1 2
7 14 1
8 1 8
8 14 4
11 2 13
11 13 14
13 4 13
13 11 14
14 7 1
14 8 2
"""
