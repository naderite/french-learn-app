from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QButtonGroup
import os
import sys
import database.dbDriver as database


class GrammarMenuScreen(QMainWindow):
    def __init__(self):
        super(GrammarMenuScreen, self).__init__()
        loadUi(os.path.abspath("Screens/Grammar/grammarMenuPage.ui"), self)

        # creating button groups
        self.acc_buttons = QButtonGroup()
        self.nom_buttons = QButtonGroup()

        # adding buttons to groups
        self.acc_buttons.addButton(self.btn_acc_lvl0, 0)
        self.acc_buttons.addButton(self.btn_acc_lvl1, 1)
        self.acc_buttons.addButton(self.btn_acc_lvl2, 2)
        self.acc_buttons.addButton(self.btn_acc_lvl3, 3)

        self.nom_buttons.addButton(self.btn_nom_lvl0, 0)
        self.nom_buttons.addButton(self.btn_nom_lvl1, 1)
        self.nom_buttons.addButton(self.btn_nom_lvl2, 2)
        self.nom_buttons.addButton(self.btn_nom_lvl3, 3)


class GrammarLevelScreen(QMainWindow):
    def __init__(self):
        super(GrammarLevelScreen, self).__init__()
        loadUi(os.path.abspath("Screens/Grammar/grammarLevelPage.ui"), self)
        self.words_buttons = QButtonGroup()
        self.add_buttons_first_half()
        self.add_buttons_second_half()
        self.words_guess_spaces = [self.word1_guess, self.word2_guess, self.word3_guess, self.word4_guess, self.word5_guess,
                                   self.word6_guess, self.word7_guess, self.word8_guess, self.word9_guess, self.word10_guess, self.word11_guess, self.word12_guess]

    def add_buttons_first_half(self):
        self.words_buttons.addButton(self.btn_word0, 0)
        self.words_buttons.addButton(self.btn_word1, 1)
        self.words_buttons.addButton(self.btn_word2, 2)
        self.words_buttons.addButton(self.btn_word3, 3)
        self.words_buttons.addButton(self.btn_word4, 4)
        self.words_buttons.addButton(self.btn_word5, 5)

    def add_buttons_second_half(self):
        self.words_buttons.addButton(self.btn_word6, 6)
        self.words_buttons.addButton(self.btn_word7, 7)
        self.words_buttons.addButton(self.btn_word8, 8)
        self.words_buttons.addButton(self.btn_word9, 9)
        self.words_buttons.addButton(self.btn_word10, 10)
        self.words_buttons.addButton(self.btn_word11, 11)


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

    def get_title(self, genre, index):
        if genre == "acc":
            title = f"Accord des adjectifs {str(index)}"
        elif genre == "nom":
            title = f"Nominalisation {str(index)}"

        return title

    def get_words(self, genre, index):
        words = self.driver.getGramWords(index, genre)
        if not words:
            sys.exit("Invalid genre")
        return [Word(word["adj"], genre, word["fem"]) for word in words] if genre == "acc" else [Word(word["vrb"], genre, word["nom"]) for word in words]
