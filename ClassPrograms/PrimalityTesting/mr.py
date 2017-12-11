"""
Use the Miller-Rabin Primality test to determine primality of numbers
"""

import random
import sympy
from sympy import *
import sys
from sys import *

def rabinMiller(num):
    # Returns True if num is a prime number.

    s = num - 1
    t = 0
    while s % 2 == 0:
        # keep halving s while it is even (and use t
        # to count how many times we halve s)
        s = s // 2
        t += 1

    for trials in range(1): # try to falsify num's primality 5 times
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1: # this test does not apply if v is 1.
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True

def miller_rabin(n, k=1):
    if n == 2:
        return True
    if not n & 1:
        return False

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for i in range(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    s = 0
    d = n - 1

    while d % 2 == 0:
        d >>= 1
        s += 1

    for i in range(k):
        a = random.randrange(2, n - 1)
        if not check(a, s, d, n):
            return False
    return True

def is_probable_prime(n, k = 7):
   """use Rabin-Miller algorithm to return True (n is probably prime)
      or False (n is definitely composite)"""
   if n < 6:  # assuming n >= 0 in all cases... shortcut small cases here
      return [False, False, True, True, False, True][n]
   elif n & 1 == 0:  # should be faster than n % 2
      return False
   else:
      s, d = 0, n - 1
      while d & 1 == 0:
         s, d = s + 1, d >> 1
      # Use random.randint(2, n-2) for very large numbers
      for a in random.sample(range(2, min(n - 2, sys.maxsize)), min(n - 4, k)):
         x = pow(a, d, n)
         if x != 1 and x + 1 != n:
            for r in range(1, s):
               x = pow(x, 2, n)
               if x == 1:
                  return False  # composite for sure
               elif x == n - 1:
                  a = 0  # so we know loop didn't continue to end
                  break  # could be strong liar, try another a
            if a:
               return False  # composite if we reached end of this loop
      return True  # probably prime if reached end of outer loop

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
        if is_probable_prime(a[l], k):
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
    x = is_probable_prime(n, k)
    while x == True:
        k = k+1
        x = is_probable_prime(n, k)
    print("%s: %s"%(n, k))
