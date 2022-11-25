from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QButtonGroup
import playsound
import os


class GrammaireMenuScreen(QMainWindow):
    def __init__(self):
        super(GrammaireMenuScreen, self).__init__()
        loadUi(os.path.abspath("Screens/Grammaire/grammaire_menuPage.ui"), self)

        #creating button groups
        self.acc_buttons = QButtonGroup()
        self.nom_buttons = QButtonGroup()

        #adding buttons to groups
        self.acc_buttons.addButton(self.btn_acc_lvl0,0)
        self.acc_buttons.addButton(self.btn_acc_lvl1,1)
        self.acc_buttons.addButton(self.btn_acc_lvl2,2)
        self.acc_buttons.addButton(self.btn_acc_lvl3,3)

        self.nom_buttons.addButton(self.btn_nom_lvl0,0)
        self.nom_buttons.addButton(self.btn_nom_lvl1,1)
        self.nom_buttons.addButton(self.btn_nom_lvl2,2)
        self.nom_buttons.addButton(self.btn_nom_lvl3,3)

class GrammaireLevelScreen(QMainWindow):
    def __init__(self):
        super(GrammaireLevelScreen, self).__init__()
        loadUi(os.path.abspath("Screens/Grammaire/grammaire_levelPage.ui"), self)
        self.words_buttons = QButtonGroup()
        self.add_buttons_first_half()
        self.add_buttons_second_half()

    def add_buttons_first_half(self):
        self.words_buttons.addButton(self.btn_word0, 0)
        self.words_buttons.addButton(self.btn_word1, 1)
        self.words_buttons.addButton(self.btn_word2, 2)
        self.words_buttons.addButton(self.btn_word3, 3)
        self.words_buttons.addButton(self.btn_word4, 4)
        self.words_buttons.addButton(self.btn_word5, 5)

    def add_buttons_second_half(self):
        self.words_buttons.addButton(self.btn_word6, 6)
        self.words_buttons.addButton(self.btn_word7, 7)
        self.words_buttons.addButton(self.btn_word8, 8)
        self.words_buttons.addButton(self.btn_word9, 9)
        self.words_buttons.addButton(self.btn_word10, 10)
        self.words_buttons.addButton(self.btn_word11, 11)
