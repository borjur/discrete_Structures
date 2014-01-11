'''
Created on Mar 2, 2013

@author: Boris Jurosevic
         CS 2420
         Assignment Bayes Theorem
         TUTORIAL: Kochanski website, module videos, stackoverflow, python forum, google and wiki
         http://stattrek.com/online-calculator/bayes-rule-calculator.aspx 
'''
import math
import time


def inter_func(number):
    for a in range(0, len(number)-1):
        
        num = number[a]
        den = number[a] + number[a + 1]
        num_1 = number[a + 1]
        den_1 = number[a + 1] + number[a]
        
            
        print (("p( A%d|B ) = %f \np( A%d|B ) = %f") %( a+1, num / (den), a+2, (num_1 / (den_1)) ))
        

def cond_func(number):
    print (number)
    for b in range(0, len(number)-3):
        num = number[b] * number[b+1]
        den = number[b+2] * number[b+3]
        print (("p( A%d|B ) = %f \np( A%d|B ) = %f") %( b+1, (num) / ( (num) + (den) ), b+2, (den) / ( (den) + (num) ) ))
        
        
nMutual_Ev = int(input("What is the number of mutual exclusive events you want ?"))
int_or_con = str(input("Intersection or Conditional? please no capital letters" ))
 

if(int_or_con == "intersection"):
    results = 0
    number = []
    numInputs = nMutual_Ev 
    while (numInputs > 0):
        number.append(float(input("What is the probability ? please enter ")))
        result_1 = numInputs - 1
        numInputs = result_1
    print (inter_func(number))
elif(int_or_con == "conditional"):
    results_2 = 2
    number = []
    numInputs = nMutual_Ev * 2 
    while (numInputs > 0):
        number.append(float(input("What is the probability ? please enter ")))
        result_2 = numInputs - 1
        numInputs = result_2
        print (cond_func(number))
else:
    print ("Enter 'intersection' or 'conditional'.  no capital letters")  
    print ("thank you!")