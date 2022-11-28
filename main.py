import sys

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QStackedWidget, QApplication, QButtonGroup, QMainWindow, QDialog
from Screens.Vocabulair.VocabularyScreens import VocabularyMenuScreen, VocabularyLevelScreen
from Screens.Grammaire.GrammaireScreens import GrammaireMenuScreen, GrammaireLevelScreen
from Screens.Conjugaison.ConjugaisonScreens import ConjugaisonMenuScreen, ConjugaisonLevelScreen


import database.dbDriver as database
import modules.vocabulary as Vocabulary
import modules.grammar as Grammar
import modules.conjugation as Conjugaison


class MainScreen(QStackedWidget):
    def __init__(self):
        super(MainScreen, self).__init__()
        self.create_screens()
        self.add_screens()
        self.group_buttons()
        self.connect_side_menu_buttons()
        self.connect_vocabulary_menu_adj_buttons()
        self.connect_vocabulary_menu_vrb_buttons()
        self.connect_garmmair_menu_acc_buttons()
        self.connect_conjugaison_grp1_menu_buttons()
        self.connect_conjugaison_grp2_menu_buttons()
        self.connect_conjugaison_grp3_menu_buttons()
        self.connect_return_buttons()
        self.connect_garmmair_menu_nom_buttons()

    def create_screens(self):
        # creating menu screens
        self.vocab_menu = VocabularyMenuScreen()
        self.gram_menu = GrammaireMenuScreen()
        self.conj_menu = ConjugaisonMenuScreen()

        # creating level screens
        self.vocab_level = VocabularyLevelScreen()
        self.gram_level = GrammaireLevelScreen()
        self.conj_level = ConjugaisonLevelScreen()

        self.solution_box = MessageBox()

    def add_screens(self):
        # adding menu screens to main window
        self.addWidget(self.vocab_menu)  # index 0
        self.addWidget(self.gram_menu)  # index 1
        self.addWidget(self.conj_menu)  # index 2

        # adding level screens to main window
        self.addWidget(self.vocab_level)  # index 3
        self.addWidget(self.gram_level)  # index 4
        self.addWidget(self.conj_level)  # index 5

        # =============== ***adding buttons to groups*** =================

    def group_buttons(self):
        self.group_goto_vocab_buttons()
        self.group_goto_gram_buttons()
        self.group_goto_conj_buttons()
        self.group_return_to_menu_buttons()

    def group_goto_vocab_buttons(self):
        self.goto_vocab_buttons = QButtonGroup()
        self.goto_vocab_buttons.addButton(self.gram_menu.btn_to_vocab, 0)
        self.goto_vocab_buttons.addButton(self.conj_menu.btn_to_vocab, 1)

    def group_goto_gram_buttons(self):
        self.goto_gram_buttons = QButtonGroup()
        self.goto_gram_buttons.addButton(self.vocab_menu.btn_to_gram, 0)
        self.goto_gram_buttons.addButton(self.conj_menu.btn_to_gram, 1)

    def group_goto_conj_buttons(self):
        self.goto_conj_buttons = QButtonGroup()
        self.goto_conj_buttons.addButton(self.gram_menu.btn_to_conj, 0)
        self.goto_conj_buttons.addButton(self.vocab_menu.btn_to_conj, 1)

    def group_return_to_menu_buttons(self):
        self.return_to_menu_buttons = QButtonGroup()
        self.return_to_menu_buttons.addButton(
            self.vocab_level.btn_goto_menu, 0)
        self.return_to_menu_buttons.addButton(self.gram_level.btn_goto_menu, 1)
        self.return_to_menu_buttons.addButton(self.conj_level.btn_goto_menu, 2)
        self.return_to_menu_buttons.addButton(
            self.solution_box.btn_goto_menu, 2)

    def connect_side_menu_buttons(self):
        self.goto_vocab_buttons.buttonClicked.connect(
            lambda: Scroll.vocab_menu(self))
        self.goto_gram_buttons.buttonClicked.connect(
            lambda: Scroll.gram_menu(self))
        self.goto_conj_buttons.buttonClicked.connect(
            lambda: Scroll.conj_menu(self))

    def connect_vocabulary_menu_adj_buttons(self):
        self.vocab_menu.btn_adj_lvl0.clicked.connect(
            lambda: Scroll.vocab_lvl(self, self.vocab_level, "adj", 0, self.solution_box))
        self.vocab_menu.btn_adj_lvl1.clicked.connect(
            lambda: Scroll.vocab_lvl(self, self.vocab_level, "adj", 1, self.solution_box))
        self.vocab_menu.btn_adj_lvl2.clicked.connect(
            lambda: Scroll.vocab_lvl(self, self.vocab_level, "adj", 2, self.solution_box))
        self.vocab_menu.btn_adj_lvl3.clicked.connect(
            lambda: Scroll.vocab_lvl(self, self.vocab_level, "adj", 3, self.solution_box))

    def connect_vocabulary_menu_vrb_buttons(self):
        self.vocab_menu.btn_vrb_lvl0.clicked.connect(
            lambda: Scroll.vocab_lvl(self, self.vocab_level, "vrb", 0, self.solution_box))
        self.vocab_menu.btn_vrb_lvl1.clicked.connect(
            lambda: Scroll.vocab_lvl(self, self.vocab_level, "vrb", 1, self.solution_box))
        self.vocab_menu.btn_vrb_lvl2.clicked.connect(
            lambda: Scroll.vocab_lvl(self, self.vocab_level, "vrb", 2, self.solution_box))
        self.vocab_menu.btn_vrb_lvl3.clicked.connect(
            lambda: Scroll.vocab_lvl(self, self.vocab_level, "vrb", 3, self.solution_box))

    def connect_garmmair_menu_acc_buttons(self):
        self.gram_menu.btn_acc_lvl0.clicked.connect(
            lambda: Scroll.gram_lvl(self, self.gram_level, "acc", 0, self.solution_box))
        self.gram_menu.btn_acc_lvl1.clicked.connect(
            lambda: Scroll.gram_lvl(self, self.gram_level, "acc", 1, self.solution_box))
        self.gram_menu.btn_acc_lvl2.clicked.connect(
            lambda: Scroll.gram_lvl(self, self.gram_level, "acc", 2, self.solution_box))
        self.gram_menu.btn_acc_lvl3.clicked.connect(
            lambda: Scroll.gram_lvl(self, self.gram_level, "acc", 3, self.solution_box))

    def connect_garmmair_menu_nom_buttons(self):
        self.gram_menu.btn_nom_lvl0.clicked.connect(
            lambda: Scroll.gram_lvl(self, self.gram_level, "nom", 0, self.solution_box))
        self.gram_menu.btn_nom_lvl1.clicked.connect(
            lambda: Scroll.gram_lvl(self, self.gram_level, "nom", 1, self.solution_box))
        self.gram_menu.btn_nom_lvl2.clicked.connect(
            lambda: Scroll.gram_lvl(self, self.gram_level, "nom", 2, self.solution_box))
        self.gram_menu.btn_nom_lvl3.clicked.connect(
            lambda: Scroll.gram_lvl(self, self.gram_level, "nom", 3, self.solution_box))

    def connect_conjugaison_grp1_menu_buttons(self):

        self.conj_menu.btn_gr1_pr.clicked.connect(
            lambda: Scroll.conj_lvl(self, self.conj_level, "present", 0, self.solution_box))
        self.conj_menu.btn_gr1_fu.clicked.connect(
            lambda: Scroll.conj_lvl(self, self.conj_level, "future", 0, self.solution_box))
        self.conj_menu.btn_gr1_im.clicked.connect(
            lambda: Scroll.conj_lvl(self, self.conj_level, "imparfait", 0, self.solution_box))
        self.conj_menu.btn_gr1_ps.clicked.connect(
            lambda: Scroll.conj_lvl(self, self.conj_level, "passe simple", 0, self.solution_box))
        self.conj_menu.btn_gr1_pc.clicked.connect(
            lambda: Scroll.conj_lvl(self, self.conj_level, "passe compose", 0, self.solution_box))

    def connect_conjugaison_grp2_menu_buttons(self):

        self.conj_menu.btn_gr2_pr.clicked.connect(
            lambda: Scroll.conj_lvl(self, self.conj_level, "present", 1, self.solution_box))
        self.conj_menu.btn_gr2_fu.clicked.connect(
            lambda: Scroll.conj_lvl(self, self.conj_level, "future", 1, self.solution_box))
        self.conj_menu.btn_gr2_im.clicked.connect(
            lambda: Scroll.conj_lvl(self, self.conj_level, "imparfait", 1, self.solution_box))
        self.conj_menu.btn_gr2_ps.clicked.connect(
            lambda: Scroll.conj_lvl(self, self.conj_level, "passe simple", 1, self.solution_box))
        self.conj_menu.btn_gr2_pc.clicked.connect(
            lambda: Scroll.conj_lvl(self, self.conj_level, "passe compose", 1, self.solution_box))

    def connect_conjugaison_grp3_menu_buttons(self):

        self.conj_menu.btn_gr3_pr.clicked.connect(
            lambda: Scroll.conj_lvl(self, self.conj_level, "present", 2, self.solution_box))
        self.conj_menu.btn_gr3_fu.clicked.connect(
            lambda: Scroll.conj_lvl(self, self.conj_level, "future", 2, self.solution_box))
        self.conj_menu.btn_gr3_im.clicked.connect(
            lambda: Scroll.conj_lvl(self, self.conj_level, "imparfait", 2, self.solution_box))
        self.conj_menu.btn_gr3_ps.clicked.connect(
            lambda: Scroll.conj_lvl(self, self.conj_level, "passe simple", 2, self.solution_box))
        self.conj_menu.btn_gr3_pc.clicked.connect(
            lambda: Scroll.conj_lvl(self, self.conj_level, "passe compose", 2, self.solution_box))

    def connect_return_buttons(self):
        self.return_to_menu_buttons.buttonClicked.connect(
            lambda: Scroll.main_menu(self, self.currentIndex() - 3))


