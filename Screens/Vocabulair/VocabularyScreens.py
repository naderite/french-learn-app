from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QButtonGroup
import os
import sys
import database.dbDriver as database

class VocabularyMenuScreen(QMainWindow):
    def __init__(self):
        super(VocabularyMenuScreen, self).__init__()
        loadUi(os.path.abspath("Screens/Vocabulair/vocabulair_menuPage.ui"), self)

        # creating button groups
        self.adj_buttons = QButtonGroup()
        self.vrb_buttons = QButtonGroup()
        self.add_buttons_to_groups()

    def add_buttons_to_groups(self):
        self.adj_buttons.addButton(self.btn_adj_lvl0, 0)
        self.adj_buttons.addButton(self.btn_adj_lvl1, 1)
        self.adj_buttons.addButton(self.btn_adj_lvl2, 2)
        self.adj_buttons.addButton(self.btn_adj_lvl3, 3)

        self.vrb_buttons.addButton(self.btn_vrb_lvl0, 0)
        self.vrb_buttons.addButton(self.btn_vrb_lvl1, 1)
        self.vrb_buttons.addButton(self.btn_vrb_lvl2, 2)
        self.vrb_buttons.addButton(self.btn_vrb_lvl3, 3)


class VocabularyLevelScreen(QMainWindow):
    def __init__(self):
        super(VocabularyLevelScreen, self).__init__()
        loadUi(os.path.abspath("Screens/Vocabulair/vocabulair_levelPage.ui"), self)
        self.words_guess_spaces = [self.word1_guess, self.word2_guess, self.word3_guess, self.word4_guess, self.word5_guess,
                                   self.word6_guess, self.word7_guess, self.word8_guess, self.word9_guess, self.word10_guess, self.word11_guess, self.word12_guess]

        # setup words buttons
        self.words_buttons = QButtonGroup()
        self.add_buttons_first_half()
        self.add_buttons_second_half()

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
        self.answer = answer

class VocabularyLevel:
    def __init__(self, genre, index):
        self.driver = database.JSONDriver()
        self.genre = genre
        self.index = index
        self.words = self.get_words(self.genre, self.index)
        self.title = self.get_title(self.genre, self.index)

    def get_title(self, genre, index):
        if genre == "adj":
            title = f"Adjectifs {str(index)}"
        elif genre == "vrb":
            title = f"Verbes {str(index)}"

        return title

    def get_words(self, genre, index):
        words = self.driver.getVocabWords(index, genre)
        if not words:
            sys.exit("Invalid genre")
        return [Word(word["fr"], genre, word["ar"]) for word in words] 