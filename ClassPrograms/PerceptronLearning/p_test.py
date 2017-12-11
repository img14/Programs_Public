import numpy
from numpy import *
import random
from random import *

class Perceptron():
	def __init__(self, w, th):
		self.inputs = None
		self.weights = w
		self.threshold = th

	def step(self, num):
		if num > self.threshold:
			return 1
		else:
			return 0

	def eval(self):
		x = array(self.inputs)
		w = array(self.weights)
		return self.step(dot(x,w))

	def set_inputs(self, ins):
		self.inputs = ins

p1 = Perceptron([1,1], 0)

for i in range(4):
	x = format(i, '02b')
	p1.set_inputs([int(x[0]),int(x[1])])
	print("%s %s | %s"%(x[0],x[1],p1.eval()))
