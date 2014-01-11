'''
Created on Feb 18, 2013

@author: Boris Jurosevic
Assignment : CS 2430 Recursion/Iteration Contrast
References: wiki, stackoverflow, python book,khan academy
       
'''


def expt_rec(b, e, n):
    b = b % n
    
    if e == 0:
        return 1
    elif e == 1:
        return b
    elif e % 2 == 0:
        p = b * b % n
        return expt_rec(p, e // 2, n) 
    else:
        return b * expt_rec(b, e - 1, n) % n
        
print ("modular exponentiation algorithm")       

print (expt_rec(7,644,645))
print (expt_rec(11,644,645))
print (expt_rec(3,2003,99))
print (expt_rec(123,1001,101))



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

print ("recursive modular exponentiation algorithm")    
print (alg(7,644,645))
print (alg(11,644,645))
print (alg(3,2003,99))
print (alg(123,1001,101))   
    