'''
Created on Feb 10, 2013

@author: Boris Jurosevic
         CS 2430
         Modular Exponentiation
         algorithm 1
         tutorial : stackoverflow (question about converting to bin), wikepedia, youtube, yahoo ansr (about list.append)
'''



def mod_Exponent(i,j, answer):
    if j == 0:
        return 1
    m = i
    z = 0
    list = []
    while m != 0:
        list.append(m % j) 
        m = m // j
        z += 1
        
        return z and list
    
    
print (mod_Exponent(7,644,645))
print (mod_Exponent(11,644,645))
print (mod_Exponent(3,2003,99))
print (mod_Exponent(123,1001,101))
    
    
    
    
    
    
