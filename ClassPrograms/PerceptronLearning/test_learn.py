"""
Testing learned weights
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
				
				

x1 = Input()
x2 = Input()

p1 = Perceptron([-6.89,7.65], 3.83)
p2 = Perceptron([6.07,-6.94], 2.89)
p3 = Perceptron([13.2,13.7], 6.85)

p1.set_inputs([x1,x2])
p2.set_inputs([x1,x2])
p3.set_inputs([p1,p2])

xor = p3

for i in range(4):
	x = format(i, '02b')
	x1.set_val(int(x[0]))
	x2.set_val(int(x[1]))
	print("%s %s| %s"%(x1.val, x2.val,xor.eval()))
