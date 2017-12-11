'''
Test majority accuracy with perceptron
'''
import csv
import math
import random
from random import *
import numpy
from numpy import *

def majority(lis):
	s = 0
	for i in lis:
		s += int(i)
	if s > len(lis)/2:
		return 1
	else:
		return 0

def a(num):
	if num > 0:
		return 1
	return 0

epoch = 500
rate = 1
def perceptron_learn(train):
	w = array([randrange(-1,1)]*11)
	for n in range(epoch):
		for x,y in train:
			f = a(dot(x,w))
			w = w + (rate*y-f)*x
	return w

fullset = list()
for i in range(1024):
	s = format(i, '010b')
	l = list(s)
	li = list()
	for it in l:
		li.append(int(it))
	li.append(1)
	ar = array(li)
	fullset.append((ar,majority(l)))


for st in range(10, 110):
	summ = 0.0
	for lkjfdalskjds in range(50):
		rows = []
		start = st
		while start > 0:
			z = randrange(len(fullset))
			if not z in rows:
				rows.append(z)
				start -= 1

		testdata = list()
		testtrain = list()
		for r in range(1024):
			if r in rows:
				testtrain.append(fullset[r])
			else:
				testdata.append(fullset[r])

		weights = perceptron_learn(testtrain)
		s = 0.0
		for x,y in testdata:
			s += abs(y - a(dot(x,weights)))
		accuracy = 1-s/len(testdata)
		#print(accuracy)
		summ+=accuracy
	print(summ/50.0)
