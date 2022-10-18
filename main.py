import sys

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QStackedWidget, QApplication, QButtonGroup, QMainWindow, QDialog
from Screens.Vocabulair.VocabularyScreens import VocabularyMenuScreen, VocabularyLevelScreen
from Screens.Grammaire.GrammaireScreens import GrammaireMenuScreen, GrammaireLevelScreen
from Screens.Conjugaison.ConjugaisonScreens import ConjugaisonMenuScreen, ConjugaisonLevelScreen
from Screens.Evaluation.EvaluationScreens import EvaluationMenuScreen, EvaluationLevelScreen

import database.json as database
import modules.vocabulary as vocabulary


class MainScreen(QStackedWidget):
    def __init__(self):
        super(MainScreen, self).__init__()
        self.create_screens()
        self.add_screens()
        self.group_buttons()
        self.connect_side_menu_buttons()
        self.connect_vocabulary_menu_adj_buttons()
        self.connect_vocabulary_menu_vrb_buttons()
        self.connect_garmmair_menu_buttons()
        self.connect_conjugaison_menu_buttons()
        self.connect_evaluation_menu_buttons()
        self.connect_return_buttons()

    def create_screens(self):
        # creating menu screens
        self.vocab_menu = VocabularyMenuScreen()
        self.gram_menu = GrammaireMenuScreen()
        self.conj_menu = ConjugaisonMenuScreen()
        self.eval_menu = EvaluationMenuScreen()

        # creating level screens
        self.vocab_level = VocabularyLevelScreen()
        self.gram_level = GrammaireLevelScreen()
        self.conj_level = ConjugaisonLevelScreen()
        self.eval_level = EvaluationLevelScreen()

    def add_screens(self):
        # adding menu screens to main window
        self.addWidget(self.vocab_menu)  # index 0
        self.addWidget(self.gram_menu)  # index 1
        self.addWidget(self.conj_menu)  # index 2
        self.addWidget(self.eval_menu)  # index 3

        # adding level screens to main window
        self.addWidget(self.vocab_level)  # index 4
        self.addWidget(self.gram_level)  # index 5
        self.addWidget(self.conj_level)  # index 6
        self.addWidget(self.eval_level)  # index 7

        # =============== ***adding buttons to groups*** =================

    def gourp_buttons(self):
        self.group_goto_vocab_buttons()
        self.group_goto_gram_buttons()
        self.group_goto_conj_buttons()
        self.group_goto_eval_buttons()
        self.group_return_to_menu_buttons()

    def group_goto_vocab_buttons(self):
        self.goto_vocab_buttons = QButtonGroup()
        self.goto_vocab_buttons.addButton(self.gram_menu.btn_to_vocab, 0)
        self.goto_vocab_buttons.addButton(self.conj_menu.btn_to_vocab, 1)
        self.goto_vocab_buttons.addButton(self.eval_menu.btn_to_vocab, 2)

    def group_goto_gram_buttons(self):
        self.goto_gram_buttons = QButtonGroup()
        self.goto_gram_buttons.addButton(self.vocab_menu.btn_to_gram, 0)
        self.goto_gram_buttons.addButton(self.conj_menu.btn_to_gram, 1)
        self.goto_gram_buttons.addButton(self.eval_menu.btn_to_gram, 2)

    def group_goto_conj_buttons(self):
        self.goto_conj_buttons = QButtonGroup()
        self.goto_conj_buttons.addButton(self.gram_menu.btn_to_conj, 0)
        self.goto_conj_buttons.addButton(self.vocab_menu.btn_to_conj, 1)
        self.goto_conj_buttons.addButton(self.eval_menu.btn_to_conj, 2)

    def group_goto_eval_buttons(self):
        self.goto_eval_buttons = QButtonGroup()
        self.goto_eval_buttons.addButton(self.gram_menu.btn_to_eval, 0)
        self.goto_eval_buttons.addButton(self.conj_menu.btn_to_eval, 1)
        self.goto_eval_buttons.addButton(self.vocab_menu.btn_to_eval, 2)

    def group_return_to_menu_buttons(self):
        self.return_to_menu_buttons = QButtonGroup()
        self.return_to_menu_buttons.addButton(
            self.vocab_level.btn_goto_menu, 0)
        self.return_to_menu_buttons.addButton(self.gram_level.btn_goto_menu, 1)
        self.return_to_menu_buttons.addButton(self.conj_level.btn_goto_menu, 2)
        self.return_to_menu_buttons.addButton(self.eval_level.btn_goto_menu, 3)

    def connect_side_menu_buttons(self):
        self.goto_vocab_buttons.buttonClicked.connect(
            lambda: Scroll.vocab_menu(self))
        self.goto_gram_buttons.buttonClicked.connect(
            lambda: Scroll.gram_menu(self))
        self.goto_conj_buttons.buttonClicked.connect(
            lambda: Scroll.conj_menu(self))
        self.goto_eval_buttons.buttonClicked.connect(
            lambda: Scroll.eval_menu(self))

    def connect_vocabulary_menu_adj_buttons(self):
        self.vocab_menu.btn_adj_lvl0.clicked.connect(
            lambda: Scroll.vocab_lvl(self, self.vocab_level, "adj", 0))
        self.vocab_menu.btn_adj_lvl1.clicked.connect(
            lambda: Scroll.vocab_lvl(self, self.vocab_level, "adj", 1))
        self.vocab_menu.btn_adj_lvl2.clicked.connect(
            lambda: Scroll.vocab_lvl(self, self.vocab_level, "adj", 2))
        self.vocab_menu.btn_adj_lvl3.clicked.connect(
            lambda: Scroll.vocab_lvl(self, self.vocab_level, "adj", 3))

    def connect_vocabulary_menu_vrb_buttons(self):
        self.vocab_menu.btn_vrb_lvl0.clicked.connect(
            lambda: Scroll.vocab_lvl(self, self.vocab_level, "vrb", 0))
        self.vocab_menu.btn_vrb_lvl1.clicked.connect(
            lambda: Scroll.vocab_lvl(self, self.vocab_level, "vrb", 1))
        self.vocab_menu.btn_vrb_lvl2.clicked.connect(
            lambda: Scroll.vocab_lvl(self, self.vocab_level, "vrb", 2))
        self.vocab_menu.btn_vrb_lvl3.clicked.connect(
            lambda: Scroll.vocab_lvl(self, self.vocab_level, "vrb", 3))

    def connect_garmmair_menu_buttons(self):
        self.gram_menu.acc_buttons.buttonClicked.connect(
            lambda: Scroll.gram_lvl(self))
        self.gram_menu.nom_buttons.buttonClicked.connect(
            lambda: Scroll.gram_lvl(self))

    def connect_conjugaison_menu_buttons(self):
        self.conj_menu.gr1_buttons.buttonClicked.connect(
            lambda: Scroll.conj_lvl(self))
        self.conj_menu.gr2_buttons.buttonClicked.connect(
            lambda: Scroll.conj_lvl(self))
        self.conj_menu.gr3_buttons.buttonClicked.connect(
            lambda: Scroll.conj_lvl(self))

    def connect_evaluation_menu_buttons(self):
        self.eval_menu.conj_buttons.buttonClicked.connect(
            lambda: Scroll.eval_lvl(self))
        self.eval_menu.gram_buttons.buttonClicked.connect(
            lambda: Scroll.eval_lvl(self))
        self.eval_menu.vocab_buttons.buttonClicked.connect(
            lambda: Scroll.eval_lvl(self))

    def connect_return_buttons(self):
        self.return_to_menu_buttons.buttonClicked.connect(
            lambda: Scroll.main_menu(self, self.currentIndex() - 4))


