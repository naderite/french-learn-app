import sys

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QStackedWidget, QApplication,QButtonGroup , QMainWindow, QDialog 
from dictionary import adjectives, verbes
from Screens.Vocabulair.VocabularyMenu import VocabularyMenuScreen
from Screens.Grammaire.GrammairMenu import GrammaireMenuScreen
from Screens.Conjugaison.ConjugaisonMenu import ConjugaisonMenuScreen
from Screens.Evaluation.EvaluationMenu import EvaluationMenuScreen


class MainScreen(QStackedWidget):
    def __init__(self):
        super(MainScreen, self).__init__()

        #creating menu screens
        vocab_menu = VocabularyMenuScreen()
        self.addWidget(vocab_menu)
        
        gram_menu = GrammaireMenuScreen()
        self.addWidget(gram_menu)
        
        conj_menu = ConjugaisonMenuScreen()
        self.addWidget(conj_menu)

        eval_menu = EvaluationMenuScreen()
        self.addWidget(eval_menu)

        #creating buttons groups
        self.goto_vocab_buttons = QButtonGroup()
        self.goto_gram_buttons = QButtonGroup()
        self.goto_conj_buttons = QButtonGroup()
        self.goto_eval_buttons = QButtonGroup()

        #adding buttons to groups
        self.goto_vocab_buttons.addButton(gram_menu.btn_to_vocab,0)
        self.goto_vocab_buttons.addButton(conj_menu.btn_to_vocab,1)
        self.goto_vocab_buttons.addButton(eval_menu.btn_to_vocab,2)

        self.goto_gram_buttons.addButton(vocab_menu.btn_to_gram,0)
        self.goto_gram_buttons.addButton(conj_menu.btn_to_gram,1)
        self.goto_gram_buttons.addButton(eval_menu.btn_to_gram,2)

        self.goto_conj_buttons.addButton(gram_menu.btn_to_conj,0)
        self.goto_conj_buttons.addButton(vocab_menu.btn_to_conj,1)
        self.goto_conj_buttons.addButton(eval_menu.btn_to_conj,2)

        self.goto_eval_buttons.addButton(gram_menu.btn_to_eval,0)
        self.goto_eval_buttons.addButton(conj_menu.btn_to_eval,1)
        self.goto_eval_buttons.addButton(vocab_menu.btn_to_eval,2)

        #connecting groups to functions
        self.goto_vocab_buttons.buttonClicked.connect(self.goto_vocab)
        self.goto_gram_buttons.buttonClicked.connect(self.goto_gram)
        self.goto_conj_buttons.buttonClicked.connect(self.goto_conj)
        self.goto_eval_buttons.buttonClicked.connect(self.goto_eval)

    
    #scrolling functions
    def goto_vocab(self):
        self.setCurrentIndex(0)

    def goto_gram(self):
        self.setCurrentIndex(1)
    
    def goto_conj(self):
        self.setCurrentIndex(2)
    
    def goto_eval(self):
        self.setCurrentIndex(3)

class Word():
    def __init__(self, name, match, sound):
        self.name = name
        self.match = match
        self.sound = sound




# main
app = QApplication(sys.argv)

window = MainScreen()
window.show()

sys.exit(app.exec())