class MessageBox(QDialog):
    def __init__(self):
        super(MessageBox, self).__init__()
        loadUi("CorrectionMessageBox.ui", self)

        # self.btn_return_home.clicked.connect(goto_home)

    def write_solution(self, words, score, level_type):
        solution_txt = f"Votre score est: {score}\ 12 \n\n"
        if level_type in ["gram", "vocab"]:
            for word in words:
                solution_txt += f"{word.name} = {word.answer} \n"
        else:
            # convert the dictionary to a list of tuples of pronoun and answer pair
            words = words.items()
            for word in words:
                solution_txt += f"{word[0]} {word[1]} \n"
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

    # levels scrolling functions
    @staticmethod
    def vocab_lvl(widget, level_widget, genre, difficulty, solution_box):
        generate_vocabulary_level(
            level_widget, genre, difficulty, solution_box)
        widget.setCurrentIndex(3)
        solution_box.btn_tryagain.clicked.connect(lambda: Scroll.reload_lvl(
            widget, level_widget, genre, difficulty, solution_box))

    @staticmethod
    def gram_lvl(widget, level_widget, genre, difficulty, solution_box):
        generate_grammar_level(level_widget, genre, difficulty, solution_box)
        widget.setCurrentIndex(4)
        solution_box.btn_tryagain.clicked.connect(lambda: Scroll.reload_lvl(
            widget, level_widget, genre, difficulty, solution_box))

    @staticmethod
    def conj_lvl(widget, level_widget, temp, groupe, solution_box):
        generate_conjuguaison_level(level_widget, temp, groupe, solution_box)
        widget.setCurrentIndex(5)
        solution_box.btn_tryagain.clicked.connect(lambda: Scroll.reload_lvl(
            widget, level_widget, temp, groupe, solution_box))

    @staticmethod
    def reload_lvl(widget, level_widget, param_1, param_2, solution_box):
        match widget.currentIndex():
            case 3:
                Scroll.vocab_lvl(widget, level_widget,
                                 param_1, param_2, solution_box)
            case 4:
                Scroll.gram_lvl(widget, level_widget, param_1,
                                param_2, solution_box)
            case 5:
                Scroll.conj_lvl(widget, level_widget, param_1,
                                param_2, solution_box)


