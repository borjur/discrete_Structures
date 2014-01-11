'''
     Boris Jurosevic
     CS2430
     Assignment: Huffman Coding
     Tutorials: Stackoverflow Huffman, code on literative programming, youtube
'''
import heapq


class Huffman(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def prebaciSveUHufman(self, a):
        tree = self.napraviDrvo(a)
        complete = []
        self.dajMiBajneri(tree, complete)
#        complete = self._to_bin(complete)
        return complete
        
    def napraviDrvo(self, a):
        heapq.heapify(a)
        while len(a) > 1:
            left = heapq.heappop(a)
            right = heapq.heappop(a)
            heapq.heappush(a, (left[0] + right[0], left, right))
        return a[0]
    
    def dajMiBajneri(self, tree, a, prefix = ''):
        if len(tree) == 2:
            return (tree[1], prefix)
        else:
            left = self.dajMiBajneri(tree[1], a, prefix + '1')
            right = self.dajMiBajneri(tree[2], a, prefix + '0')
            if left != None:
                a.append(left)
            if right != None:
                a.append(right)
                
    def dajMiOpetBajneri(self, tree, prefix = ''):
        if len(tree) == 2:
            print(tree[1], prefix)
        else:
            self.dajMiOpetBajneri(tree[1], prefix + '1')
            self.dajMiOpetBajneri(tree[2], prefix + '0')

                
    def uBajneri(self, a):
        list = []
        for x in a:
            n = self._str_to_bin(x[1])
            list.append((x[0], n))
        return list
                
    def tekstU_Bajneri(self, str):
        reverse = str[::-1]
        int = 0
        if reverse[0] == "1":
            int += 1
        for i in range(1, len(reverse)):
            if reverse[i] == "1":
                int += 2**i
        return bin(int)
    
    