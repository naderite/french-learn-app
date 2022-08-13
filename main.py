import sys

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QStackedWidget, QApplication, QButtonGroup, QMainWindow, QDialog
from dictionary import adjectives, verbes
from Screens.Vocabulair.VocabularyScreens import VocabularyMenuScreen, VocabularyLevelScreen
from Screens.Grammaire.GrammaireScreens import GrammaireMenuScreen, GrammaireLevelScreen
from Screens.Conjugaison.ConjugaisonScreens import ConjugaisonMenuScreen, ConjugaisonLevelScreen
from Screens.Evaluation.EvaluationScreens import EvaluationMenuScreen, EvaluationLevelScreen


class MainScreen(QStackedWidget):
    def __init__(self):
        super(MainScreen, self).__init__()

        # creating menu screens
        self.vocab_menu = VocabularyMenuScreen()
        self.gram_menu = GrammaireMenuScreen()
        self.conj_menu = ConjugaisonMenuScreen()
        self.eval_menu = EvaluationMenuScreen()

        # adding menus
        self.addWidget(self.vocab_menu)#index 0
        self.addWidget(self.gram_menu)# index 1
        self.addWidget(self.conj_menu)# index 2
        self.addWidget(self.eval_menu)# index 3

        #creating level screens
        self.vocab_level = VocabularyLevelScreen()
        self.gram_level = GrammaireLevelScreen()
        self.conj_level = ConjugaisonLevelScreen()
        self.eval_level = EvaluationLevelScreen()

        #adding levels
        self.addWidget(self.vocab_level)#index 4
        self.addWidget(self.gram_level)# index 5
        self.addWidget(self.conj_level)# index 6 
        self.addWidget(self.eval_level)# index 7

        self.setup_button_groups()


    def setup_button_groups(self):
        # creating buttons groups
        self.goto_vocab_buttons = QButtonGroup()
        self.goto_gram_buttons = QButtonGroup()
        self.goto_conj_buttons = QButtonGroup()
        self.goto_eval_buttons = QButtonGroup()

        # adding buttons to groups
        self.goto_vocab_buttons.addButton(self.gram_menu.btn_to_vocab, 0)
        self.goto_vocab_buttons.addButton(self.conj_menu.btn_to_vocab, 1)
        self.goto_vocab_buttons.addButton(self.eval_menu.btn_to_vocab, 2)

        self.goto_gram_buttons.addButton(self.vocab_menu.btn_to_gram, 0)
        self.goto_gram_buttons.addButton(self.conj_menu.btn_to_gram, 1)
        self.goto_gram_buttons.addButton(self.eval_menu.btn_to_gram, 2)

        self.goto_conj_buttons.addButton(self.gram_menu.btn_to_conj, 0)
        self.goto_conj_buttons.addButton(self.vocab_menu.btn_to_conj, 1)
        self.goto_conj_buttons.addButton(self.eval_menu.btn_to_conj, 2)

        self.goto_eval_buttons.addButton(self.gram_menu.btn_to_eval, 0)
        self.goto_eval_buttons.addButton(self.conj_menu.btn_to_eval, 1)
        self.goto_eval_buttons.addButton(self.vocab_menu.btn_to_eval, 2)

        # connecting side menu groups to functions
        self.goto_vocab_buttons.buttonClicked.connect(lambda: Scroll.vocab_menu(self))
        self.goto_gram_buttons.buttonClicked.connect(lambda: Scroll.gram_menu(self))
        self.goto_conj_buttons.buttonClicked.connect(lambda: Scroll.conj_menu(self))
        self.goto_eval_buttons.buttonClicked.connect(lambda: Scroll.eval_menu(self))

        #connceting main menu group to functions
        self.vocab_menu.adj_buttons.buttonClicked.connect(lambda: Scroll.vocab_lvl(self))
        self.vocab_menu.vrb_buttons.buttonClicked.connect(lambda: Scroll.vocab_lvl(self))

        self.gram_menu.acc_buttons.buttonClicked.connect(lambda: Scroll.gram_lvl(self))
        self.gram_menu.nom_buttons.buttonClicked.connect(lambda: Scroll.gram_lvl(self))

        self.conj_menu.gr1_buttons.buttonClicked.connect(lambda: Scroll.conj_lvl(self))
        self.conj_menu.gr2_buttons.buttonClicked.connect(lambda: Scroll.conj_lvl(self))
        self.conj_menu.gr3_buttons.buttonClicked.connect(lambda: Scroll.conj_lvl(self))

        self.eval_menu.conj_buttons.buttonClicked.connect(lambda: Scroll.eval_lvl(self))
        self.eval_menu.gram_buttons.buttonClicked.connect(lambda: Scroll.eval_lvl(self))
        self.eval_menu.vocab_buttons.buttonClicked.connect(lambda: Scroll.eval_lvl(self))

