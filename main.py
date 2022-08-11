import sys
import winsound

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QStackedWidget, QApplication, QWidget, QMainWindow, QDialog, QStackedLayout

from dictionary import adjectives, verbes
from mainwindow import Ui_MainWindow


# screens
class HomeScreen(QMainWindow):
    def __init__(self, widget):
        super(HomeScreen, self).__init__()
        self.widget = widget
        loadUi("mainwindow.ui",self)

        #self.stacklayout = QStackedLayout
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.btn_adj_lvl1.clicked.connect(lambda: self.goto_level("adj", 0))
        self.btn_adj_lvl2.clicked.connect(lambda: self.goto_level("adj", 1))
        self.btn_adj_lvl3.clicked.connect(lambda: self.goto_level("adj", 2))
        self.btn_adj_lvl4.clicked.connect(lambda: self.goto_level("adj", 3))

        self.btn_vrb_lvl1.clicked.connect(lambda: self.goto_level("vrb", 0))
        self.btn_vrb_lvl2.clicked.connect(lambda: self.goto_level("vrb", 1))
        self.btn_vrb_lvl3.clicked.connect(lambda: self.goto_level("vrb", 2))
        self.btn_vrb_lvl4.clicked.connect(lambda: self.goto_level("vrb", 3))

        self.toolButton.clicked.connect(self.grampage)    

    def grampage(self):
        self.main_menu.setCurrentIndex(1)

    def goto_level(self, genre, diffculty):

        level_ui = LevelScreen(self.widget, genre, diffculty)
        self.widget.addWidget(level_ui)
        self.widget.setCurrentIndex(widget.currentIndex()+1)


class LevelScreen(QMainWindow):
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
        winsound.PlaySound(r"WordsPronunciation\{}".format(
            sound), winsound.SND_FILENAME)


class MessageBox(QDialog):
    def __init__(self, words, score):
        super(MessageBox, self).__init__()
        loadUi("CorrectionMessageBox.ui", self)
        self.show_solution(words, score)
        self.btn_return_home.clicked.connect(goto_home)

    def show_solution(self, words, score):
        solution_txt = f"Votre score est: {score}\ 12 \n\n"
        for word in words:
            solution_txt += f"{word.name} = {word.match} \n"
        self.msg_txt.setText(solution_txt)


# backend classes
class Level():
    def __init__(self, genre, index):
        self.genre = genre
        self.index = index
        self.words = self.get_words(self.genre, self.index)
        self.title = self.get_title(self.genre, self.index)

    def get_title(self, genre, index):
        if genre == "adj":
            title = "Adjectifs " + str(index)
        elif genre == "vrb":
            title = "Verbes " + str(index)

        return title

    def get_words(self, genre, index):
        words = []
        if genre == "adj":
            for n in range(1, 13):
                lvl_dict = dict(adjectives[index])
                word_name = lvl_dict.get(str(n))[0]
                word_match = lvl_dict.get(str(n))[1]
                word_sound = lvl_dict.get(str(n))[2]
                words.append(Word(word_name, word_match, word_sound))
            return words
        elif genre == "vrb":
            for n in range(1, 13):
                lvl_dict = dict(verbes[index])
                word_name = lvl_dict.get(str(n))[0]
                word_match = lvl_dict.get(str(n))[1]
                words.append(Word(word_name, word_match))
            return words


class Word():
    def __init__(self, name, match, sound):
        self.name = name
        self.match = match
        self.sound = sound


# scroling functions
def goto_home():
    home = HomeScreen(widget)
    widget.addWidget(home)
    widget.setCurrentIndex(widget.currentIndex()+1)


# main
app = QApplication(sys.argv)
widget = QStackedWidget()
home = HomeScreen(widget)
widget.addWidget(home)
widget.show()

sys.exit(app.exec())
