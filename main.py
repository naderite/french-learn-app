import sys

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QStackedWidget, QApplication, QWidget, QMainWindow

from dictionary import synonyms, antonims


# screens
class HomeScreen(QMainWindow):
    def __init__(self, widget):
        super(HomeScreen, self).__init__()
        self.widget = widget
        loadUi("mainwindow.ui", self)

        self.btn_syn_lvl1.clicked.connect(lambda: self.gotoLevel("syn", 0))
        self.btn_syn_lvl2.clicked.connect(lambda: self.gotoLevel("syn", 1))
        self.btn_syn_lvl3.clicked.connect(lambda: self.gotoLevel("syn", 2))
        self.btn_syn_lvl4.clicked.connect(lambda: self.gotoLevel("syn", 3))

        self.btn_ant_lvl1.clicked.connect(lambda: self.gotoLevel("ant", 0))
        self.btn_ant_lvl2.clicked.connect(lambda: self.gotoLevel("ant", 1))
        self.btn_ant_lvl3.clicked.connect(lambda: self.gotoLevel("ant", 2))
        self.btn_ant_lvl4.clicked.connect(lambda: self.gotoLevel("ant", 3))

    def gotoLevel(self, genre, index):

        level_ui = LevelScreen(genre, index)
        self.widget.addWidget(level_ui)
        self.widget.setCurrentIndex(widget.currentIndex()+1)


class LevelScreen(QMainWindow):
    def __init__(self, genre, index):
        super(LevelScreen, self).__init__()
        loadUi("levelwindow.ui", self)
        self.generateLevel(genre, index)

    def generateLevel(self, genre, index):
        level = Level(genre, index)

        #write level title
        self.lvl_title.setText(level.title)

        # setup LevelScreen buttons text
        self.B_word1.setText(level.words[0].name)
        self.B_word2.setText(level.words[1].name)
        self.B_word3.setText(level.words[2].name)
        self.B_word4.setText(level.words[3].name)
        self.B_word5.setText(level.words[4].name)
        self.B_word6.setText(level.words[5].name)
        self.B_word7.setText(level.words[6].name)
        self.B_word8.setText(level.words[7].name)
        self.B_word9.setText(level.words[8].name)
        self.B_word10.setText(level.words[9].name)
        self.B_word11.setText(level.words[10].name)
        self.B_word12.setText(level.words[11].name)


# backend classes
class Level():
    def __init__(self, genre, index):
        self.genre = genre
        self.index = index
        self.words = self.getWords(self.genre, self.index)
        self.title = self.getTitle(self.genre, self.index)

    def getTitle(self, genre, index):
        if genre == "syn":
            title = "Synonyme " + str(index)
        elif genre == "ant":
            title = "Antomnyme " + str(index)
        
        return title

    def getWords(self, genre, index):
        words = []
        if genre == "syn":
            for n in range(1, 13):
                lvl_dict = dict(synonyms[index])
                word_name = lvl_dict.get(str(n))[0]
                word_syn = lvl_dict.get(str(n))[1]
                words.append(Word(word_name, word_syn))
            return words
        elif genre == "ant":
            for n in range(1, 13):
                lvl_dict = dict(antonims[index])
                word_name = lvl_dict.get(str(n))[0]
                word_ant = lvl_dict.get(str(n))[1]
                words.append(Word(word_name, word_ant))
            return words


class Word():
    def __init__(self, name, match):
        self.name = name
        self.match = match


# main
app = QApplication(sys.argv)


widget = QStackedWidget()
home = HomeScreen(widget)
widget.addWidget(home)
widget.setMinimumHeight(1080)
widget.setMinimumWidth(1920)
widget.show()

sys.exit(app.exec())
