from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QStackedWidget, QApplication, QWidget, QMainWindow, QDialog, QStackedLayout
import playsound


class GrammaireMenuScreen(QMainWindow):
    def __init__(self):
        super(GrammaireMenuScreen, self).__init__()
        loadUi(r"Screens\Grammaire\grammaire_menuPage.ui", self)
