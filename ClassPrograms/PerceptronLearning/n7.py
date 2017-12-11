"""
Combining multiple perceptron objects to make unit circle
-Using sigmoid instead of step
-changing rounding and k parameters
"""
import numpy
from numpy import *
import random
from random import *
import math
from math import *

class Perceptron():
	def __init__(self, w, th):
		self.weights = w
		self.threshold = th

	def my_round(self, num):
		if num >= 0.6:
			return 1.0
		return 0

	def sigmoid(self, num):
		return 1.0/(1.0 + exp(-5*(num-self.threshold)))

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
		return self.my_round(self.sigmoid(dot(x,w)))

	def set_inputs(self, ins):
		self.inputs = ins

class Input(Perceptron):
	def __init__(self, num = 0):
		self.val = num
	def set_val(self, num):
		self.val = num
	def eval(self):
		return self.val

def circle(x,y):
	if x**2 + y**2 <= 1:
		return 1
	return 0
							
x1 = Input()
x2 = Input()

p1 = Perceptron([1,0], -1)
p2 = Perceptron([-1,0], -1)
p3 = Perceptron([0,1], -1)
p4 = Perceptron([0,-1],-1)
p5 = Perceptron([sqrt(2)/2,sqrt(2)/2], -1)
p6 = Perceptron([-sqrt(2)/2,sqrt(2)/2], -1)
p7 = Perceptron([sqrt(2)/2,-sqrt(2)/2], -1)
p8 = Perceptron([-sqrt(2)/2,-sqrt(2)/2],-1)
p9 = Perceptron([1,1,1,1,1,1,1,1], 7.5) 

p1.set_inputs([x1,x2])
p2.set_inputs([x1,x2])
p3.set_inputs([x1,x2])
p4.set_inputs([x1,x2])
p5.set_inputs([x1,x2])
p6.set_inputs([x1,x2])
p7.set_inputs([x1,x2])
p8.set_inputs([x1,x2])
p9.set_inputs([p1, p2, p3, p4,p5,p6,p7,p8])

count = 0.0
correct = 0.0
for x in arange(-1.5,1.5,.1):
	for y in arange(-1.5,1.5,.1):
		x1.set_val(x)
		x2.set_val(y)
		val = p9.eval()
		real_val = circle(x,y)
		if real_val == val:
			correct += 1
		count +=1
print(correct/count)