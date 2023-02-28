#import karte
#import human
from briskula import Briskula
from igrac import Igrac


if __name__ == "__main__":
    igrac = Igrac("Prvi")
    racunalo = Igrac("Drugi")
    brojac = 0
    
    #briskula = Briskula(igrac, racunalo, {})
    
    while(brojac < 100):
        b1 = Briskula(igrac, racunalo, {})
        b1.odigraj_partiju(False)
        #briskula.odigraj_partiju(false)
        brojac += 1
    
    while(brojac < 200):
        b1 = Briskula(racunalo, igrac, {})
        b1.odigraj_partiju(False)
        #briskula.odigraj_partiju(False)
        brojac += 1
    