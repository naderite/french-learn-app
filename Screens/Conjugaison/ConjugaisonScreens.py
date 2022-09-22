from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QMainWindow, QDialog, QButtonGroup
import playsound
import os


class ConjugaisonMenuScreen(QMainWindow):
    def __init__(self):
        super(ConjugaisonMenuScreen, self).__init__()
        loadUi(os.path.abspath("Screens/Conjugaison/conjugaison_menuPage.ui"), self)


        #creating button groups
        self.gr1_buttons = QButtonGroup()
        self.gr2_buttons = QButtonGroup()
        self.gr3_buttons = QButtonGroup()

        #adding buttons to groups
        self.gr1_buttons.addButton(self.btn_gr1_pr,0)
        self.gr1_buttons.addButton(self.btn_gr1_fu,1)
        self.gr1_buttons.addButton(self.btn_gr1_im,2)
        self.gr1_buttons.addButton(self.btn_gr1_ps,3)
        self.gr1_buttons.addButton(self.btn_gr1_pc,4)

        self.gr2_buttons.addButton(self.btn_gr2_pr,0)
        self.gr2_buttons.addButton(self.btn_gr2_fu,1)
        self.gr2_buttons.addButton(self.btn_gr2_im,2)
        self.gr2_buttons.addButton(self.btn_gr2_ps,3)
        self.gr2_buttons.addButton(self.btn_gr2_pc,4)

        self.gr3_buttons.addButton(self.btn_gr3_pr,0)
        self.gr3_buttons.addButton(self.btn_gr3_fu,1)
        self.gr3_buttons.addButton(self.btn_gr3_im,2)
        self.gr3_buttons.addButton(self.btn_gr3_ps,3)
        self.gr3_buttons.addButton(self.btn_gr3_pc,4)


class ConjugaisonLevelScreen(QMainWindow):
    def __init__(self):
        super(ConjugaisonLevelScreen, self).__init__()
        loadUi(os.path.abspath("Screens/Conjugaison/conjugaison_levelPage.ui"), self)    
