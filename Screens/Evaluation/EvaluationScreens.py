from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QMainWindow, QButtonGroup
import playsound


class EvaluationMenuScreen(QMainWindow):
    def __init__(self):
        super(EvaluationMenuScreen, self).__init__()
        loadUi(r"Screens\Evaluation\evaluation_menuPage.ui", self)

        #creat button groups
        self.vocab_buttons = QButtonGroup()
        self.conj_buttons = QButtonGroup()
        self.gram_buttons = QButtonGroup()

        #adding button to groups
        self.vocab_buttons.addButton(self.btn_vocab_lvl1,0)
        self.vocab_buttons.addButton(self.btn_vocab_lvl2,2)
        self.vocab_buttons.addButton(self.btn_vocab_lvl3,3)

        self.conj_buttons.addButton(self.btn_conj_lvl1,0)
        self.conj_buttons.addButton(self.btn_conj_lvl2,2)
        self.conj_buttons.addButton(self.btn_conj_lvl3,3)

        self.gram_buttons.addButton(self.btn_gram_lvl1,0)
        self.gram_buttons.addButton(self.btn_gram_lvl2,2)
        self.gram_buttons.addButton(self.btn_gram_lvl3,3)


class EvaluationLevelScreen(QMainWindow):
    def __init__(self):
        super(EvaluationLevelScreen, self).__init__()
        loadUi(r"Screens\Evaluation\evaluation_levelPage.ui", self)