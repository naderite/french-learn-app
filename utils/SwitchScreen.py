from modules.Vocabulary import VocabularyLevel
from modules.Grammar import GrammarLevel
from modules.Conjugation import ConjugationLevel


class Scroll:
    # menus scrolling function
    @staticmethod
    def main_menu(widget, index, solution_box):
        widget.setCurrentIndex(index)
        solution_box.close()

    @staticmethod
    def vocab_menu(widget):
        widget.setCurrentIndex(0)

    @staticmethod
    def gram_menu(widget):
        widget.setCurrentIndex(1)

    @staticmethod
    def conj_menu(widget):
        widget.setCurrentIndex(2)

    # levels scrolling functions
    @staticmethod
    def vocab_lvl(widget, level_widget, genre, difficulty, solution_box):
        generateLevel.vocabulary(
            level_widget, genre, difficulty, solution_box)
        widget.setCurrentIndex(3)
        solution_box.ui.btn_tryagain.clicked.connect(lambda: Scroll.reload_lvl(
            widget, level_widget, genre, difficulty, solution_box))

    @staticmethod
    def gram_lvl(widget, level_widget, genre, difficulty, solution_box):
        generateLevel.grammar(level_widget, genre, difficulty, solution_box)
        widget.setCurrentIndex(4)
        solution_box.ui.btn_tryagain.clicked.connect(lambda: Scroll.reload_lvl(
            widget, level_widget, genre, difficulty, solution_box))

    @staticmethod
    def conj_lvl(widget, level_widget, temp, groupe, solution_box):
        generateLevel.conjugation(level_widget, temp, groupe, solution_box)
        widget.setCurrentIndex(5)
        solution_box.ui.btn_tryagain.clicked.connect(lambda: Scroll.reload_lvl(
            widget, level_widget, temp, groupe, solution_box))

    @staticmethod
    def reload_lvl(widget, level_widget, param_1, param_2, solution_box):
        match widget.currentIndex():
            case 3:
                Scroll.vocab_lvl(widget, level_widget,
                                 param_1, param_2, solution_box)
            case 4:
                Scroll.gram_lvl(widget, level_widget, param_1,
                                param_2, solution_box)
            case 5:
                Scroll.conj_lvl(widget, level_widget, param_1,
                                param_2, solution_box)
        solution_box.close()


class generateLevel:

    @staticmethod
    def grammar(level_widget, genre, difficulty, solution_box):
        level = GrammarLevel(genre, difficulty)
        # write level title and question
        level_widget.ui.lvl_title.setText(level.title)
        level_widget.ui.lvl_question.setText(level.question)
        # setup LevelScreen buttons text
        for button in level_widget.words_buttons.buttons():
            button.setText(
                level.words[level_widget.words_buttons.id(button)].name)

        # reset the words guess space
        for guess_space in level_widget.words_guess_spaces:
            guess_space.setText("")
        # correct button
        level_widget.ui.btn_correct.clicked.connect(
            lambda: generateLevel.correct(level_widget, level.words, "gram", solution_box))

    @staticmethod
    def vocabulary(level_widget, genre, difficulty, solution_box):

        level = VocabularyLevel(genre, difficulty)
        # write level title
        level_widget.ui.lvl_title.setText(level.title)
        # setup LevelScreen buttons text
        for button in level_widget.words_buttons.buttons():
            button.setText(
                level.words[level_widget.words_buttons.id(button)].name)

        # reset the words guess space
        for guess_space in level_widget.words_guess_spaces:
            guess_space.setText("")
        # correct button
        level_widget.ui.btn_correct.clicked.connect(
            lambda: generateLevel.correct(level_widget, level.words, "vocab", solution_box))

    @staticmethod
    def conjugation(level_widget, temp, groupe, solution_box):
        level = ConjugationLevel(temp, groupe)
        # write level title and level question
        level_widget.ui.lvl_title.setText(level.title)
        level_widget.ui.lvl_question.setText(level.question)
        # setup level screen button
        level_widget.ui.lvl_verb.setText(level.verb)
        # correct button
        level_widget.ui.btn_correct.clicked.connect(
            lambda: generateLevel.correct(level_widget, level.answer, "conj", solution_box))

        # reset the words guess space
        for guess_space in level_widget.words_guess_spaces:
            guess_space.setText("")

    @staticmethod
    def correct(level_widget, original_words, level_type, solution_box):
        guesses = generateLevel.get_guesses(level_widget)
        score = 0
        if level_type in ["gram", "vocab"]:
            for guess in guesses:
                index = 0
                answer = original_words[index].answer
                guess = (guess.strip())
                if guess in answer and len(guess) > 1:
                    score += 1
                index += 1
        else:
            answers = original_words.values()
            score = sum(guess in answers for guess in guesses)
        # setup message box and show the solution

        solution_box.write_solution(original_words, score, level_type)
        solution_box.show()
        solution_box.exec_()

    @staticmethod
    def get_guesses(widget):
        return [guess.text() for guess in widget.words_guess_spaces]
