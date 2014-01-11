'''
     Boris Jurosevic
     CS2430
     Assignment: Huffman Coding
     Tutorials: Stackoverflow Huffman, code on literative programming, youtube
'''
import os
os.getcwd()
import fileinput
import decimal
import heapq
import math
import copy

class File_Input(object):
    '''
    classdocs
    '''
    # constructor File_Input
    def __init__(self):
        '''
        Huffman coding
        '''
        #read the file file_inputs 
    def citajFile(self):
        start = 0
        pishi = open('loremipsum.txt', 'r')
        file = pishi.read()
        pishi.close()
        return file
     # read the file
    def citaj(self):
        readTheFile = open('loremipsum.txt', 'r')
        str = readTheFile.read()
        #convert it into a list
        putIn = {}
        broj = len(str)
        self.brojiListu(putIn, str)
        inside = self.konvertirajListu(putIn, broj)
        
        readTheFile.close()
        return inside 
    # konvert the list
    def konvertirajListu(self, alphabet, samoBroji):
        ovajArray = []
        for ubaci in alphabet:
            allTogether = alphabet[ubaci] / samoBroji
            ovajArray.append((decimal.Decimal(allTogether), ubaci))
        return ovajArray
    # count the list
    def brojiListu(self, greek, brojiBrojeve):
        list = []
        for brojj in brojiBrojeve:
            if brojj in greek.keys():
                greek[brojj] = greek[brojj] + 1
            else:
                greek[brojj] = 1
      #count that list      
    def brojiListu2(self, figura, information):
        brojevih = len(information)
        for zed in range(len(information)):
            # pokusaj da vratis file
            try:
                broj = information[zed]
                posebno = figura.index(broj)
                figura[posebno].increment(brojevih)
            except:
                figura.append((broj, brojevih))
        print(brojevih, "text in a file")
        
        
        def brojiListu2(self, greek, brojiBrojeve):
            list = []
            for brojj in brojiBrojeve:
                if brojj in greek.keys():
                    greek[brojj] = greek[brojj] + 1
                else:
                        greek[brojj] = 1
                        
          #count that list      
    def brojiListu3(self, figura, information):
        brojevih = len(information)
        for zed in range(len(information)):
            # pokusaj da vratis file
            try:
                broj = information[zed]
                posebno = figura.index(broj)
                figura[posebno].increment(brojevih)
            except:
                figura.append((broj, brojevih))
        print(brojevih, "testing text in a file")
        
        
        