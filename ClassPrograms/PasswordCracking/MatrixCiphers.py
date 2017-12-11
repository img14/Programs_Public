from Cryptoalphabet import *
from sympy import *
from random import randint

def encrypt(E, p, a):
    """Apply matrix E to string p mod 26 and return an encrypted string,
       relative to Cryptoalphabet a """
    return a.MtoS(matrix_mod(E*a.StoM(p),len(a.alphabet)))

def decrypt(D, c, a):
    """Apply matrix D to string c mod 26 and return a decrypted string,
       relative to Cryptoalphabet a """
    return a.MtoS(matrix_mod(D*a.StoM(c),len(a.alphabet)))

def get_decryption_matrix(P,C, a):
    """ Knowing two digraphs in string P are encoded as string C, determine
        a unique decryption matrix, relative to Cryptoalphabet a """
    p = a.StoM(P)
    c = a.StoM(C)
    if gcd(c.det(), len(a.alphabet)) > 1:
        ci = get_random_invertible_matrix(len(a.alphabet))
    else:
        ci = c.inv_mod(len(a.alphabet))
    D = matrix_mod(p*ci,len(a.alphabet))
    return D

def get_random_invertible_matrix(m):
    """ return a random 2x2 matrix M with gcd(det(M),m)= 1 """
    d = 2
    while d>1:
        M = Matrix([[randint(0,m-1), randint(0,m-1)],[randint(0,m-1), randint(0,m-1)]])
        d = gcd(M.det(), m)
    return M
