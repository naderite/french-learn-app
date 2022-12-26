from ui import grammarLevelPage, grammarMenuPage
from PyQt5.QtWidgets import QMainWindow, QButtonGroup
import os
import sys
import database.dbDriver as database


class GrammarMenuScreen(QMainWindow):
    def __init__(self):
        super(GrammarMenuScreen, self).__init__()
        self.ui = grammarMenuPage.Ui_MainWindow()
        self.ui.setupUi(self)

        # creating button groups
        self.acc_buttons = QButtonGroup()
        self.nom_buttons = QButtonGroup()

        # adding buttons to groups
        self.acc_buttons.addButton(self.ui.btn_acc_lvl0, 0)
        self.acc_buttons.addButton(self.ui.btn_acc_lvl1, 1)
        self.acc_buttons.addButton(self.ui.btn_acc_lvl2, 2)
        self.acc_buttons.addButton(self.ui.btn_acc_lvl3, 3)

        self.nom_buttons.addButton(self.ui.btn_nom_lvl0, 0)
        self.nom_buttons.addButton(self.ui.btn_nom_lvl1, 1)
        self.nom_buttons.addButton(self.ui.btn_nom_lvl2, 2)
        self.nom_buttons.addButton(self.ui.btn_nom_lvl3, 3)


class GrammarLevelScreen(QMainWindow):
    def __init__(self):
        super(GrammarLevelScreen, self).__init__()
        self.ui = grammarLevelPage.Ui_MainWindow()
        self.ui.setupUi(self)

        self.words_buttons = QButtonGroup()
        self.add_buttons_first_half()
        self.add_buttons_second_half()
        self.words_guess_spaces = [self.ui.word1_guess, self.ui.word2_guess, self.ui.word3_guess, self.ui.word4_guess, self.ui.word5_guess,
                                   self.ui.word6_guess, self.ui.word7_guess, self.ui.word8_guess, self.ui.word9_guess, self.ui.word10_guess, self.ui.word11_guess, self.ui.word12_guess]
        self.level = None

    def add_buttons_first_half(self):
        self.words_buttons.addButton(self.ui.btn_word0, 0)
        self.words_buttons.addButton(self.ui.btn_word1, 1)
        self.words_buttons.addButton(self.ui.btn_word2, 2)
        self.words_buttons.addButton(self.ui.btn_word3, 3)
        self.words_buttons.addButton(self.ui.btn_word4, 4)
        self.words_buttons.addButton(self.ui.btn_word5, 5)

    def add_buttons_second_half(self):
        self.words_buttons.addButton(self.ui.btn_word6, 6)
        self.words_buttons.addButton(self.ui.btn_word7, 7)
        self.words_buttons.addButton(self.ui.btn_word8, 8)
        self.words_buttons.addButton(self.ui.btn_word9, 9)
        self.words_buttons.addButton(self.ui.btn_word10, 10)
        self.words_buttons.addButton(self.ui.btn_word11, 11)


class Word:
    def __init__(self, name, genre, answer):
        self.name = name
        self.genre = genre
        self.answer = answer  # if verb its the noun, if an adjective its the female accord


class GrammarLevel:
    def __init__(self, genre, index):
        self.driver = database.JSONDriver()
        self.genre = genre
        self.index = index
        self.words = self.get_words(self.genre, self.index)
        self.title = self.get_title(self.genre, self.index)
        self.question = self.get_question(self.genre)

    def get_title(self, genre, index):
        return f"Accord {str(index)}" if genre == "acc" else f"Nominalisation {str(index)}"

    def get_question(self, genre):
        return "accorder ces adjectifs au femenin" if genre == "acc" else "donner le correspendant à chaque verbe"

    def get_words(self, genre, index):
        words = self.driver.getGramWords(index, genre)
        if not words:
            sys.exit("Invalid genre")
        return [Word(word["adj"], genre, word["fem"]) for word in words] if genre == "acc" else [Word(word["vrb"], genre, word["nom"]) for word in words]
