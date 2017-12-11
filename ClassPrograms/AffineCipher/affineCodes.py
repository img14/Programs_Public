"""
Methods to decode, encode and crack an affine cipher
"""

from cryptomath import *
from Cryptoalphabet import Cryptoalphabet

alpha = Cryptoalphabet("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def affine_encode(plaintext, a, b):
	e_string = ""
	for c in plaintext:
		i = alpha.getIndex(c)
		n = (a*i + b)%26
		e_string = e_string + alpha.charNum(n)
	return e_string

def affine_decode(ciphertext, a, b):
	d_string = ""
	ciphertext = alpha.prepare(ciphertext)
	for c in ciphertext:
		i = alpha.getIndex(c)
		a1,b1 = lin_inverse(a,b,26)
		n = (a1*i + b1)%26
		d_string = d_string + alpha.charNum(n)
	return d_string

def affine_crack(c1,p1,c2,p2):
	ct1 = alpha.getIndex(c1)
	pt1 = alpha.getIndex(p1)
	ct2 = alpha.getIndex(c2)
	pt2 = alpha.getIndex(p2)
	x = a_lin_sys_solve(pt1,ct1,pt2,ct2,26)
	y = lin_solve(1,x*pt1,ct1,26)
	return(x,y)

def affine_c_d(ciphertext,crib):
	c1 = ciphertext[0]
	p1 = crib[0]
	c2 = ciphertext[1]
	p2 = crib[1]
	x,y = affine_crack(c1,p1,c2,p2)
	#print(x,y)
	return affine_decode(ciphertext,x,y)