class MessageBox(QDialog):
    def __init__(self):
        super(MessageBox, self).__init__()
        loadUi("CorrectionMessageBox.ui", self)

        # self.btn_return_home.clicked.connect(goto_home)

    def solve(self, words, score):
        solution_txt = f"Votre score est: {score}\ 12 \n\n"
        for word in words:
            solution_txt += f"{word.name} = {word.answer} \n"
        self.msg_txt.setText(solution_txt)


class Scroll:
    # menus scrolling function
    @staticmethod
    def main_menu(widget, index):
        widget.setCurrentIndex(index)

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

    # levels scrolling functions

    def vocab_lvl(self, level_widget, genre, difficulty):
        generate_vocabulary_level(level_widget, genre, difficulty)
        self.setCurrentIndex(4)

    @staticmethod
    def gram_lvl(widget):
        widget.setCurrentIndex(5)

    @staticmethod
    def conj_lvl(widget):
        widget.setCurrentIndex(6)

    @staticmethod
    def eval_lvl(widget):
        widget.setCurrentIndex(7)


def generate_vocabulary_level(level_widget, genre, difficulty,):

    level = vocabulary.Level(genre, difficulty)
    # write level title
    level_widget.lvl_title.setText(level.title)
    # setup LevelScreen buttons text
    for button in level_widget.words_buttons.buttons():
        button.setText(level.words[level_widget.words_buttons.id(button)].name)

    # correct button

    level_widget.btn_correct.clicked.connect(
        lambda: correct(level, level_widget, level.words))


def correct(level, level_widget, orignal_words):
    guesses = get_guesses(level_widget, "vocab")
    score = 0
    for guess in guesses:
        i = 0
        answer = orignal_words[i].answer
        guess = (guess.strip())
        if guess in answer and len(guess) > 1:
            score += 1
        i += 1
    # setup message box and show the solution
    solution_box = MessageBox()
    solution_box.solve(level.words, score)
    solution_box.show()
    solution_box.exec_()


def get_guesses(widget, level_type):

    guesses = []
    if level_type in "vocab gram":
        guesses.extend((widget.word1_guess.text(), widget.word2_guess.text(), widget.word3_guess.text(), widget.word4_guess.text(), widget.word5_guess.text(), widget.word6_guess.text(
        ), widget.word7_guess.text(), widget.word8_guess.text(), widget.word9_guess.text(), widget.word10_guess.text(), widget.word11_guess.text(), widget.word12_guess.text()))

    elif level_type == "conj":
        guesses.extend((widget.word1_guess.text(), widget.word2_guess.text(), widget.word3_guess.text(
        ), widget.word4_guess.text(), widget.word5_guess.text(), widget.word6_guess.text()))
    return guesses


"""ERRORED
def get_pressed_button(buttons_group):
    for button in buttons_group.buttons():
        if button.isDown():
            return button"""


# main
app = QApplication(sys.argv)

window = MainScreen()
window.show()

sys.exit(app.exec())
