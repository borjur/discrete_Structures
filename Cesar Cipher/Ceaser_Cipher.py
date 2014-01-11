'''
Created on Mar 4, 2013

@author: Boris Jurosevic
         CS 2430
         Assignment: Ceaser Cipher
         TUTORIAL: stackoverflow, youtube videos,python forum. 
'''


import time
import string
from string import ascii_lowercase

def Ceaser(words, enter):
    converts = ""
    
    new = ""
    for a in words:
        if aDict.count(a):
            if(enter == "encrypt"):
                enc = into[aDict.index(a.lower())]
                new = new + enc
                '''if not (enter != "encrypt"):
                    print ("wrong spelling!")'''
                 
            elif(enter == "decrypt"):
                dec = aDict[into.index(a)]
                new = new + dec
                '''if not (enter != "decrypt"):
                    print ("wrong spelling!")'''
        else:
            new = new + a
    return new


aDict = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
into = []
convert = ""
encryption = ""
decryption = ""
print("Welcome to Ceaser Cipher")
enter = (input("Do you want to encrypt or decrypt? Please no capital letters "))
words = str(input("Enter the word you want to " + enter ))
shift = int(input("Enter the number of letters it is going to be shifted to the right "))

for a in range(0, len(aDict)):
    b = len(aDict)
    into.append((aDict[(a+shift)%b]))
 

if(enter == "encrypt"):
    print ("This encrypted word is: %s" %(Ceaser(words, enter)))
elif(enter == "decrypt"):
    print ("This decrypted word is: %s" %(Ceaser(words, enter)))
    if not (enter == "encrypt" or enter == "decrypt"):
        print (" Its not encrypted or decrypted. Please try again")
else:
    print("You did not spell right encrypt or decrypt. Please no capital letters. Try again!")
    
    