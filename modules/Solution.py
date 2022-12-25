from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog


class MessageBox(QDialog):
    def __init__(self):
        super(MessageBox, self).__init__()
        loadUi("ui/CorrectionMessageBox.ui", self)

        # self.btn_return_home.clicked.connect(goto_home)

    def write_solution(self, words, score, level_type):

        if level_type in ["gram", "vocab"]:
            solution_txt = f"Votre score est: {score}\ 12 \n\n"
            for word in words:
                solution_txt += f"{word.name} = {word.answer} \n"
        else:
            solution_txt = f"Votre score est: {score}\ 6 \n\n"
            # convert the dictionary to a list of tuples of pronoun and answer pair
            words = words.items()
            for word in words:
                solution_txt += f"{word[0]} {word[1]} \n"
        self.msg_txt.setText(solution_txt)
