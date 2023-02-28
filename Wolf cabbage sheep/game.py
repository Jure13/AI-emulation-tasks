from copy import deepcopy


class Stanje:
    def __init__(self, lijevo = "VOKB||----", desno = "----||VOKB"):
            self.Lijevo = lijevo
            self.Desno = desno
            self.State = list(lijevo)

    def __str__(self):
        return str(self.State)
    
    def next_states(self):
        states = []
        
        for i in self.all_actions():
            temp = self.copy()
            
            temp.action(i)
            states.append(temp)
            
        return states
            

    def is_solved(self):
        if self.State == list(self.Desno):
            return True
        else:
            return False

    def is_terminal(self):
        if self.State == list(self.Desno):
            return True
        else:
            if self.State == list("VO-- || --KB") or self.State == list("-OK- ||V--B")  or self.State == list("--KB || VO--") or self.State == list("V--B || -OK-") or self.State == list("VOK- || ---B"):
                return True
            else:
                return False
        
    def action(self, action):
        
        index = self.newIndex(action)
        self.State[index] = '-'
        
        if index + 6 < len(self.State):
            self.State[index + 6] = action
            self.State[-1] = 'B'
            self.State[3] = '-'
        else:
            self.State[index - 6] = action
            self.State[3] = 'B'
            self.State[-1] = '-'   

    def newIndex(self, action):
        for index in range(len(self.State)):
            if self.State[index] == action:
                return index

    def all_actions(self):
        potentialStates = ["V", "O", "K", "B"]
        futureStates = []
                
        for state in potentialStates:
            if self.newIndex(state) >= 6 and self.State[-1] == "B":
                futureStates.append(state)
            elif self.newIndex(state) < 4 and self.State[3] == "B":
                futureStates.append(state)
                
        return futureStates

    def undo_action(self, action):
        self.action(action)
        
        return self.State

    def copy(self):
        return deepcopy(self)



if __name__ == "__main__":
    igra = Stanje()
    print(igra)
