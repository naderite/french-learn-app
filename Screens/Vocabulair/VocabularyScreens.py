from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QButtonGroup
import playsound


class VocabularyMenuScreen(QMainWindow):
    def __init__(self):
        super(VocabularyMenuScreen, self).__init__()
        loadUi(r"Screens\Vocabulair\vocabulair_menuPage.ui", self)

        #creating button groups
        self.adj_buttons = QButtonGroup()
        self.vrb_buttons = QButtonGroup()

        #adding buttons to groups
        self.adj_buttons.addButton(self.btn_adj_lvl0,0)
        self.adj_buttons.addButton(self.btn_adj_lvl1,1)
        self.adj_buttons.addButton(self.btn_adj_lvl2,2)
        self.adj_buttons.addButton(self.btn_adj_lvl3,3)

        self.vrb_buttons.addButton(self.btn_vrb_lvl0,0)
        self.vrb_buttons.addButton(self.btn_vrb_lvl1,1)
        self.vrb_buttons.addButton(self.btn_vrb_lvl2,2)
        self.vrb_buttons.addButton(self.btn_vrb_lvl3,3)


class VocabularyLevelScreen(QMainWindow):
    def __init__(self):
        super(VocabularyLevelScreen, self).__init__()
        loadUi(r"Screens\Vocabulair\vocabulair_levelPage.ui", self)
