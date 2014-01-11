'''
Created on Feb 16, 2013

@author: Agape
'''
def alg(base, exp, modulus) :
    base %= modulus
    p = 0

    if (exp == 0):
        p = 1
    elif (exp%2):
        exp = exp - 1
        z = alg(base,exp,modulus)
        p = base * z
    else :
        exp = exp // 2
        y = alg(base,exp,modulus)
        p = y
        p *= p

    return p%modulus

