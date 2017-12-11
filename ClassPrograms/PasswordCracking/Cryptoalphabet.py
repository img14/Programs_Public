from sympy import *


def matrix_mod(M, m):
    return M.applyfunc(lambda x: Mod(x, m))

class Cryptoalphabet:
    def __init__(self, alphabet):
        self.alphabet = alphabet.upper()
        self.m = len(self.alphabet)

    def getIndex(self, c):
        c = c.upper()
        return self.alphabet.index(c)

    def charNum(self, i):
        i = i % len(self.alphabet)
        return self.alphabet[i]

    def prepare(self, s):
        v = ""
        for c in s:
            if c in self.alphabet:
                v = v + c.upper()
        return v

    def digraphToInt(self, s):
        a = self.getIndex(s[0]) + 1
        b = self.getIndex(s[1]) + 1
        return 26*a+b
    def intToDigraph(self, i):
        a = self.charNum(i/26 - 1)
        b = self.charNum(i%26 - 1)
        s = a+b
        return s

    def pad_s(self, s, padchar="X"):
        """ Add padchar (default 'X') to s if length of s is odd"""
        if len(s)%2 == 1:
            s = s + padchar
        return s
    
    def pad_a(self, a, padchar="X"):
        """ Add the numerical value of padchar (default 'X') to list a if length of a is odd """
        # you may not need this function in your code
        if len(a)%2 == 1:
            a.append(self.getIndex(padchar))
        return a
    
    def StoM(self, S):
        """ Return a 2 x C matrix formed from the even-length string S, where C = len(S)/2"""
        return Matrix(self.stoa(S)).reshape(len(self.stoa(S)) // 2, 2).transpose()

    def MtoS(self, M):
        """ Turn a 2 x C matrix of numbers into a string S, where len(S) = C*2 """
        s = ""
        S = Matrix(M.transpose().reshape(1,len(M.row(0))*2))
        for i in S.row(0):
            s = s + str(self.charNum(i))
        return s
    
    def stoa(self, s):
        """ Turn a string s into an (even-length) list of numbers, using getIndex(),
            padding the string with an extra char at the end if necessary """
        a = []
        s = self.pad_s(s)
        for c in s:
            a.append(self.getIndex(c))
        return a
    
    def atos(self, a):
        """ Turn a list of numbers into a string, using charNum(),
            does not assume len(a) is even """
        s = ""
        a = self.pad_a(a)
        for x in a:
            s = s + str(x)
        return s
