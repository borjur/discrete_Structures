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

list= set([])

while (len(list) < 50):
    broj = random.randrange(1,1000)
    list.add(broj)
    
bubbleSort=[32,23,53,1,65]
end=(len(bubbleSort)-1)
while True:
    sorting=False
    for k in range(0,end):
        if bubbleSort[k]>bubbleSort[k+1]:
            i = k + 1
            bubbleSort[i],bubbleSort[k]=bubbleSort[k],bubbleSort[i]
           
            sorting=True
    if sorting == False:
        break 
print('we can see the bubble sort sorting numbers in order')
print(bubbleSort)

elapsed = (time.clock() - start)

print('timing of this sort algorithm generating 50 random numbers between 1 and 1000  is')
print(elapsed)



    
