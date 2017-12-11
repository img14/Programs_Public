"""
Program to encode and decode RSA messages
"""
import sympy
from sympy import *
import random

def choose_modulus(k,l,m):
	p1 = find_prime(k,l)
	p2 = find_prime(k,l)
	while not abs(log(p1,2) - log(p2,2)) < m:
		p1 = find_prime(k,l)
		p2 = find_prime(k,l)
	return p1,p2

def choose_encryption_key_old(m):
	e = random.randrange(2,m)
	while not gcd(e, totient(m)) == 1:
		e = random.randrange(2,m)
	return e

def choose_encryption_key(p1,p2):
	m = p1*p2
	e = random.randrange(2, p1*p2)
	while not gcd(e, (p1-1)*(p2-1)) == 1:
		e = random.randrange(2, p1*p2)
	return e

def compute_decryption_key(e, p1, p2):
	d = inv_mod(e, (p1-1)*(p2-1))
	return d

def RSA_encrypt(P, e, m):
	return power_mod(P,e,m)

def RSA_decrypt(C, d, m):
	return power_mod(C,d,m)

def RSA_crack(C, e, m):
	return power_mod(C, inv_mod(e,totient(m)), m)

def power_mod(a, b, m):
	return pow(a,b,m)

def string_to_int(s):
	return int.from_bytes(s.encode(),'big')

def int_to_string(n):
	return n.to_bytes((n.bit_length()+7)//8,'big').decode().strip()

def find_prime(k, l):
	x = random.randrange(2**k+2, 2**l-1)
	while (not isprime(x)):
		x = random.randrange(2**k+2, 2**l-1)
	return x

def xgcd(b, n):
	x0, x1, y0, y1 = 1, 0, 0, 1
	while n != 0:
		q, b, n = b // n, n, b % n
		x0, x1 = x1, x0 - q * x1
		y0, y1 = y1, y0 - q * y1
	return b, x0, y0

def inv_mod(b, n):
	g, x, _ = xgcd(b, n)
	if g == 1:
		return x % n

"""
RSA Message Exchange
"""

#Our numbers
pi,pj = choose_modulus(200,204,50)
my_mod = pi * pj
my_enc_key = choose_encryption_key(pi, pj)
print("My Primes: ", pi, pj)
print("My Modulus: ", my_mod)
print("My Encryption Key: ", my_enc_key)

#Encoding a message with someone else's numbers
their_mod = 9974085880263379580394176919091237671243630991492368310958180254243729015156794407476067877070352245916181312913506081413978120979798227144179681175879
their_enc_key = 1274570651282105475941777766587577582023518221190732522597076146804533049158766343138826132941234187595481937482071481202376751312818066989598920155989
messageString = "Hi. This is a creative message."
messageBytes = string_to_int(messageString)
print("Message: ", messageBytes)
encMessage = RSA_encrypt(messageBytes, their_enc_key, their_mod)
print("Encoded Message: ", encMessage)

#Decoding the message sent to us
#my_dec_key = compute_decryption_key(my_enc_key, pi, pj)
my_dec_key = compute_decryption_key(9034302786477632084177231467338707794932890382219531012244768011578912282025102742921209071808720002426284716566453084939, 2852799332826165576549683721934686650431760177477582224441789, 10582260058434591375044316914661108554362583639774055485540087)
messageReceived = 7685639402658570041332092386730857722829508721500337074039018855544141530770944219201236076815619964810541252211564571230
decMessage = RSA_decrypt(messageReceived, my_dec_key, 30189064434495182222794692701630732429757499485911917941672183961436119037704394785112588879375758643631173789514757495643)
print("Dec Bytes: ", decMessage)
decString = int_to_string(decMessage)
print("Decoded Message: ", decString)

