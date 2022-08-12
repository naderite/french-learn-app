from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QStackedWidget, QApplication, QWidget, QMainWindow, QDialog, QStackedLayout
import playsound


class ConjugaisonMenuScreen(QMainWindow):
    def __init__(self):
        super(ConjugaisonMenuScreen, self).__init__()
        loadUi(r"Screens\Conjugaison\conjugaison_menuPage.ui", self)
