from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QButtonGroup
import os
import database.dbDriver as database

class ConjugaisonMenuScreen(QMainWindow):
    def __init__(self):
        super(ConjugaisonMenuScreen, self).__init__()
        loadUi(os.path.abspath("Screens/Conjugaison/conjugaison_menuPage.ui"), self)

        # creating button groups
        self.gr1_buttons = QButtonGroup()
        self.gr2_buttons = QButtonGroup()
        self.gr3_buttons = QButtonGroup()

        # adding buttons to groups
        self.gr1_buttons.addButton(self.btn_gr1_pr, 0)
        self.gr1_buttons.addButton(self.btn_gr1_fu, 1)
        self.gr1_buttons.addButton(self.btn_gr1_im, 2)
        self.gr1_buttons.addButton(self.btn_gr1_ps, 3)
        self.gr1_buttons.addButton(self.btn_gr1_pc, 4)

        self.gr2_buttons.addButton(self.btn_gr2_pr, 0)
        self.gr2_buttons.addButton(self.btn_gr2_fu, 1)
        self.gr2_buttons.addButton(self.btn_gr2_im, 2)
        self.gr2_buttons.addButton(self.btn_gr2_ps, 3)
        self.gr2_buttons.addButton(self.btn_gr2_pc, 4)

        self.gr3_buttons.addButton(self.btn_gr3_pr, 0)
        self.gr3_buttons.addButton(self.btn_gr3_fu, 1)
        self.gr3_buttons.addButton(self.btn_gr3_im, 2)
        self.gr3_buttons.addButton(self.btn_gr3_ps, 3)
        self.gr3_buttons.addButton(self.btn_gr3_pc, 4)


class ConjugaisonLevelScreen(QMainWindow):
    def __init__(self):
        super(ConjugaisonLevelScreen, self).__init__()
        loadUi(os.path.abspath("Screens/Conjugaison/conjugaison_levelPage.ui"), self)
        self.words_guess_spaces = [self.word1_guess, self.word2_guess,
                                   self.word3_guess, self.word4_guess, self.word5_guess, self.word6_guess]

class ConjugaisonLevel:
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