'''
Created on Nov 4, 2012

@author: Boris Jurosevic
         Assignment: Knights Tour
'''

class Tile(object):
    '''
    Knights Tour
    '''


    def __init__(self, red, stub, pomjeri, broji):
        '''
        Constructor
        '''
        self._pomjeri = pomjeri
        self._broji = broji
        self._set_rowKnightsTour(red)
        self._set_colKnightsTour(stub)
        
    
    def _set_rowKnightsTour(self, line):
        self._row = line
    
    def _set_colKnightsTour(self, dole):
        self._col = dole
    
    def get_rowKnightsTour(self):
        return self._row
    
    def get_colKnightsTour(self):
        return self._col
    
    def get_moveKnightsTour(self):
        return self._pomjeri
    
    def get_countKnightsTour(self):
        return self._broji
    
    def __str__(self):
        return str.format("{0:2}. ({1}, {2}) ", self._broji, self._row, self._col)