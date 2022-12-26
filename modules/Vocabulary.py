from ui import vocabularyLevelPage, vocabularyMenuPage
from PyQt5.QtWidgets import QMainWindow, QButtonGroup
import os
import sys
import database.dbDriver as database


class VocabularyMenuScreen(QMainWindow):
    def __init__(self):
        super(VocabularyMenuScreen, self).__init__()
        self.ui = vocabularyMenuPage.Ui_MainWindow()
        self.ui.setupUi(self)

        # creating button groups
        self.adj_buttons = QButtonGroup()
        self.vrb_buttons = QButtonGroup()
        self.add_buttons_to_groups()

    def add_buttons_to_groups(self):
        self.adj_buttons.addButton(self.ui.btn_adj_lvl0, 0)
        self.adj_buttons.addButton(self.ui.btn_adj_lvl1, 1)
        self.adj_buttons.addButton(self.ui.btn_adj_lvl2, 2)
        self.adj_buttons.addButton(self.ui.btn_adj_lvl3, 3)

        self.vrb_buttons.addButton(self.ui.btn_vrb_lvl0, 0)
        self.vrb_buttons.addButton(self.ui.btn_vrb_lvl1, 1)
        self.vrb_buttons.addButton(self.ui.btn_vrb_lvl2, 2)
        self.vrb_buttons.addButton(self.ui.btn_vrb_lvl3, 3)


class VocabularyLevelScreen(QMainWindow):

    def __init__(self):
        super(VocabularyLevelScreen, self).__init__()
        self.ui = vocabularyLevelPage.Ui_MainWindow()
        self.ui.setupUi(self)

        self.words_guess_spaces = [self.ui.word1_guess, self.ui.word2_guess, self.ui.word3_guess, self.ui.word4_guess, self.ui.word5_guess,
                                   self.ui.word6_guess, self.ui.word7_guess, self.ui.word8_guess, self.ui.word9_guess, self.ui.word10_guess, self.ui.word11_guess, self.ui.word12_guess]

        # setup words buttons
        self.words_buttons = QButtonGroup()
        self.add_buttons_first_half()
        self.add_buttons_second_half()

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
