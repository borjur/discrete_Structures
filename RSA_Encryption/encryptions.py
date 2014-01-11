'''
Created on Feb 16, 2013

@author: Agape
'''
from Modular import alg

class Encryptions(object):
    p = 61
    q = 53
    e = 17
    self = p
    self = q
    self = e
    
   
    def encrypt(self, message):
        a = self._convert_to_numeric(message)
       
        for i in range(len(a)):
                a[i] = self._encrypt(a[i])
        m = ""
        for i in range(len(a)):
            if i != 0:
                m += ","
            m += str(a[i])
        return m
   
    def _encrypt(self, m):
        p = self.p
        q = self.q
        n = p * q
        e = self.e
        return alg(m, e, n)

        
    def _convert_to_numeric(self, message):
        m = []

        for i in range(len(message)):
            m.append(self._letter_to_num(message[i]))
        return m
   
           
    def _letter_to_num(self, m):
        return ord(m)
        