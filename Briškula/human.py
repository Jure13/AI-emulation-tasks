#import igrac
from igrac import Igrac

class Human(Igrac):
    def __init__(self, ime):
        self.Ime = ime

    def akcija(self, stanje):
        # print("Ruka: ", stanje["ruka"])
        length = len(stanje["ruka"])
        indeks = -1
        
        #print("Ruka: ", stanje["ruka"], "\nOdigrana: ", stanje["stol"])
        
        while(indeks < 0 or indeks >= length):
            indeks = int(input("Odaberi kartu (1, 2, 3): "))
            indeks -= 1
            
            if(indeks < 0 or indeks >= length):
                print("Ili 1 ili 2 ili 3!\n")
                
        return indeks
                

if __name__ == '__main__':
    igrac = Human("Igrač")