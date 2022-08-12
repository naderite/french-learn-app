from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QStackedWidget, QApplication, QWidget, QMainWindow, QDialog, QStackedLayout
import playsound


class EvaluationMenuScreen(QMainWindow):
    def __init__(self):
        super(EvaluationMenuScreen, self).__init__()
        loadUi(r"Screens\Evaluation\evaluation_menuPage.ui", self)
