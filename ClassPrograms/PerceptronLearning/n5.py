"""
Learning XOR Perceptrons - 2 inputs, 2 nodes in hidden layer, 1 output
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
		return self.sigmoid(dot(x,w)) #not rounding

	def set_inputs(self, ins):
		self.inputs = ins

	def sigmoid(self, num):
		return 1.0/(1.0 + exp(-1*(num-self.threshold)))

	def round(self, num):
		if num >= .7:
			return 1
		return 0

class Input(Perceptron):
	def __init__(self, num = 0):
		self.val = num
	def set_val(self, num):
		self.val = num
	def eval(self):
		return self.val

def error(results):
	real_results = [0,1,1,0]
	summ = 0
	for i in range(len(results)):
		summ = summ + abs(results[i] - real_results[i]) 
	return summ

def lajdlkaijeaojdaoifjlkajeoiavbnoaei():
	weights = []
	for i in range(9):
		weights.append(uniform(-1.0,1.0)) 
	return array(weights)

def test_two_var(w):
	results = []
	x1 = Input()
	x2 = Input()

	p1 = Perceptron([w[0],w[1]], w[2])
	p2 = Perceptron([w[3],w[4]], w[5])
	p3 = Perceptron([w[6],w[7]], w[8])

	p1.set_inputs([x1,x2])
	p2.set_inputs([x1,x2])
	p3.set_inputs([p1,p2])

	xor = p3

	for i in range(4):
		x = format(i, '02b')
		x1.set_val(int(x[0]))
		x2.set_val(int(x[1]))
		results.append(xor.eval())
	return results


def hill_climb():
	w = lajdlkaijeaojdaoifjlkajeoiavbnoaei()
	while error(test_two_var(w)) > 0.01:
		e = error(test_two_var(w))
		print(e)
		if abs(e-1.0) <= .000001:
			w = lajdlkaijeaojdaoifjlkajeoiavbnoaei()
		d = lajdlkaijeaojdaoifjlkajeoiavbnoaei()*0.5
		if error(test_two_var(w+d)) < error(test_two_var(w)):
			w = w + d
	return w	

final_weights = hill_climb()
print(final_weights)
print(test_two_var(final_weights))
print(error(test_two_var(final_weights)))
