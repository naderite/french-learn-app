import sys
import database.dbDriver as database
     
class Level:
    def __init__(self, temp, groupe):
        self.driver = database.JSONDriver()
        self.groupe = groupe
        self.temp = temp
        self.verb = self.get_verb(self.groupe)
        self.answer = self.driver.getConjAnswer(temp, groupe)
        self.title = f"{self.verb} au {self.temp}"

    def get_verb(self, groupe):
        match groupe:
            case 0: return "acheter"
            case 1: return "finir"
            case 2: return "pouvoir"