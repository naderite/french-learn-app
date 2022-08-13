from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QButtonGroup
import playsound


class GrammaireMenuScreen(QMainWindow):
    def __init__(self):
        super(GrammaireMenuScreen, self).__init__()
        loadUi(r"Screens\Grammaire\grammaire_menuPage.ui", self)

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
        loadUi(r"Screens\Grammaire\grammaire_levelPage.ui", self)
    
