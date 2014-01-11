'''
     Boris Jurosevic
     CS2430
     Assignment: Huffman Coding
     Tutorials: Stackoverflow Huffman, code on literative programming, youtube
'''

from __future__ import print_function
from file_input import File_Input
from huffman import Huffman
import math
import copy
# most important method
def glavnaMethod():
    count = 0
    ukucaj= File_Input()
    igra = Huffman()
    dajSveRezultatee = ukucaj.citaj()
    dioIgre = igra.prebaciSveUHufman(copy.copy(dajSveRezultatee))
    kucajText = ukucaj.citajFile()
    
    bajneri = sveU_bajneriju(dioIgre, kucajText)
    pokaziSveScore(kucajText, bajneri, dioIgre)
    Izbor(dajSveRezultatee, dioIgre, kucajText, bajneri)
    

# all about comperssor
def pokaziSveKompresovane(x, stol):
    konvertiraj = ""
    brojiBrojeve = 0
    for zed in str:
        for alpha in range(len(stol)):
            if zed == stol[alpha][0]:
                dictionary = stol[alpha][1]
                print(dictionary, end = ' ')
                brojiBrojeve += len(dictionary)
                if brojiBrojeve > 100:
                    print()
                    count = 0
 # for testing binary
def sveU_bajneriju(dictionary, bajneri):
    count = 0
    bajneriText = ""
    for abeceda in bajneri:
        for x in dictionary:
            if abeceda == x[0]:
                bajneriText += x[1]
    return bajneriText
# for testing compression
def pokaziSveKompresovane2(str, huffTable):
    binStr = ""
    count = 0
    for c in str:
        for i in range(len(huffTable)):
            if c == huffTable[i][0]:
                print(huffTable[i][1], end = ' ')
                count += len(huffTable[i][1])
                if count > 100:
                    print()
                    count = 0
# this is where the binary comes in                  
def sveU_bajneriju2(dictionary, bajneri):
    bajneriText = ""
    for abeceda in bajneri:
        for x in dictionary:
            if abeceda == x[0]:
                bajneriText += x[1]
    return bajneriText                   

# and of course the choices we want to print
def Izbor(dajSveRezultatee, dioIgre, str, binStr):
    cont = True
    while cont:
        print("\nDisplaying HUFFMAN CODING. What result would you like to see ?  ")
        print("1. Frequency")
        print("2. Binary")
        print("3. Original")
        print("4. Compressed")
        choice = input("Please select one of the following: ")
        try:
            opt = int(choice)
        except:
            opt = 10
        print()
        
        if opt == 1:
            pokaziUformatu(dajSveRezultatee)
        elif opt == 2:
            printajMiSve(dioIgre)
        elif opt == 3:
            print(str)
        elif opt == 4:
            pokaziSveKompresovane(str, dioIgre)
        else:
            print("Try again!")
# everything you want displayed in the end           
def pokaziSveScore(rijeci, bajneri, stol):
   
    print("How many number of characters does it have ? ", len(stol))
    print("What is the starting file length?", len(rijeci))
    expLen = len(rijeci) * math.ceil(math.log(len(stol), 2))
    print("What is the expected file length ? <", expLen)
    print("What is the compressed file length ?", len(bajneri) / 8)
# different formats are coming in here
def pokaziUformatu(a):
    for x in a:
        print(str.format("{0}, {1:.5}", x[1], x[0]))
#testing a method for different formats      
def pokaziUformatu2(a):
    for x in a:
        print(str.format("{0}, {2:.10}", x[-1], x[0]))        
# method that finally displays it all   
def printajMiSve(a):
    for x in a:
        print(x)
# main class
if __name__ == '__main__':
    glavnaMethod()
    