class Scroll:
    #menus
    @staticmethod
    def vocab_menu(widget):
        widget.setCurrentIndex(0)
    @staticmethod
    def gram_menu(widget):
        widget.setCurrentIndex(1)
    @staticmethod
    def conj_menu(widget):
        widget.setCurrentIndex(2)
    @staticmethod
    def eval_menu(widget):
        widget.setCurrentIndex(3)

    #levels
    @staticmethod
    def vocab_lvl(widget):
        widget.setCurrentIndex(4)
    @staticmethod
    def gram_lvl(widget):
        widget.setCurrentIndex(5)
    @staticmethod
    def conj_lvl(widget):
        widget.setCurrentIndex(6)
    @staticmethod
    def eval_lvl(widget):
        widget.setCurrentIndex(7)

"""class LevelScreen(QMainWindow):
    def __init__(self, widget, genre, diffculty):
        super(LevelScreen, self).__init__()
        loadUi("LevelWindow.ui", self)

        self.widget = widget

        self.lvl = self.generate_level(genre, diffculty)
        self.btn_correct.clicked.connect(self.correct)
        self.btn_return_home.clicked.connect(goto_home)

    def generate_level(self, genre, diffculty):
        level = Level(genre, diffculty)

        # write level title
        self.lvl_title.setText(level.title)

        # setup LevelScreen buttons text
        self.btn_word1.setText(level.words[0].name)
        self.btn_word2.setText(level.words[1].name)
        self.btn_word3.setText(level.words[2].name)
        self.btn_word4.setText(level.words[3].name)
        self.btn_word5.setText(level.words[4].name)
        self.btn_word6.setText(level.words[5].name)
        self.btn_word7.setText(level.words[6].name)
        self.btn_word8.setText(level.words[7].name)
        self.btn_word9.setText(level.words[8].name)
        self.btn_word10.setText(level.words[9].name)
        self.btn_word11.setText(level.words[10].name)
        self.btn_word12.setText(level.words[11].name)

        # connect LevelScreen buttons to the sound playing function
        self.btn_word1.clicked.connect(lambda: self.hear(level.words[0].sound))
        self.btn_word2.clicked.connect(lambda: self.hear(level.words[1].sound))
        self.btn_word3.clicked.connect(lambda: self.hear(level.words[2].sound))
        self.btn_word4.clicked.connect(lambda: self.hear(level.words[3].sound))
        self.btn_word5.clicked.connect(lambda: self.hear(level.words[4].sound))
        self.btn_word6.clicked.connect(lambda: self.hear(level.words[5].sound))
        self.btn_word7.clicked.connect(lambda: self.hear(level.words[6].sound))
        self.btn_word8.clicked.connect(lambda: self.hear(level.words[7].sound))
        self.btn_word9.clicked.connect(lambda: self.hear(level.words[8].sound))
        self.btn_word10.clicked.connect(
            lambda: self.hear(level.words[9].sound))
        self.btn_word11.clicked.connect(
            lambda: self.hear(level.words[10].sound))
        self.btn_word12.clicked.connect(
            lambda: self.hear(level.words[11].sound))

        return level

    def correct(self):
        guesses = self.get_guesses()
        score = 0
        for index in range(12):
            if guesses[index].strip() in self.lvl.words[index].match and guesses[index].strip() != "":
                score += 1

        # setup message box and show the solution
        solution_box = MessageBox(self.lvl.words, score)

        solution_box.show()
        solution_box.exec_()

    def get_guesses(self):
        guesses = []

        guesses.append(self.word1_guess.text())
        guesses.append(self.word2_guess.text())
        guesses.append(self.word3_guess.text())
        guesses.append(self.word4_guess.text())
        guesses.append(self.word5_guess.text())
        guesses.append(self.word6_guess.text())
        guesses.append(self.word7_guess.text())
        guesses.append(self.word8_guess.text())
        guesses.append(self.word9_guess.text())
        guesses.append(self.word10_guess.text())
        guesses.append(self.word11_guess.text())
        guesses.append(self.word12_guess.text())

        return guesses

    def hear(self, sound):
        playsound(r"WordsPronunciation\{}".format(sound))
"""


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
