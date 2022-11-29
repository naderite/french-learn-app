import sys
from PyQt5.QtWidgets import QStackedWidget, QApplication

from Screens.Vocabulair.VocabularyScreens import VocabularyMenuScreen, VocabularyLevelScreen
from Screens.Grammaire.GrammaireScreens import GrammaireMenuScreen, GrammaireLevelScreen
from Screens.Conjugaison.ConjugaisonScreens import ConjugaisonMenuScreen, ConjugaisonLevelScreen
from Screens.Solution.SolutionScreen import MessageBox
import utils.Buttons as ButtonsUtils


class MainScreen(QStackedWidget):
    def __init__(self):
        super(MainScreen, self).__init__()
        self.create_screens()
        self.add_screens()
        ButtonsUtils.Group.create_groups(self)
        ButtonsUtils.Connect.connect_all(self)

    def create_screens(self):
        # creating menu screens
        self.vocab_menu = VocabularyMenuScreen()
        self.gram_menu = GrammaireMenuScreen()
        self.conj_menu = ConjugaisonMenuScreen()

        # creating level screens
        self.vocab_level = VocabularyLevelScreen()
        self.gram_level = GrammaireLevelScreen()
        self.conj_level = ConjugaisonLevelScreen()

        self.solution_box = MessageBox()

    def add_screens(self):
        # adding menu screens to main window
        self.addWidget(self.vocab_menu)  # index 0
        self.addWidget(self.gram_menu)  # index 1
        self.addWidget(self.conj_menu)  # index 2

        # adding level screens to main window
        self.addWidget(self.vocab_level)  # index 3
        self.addWidget(self.gram_level)  # index 4
        self.addWidget(self.conj_level)  # index 5


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainScreen()
    window.show()

    sys.exit(app.exec())
