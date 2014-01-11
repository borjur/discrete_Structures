'''
Created on Feb 16, 2013

@author: Agape
'''
from encryptions import Encryptions

def main():
    enc = Encryptions()
    message = "The Queen Can't Roll When Sand is in the Jar."
    message = enc.encrypt(message)
    print(message)
    


if __name__ == '__main__':
    main()
    
    
