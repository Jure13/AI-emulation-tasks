from stapici import Stapic


def MiniMax(igra, alpha, beta):
    
    if igra.provjera():
        if igra.Igrac == "prvi":
            return -100, 0
        elif igra.Igrac == "drugi":
            return 100, 0
    
    if igra.Igrac == "prvi": 
        AI = 0     
        for action in range(1, 3):
            igra.action(action)
            
            temp, newAction = MiniMax(igra, alpha, beta)
                        
            igra.undo_action(action)
            if(temp < beta):
                beta = temp
                AI = action
            if(alpha >= beta):
                break        
                
        return beta, AI   
     
    else:
        AI = 0
        for action in range(1, 3):
            igra.action(action)  
                     
            temp, newAction = MiniMax(igra, alpha, beta)
            
            igra.undo_action(action)            
            if(temp > alpha):
                alpha = temp
                AI = action
            if(alpha >= beta):
                break    
                        
        return alpha, AI   



def Partija(igra):
    while igra.provjera() == False:
        print(igra)
        
        odabir = int(input("Odaberi 1 ili 2 štapića sa poda:\n"))
        igra.action(odabir)
        
        print(igra)
        
        temp, AI = MiniMax(igra, alpha = -1000, beta = 1000)
        igra.action(AI)
        print("Računalo vuče " + str(AI) + " štapić(a).\n")
        print(igra)
        
    print("Gubitnik je " + igra.Igrac + " igrač!\n")
       


if __name__ == "__main__":
    igra = Stapic()
    Partija(igra)