#from ast import If
from karte import Karte, Spil
from human import Human
from igrac import Igrac
from random import randint


class Briskula:
    BODOVI = {
        1: 11,
        2: 0,
        3: 10,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        11: 2,
        12: 3,
        13: 4
    }
    
    SNAGA = {
        "1": 1,
        "2": 10,
        "3": 2,
        "4": 9,
        "5": 8,
        "6": 7,
        "7": 6,
        "11": 5,
        "12": 4,
        "13": 3
    }
    
    def __init__(self, prvi, drugi):
        self.Prvi = prvi
        self.Drugi = drugi
        self.Brojac = 0
        self.Spil = Spil()
        self.Briskula = self.Spil.peskaj()
        self.Spil.dodaj(self.Briskula)
        self.Stol = []
        self.Potez = 1        
        self.I = 1
        for I in range(3):
            self.Prvi.Ruka.append(self.Spil.peskaj())
            self.Drugi.Ruka.append(self.Spil.peskaj())
        
    def __str__(self):
        return "Karata je u špilu: "+ self.Stol + "\nPrvi: " + self.Prvi.ime + "\nDrugi: " + self.Drugi.ime + "\nBriškula:  " + self.Briskula + "\nStol: " + self.Stol + "\nTvoje karte: " + str(self.Drugi.Ruka)
    
    def ispisStola(self):
        for karta in self.Stol:
            print("Odigrana: ", karta)
        
    def rezultat(self):
        prviBodovi = 0
        drugiBodovi = 0
        
        # prviBodovi += (self.BODOVI[i.broj] for i in self.Prvi.Dobivene)
        # drugiBodovi += (self.BODOVI[j.broj] for j in self.Drugi.Dobivene)
        
        for i in self.Prvi.Dobivene:
            prviBodovi += self.BODOVI[i.broj]
        for j in self.Drugi.Dobivene:
            drugiBodovi += self.BODOVI[j.broj]
             
        if(prviBodovi > 60):
            print("Prvi ima ", prviBodovi, " bodova, a drugi ", drugiBodovi, ".\n")
            return 1

        elif(drugiBodovi > 60):
            print("Prvi ima ", prviBodovi, " bodova, a drugi ", drugiBodovi, ".\n")
            return 2

        else:
            print("Neriješeno! Igrači imaju po 60 bodova.\n")
            return 0
    
    def stanje(self):
        #length = len(self.Stanje["ruka"].karte)
        
        if(self.Potez == 1):
            return {"briskula": self.Briskula, "ruka": self.Prvi.Ruka, "stol": self.Stol, "dobivene": self.Prvi.Dobivene, "dobiveneProtivinik": self.Drugi.Dobivene}
        else:
            return {"briskula": self.Briskula, "ruka": self.Drugi.Ruka, "stol": self.Stol, "dobivene": self.Drugi.Dobivene, "dobiveneProtivinik": self.Prvi.Dobivene}
        
        # if(len(self.Stanje["stol"].karte) > 0):
        #     while(length < 3):
        #         odabir = self.Stanje["stol"].peskaj()
        #         self.Stanje["ruka"].karte.append(odabir)
        #         length += 1
        
        # return self.Stanje
    
    def odigraj_ruku(self, prikaz = True):
        self.Brojac += 1
        
        if(self.Potez == 1):
            indeksPrvog = self.Prvi.akcija(self.stanje())
            self.Stol.append(self.Prvi.Ruka[indeksPrvog])
            print("Odigrana karta: ",self.Stol[len(self.Stol) - 1])
            prviKarta = self.Prvi.Ruka[indeksPrvog]
            self.Prvi.Ruka.pop(indeksPrvog)    
        # print("Ruka prvog: ", (self.Stanje["ruka"]))
        # p1 = self.Prvi.akcija(self.Stanje)
        # p1_card = self.Stanje["ruka"].karte.pop(p1)
        
            indeksDrugog = self.Drugi.akcija(self.stanje())
            self.Stol.append(self.Drugi.Ruka[indeksDrugog])
            print("Odigrana karta: ",self.Stol[len(self.Stol) - 1])
            drugiKarta = self.Drugi.Ruka[indeksDrugog]
            self.Drugi.Ruka.pop(indeksDrugog)   
        # print("Ruka drugog: ", self.Stanje["ruka"])
        # p2 = self.Drugi.akcija(self.Stanje)
        # self.Stanje = self.stanje()
        # p2_card = self.Stanje["ruka"].karte.pop(p2)
        else:
            indeksDrugog = self.Drugi.akcija(self.stanje())
            self.Stol.append(self.Drugi.Ruka[indeksDrugog])
            print("Odigrana karta: ",self.Stol[len(self.Stol) - 1])
            drugiKarta = self.Drugi.Ruka[indeksDrugog]
            self.Drugi.Ruka.pop(indeksDrugog)
            
            indeksPrvog = self.Prvi.akcija(self.stanje())
            self.Stol.append(self.Prvi.Ruka[indeksPrvog])
            print("Odigrana karta: ",self.Stol[len(self.Stol) - 1])
            prviKarta = self.Prvi.Ruka[indeksPrvog]
            self.Prvi.Ruka.pop(indeksPrvog)
             
        self.Stol.clear()
         
        # if(prikaz == True):
        #     #print("Špil: ", self.Stanje["stol"])
        #     print("Špil: ", len(self.Stanje["stol"].karte), " karata\n")
        #     print("Prvi baca: ", p1_card, "\nDrugi baca: ", p2_card)
        #     print(self.Brojac, ". odigrana ruka\n----------\n----------")

        return prviKarta, drugiKarta
    
    def odigraj_partiju(self, prikaz = True):
        # spil = Spil()
        # self.Stanje["stol"] = spil
        # print(spil)
        # self.Stanje["ruka"] = Karte([])
        # self.Stanje["dobivene"] = []
        # self.Stanje["dobiveneProtivnik"] = []
        # self.Stanje["zog"] = self.Stanje["stol"].peskaj()
        # print("Briškula je: ",self.Stanje["zog"])
        # self.Stanje.update({"stol": self.Stanje["stol"]})
        # self.Stanje["stol"].dodaj(self.Stanje["zog"])
        
        #while(len(self.Stanje["stol"].karte) > 0):
            # while(len(self.Stanje["ruka"].karte) < 3):
            #     odluka = self.Stanje["stol"].peskaj()
            #     self.Stanje["ruka"].karte.append(odluka)
        
        # while(len(self.Prvi.Ruka) < 3):
        #     self.Prvi.Ruka.append(self.Spil.peskaj())
        # while(len(self.Drugi.Ruka) < 3):
        #     self.Drugi.Ruka.append(self.Spil.peskaj())
        
        velicinaSpila = 34
            
        while(velicinaSpila > 2):
            prviKarta, drugiKarta = self.odigraj_ruku(prikaz)
            
            for key, value in self.SNAGA.items():
                if(str(prviKarta.broj) == key):
                    temp1 = value
                    
            for key, value in self.SNAGA.items():
                if(str(drugiKarta.broj) == key):
                    temp2 = value
            
            if(prviKarta.zog == self.Briskula and drugiKarta.zog == self.Briskula):
                if(temp1 > temp2):
                    self.Prvi.Dobivene.append(prviKarta)
                    self.Prvi.Dobivene.append(drugiKarta)
                    self.Potez = 1
                    self.Prvi.Ruka.append(self.Spil.peskaj())
                    self.Drugi.Ruka.append(self.Spil.peskaj())
                else:
                    self.Drugi.Dobivene.append(prviKarta)
                    self.Drugi.Dobivene.append(drugiKarta)
                    self.Potez = 2
                    self.Drugi.Ruka.append(self.Spil.peskaj())
                    self.Prvi.Ruka.append(self.Spil.peskaj())
                    
            elif(prviKarta.zog == self.Briskula and drugiKarta.zog != self.Briskula):
                self.Prvi.Dobivene.append(prviKarta)
                self.Prvi.Dobivene.append(drugiKarta)
                self.Potez = 1
                self.Prvi.Ruka.append(self.Spil.peskaj())
                self.Drugi.Ruka.append(self.Spil.peskaj())
                
            elif(prviKarta.zog != self.Briskula and drugiKarta.zog == self.Briskula):
                self.Drugi.Dobivene.append(prviKarta)
                self.Drugi.Dobivene.append(drugiKarta)
                self.Potez = 2
                self.Drugi.Ruka.append(self.Spil.peskaj())
                self.Prvi.Ruka.append(self.Spil.peskaj())
            
            else:
                if(prviKarta.zog == drugiKarta.zog):
                    if(temp1 > temp2):
                        self.Prvi.Dobivene.append(prviKarta)
                        self.Prvi.Dobivene.append(drugiKarta)
                        self.Potez = 1
                        self.Prvi.Ruka.append(self.Spil.peskaj())
                        self.Drugi.Ruka.append(self.Spil.peskaj())
                    else:
                        self.Drugi.Dobivene.append(prviKarta)
                        self.Drugi.Dobivene.append(drugiKarta)
                        self.Potez = 2
                        self.Drugi.Ruka.append(self.Spil.peskaj())
                        self.Prvi.Ruka.append(self.Spil.peskaj())
                else:
                    self.Prvi.Dobivene.append(prviKarta)
                    self.Prvi.Dobivene.append(drugiKarta)
                    self.Potez = 1
                    self.Prvi.Ruka.append(self.Spil.peskaj())
                    self.Drugi.Ruka.append(self.Spil.peskaj())
                    
            velicinaSpila -= 2
            print(self.Drugi.ispisRuke())
            #print(self.ispisStola())        
            #print(self.Stol[1])
                    
        # if(len(self.Stanje["ruka"].karte) > 0):
            
        prviKarta, drugiKarta = self.odigraj_ruku(prikaz)
        for key, value in self.SNAGA.items():
            if(str(prviKarta.broj) == key):
                temp1 = value
                    
        for key, value in self.SNAGA.items():
            if(str(drugiKarta.broj) == key):
                temp2 = value    
            
        if(prviKarta.zog == self.Briskula and drugiKarta.zog == self.Briskula):
            if(temp1 > temp2):
                self.Prvi.Dobivene.append(prviKarta)
                self.Prvi.Dobivene.append(drugiKarta)
                self.Potez = 1
                self.Prvi.Ruka.append(self.Spil.peskaj())
                self.Drugi.Ruka.append(self.Spil.peskaj())
            else:
                self.Drugi.Dobivene.append(prviKarta)
                self.Drugi.Dobivene.append(drugiKarta)
                self.Potez = 2
                self.Drugi.Ruka.append(self.Spil.peskaj())
                self.Prvi.Ruka.append(self.Spil.peskaj())
                    
        elif(prviKarta.zog == self.Briskula and drugiKarta.zog != self.Briskula):
            self.Prvi.Dobivene.append(prviKarta)
            self.Prvi.Dobivene.append(drugiKarta)
            self.Potez = 1
            self.Prvi.Ruka.append(self.Spil.peskaj())
            self.Drugi.Ruka.append(self.Spil.peskaj())
                
        elif(prviKarta.zog != self.Briskula and drugiKarta.zog == self.Briskula):
            self.Drugi.Dobivene.append(prviKarta)
            self.Drugi.Dobivene.append(drugiKarta)
            self.Potez = 2
            self.Drugi.Ruka.append(self.Spil.peskaj())
            self.Prvi.Ruka.append(self.Spil.peskaj())
            
        else:
            if(prviKarta.zog == drugiKarta.zog):
                if(temp1 > temp2):
                    self.Prvi.Dobivene.append(prviKarta)
                    self.Prvi.Dobivene.append(drugiKarta)
                    self.Potez = 1
                    self.Prvi.Ruka.append(self.Spil.peskaj())
                    self.Drugi.Ruka.append(self.Spil.peskaj())
                else:
                    self.Drugi.Dobivene.append(prviKarta)
                    self.Drugi.Dobivene.append(drugiKarta)
                    self.Potez = 2
                    self.Drugi.Ruka.append(self.Spil.peskaj())
                    self.Prvi.Ruka.append(self.Spil.peskaj())
            else:
                self.Prvi.Dobivene.append(prviKarta)
                self.Prvi.Dobivene.append(drugiKarta)
                self.Potez = 1
                self.Prvi.Ruka.append(self.Spil.peskaj())
                self.Drugi.Ruka.append(self.Spil.peskaj())
                    
                    
        if(self.rezultat() == 0):
            print("Neriješeno!")
        elif(self.rezultat() == 1):
            print("Pobjeda prvog igrača!")
        elif(self.rezultat() == 2):
            print("Pobjeda drugog igrača!")
        else:
            print("Greška!!!")
        
class IgracBriskule(Human):
    def __init__(self, ime):
        self.Ime = ime
        self.Ruka = []
        self.Dobivene = []
        
    def ispisRuke(self):
        for karta in self.Ruka:
            print("Karta: ", karta,)    
        
if __name__ == '__main__':
    prviIgrac = IgracBriskule("Prvi")
    drugiIgrac = IgracBriskule("Drugi")

    igra = Briskula(prviIgrac, drugiIgrac)
    
    igra.odigraj_partiju()
