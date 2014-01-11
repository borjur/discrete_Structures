'''
Created on Jan 26, 2013
CS 2430 Algorithm Assignment
@author: Boris Jurosevic
references = I have used Python book to see how loops works and stackoverflow to see 
how the formula works and I have made it into my own, as well as python wikepedia 
'''
import random
import time

start = time.clock()

list= set([])

while (len(list) < 50):
    broj = random.randrange(1,1000)
    list.add(broj)
    
quickSort=[2,43,10,4,32]

def sorting_quick(quickSort):
    while quickSort==[]: 
        return  quickSort
    else:
        pivotIndex = quickSort[0]
        index = quickSort[1:]
        front=sorting_quick([pivot  for  pivot  in  index   if  pivot  <  pivotIndex])
        back=sorting_quick([pivot  for  pivot  in  index   if  pivot  >=  pivotIndex])
        return(front+quickSort[0:1]+back)
    
elapsed = (time.clock() - start)    

print('original quick sort')
print(quickSort)
print('we can see the quick sort sorting numbers in order')
print(sorting_quick(quickSort))

print('timing of quick sort algorithm generating 50 random numbers between 1 and 1000 is ')
print(elapsed)
