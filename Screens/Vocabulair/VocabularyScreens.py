from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QButtonGroup
import playsound
import os


class VocabularyMenuScreen(QMainWindow):
    def __init__(self):
        super(VocabularyMenuScreen, self).__init__()
        loadUi(os.path.abspath("Screens/Vocabulair/vocabulair_menuPage.ui"), self)

        #creating button groups
        self.adj_buttons = QButtonGroup()
        self.vrb_buttons = QButtonGroup()

        #adding buttons to groups
        self.adj_buttons.addButton(self.btn_adj_lvl0,0)
        self.adj_buttons.addButton(self.btn_adj_lvl1,1)
        self.adj_buttons.addButton(self.btn_adj_lvl2,2)
        self.adj_buttons.addButton(self.btn_adj_lvl3,3)
        #**********************************************
        self.vrb_buttons.addButton(self.btn_vrb_lvl0,0)
        self.vrb_buttons.addButton(self.btn_vrb_lvl1,1)
        self.vrb_buttons.addButton(self.btn_vrb_lvl2,2)
        self.vrb_buttons.addButton(self.btn_vrb_lvl3,3)



class VocabularyLevelScreen(QMainWindow):
    def __init__(self):
        super(VocabularyLevelScreen, self).__init__()
        loadUi(os.path.abspath("Screens/Vocabulair/vocabulair_levelPage.ui"), self)

        #setup words buttons 
        self.words_buttons = QButtonGroup()

        self.words_buttons.addButton(self.btn_word0,0)
        self.words_buttons.addButton(self.btn_word1,1)
        self.words_buttons.addButton(self.btn_word2,2)
        self.words_buttons.addButton(self.btn_word3,3)
        self.words_buttons.addButton(self.btn_word4,4)
        self.words_buttons.addButton(self.btn_word5,5)
        self.words_buttons.addButton(self.btn_word6,6)
        self.words_buttons.addButton(self.btn_word7,7)
        self.words_buttons.addButton(self.btn_word8,8)
        self.words_buttons.addButton(self.btn_word9,9)
        self.words_buttons.addButton(self.btn_word10,10)
        self.words_buttons.addButton(self.btn_word11,11)


