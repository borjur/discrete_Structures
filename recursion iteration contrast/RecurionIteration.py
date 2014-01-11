'''
Created on Feb 19, 2013

@author: Boris Jurosevic
Assignment : CS 2430 Recursion/Iteration Contrast
References: wiki, stackoverflow, python book,khan academy
       
'''



def recursive_fib (n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return recursive_fib(n - 1) + recursive_fib(n - 2)
    
print ("recursive algorithm is")    
    
for i in range(15):
    print (recursive_fib(i))
    
    
    
def iterative_fib (n): 
    a = 0
    b = 1
    
    if( n == 0):
        return 0
    else:
        for i in range(1,n):
            z = (a + b)
            a = b
            y = z
            
        else:
            return y
        
print ("and iterative algorithm is")          
    
for i in range(15):
    print (recursive_fib(i))
        
        
       
    
    
    
    
        
    