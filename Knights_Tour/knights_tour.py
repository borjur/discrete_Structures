'''
Created on Nov 4, 2012

@author: Boris Jurosevic
         Assignment: Knights Tour
'''
from __future__ import print_function
from random import randint
from tile import Tile
from columns import Column


class KnightsTour(object):
    '''
    knights tour
    '''

    
    def __init__(self):
        '''
        constructor = Constructor
        '''
    
    def saberi(self):
        leng = 0
        self.tabla = self._napraviIgru()
        self.duzina = len(self.tabla)
        vecSabrano = 0
        dribling = []
        dribling.append(self.pocetak)
        self.tabla[self.pocetak.get_rowKnightsTour()][self.pocetak.get_colKnightsTour()] = "X"
        
        while vecSabrano < 4:
            danasnji = dribling[len(dribling) - 1]
            a = danasnji.get_rowKnightsTour()
            b = danasnji.get_colKnightsTour()
            
            if (a, b) in self.KnightsTourL:
                self._saberiFiguru(dribling, self.KnightsTourL)
                vecSabrano = vecSabrano + 1
            elif (a, b) in self.KnightsTourR:
                self._saberiFiguru(dribling, self.KnightsTourR)
                vecSabrano = vecSabrano + 1
            elif (a, b) in self.RKnightsTour:
                self._saberiFiguru(dribling, self.RKnightsTour)
                vecSabrano = vecSabrano + 1
            elif (a, b) in self.LKnightsTour:
                self._saberiFiguru(dribling, self.LKnightsTour)
                vecSabrano = vecSabrano + 1
        self._prikaziIgru(dribling)
        self._prikazi()
        
    def _saberiFiguru(self, a, b):
        current = a[len(a) - 1]
        broj = 0
        primotaj = 0
        
        while broj < 16:
            quad = self._dodajKvadrat(current.get_rowKnightsTour(), current.get_colKnightsTour())
            kvoter = 0
            
            while kvoter < 3:
                next = self._dodajPomjeri(a)
                
                if (next.get_rowKnightsTour(), next.get_colKnightsTour()) in b and quad == self._dodajKvadrat(next.get_rowKnightsTour(), next.get_colKnightsTour()):
                    a.append(next)
                    self.tabla[next.get_rowKnightsTour()][next.get_colKnightsTour()] = next.get_countKnightsTour()
                    
                    if next.get_countKnightsTour() == 63:
                        return
                    
                    broj += 1
                    kvoter += 1

                    
            
            if broj % 15 == 0:
                while True:
                    next = self._dodajPomjeri(a)
                    if next.get_moveKnightsTour() == -1:
                        self._premotaj(a)
                        broj -= 3
                        break
                    if quad != self._dodajKvadrat(next.get_rowKnightsTour(), next.get_colKnightsTour()):
                        a.append(next)
                        self.tabla[next.get_rowKnightsTour()][next.get_colKnightsTour()] = next.get_countKnightsTour()
                        broj += 1
                        return
                continue
                           
            while True: 
                next = self._dodajPomjeri(a)
                if (next.get_rowKnightsTour(), next.get_colKnightsTour()) in b and quad != self._dodajKvadrat(next.get_rowKnightsTour(), next.get_colKnightsTour()):
                    a.append(next)
                    self.tabla[next.get_rowKnightsTour()][next.get_colKnightsTour()] = next.get_countKnightsTour()
                    broj += 1
                    current = next
                    break
                
                
                if next.get_moveKnightsTour() == -1:
                    self._premotaj(a)
                    broj -= 3
                    break
                
    def _premotaj(self, pomjeri):
        for i in range(3):
            izbrisi = pomjeri.pop()
            self.tabla[izbrisi.get_rowKnightsTour()][izbrisi.get_colKnightsTour()] = 0


    
    def _napraviIgru(self):
            tablaGam = [
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0]
             ]
            red = randint(0, 7)
            stub = randint(0, 7)
            self.pocetak = Tile(red, stub, 0, 0)
            return tablaGam
    
    def _prikazi(self):
        print()
        print("displaying Knights Tour game")
        for red in range(self.duzina):
            print()
            if red == 0:
                print("***************************************** ")
            else:
                print("|****|****|****|****|****|****|****|****|")
            for stub in range(self.duzina):
                if stub == self.duzina -1:
                    if self.tabla[red][stub]:
                        print(str.format("| {0:2} |", self.tabla[red][stub]),  end="")
                    else:
                        print("|    |", end="")
                else:
                    if self.tabla[red][stub]:
                        print(str.format("| {0:2} ", self.tabla[red][stub]), end="")
                    else:
                        print("|    ", end="")
        print()
        print("|****|****|****|****|****|****|****|****|")
        
    def _dodajKvadrat(self, red, stub):
        if red >= 0 and red <= 3:
            if stub >= 0 and stub <= 3:
                return self.kvadratJedan            
        if red >= 4 and red <= 7:
            if stub >= 0 and stub <= 3:
                return self.kvadratDva            
        if red >= 4 and red <= 7:
            if stub >= 4 and stub <= 7:
                return self.kvadratTri    
        return self.kvadratCetri
        
    def _dodajPomjeri(self, pomjer):
        pocetak = pomjer[len(pomjer) - 1]
        dribling = pocetak.get_moveKnightsTour()
        red = pocetak.get_rowKnightsTour()
        stub = pocetak.get_colKnightsTour()
        while True:
            dribling += 1
            if dribling == 1:
                a = pocetak.get_countKnightsTour()
                if self._red_kolona(red - 2, stub - 1) == 0:
                    pomjer.pop()
                    pomjer.append(Tile(red, stub, 1, a))
                    tile = Tile(red - 2, stub - 1, 0, a + 1)
              
                    return(tile)
            elif dribling == 2:
                a = pocetak.get_countKnightsTour()
                if self._red_kolona(red - 1, stub - 2) == 0:
                    pomjer.pop()
                    pomjer.append(Tile(red, stub, 2, a))
                    tile = Tile(red - 1, stub - 2, 0, a + 1)
                    return(tile)
            elif dribling == 3:
                a = pocetak.get_countKnightsTour()
                if self._red_kolona(red + 1, stub - 2) == 0:
                    pomjer.pop()
                    pomjer.append(Tile(red, stub, 3, a))
                    tile = Tile(red + 1, stub - 2, 0, a + 1)
                    return(tile)
            elif dribling == 4:
                a = pocetak.get_countKnightsTour()
                if self._red_kolona(red + 2, stub - 1) == 0:
                    pomjer.pop()
                    pomjer.append(Tile(red, stub, 4, a))
                    tile = Tile(red + 2, stub - 1, 0, a+ 1)
                    return(tile)
            elif dribling == 5:
                a = pocetak.get_countKnightsTour()
                if self._red_kolona(red + 2, stub + 1) == 0:
                    pomjer.pop()
                    pomjer.append(Tile(red, stub, 5, a))
                    tile = Tile(red + 2, stub + 1, 0, a + 1)
                    return(tile)
            elif dribling == 6:
                a = pocetak.get_countKnightsTour()
                if self._red_kolona(red + 1, stub + 2) == 0:
                    pomjer.pop()
                    pomjer.append(Tile(red, stub, 6, a))
                    tile = Tile(red + 1, stub + 2, 0, a + 1)
                    return(tile)
            elif dribling == 7:
                a = pocetak.get_countKnightsTour()
                if self._red_kolona(red - 1, stub + 2) == 0:
                    pomjer.pop()
                    pomjer.append(Tile(red, stub, 7, a))
                    tile = Tile(red - 1, stub + 2, 0, a + 1)
                    return(tile) 
            elif dribling == 8:
                a = pocetak.get_countKnightsTour()
                if self._red_kolona(red - 2, stub + 1) == 0:
                    pomjer.pop()
                    pomjer.append(Tile(red, stub, 8, a))
                    tile = Tile(red - 2, stub + 1, 0, a + 1)
                    return(tile)
            else:
                return (Tile(-1, -1, -1, -1))
        
    def _red_kolona(self, red, stub):
        if red < 0 or red >= self.duzina:
            return 1
        elif stub < 0 or stub >= self.duzina:
            return 1
        elif self.tabla[red][stub] != 0:
            return 1
        else:
            return 0


    def _prikaziIgru(self, pomjeri):
        print(" Knights Tour from beginning to the end")
        for i in range(len(pomjeri)):
            pomjer = pomjeri[i]
            print(pomjer, end = "")
            if i % 8 == 7:
                print()
                
                
                
    tablaGame = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
    KnightsTourL = {(2,0),(0,1),(1,3),(3,2),(6,0),(4,1),(5,3),(7,2),(6,4),(4,5),(7,6),(5,7), (2,4),(0,5),(3,6),(1,7)}
    KnightsTourR = {(1,0),(0,2),(3,1),(2,3),(5,0),(4,2),(7,1),(6,3),(5,4),(7,5),(6,7),(4,6), (1,4),(3,5),(0,6),(2,7)}
    RKnightsTour = {(0,0),(2,1),(1,2),(3,3),(4,0),(6,1),(5,2),(7,3),(4,4),(6,5),(5,6),(7,7), (0,4),(2,5),(1,6),(3,7)}
    LKnightsTour = {(3,0),(0,3),(1,1),(2,2),(7,0),(5,1),(6,2),(4,3),(7,4),(5,5),(6,6),(4,7),(3,4),(1,5),(2,6),(0,7)}
    
    kvadratJedan, kvadratDva, kvadratTri, kvadratCetri = range(1, 5)
        
        