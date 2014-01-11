'''
Created on Feb 10, 2013

@author: Boris Jurosevic
         CS 2430
         Modular Exponentiation
         algorithm 5
         tutorial : stackoverflow (question about converting to bin), wikepedia, youtube
'''
import math

def mod_anotherExponent(a, b, c):
    x = 1

    answer = bin(b)[:1:-1]
    
    if x == 1:
        p = (a) % (c)
    a = len(answer)
    for i in range(a):
        while answer[i] == '1':
            x *= p % c
            p *= p % c
            return x

print (mod_anotherExponent(7, 644, 645))
print (mod_anotherExponent(11, 644, 645))
print (mod_anotherExponent(3, 2003, 99))
print (mod_anotherExponent(123, 1001, 101))    
