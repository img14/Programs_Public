"""
Test the primality of large numbers
"""
import random
import sympy
from sympy import *

def primetest(m, k):
	r,d = factor(m-1)
	for i in range(k):
		a = random.randrange(2, m-1)
		x = pow(a, d, m)
		if x == 1 or x == m - 1:
			continue
		for i in range(r):
			x = pow(x, 2, m)
			if x == 1:
				return False
			if x == m - 1:
				continue
		return False
	return True

def factor(n):
	x = 0
	while n%2 == 0:
		n = n/2
		x = x+1
	return x, int(n)

for k in range(1, 100):
	a = [0]*1000
	for i in range(1000):
		a[i] = random.randrange(2**200, 2**250)

	sympyprime = [0]*1000
	for j in range(1000):
		if isprime(a[j]):
			sympyprime[j] = 1

	myprime = [0]*1000
	for l in range(1000):
		if primetest(a[l], k):
			myprime[l] = 1

	correct = 0
	for z in range(1000):
		if sympyprime[z] == myprime[z]:
			correct += 1
	print("%s: %s"%(k,correct))

c = []
f = open("carmichael.txt",'r')
for i in f:
	c.append(int(i))

for n in c:
	k = 1
	x = primetest(n, k)
	while x == True:
		k = k+1
		x = primetest(n, k)
	print("%s: %s"%(n, k))


'''
for k in range(1, 100):
	sum = 0
	for i in range(100):
		a = [0]*1000
		for i in range(1000):
			a[i] = random.randrange(2^200, 2^250)

		sympyprime = [0]*1000
		for j in range(1000):
			if isprime(a[j]):
				sympyprime[j] = 1

		myprime = [0]*1000
		for l in range(1000):
			if primetest(a[l], k):
				myprime[l] = 1

		correct = 0
		for z in range(1000):
			if sympyprime[z] == myprime[z]:
				correct += 1
		sum = sum + correct
	print("%s: %s"%(k,sum/100))
'''