def generate_grammar_level(level_widget, genre, difficulty, solution_box):
    level = Grammar.Level(genre, difficulty)
    # write level title
    level_widget.lvl_title.setText(level.title)
    # setup LevelScreen buttons text
    for button in level_widget.words_buttons.buttons():
        button.setText(level.words[level_widget.words_buttons.id(button)].name)

    # reset the words guess space
    for guess_space in level_widget.words_guess_spaces:
        guess_space.setText("")
    # correct button
    level_widget.btn_correct.clicked.connect(
        lambda: correct(level_widget, level.words, "gram", solution_box))


def generate_vocabulary_level(level_widget, genre, difficulty, solution_box):

    level = Vocabulary.Level(genre, difficulty)
    # write level title
    level_widget.lvl_title.setText(level.title)
    # setup LevelScreen buttons text
    for button in level_widget.words_buttons.buttons():
        button.setText(level.words[level_widget.words_buttons.id(button)].name)

    # reset the words guess space
    for guess_space in level_widget.words_guess_spaces:
        guess_space.setText("")
    # correct button
    level_widget.btn_correct.clicked.connect(
        lambda: correct(level_widget, level.words, "vocab", solution_box))


def generate_conjuguaison_level(level_widget, temp, groupe, solution_box):
    level = Conjugaison.Level(temp, groupe)
    level_widget.lvl_title.setText(level.title)
    level_widget.lvl_verb.setText(level.verb)
    level_widget.btn_correct.clicked.connect(
        lambda: correct(level_widget, level.answer, "conj", solution_box))

    # reset the words guess space
    for guess_space in level_widget.words_guess_spaces:
        guess_space.setText("")


def correct(level_widget, original_words, level_type, solution_box):
    guesses = get_guesses(level_widget)
    score = 0
    if level_type in ["gram", "vocab"]:
        for guess in guesses:
            index = 0
            answer = original_words[index].answer
            guess = (guess.strip())
            if guess in answer and len(guess) > 1:
                score += 1
            index += 1
    else:
        answers = original_words.values()
        score = sum(guess in answers for guess in guesses)
    # setup message box and show the solution

    solution_box.write_solution(original_words, score, level_type)
    solution_box.show()
    solution_box.exec_()


def get_guesses(widget):
    return [guess.text() for guess in widget.words_guess_spaces]


# main
app = QApplication(sys.argv)

window = MainScreen()
window.show()

sys.exit(app.exec())
