import imp
from karte import Karta
from random import randint

class Igrac:
    def __init__(self, ime):
        self.Ime = ime
    
    def akcija(self, stanje):
        
        # print("Špil: ", stanje["stol"])
        
        return randint(0, len(stanje["ruka"]) - 1)
        


if __name__ == '__main__':
    igrac = Igrac("Igrač")