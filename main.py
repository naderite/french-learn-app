import sys

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QStackedWidget, QApplication, QButtonGroup, QMainWindow, QDialog
from dictionary import adjectives, verbes
from Screens.Vocabulair.VocabularyMenu import VocabularyMenuScreen
from Screens.Grammaire.GrammairMenu import GrammaireMenuScreen
from Screens.Conjugaison.ConjugaisonMenu import ConjugaisonMenuScreen
from Screens.Evaluation.EvaluationMenu import EvaluationMenuScreen


class MainScreen(QStackedWidget):
    def __init__(self):
        super(MainScreen, self).__init__()

        # creating menu screens
        vocab_menu = VocabularyMenuScreen()
        self.addWidget(vocab_menu)

        gram_menu = GrammaireMenuScreen()
        self.addWidget(gram_menu)

        conj_menu = ConjugaisonMenuScreen()
        self.addWidget(conj_menu)

        eval_menu = EvaluationMenuScreen()
        self.addWidget(eval_menu)

        # creating buttons groups
        self.goto_vocab_buttons = QButtonGroup()
        self.goto_gram_buttons = QButtonGroup()
        self.goto_conj_buttons = QButtonGroup()
        self.goto_eval_buttons = QButtonGroup()

        # adding buttons to groups
        self.goto_vocab_buttons.addButton(gram_menu.btn_to_vocab, 0)
        self.goto_vocab_buttons.addButton(conj_menu.btn_to_vocab, 1)
        self.goto_vocab_buttons.addButton(eval_menu.btn_to_vocab, 2)

        self.goto_gram_buttons.addButton(vocab_menu.btn_to_gram, 0)
        self.goto_gram_buttons.addButton(conj_menu.btn_to_gram, 1)
        self.goto_gram_buttons.addButton(eval_menu.btn_to_gram, 2)

        self.goto_conj_buttons.addButton(gram_menu.btn_to_conj, 0)
        self.goto_conj_buttons.addButton(vocab_menu.btn_to_conj, 1)
        self.goto_conj_buttons.addButton(eval_menu.btn_to_conj, 2)

        self.goto_eval_buttons.addButton(gram_menu.btn_to_eval, 0)
        self.goto_eval_buttons.addButton(conj_menu.btn_to_eval, 1)
        self.goto_eval_buttons.addButton(vocab_menu.btn_to_eval, 2)

        # connecting groups to functions
        self.goto_vocab_buttons.buttonClicked.connect(self.goto_vocab)
        self.goto_gram_buttons.buttonClicked.connect(self.goto_gram)
        self.goto_conj_buttons.buttonClicked.connect(self.goto_conj)
        self.goto_eval_buttons.buttonClicked.connect(self.goto_eval)

    # scrolling functions

    def goto_vocab(self):
        self.setCurrentIndex(0)

    def goto_gram(self):
        self.setCurrentIndex(1)

    def goto_conj(self):
        self.setCurrentIndex(2)

    def goto_eval(self):
        self.setCurrentIndex(3)


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
