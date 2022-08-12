from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QStackedWidget, QApplication, QWidget, QMainWindow, QDialog, QStackedLayout
import playsound


class VocabularyMenuScreen(QMainWindow):
    def __init__(self):
        super(VocabularyMenuScreen, self).__init__()
        loadUi(r"Screens\Vocabulair\vocabulair_menuPage.ui", self)


