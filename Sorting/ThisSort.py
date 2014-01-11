'''
Created on Jan 26, 2013
CS 2430 Algorithm Assignment
@author: Boris Jurosevic
references = I have used Python book to see how loops works and stackoverflow to see 
how the formula works and I have made it into my own, as well as python wikepidea 
'''
import random
import time

start = time.clock()

listing= set([])

while (len(listing) < 50):
    broj = random.randrange(1,1000)
    listing.add(broj)
    
list=[42,2,32,43,5]
def this_sort(thisSort):
    sorting = False
    end = len(thisSort)
    for index in range(0,end):
        value = thisSort[index]
        i = index - 1
        while i >= 0:
            k = i + 1
            if value < thisSort[i]:
                thisSort[k], thisSort[i] = thisSort[i], thisSort[k]
                
                i = i - 1
            else:
                break
            
elapsed = (time.clock() - start)           
print('we can see that this sort is sorting numbers in order')            
this_sort(list)
print (list)

print('timing of this sort algorithm generating 50 random numbers between 1 and 1000 is ')
print(elapsed) 
                
                


