'''
Created on Jan 18, 2013
CS 2430 Factorial Assignment
@author: Boris Jurosevic
references = I have used Python book to see how loops works and stackoverflow to see 
how the formula works and I have made it into my own
'''
print ("factorial numbers are from 1 to 100 are:")

def isFactorial(n):
    result = 1
    
    if n < 0:
        print ("number is negative")
    
    if n > 1:
        result = isFactorial(n - 1) * n
    return result
for num in range(1,101):
    
 print (num , isFactorial(num))
 
print ("factorial of a 500 is") 
print (isFactorial(500))





     


    
    
 

        
        