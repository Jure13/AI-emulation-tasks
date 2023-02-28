class Stapic:
    def __init__(self):
        self.Stapici = 11
        self.Igrac = "prvi"


    def __str__(self):
        return ("Štapića na podu: " + str(self.Stapici) + "\nIgra " + self.Igrac + " igrač.")

    def action(self, action):
        self.Stapici = self.Stapici - action
        self.promjena()

    def undo_action(self, action):
        self.Stapici = self.Stapici + action
        self.promjena()

    def promjena(self):
        if(self.Igrac == "prvi"):
            self.Igrac = "drugi"
        else:
            self.Igrac = "prvi"

    def provjera(self):
        if self.Stapici <= 2:
            return True
        else:
            return False



if __name__ == "__main__":
    stapic = Stapic()
